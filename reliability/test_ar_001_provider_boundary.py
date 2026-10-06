"""Provider transport boundary checks using dummy credentials and no network."""
import json
import unittest
from unittest.mock import MagicMock, patch
import urllib.request

from reliability import agent_reliability_ar_001_harness as harness


class ProviderBoundaryTests(unittest.TestCase):
    def test_redirects_never_build_a_followup_request(self):
        request = urllib.request.Request("https://api.openai.com/v1/responses", data=b"{}",
                                         headers={"Authorization": "Bearer test-only"})
        handler = harness._RejectProviderRedirects()
        for code in (301, 302, 303, 307, 308):
            for url in ("https://example.invalid/", "http://api.openai.com/", "https://api.openai.com/other"):
                with self.subTest(code=code, url=url):
                    with self.assertRaisesRegex(harness.HarnessError, "redirect rejected"):
                        handler.redirect_request(request, None, code, "redirect", {}, url)

    def invoke_with(self, raw):
        opener = MagicMock()
        response = opener.open.return_value.__enter__.return_value
        response.read.return_value = raw
        response.headers.get.return_value = "request-test"
        with patch.object(harness, "validate_execution_authorization"), patch.object(
                harness.urllib.request, "build_opener", return_value=opener) as build:
            result = harness.call_openai({}, None, api_key="test-only")
        return result, build, opener, response

    def test_success_reads_once_with_limit_and_no_implicit_proxy(self):
        raw = json.dumps({"model": harness.MODEL, "output": [
            {"type": "message", "content": [{"type": "output_text", "text": "{}"}]}]}).encode()
        (_, metadata), build, opener, response = self.invoke_with(raw)
        self.assertEqual(metadata["returned_model"], harness.MODEL)
        response.read.assert_called_once_with(harness.MAX_RESPONSE_BYTES + 1)
        opener.open.assert_called_once()
        proxy_handler, redirect_handler = build.call_args.args
        self.assertEqual(proxy_handler.proxies, {})
        self.assertIsInstance(redirect_handler, harness._RejectProviderRedirects)

    def test_oversized_response_rejected_without_retry(self):
        opener = MagicMock()
        opener.open.return_value.__enter__.return_value.read.return_value = b"x" * (harness.MAX_RESPONSE_BYTES + 1)
        with patch.object(harness, "validate_execution_authorization"), patch.object(
                harness.urllib.request, "build_opener", return_value=opener):
            with self.assertRaisesRegex(harness.HarnessError, "exceeds size limit"):
                harness.call_openai({}, None, api_key="test-only")
        opener.open.assert_called_once()
