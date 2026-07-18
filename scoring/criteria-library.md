# Criteria Library

Version: v0.2 draft

This file defines the observable scoring signals used by Operator Intelligence™ assessments.

Each criterion maps an observable business signal to required evidence, scoring guidance, and a recommended improvement path.

## How to use this library

For every assessed client:

1. Capture evidence.
2. Score each applicable criterion from 0–100.
3. Assign confidence using `confidence-model.md`.
4. Record findings in the decision ledger.
5. Map weak signals to recommendations.
6. Route the highest-impact items into the 90-day roadmap.

## Universal scoring anchors

| Score | Meaning |
|---:|---|
| 0 | Missing, broken, or actively harmful. |
| 25 | Present but weak, incomplete, or unreliable. |
| 50 | Functional baseline. Acceptable but not strong. |
| 75 | Strong and commercially useful. Improvement opportunities remain. |
| 100 | Excellent, differentiated, measurable, and integrated. |

## Recommendation priority logic

| Priority | Use when |
|---|---|
| Critical | The issue directly blocks leads, trust, contact, tracking, or execution. |
| High | The issue materially reduces conversion, local visibility, or follow-up. |
| Medium | The issue supports growth but is not the first constraint. |
| Low | The issue is useful polish, optional refinement, or later-stage optimization. |

---

# 1. Website Structure and UX Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-WEB-001 | Homepage immediately communicates business type. | Homepage screenshot above the fold. | Low score if visitor cannot identify service category within 5 seconds. | Rewrite hero section with clear service category, location, and outcome. |
| OI-WEB-002 | Homepage communicates service area. | Hero, footer, contact page, service-area copy. | Low score if city or service region is absent or unclear. | Add location/service-area language to hero, footer, service pages, and metadata. |
| OI-WEB-003 | Primary navigation is simple and buyer-oriented. | Navigation screenshot desktop and mobile. | Low score if services, contact, or estimate path are hard to find. | Simplify navigation around Services, Proof, Reviews, About, and Estimate. |
| OI-WEB-004 | Services are organized into clear pages. | Site menu, URL list, service-page inventory. | Low score if all services are collapsed into one thin page. | Build dedicated pages for core and high-value services. |
| OI-WEB-005 | Website works cleanly on mobile. | Mobile screenshots of homepage, menu, service page, form. | Low score if layout breaks, text is small, buttons are hard to tap, or form is difficult. | Redesign mobile layout around tap-to-call, short sections, and simple forms. |
| OI-WEB-006 | Phone number is visible without searching. | Header, mobile header, footer, contact page. | Low score if phone number is buried or not tap-enabled. | Add persistent phone path in header and mobile action area. |
| OI-WEB-007 | Contact or estimate page is easy to reach. | Navigation, hero CTA, footer, service-page CTAs. | Low score if contact path requires multiple steps. | Add repeated estimate CTAs at top, middle, and bottom of key pages. |
| OI-WEB-008 | Website has a logical page hierarchy. | Sitemap, navigation, internal links. | Low score if important pages are orphaned or buried. | Restructure page hierarchy by service, location, proof, and contact. |
| OI-WEB-009 | Visual hierarchy supports scanning. | Screenshots of key pages. | Low score if text blocks are dense, headings unclear, or CTAs blend in. | Rewrite and redesign sections with clear headings, short copy, proof, and action. |
| OI-WEB-010 | Page content supports buyer decision-making. | Service pages and homepage copy. | Low score if pages only describe services without process, proof, objections, or next steps. | Add process, proof, FAQs, pricing factors, and estimate expectations. |
| OI-WEB-011 | Website avoids template-generic presentation. | Homepage and competitor comparison. | Low score if copy and layout are indistinguishable from local competitors. | Add distinct positioning, local proof, owner/team story, and project examples. |
| OI-WEB-012 | Footer supports trust and navigation. | Footer screenshot. | Low score if footer lacks phone, service area, pages, business details, or credibility signals. | Build footer with contact, service links, local area, credentials, and review link. |

---

