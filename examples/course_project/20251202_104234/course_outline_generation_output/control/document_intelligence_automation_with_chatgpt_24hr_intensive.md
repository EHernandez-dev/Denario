<!-- filename: document_intelligence_automation_with_chatgpt_24hr_intensive.md -->
# Document Intelligence & Automation with ChatGPT — 24-hour Intensive (No-Code)

### Overview:
This hands-on intensive equips professionals to transform messy PDFs, scans, and mixed document bundles into accurate, auditable decisions without writing code. Across ten scaffolded modules, participants will operationalize Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads and multi-file analysis, Memory/Custom Instructions, and Custom GPTs with Knowledge and no-code Actions, plus GPT Store and Teams/Enterprise features. The culminating capstone produces a validated doc-to-decision workflow with grounded citations, QA metrics, and a governance SOP ready for team deployment.

## 1. Prompting & Context Foundations + Environment Setup
### Description:
Establish a reproducible prompting discipline and a secure, auditable platform posture before touching documents. Calibrate RTCFCE (Role, Task, Context, Format, Constraints, Examples), ReAct, checklist prompts, and A/B prompt versioning to produce measurable gains. Configure Memory and Custom Instructions to encode privacy stance, citation behavior, role fidelity, and escalation. Verify feature access to ADA, Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, and the Custom GPT builder to de-risk downstream labs.

### Takeaways:
- Seeded RTCFCE/ReAct prompt library with A/B variants and selection rationale.
- Memory and Custom Instructions configured for privacy posture and grounded citations.
- A/B evaluation checklist and logging template for reproducible prompt trials.

### Learning Goals:
- Participants design RTCFCE and ReAct prompts and run A/B comparisons with logged outcomes.
- Participants configure Memory/Custom Instructions to enforce privacy and citation constraints.
- Participants verify access to ADA, Browse, Vision, image generation, and multi-file uploads.
- Participants define pass/fail criteria and versioning rules for prompt evolution.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

## 2. Vision/OCR for Messy PDFs, Tables, and Images
### Description:
Develop resilient extraction workflows for degraded and heterogeneous sources using Vision for PDFs/tables/images and file uploads/multi-file analysis. Address skew, low contrast, stamps/handwriting, and multi-page tables; implement structured error logging and a 5-point QA checklist to triage defects and guide remediation. Stabilize prompt patterns for page segmentation, table/form extraction, and mixed bundles.

### Takeaways:
- Extracted CSV(s) from Vision/OCR plus error_log and completed 5-point QA checklist.
- Reusable prompt patterns for tables/forms and page-level triage.
- Remediation rubric for re-scan, rebatching, or manual correction triggers.

### Learning Goals:
- Participants batch-upload PDFs/images and extract tabular/form data with Vision.
- Participants log OCR anomalies (split/merged cells, header loss, misreads) with examples.
- Participants apply the 5-point QA checklist to decide remediation priorities.
- Participants design fallback prompting and batching strategies for problematic pages.

### Exercise Description:
Duration: 150 minutes, Debrief: 30 minutes

## 3. ADA Normalization & Reproducibility
### Description:
Normalize extracted data to a canonical schema in ADA, enforcing data typing, unit harmonization, controlled vocabularies, and schema validation. Generate anomaly_report and maintain change_log so every transformation is auditable and reproducible. Emphasize deterministic re-runs, versioned filenames, and artifact lineage to satisfy governance.

### Takeaways:
- normalized.csv with canonical fields, types, and units.
- anomaly_report capturing outliers, missingness, and schema violations.
- change_log documenting transformation steps and decision rationale.

### Learning Goals:
- Participants define canonical schemas and normalization rules (dates, currencies, units, taxonomies).
- Participants generate anomaly reports and set acceptance thresholds.
- Participants re-run normalization to verify determinism and document residual variance.
- Participants apply naming/versioning conventions for traceability across artifacts.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 4. Redlining & Document Comparison
### Description:
Operationalize redlining with Vision and ADA across contracts, policies, SOPs, and structured appendices. Extract clause/table-level diffs, classify risk-bearing edits, and produce executive-ready change summaries. Use image generation to optionally annotate visual highlights aligned with textual diffs to accelerate stakeholder review.

