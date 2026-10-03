# Vendored Guardian candidate

This is the stdlib-only Guardian 1.1.0 source candidate from Drew's local
guardian-agent workspace, including the exact-authorized inference profile.
It is not a published package release. The MIT license is included.

The snapshot avoids installing an unpinned external package in the credentialed
pilot job. Its regression tests run in the deterministic reliability workflow.
Review source changes and keep the copy in sync with Guardian before adoption.
The host workflow, verifier, and vendored code are trusted execution components;
Guardian is not a sandbox for hostile changes to those components.