# 2. Messaging and Offer Clarity Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-MSG-001 | Hero message states a specific customer outcome. | Homepage hero copy. | Low score if hero only says “professional services” or similar generic language. | Rewrite hero around outcome, service, location, and trust proof. |
| OI-MSG-002 | Copy explains why the company is different. | Homepage, about page, service pages. | Low score if differentiators are absent or generic. | Define 3–5 operational differentiators and place them near decision points. |
| OI-MSG-003 | Copy addresses buyer pain points. | Service-page copy. | Low score if copy only lists tasks and does not address concerns. | Add pain-point sections for risk, timeline, quality, cleanup, price, and trust. |
| OI-MSG-004 | Service descriptions are specific. | Service-page inventory. | Low score if service descriptions are thin or interchangeable. | Expand service pages with scope, process, proof, FAQs, and qualifying details. |
| OI-MSG-005 | The offer is clear. | Homepage, service pages, CTAs. | Low score if buyer cannot tell what action to take or what they receive. | Clarify offer: estimate, consultation, inspection, quote, or service call. |
| OI-MSG-006 | Copy explains process. | Homepage and service pages. | Low score if customers do not know what happens after inquiry. | Add “How It Works” section with steps from request to completion. |
| OI-MSG-007 | Copy reduces objections. | FAQs, service pages. | Low score if pricing, timeline, prep, cleanup, warranties, or availability are unaddressed. | Add objection-handling FAQ and service-specific expectation sections. |
| OI-MSG-008 | Message is locally relevant. | Local references, city/service-area copy, project examples. | Low score if content could apply to any city. | Add local project examples, neighborhoods, service-area language, and regional relevance. |
| OI-MSG-009 | Copy avoids vague claims. | Full-site copy review. | Low score if claims like quality, reliable, affordable appear without proof. | Replace vague claims with evidence, examples, process, guarantees, and customer quotes. |
| OI-MSG-010 | The highest-value services are emphasized. | Homepage sections, navigation, CTAs. | Low score if high-value services are hidden or treated equally with minor services. | Reorder content and CTAs around profitable or strategic service lines. |

---

# 3. Conversion Infrastructure Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-CONV-001 | Primary CTA is visible above the fold. | Homepage above-fold screenshot. | Low score if CTA is absent, vague, or visually weak. | Add direct estimate-oriented CTA in hero. |
| OI-CONV-002 | CTA language matches buyer intent. | CTA text inventory. | Low score if CTA says only “Learn More” or “Submit” at primary decision points. | Use specific action language such as “Request a Free Estimate.” |
| OI-CONV-003 | CTAs appear throughout service pages. | Service-page screenshots. | Low score if CTA appears only once or only in navigation. | Add contextual CTAs after proof, process, FAQs, and final section. |
| OI-CONV-004 | Contact form captures useful qualification data. | Contact form fields. | Low score if form only asks name, email, message. | Add fields for service type, location, urgency, project details, and preferred contact method. |
| OI-CONV-005 | Form friction is appropriate. | Form length and field review. | Low score if form is too long for simple inquiry or too short for complex estimate. | Match form length to decision stage and service complexity. |
| OI-CONV-006 | Confirmation message sets expectations. | Post-submit behavior. | Low score if no clear confirmation or next step appears. | Add confirmation with response window, next step, and alternate contact path. |
| OI-CONV-007 | Mobile tap-to-call exists. | Mobile page test. | Low score if phone number is not tappable or hard to access. | Add tap-to-call button in mobile header or sticky action bar. |
| OI-CONV-008 | Service pages contain service-specific inquiry prompts. | Service-page CTA review. | Low score if all pages use identical generic contact prompts. | Add page-specific CTAs tied to the service being viewed. |
| OI-CONV-009 | Buyer can provide project details easily. | Form fields, intake options. | Low score if project context is hard to submit. | Add structured intake fields and optional photo/project description prompts. |
| OI-CONV-010 | Response time expectation is visible. | Contact page, form confirmation, homepage. | Low score if buyer has no idea when they will hear back. | State response standard, for example same business day or next business day. |
| OI-CONV-011 | Social proof appears near CTAs. | CTA section screenshots. | Low score if proof and action are separated. | Pair CTAs with reviews, project proof, guarantees, or trust badges. |
| OI-CONV-012 | There are multiple conversion paths. | Phone, form, booking, social, email paths. | Low score if only one path exists and it is weak. | Offer phone, estimate form, and optional scheduling/inquiry path. |
| OI-CONV-013 | The website supports urgent buyers when relevant. | Service pages and CTAs for time-sensitive work. | Low score if urgent-intent visitors receive no clear path. | Add urgent-service CTA, phone prominence, and clear availability language. |
| OI-CONV-014 | Lead source can be tracked. | Forms, analytics, CRM, UTM readiness. | Low score if inquiries arrive without source or page context. | Add conversion tracking, hidden source fields, CRM source labels, and reporting. |