### Takeaways:
- Redline brief with structured change summaries and risk/impact annotations.
- Prompt patterns for section/paragraph/table alignment and comparison.
- Optional annotated visuals for faster stakeholder comprehension.

### Learning Goals:
- Participants align comparable sections and extract granular diffs using Vision and ADA.
- Participants classify changes by business risk and escalation triggers.
- Participants produce stakeholder-ready redline summaries with optional visual highlights.
- Participants document handling strategies for reflowed text, scanned markups, and embedded images.

### Exercise Description:
Duration: 80 minutes, Debrief: 30 minutes

## 5. Knowledge-backed Q&A with Custom GPTs
### Description:
Stand up a Custom GPT with Knowledge files for grounded Q&A and correct abstention. Use Custom Instructions to enforce citation format, privacy posture, tone, and safety; calibrate retrieval options (chunking, metadata) and build a 10-question retrieval QA suite logged to a retrieval test log. Introduce no-code Actions via structured outputs (JSON-like responses) to enable predictable downstream handoffs.

### Takeaways:
- Custom GPT scaffold with Knowledge uploaded and retrieval options calibrated.
- 10-question retrieval QA suite with logged pass/fail, citations, and abstentions.
- Structured output template for no-code Actions readiness.

### Learning Goals:
- Participants configure a Custom GPT with Knowledge and enforce citation/abstention rules.
- Participants design and run a retrieval QA suite with measurable thresholds.
- Participants produce structured outputs for reliable handoffs to non-technical consumers.
- Participants document tuning levers (chunking, file formats, Knowledge refresh cadence).

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 6. Browsing, Grounding, and Citations Under Uncertainty
### Description:
Enable Browse to incorporate time-sensitive or external evidence within constrained domains. Practice verification steps, decide when to answer versus abstain, and document link provenance and source quality. Integrate browsed evidence with Knowledge-backed responses without compromising auditability.

### Takeaways:
- Browse policy template with domain allowlists and source-quality criteria.
- Citation exemplars with verification notes and link provenance.
- Safe-failure and escalation patterns for ambiguous or out-of-distribution prompts.

### Learning Goals:
- Participants configure Browse within scoped domains and capture traceable citations.
- Participants validate sources and record verification steps aligned to governance.
- Participants implement abstention and escalation when evidence is insufficient.
- Participants integrate browsed and Knowledge responses while preserving provenance.

### Exercise Description:
Duration: 70 minutes, Debrief: 35 minutes

## 7. Governance, Privacy, and Auditability for Enterprise
### Description:
Translate QA metrics into enforceable governance using Teams/Enterprise controls, Memory policy, GPT Store policies, artifact versioning, and retention. Draft a governance SOP and privacy checklist; define a risk-rating rubric across document types (contracts, invoices, PHI, IP) and legal escalation triggers. Codify audit trails, timestamp/version conventions, and reviewer sign-offs.

### Takeaways:
- Governance SOP and privacy checklist (data minimization, retention, consent).
- Audit-trail template with timestamp and versioning conventions.
- Risk-rating rubric with sign-off triggers and legal escalation points.

### Learning Goals:
- Participants author a governance SOP tied to retrieval QA and normalization thresholds.
- Participants complete a privacy checklist and define retention/versioning conventions.
- Participants apply risk ratings and identify legal/contractual sign-off criteria.
- Participants configure Teams/Enterprise sharing and data controls to meet policy.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 8. Deployment via Teams/Enterprise and GPT Store
### Description:
Operationalize internal sharing and optional external publication. Configure Teams/Enterprise org sharing, collections, and permissions; evaluate GPT Store publication constraints and readiness. Establish release cadence, change notes, rollback plans, and a consumer SOP to standardize no-code handoffs to downstream users.