---

# 4. Local SEO Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-SEO-001 | Website has dedicated pages for core services. | URL inventory. | Low score if core services share one general page. | Build service-specific pages for each primary revenue line. |
| OI-SEO-002 | Website has pages for high-value services. | Service list vs URL list. | Low score if profitable services lack individual pages. | Create landing pages for highest-margin or highest-demand services. |
| OI-SEO-003 | Title tags include service and location. | Page title review. | Low score if titles are generic or duplicated. | Rewrite title tags with service, city, and brand. |
| OI-SEO-004 | Meta descriptions are specific and action-oriented. | Meta description review. | Low score if missing, duplicated, or vague. | Write unique descriptions with service, location, proof, and action. |
| OI-SEO-005 | H1 headings clearly match page intent. | H1 review. | Low score if headings are missing, duplicated, or vague. | Add one clear H1 per page tied to service and local intent. |
| OI-SEO-006 | Internal linking supports service discovery. | Link crawl or manual page review. | Low score if service pages are isolated. | Add internal links from homepage, service hub, blog, and footer. |
| OI-SEO-007 | Website includes local service-area content. | Service area page, footer, homepage. | Low score if local area is thin or absent. | Add service-area section and selective local landing pages. |
| OI-SEO-008 | Pages answer common buyer questions. | FAQ and service content review. | Low score if pages lack FAQs or decision-support content. | Add service-specific FAQs and pricing/process explanations. |
| OI-SEO-009 | Image alt text supports context. | Image alt review. | Low score if key images have missing or generic alt text. | Add descriptive alt text for project, service, and location context. |
| OI-SEO-010 | URLs are clean and descriptive. | URL inventory. | Low score if URLs are unclear, duplicated, or parameter-heavy. | Use clean service/location URL structure. |
| OI-SEO-011 | Website has indexable pages. | Robots, page source, search visibility. | Low score if important pages are blocked or not indexed. | Fix indexing, sitemap, robots, canonical, and crawl issues. |
| OI-SEO-012 | Sitemap exists and is current. | Sitemap URL or CMS settings. | Low score if sitemap is missing or outdated. | Generate and submit XML sitemap. |
| OI-SEO-013 | Content targets buyer intent, not only blog traffic. | Blog and page topic review. | Low score if content is generic and not tied to services. | Build content around service questions, project examples, and local demand. |
| OI-SEO-014 | Website includes project or case-study content. | Project pages, gallery, blog. | Low score if completed work is not indexable or described. | Add project case studies with service, location, challenge, and outcome. |
| OI-SEO-015 | Local citations are consistent. | Directory audit. | Low score if name, address, phone, or website are inconsistent. | Clean up citations and standardize business information. |
| OI-SEO-016 | Schema opportunities are addressed. | Structured data review. | Low score if no relevant local business or FAQ schema exists. | Add LocalBusiness, Service, FAQ, Review, or Breadcrumb schema where appropriate. |

---

# 5. Google Business Profile Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-GBP-001 | Profile exists and is findable. | Google search screenshot. | Low score if profile is absent, duplicated, or hard to find. | Claim, verify, clean, or consolidate profile. |
| OI-GBP-002 | Primary category matches service. | GBP category screenshot. | Low score if category is wrong or too broad. | Select strongest primary category for core service. |
| OI-GBP-003 | Secondary categories support services. | GBP category review. | Low score if relevant secondary categories are missing. | Add accurate secondary categories. |
| OI-GBP-004 | Services are listed completely. | GBP services screenshot. | Low score if key services are missing. | Add all major services with clear descriptions. |
| OI-GBP-005 | Business description is specific. | GBP description. | Low score if description is vague, keyword-stuffed, or outdated. | Rewrite description around services, location, proof, and customer value. |
| OI-GBP-006 | Photos are recent and useful. | Photo tab review. | Low score if photos are outdated, sparse, or low-quality. | Upload recent project, team, vehicle, equipment, and finished-work photos. |
| OI-GBP-007 | Review count is competitive. | GBP review count vs competitors. | Low score if review volume is far behind visible competitors. | Build review generation system and weekly review request cadence. |
| OI-GBP-008 | Review velocity is healthy. | Recent reviews. | Low score if reviews are old or sporadic. | Automate review requests after completed work. |
| OI-GBP-009 | Reviews receive owner responses. | Review response review. | Low score if responses are absent or inconsistent. | Respond to every review with specific, professional replies. |
| OI-GBP-010 | Q&A is managed. | GBP Q&A section. | Low score if questions are unanswered or absent where useful. | Seed common Q&A and monitor new questions. |
| OI-GBP-011 | Posts or updates are used. | GBP posts tab. | Low score if no recent updates exist. | Add monthly project updates, seasonal reminders, or service highlights. |
| OI-GBP-012 | Website and GBP service alignment is consistent. | Compare GBP services to website pages. | Low score if GBP lists services not represented on website or vice versa. | Align GBP services, website pages, and internal linking. |

---

# 6. Reputation and Trust Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-TRUST-001 | Reviews are visible on website. | Homepage/service page screenshots. | Low score if reviews exist externally but not on site. | Add review highlights to homepage, service pages, and CTA sections. |
| OI-TRUST-002 | Review language is specific. | Review excerpts. | Low score if reviews are generic or not service-specific. | Ask customers for reviews that mention service, location, communication, and outcome. |
| OI-TRUST-003 | Project photos are visible. | Gallery and service-page review. | Low score if little or no real work is shown. | Build gallery and service-specific project proof sections. |
| OI-TRUST-004 | Before/after proof exists where relevant. | Gallery, social, website. | Low score if transformation work lacks proof. | Add before/after sections and project captions. |
| OI-TRUST-005 | Team or owner identity is visible. | About page, homepage, social. | Low score if business feels anonymous. | Add owner/team section with local story and credibility. |
| OI-TRUST-006 | Credentials are stated. | Website, footer, about page. | Low score if license, insurance, certifications, or associations are absent when relevant. | Add credential section and verification language. |
| OI-TRUST-007 | Warranty or satisfaction promise is clear. | Service pages and footer. | Low score if risk-reduction policy is absent or vague. | Add warranty, workmanship, or satisfaction language with accurate scope. |
| OI-TRUST-008 | Process is explained. | Homepage and service pages. | Low score if customer does not know what to expect. | Add process section from inquiry through completion. |
| OI-TRUST-009 | Safety or professionalism signals are present. | Service pages, photos, copy. | Low score if high-risk work lacks process or safety proof. | Add safety, cleanup, preparation, equipment, and professionalism details. |
| OI-TRUST-010 | Local proof is visible. | Project locations, reviews, community mentions. | Low score if local legitimacy is not demonstrated. | Add local project examples and community/service-area proof. |
| OI-TRUST-011 | Contact information is complete and consistent. | Header, footer, contact page, directories. | Low score if phone, address/service area, or business name varies. | Standardize contact details across site and profiles. |
| OI-TRUST-012 | Trust signals appear before the buyer must decide. | CTA sections and page structure. | Low score if proof appears only after the final contact form. | Move strongest proof near hero and primary CTAs. |

---