### Takeaways:
- Deployment plan with scoped access/permissions and release/rollback procedures.
- Consumer SOP defining stable inputs/outputs and incident response paths.
- Readiness checklist for internal-only versus GPT Store publication.

### Learning Goals:
- Participants configure Teams/Enterprise sharing and least-privilege permission models.
- Participants prepare versioned releases with change notes and rollback plans.
- Participants draft a consumer SOP for safe, repeatable downstream use.
- Participants evaluate GPT Store publication options against policy constraints.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

## 9. Capstone Build: End-to-End Doc-to-Decision Pipeline
### Description:
Integrate Vision/OCR extraction, ADA normalization, redlining, Knowledge-backed Q&A with Browse, and governance into a cohesive pipeline. Produce a decision memo with grounded citations and append all supporting artifacts (extractions, normalized.csv, anomaly_report, change_log, retrieval_test_log, governance SOP, privacy checklist). Validate performance against predefined QA thresholds.

### Takeaways:
- Full pipeline run with linked, versioned artifacts and audit trail.
- Decision memo with citations and appended governance SOP and privacy checklist.
- Self-assessed pass/fail outcome mapped to rubric thresholds.

### Learning Goals:
- Participants execute the pipeline on a fresh document pack meeting accuracy/governance thresholds.
- Participants assemble and cross-reference artifacts coherently in a decision memo.
- Participants identify limitations and propose prioritized improvements for deployment.

### Exercise Description:
Duration: 75 minutes, Debrief: 15 minutes

## 10. Defense, Assessment, and Handover
### Description:
Defend the capstone with a concise walkthrough of artifacts, QA metrics, and governance posture. Formalize Teams/Enterprise deployment steps and record pass/fail with rationale; capture peer/facilitator feedback for productionization and scaling. Align targeted next steps to mature retrieval QA and no-code Actions.

### Takeaways:
- Peer-reviewed feedback and facilitator rubric scores.
- Documented pass/fail decision, deployment readiness, and risk mitigations.
- Targeted post-course roadmap and recommended follow-ups.

### Learning Goals:
- Participants defend design choices using evidence from logs, metrics, and citations.
- Participants finalize deployment readiness including permissions and rollback plans.
- Participants select follow-up modules to deepen capability in retrieval QA and no-code Actions.

### Exercise Description:
Duration: 20 minutes, Debrief: 10 minutes

---

Further resources for course organizers (preparation):
- OpenAI status and feature availability: https://status.openai.com
- Advanced Data Analysis (ADA): https://help.openai.com/en/articles/8554397-advanced-data-analysis
- Vision for PDFs/tables/images: https://platform.openai.com/docs/guides/vision
- Browse capability: https://help.openai.com/en/articles/8554400-browsing
- Custom GPTs and Knowledge: https://help.openai.com/en/articles/8554408-custom-gpts
- Teams/Enterprise features and admin: https://openai.com/enterprise
- GPT Store guidelines and policies: https://openai.com/blog/introducing-the-gpt-store
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Accessibility (WCAG 2.1): https://www.w3.org/WAI/standards-guidelines/wcag/

Further resources for participants (learning):
- OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering
- ReAct prompting pattern: https://arxiv.org/abs/2210.03629
- Evaluating LLMs (test suites and metrics): https://arxiv.org/abs/2307.03109
- Practical data cleaning and normalization: https://library.carleton.ca/guides/data-cleaning
- Responsible AI practices (governance basics): https://ai.google/responsibilities/responsible-ai-practices
- Contract redlining primer: https://www.americanbar.org/groups/business_law/publications/committee_newsletters/CL182000/
- Versioning and audit trails in data projects: https://dvc.org/doc/start

Recommended next steps (optional follow-ups):
- Advanced Knowledge Retrieval QA (2 hours): configure multi-file Knowledge sets and achieve ≥95% grounded answers with correct abstention; build a 10-question retrieval QA suite with pass/fail criteria.
- No-Code Actions via Structured Outputs (3 hours): design stable JSON schemas for handoffs, validate schema conformance, and document a mock consumer SOP for downstream tools.