# 7. Social Presence and Content Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-SOC-001 | Facebook page exists and is branded. | Page screenshot. | Low score if page is missing, incomplete, or inconsistent with website. | Complete branding, cover image, services, contact info, and website link. |
| OI-SOC-002 | Social profiles use consistent business information. | Profile audit. | Low score if names, phone, links, or service area conflict. | Standardize profile information across channels. |
| OI-SOC-003 | Recent activity exists. | Post dates. | Low score if profile appears abandoned. | Add consistent posting cadence, at least weekly or biweekly. |
| OI-SOC-004 | Posts show real work. | Post review. | Low score if posts are generic, stock-heavy, or only promotional. | Publish project photos, process clips, finished work, and customer stories. |
| OI-SOC-005 | Content educates buyers. | Post themes. | Low score if no helpful guidance exists. | Add tips, seasonal advice, FAQs, and maintenance education. |
| OI-SOC-006 | Content includes proof and trust. | Reviews, testimonials, crew posts. | Low score if social content does not build credibility. | Add testimonials, crew spotlights, before/after posts, and review highlights. |
| OI-SOC-007 | Social CTAs are clear. | Page buttons and post CTAs. | Low score if posts do not guide next action. | Add estimate, call, message, or website CTA to posts and page button. |
| OI-SOC-008 | Social content supports SEO and website. | Links from posts to pages. | Low score if social exists in isolation. | Link project/service posts back to relevant website pages. |
| OI-SOC-009 | Response behavior appears professional. | Comments, messages if available, public replies. | Low score if comments are unanswered or tone is weak. | Define response standard and message templates. |
| OI-SOC-010 | Seasonal campaigns exist. | Post calendar and promos. | Low score if content does not match service seasonality. | Build seasonal campaign calendar around demand windows. |

---

# 8. Automation and Operations Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-AUTO-001 | All inquiries enter one tracked system. | CRM, spreadsheet, email routing, intake flow. | Low score if leads are scattered across phone, inbox, social, and memory. | Implement CRM or lead tracker as single source of truth. |
| OI-AUTO-002 | Website forms create internal notifications. | Form settings or client confirmation. | Low score if submissions can be missed. | Route submissions to email/SMS/internal channel with backup notification. |
| OI-AUTO-003 | Inquiry confirmation is automated. | Form response behavior. | Low score if customer receives no clear acknowledgement. | Add automated confirmation email or SMS. |
| OI-AUTO-004 | Lead owner is assigned. | CRM fields or workflow. | Low score if no person owns follow-up. | Add owner field and assignment rule. |
| OI-AUTO-005 | Lead status is tracked. | CRM/stage review. | Low score if leads are not marked new, contacted, estimated, won, or lost. | Add pipeline stages and required status updates. |
| OI-AUTO-006 | Follow-up reminders exist. | CRM task review. | Low score if follow-up depends on memory. | Add reminder tasks for uncontacted leads and open estimates. |
| OI-AUTO-007 | Estimate outcomes are tracked. | CRM/report review. | Low score if won/lost estimates are unknown. | Track estimate sent, accepted, declined, stale, and lost reason. |
| OI-AUTO-008 | Review requests are systematized. | Review workflow. | Low score if reviews are requested manually or inconsistently. | Automate review request after job completion. |
| OI-AUTO-009 | Missed inquiries have recovery path. | Phone/social/email process. | Low score if missed calls or messages receive no prompt follow-up. | Add missed-inquiry response workflow. |
| OI-AUTO-010 | Customer records include service history. | CRM/customer database. | Low score if past customers cannot be segmented. | Store service type, date, value, and follow-up opportunities. |
| OI-AUTO-011 | Repeat or seasonal outreach exists. | Email/SMS campaigns, CRM lists. | Low score if past customers are never reactivated. | Build seasonal reactivation and maintenance campaigns. |
| OI-AUTO-012 | Internal handoffs are documented. | SOPs, workflow notes. | Low score if handoffs are informal or unclear. | Document handoff from inquiry to estimate to scheduled work. |
| OI-AUTO-013 | Standard response templates exist. | Email/SMS templates. | Low score if responses are improvised every time. | Create templates for inquiry, estimate follow-up, scheduling, review, and referral. |
| OI-AUTO-014 | Operational dashboard exists. | Dashboard or report review. | Low score if owner cannot see pipeline health. | Build dashboard for leads, sources, estimates, reviews, and follow-up. |

---

# 9. AI Readiness and Governance Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-AI-001 | Core workflows are documented. | SOPs, checklists, client confirmation. | Low score if AI would be placed into undefined workflows. | Document lead, estimate, customer communication, and review workflows first. |
| OI-AI-002 | Customer data is structured. | CRM fields, spreadsheet, forms. | Low score if data is inconsistent or unstructured. | Standardize lead and customer fields before AI automation. |
| OI-AI-003 | AI use cases are defined. | Strategy notes, owner interview. | Low score if AI interest is vague or tool-first. | Define use cases by task, risk, owner, inputs, and expected output. |
| OI-AI-004 | Human review gates exist. | Workflow design. | Low score if AI could send customer-facing content without review in sensitive contexts. | Add review gates for pricing, promises, complaints, and unusual requests. |
| OI-AI-005 | Customer-facing AI boundaries are clear. | Chatbot/assistant config or policy. | Low score if AI can overpromise, misprice, or answer beyond scope. | Define allowed topics, blocked topics, escalation rules, and disclaimers. |
| OI-AI-006 | Knowledge base exists. | FAQs, service docs, policies. | Low score if AI has no reliable source material. | Build approved knowledge base from services, FAQs, process, and policies. |
| OI-AI-007 | AI outputs can be audited. | Logs, CRM notes, transcript storage. | Low score if AI decisions or messages leave no record. | Store AI-assisted outputs and customer interactions in audit log. |
| OI-AI-008 | Data privacy expectations are defined. | Policy, tool settings, workflow. | Low score if sensitive customer details are copied into tools without rules. | Define data-handling rules and tool boundaries. |
| OI-AI-009 | AI supports low-risk work first. | Use-case prioritization. | Low score if first use case is high-risk pricing or binding commitments. | Start with drafting, FAQ support, intake summarization, and internal assistance. |
| OI-AI-010 | Escalation path exists. | Assistant rules or SOP. | Low score if AI has no route for uncertainty or exceptions. | Add escalation to human owner for uncertain, high-risk, or out-of-scope cases. |
| OI-AI-011 | Prompt standards exist. | Prompt templates or instructions. | Low score if AI instructions are informal and inconsistent. | Apply PromptBP-style prompt blocks for role, objective, inputs, outputs, and rules. |
| OI-AI-012 | AI performance is reviewed. | QA process, sample review, metrics. | Low score if no one checks quality or failure patterns. | Add monthly AI review with examples, corrections, and updated rules. |

---

# 10. Analytics and Reporting Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-AN-001 | Website analytics are installed. | Tag check or analytics access. | Low score if no analytics exist or cannot be verified. | Install or verify analytics tracking. |
| OI-AN-002 | Search Console is configured. | Search Console access or verification. | Low score if organic search data is unavailable. | Configure Search Console and submit sitemap. |
| OI-AN-003 | Form submissions are tracked. | Analytics events, CRM, form logs. | Low score if form leads cannot be counted. | Track form submissions as conversion events. |
| OI-AN-004 | Phone clicks are tracked. | Analytics events or call tracking. | Low score if phone activity is invisible. | Add click-to-call event tracking or call tracking. |
| OI-AN-005 | Lead source is captured. | CRM/source fields. | Low score if all leads appear as unknown source. | Add source fields, UTM capture, and page context. |
| OI-AN-006 | Estimate outcomes are reported. | CRM/pipeline report. | Low score if accepted/lost estimates are unknown. | Track estimate outcome and lost reason. |
| OI-AN-007 | Review growth is monitored. | Review dashboard or manual tracker. | Low score if review velocity is unknown. | Track review count, rating, recency, and response completion monthly. |
| OI-AN-008 | Service-page performance is visible. | Analytics page reports. | Low score if high-value pages are not monitored. | Build report for top landing pages, service pages, and conversion paths. |
| OI-AN-009 | Monthly reporting cadence exists. | Meeting notes, dashboards, reports. | Low score if data is never reviewed. | Create monthly operator review cadence with decisions and action items. |
| OI-AN-010 | Reports produce decisions. | Prior reports and action logs. | Low score if reporting is passive or vanity-only. | Tie dashboard metrics to action list, owner, due date, and next review. |

---

# 11. Competitive Position Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-COMP-001 | Main competitors are identifiable. | Search results, client input. | Low score if business cannot name or see competitive set. | Build competitor list by service, location, and search visibility. |
| OI-COMP-002 | Business review profile is competitive. | Review comparison table. | Low score if competitors have materially stronger review count, rating, or recency. | Build review generation and response program. |
| OI-COMP-003 | Business has comparable service-page depth. | Competitor page inventory. | Low score if competitors have dedicated pages for services client lacks. | Build missing service pages based on competitive gap. |
| OI-COMP-004 | Business has stronger proof than competitors. | Gallery, testimonials, case studies comparison. | Low score if competitors show more work proof. | Add proof library, project gallery, before/after assets, and case studies. |
| OI-COMP-005 | Business message is differentiated. | Homepage copy comparison. | Low score if messaging sounds identical to competitors. | Define unique positioning and proof-backed differentiators. |
| OI-COMP-006 | Business appears in local search for target terms. | Search screenshots. | Low score if competitors appear consistently and client does not. | Prioritize local SEO and GBP optimization for target terms. |
| OI-COMP-007 | Competitors have stronger conversion paths. | CTA/form comparison. | Low score if competitors make inquiry easier. | Upgrade CTA, form, phone path, and estimate workflow. |
| OI-COMP-008 | Competitors have stronger content cadence. | Blog/social/GBP update comparison. | Low score if competitors publish more useful proof or education. | Build monthly content plan around services and projects. |
| OI-COMP-009 | Competitors show stronger brand polish. | Visual/design comparison. | Low score if client appears less professional or outdated. | Improve visual identity, page layout, photos, and trust presentation. |
| OI-COMP-010 | Competitive gap is documented in roadmap. | Final roadmap. | Low score if competitive findings do not translate into action. | Convert top gaps into prioritized initiatives. |

---

# 12. Offer and Sales System Criteria

| ID | Observable signal | Evidence to capture | Scoring guidance | Mapped recommendation |
|---|---|---|---|---|
| OI-OFFER-001 | Business has a clear entry offer. | Homepage, CTAs, sales materials. | Low score if prospect does not know whether to request estimate, inspection, consultation, or service. | Define primary entry offer and align all CTAs. |
| OI-OFFER-002 | High-value services are packaged clearly. | Service pages and proposal language. | Low score if profitable services lack clear positioning. | Create service packages or dedicated landing pages for high-value work. |
| OI-OFFER-003 | Pricing factors are explained when appropriate. | FAQs and service pages. | Low score if pricing uncertainty is unaddressed. | Add pricing-factor explanation without overcommitting to exact prices. |
| OI-OFFER-004 | Sales process is clear. | Website process section, client interview. | Low score if customer journey from inquiry to booked work is unclear. | Add sales/process map and internal SOP. |
| OI-OFFER-005 | Follow-up after estimate is consistent. | CRM, templates, owner interview. | Low score if open estimates are not systematically followed up. | Add estimate follow-up sequence and pipeline reminders. |
| OI-OFFER-006 | Lost reasons are captured. | CRM/report review. | Low score if the business does not know why prospects decline. | Add lost-reason fields and monthly review. |
| OI-OFFER-007 | Referral system exists. | Website, email/SMS templates, process docs. | Low score if satisfied customers are not prompted for referrals. | Add referral prompt after successful completion and review request. |
| OI-OFFER-008 | Retention or reactivation path exists. | CRM campaigns, customer list. | Low score if past customers are never recontacted. | Build seasonal, maintenance, or reactivation campaigns. |

---

# Summary Counts

Total criteria: **140 observable scoring signals**

| Category | Count |
|---|---:|
| Website structure and UX | 12 |
| Messaging and offer clarity | 10 |
| Conversion infrastructure | 14 |
| Local SEO | 16 |
| Google Business Profile | 12 |
| Reputation and trust | 12 |
| Social presence and content | 10 |
| Automation and operations | 14 |
| AI readiness and governance | 12 |
| Analytics and reporting | 10 |
| Competitive position | 10 |
| Offer and sales system | 8 |

---

# Next build layer

The next highest-leverage file is `scoring/recommendation-map.md`.

That file should convert repeated weak criteria into packaged implementation offers, for example:

- Website Conversion Fix Pack
- Local SEO Expansion Pack
- Google Business Profile Authority Pack
- Review Generation System
- CRM and Follow-Up System
- AI Intake Assistant
- Monthly Operator Dashboard
- Contractor Growth System
