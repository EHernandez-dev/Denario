<!-- filename: document-intelligence-automation-chatgpt-24hr-intensive.md -->
# Document Intelligence & Automation with ChatGPT — 24-hour Intensive (No-Code)

### Overview:
A hands-on, no-code intensive for analysts, operations leaders, and governance/compliance practitioners who must turn messy PDFs and scans into accurate, auditable decisions. The course scaffolds from prompting and context foundations to Vision/OCR extraction, ADA-based normalization/QA, redlining, retrieval-grounded Q&A (with Browse), governance, and enterprise deployment. Participants explicitly use Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads and multi-file analysis, Memory/Custom Instructions, and Custom GPTs with Knowledge and no-code Actions, plus GPT Store and Teams/Enterprise features.

## 1. Prompting & Context Foundations + Environment Setup (2:30)
### Description:
Institute a reproducible prompting discipline and secure platform posture that will govern the end-to-end pipeline. Calibrate RTCFCE (Role, Task, Context, Format, Constraints, Examples), ReAct, checklist prompts, and A/B prompt versioning to drive measurable, testable improvements. Configure Memory and Custom Instructions to encode privacy posture and grounded citation behavior. Verify access to Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, and the Custom GPT builder.

### Takeaways:
- Seeded RTCFCE/ReAct prompt library with A/B variants and selection rationale
- Memory/Custom Instructions that enforce privacy posture, tone, and citation style
- A/B evaluation checklist and logging template to reduce variance

### Learning Goals:
- Participants design RTCFCE and ReAct prompts and run A/B evaluations with logged outcomes.
- Participants configure Memory/Custom Instructions to constrain privacy and citation behavior.
- Participants verify access to ADA, Browse, Vision for PDFs/tables/images, image generation, and multi-file uploads.
- Participants define pass/fail criteria and versioning rules for prompt evolution.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

---

## 2. Vision/OCR for Messy PDFs, Tables, and Images (4:00)
### Description:
Engineer resilient extraction for degraded, heterogeneous sources using Vision for PDFs/tables/images with file uploads and multi-file analysis. Address recovery challenges: skew/low contrast, stamps/handwriting, multi-page tables, and mixed bundles. Implement structured error logging and a 5-point QA checklist to triage defects, guide remediation, and prepare for normalization in ADA.

### Takeaways:
- Extracted CSV(s) from Vision/OCR with error_log entries and a completed 5-point QA checklist
- Reusable prompt patterns for table/form extraction and page-level triage
- Remediation rubric for re-scan, batching, or manual correction

### Learning Goals:
- Participants batch-upload PDFs/images and extract tabular/form data using Vision for PDFs/tables/images.
- Participants log OCR anomalies (split/merged cells, header loss, misreads) in error_log.csv with examples.
- Participants apply the 5-point QA checklist to decide re-scan versus remediation.
- Participants design fallback prompting and batching strategies for problematic pages.

### Exercise Description:
Duration: 150 minutes, Debrief: 30 minutes

---

## 3. ADA Normalization & Reproducibility (3:00)
### Description:
Normalize extracted data to a canonical schema inside ADA. Enforce typing, unit harmonization, controlled vocabularies, and schema validation; produce anomaly_report.csv and maintain change_log.csv so every transformation is auditable and reproducible. Emphasize deterministic re-runs and versioned filenames aligned with governance.

### Takeaways:
- normalized.csv with canonical fields/types/units
- anomaly_report.csv covering outliers, missingness, and schema violations
- change_log.csv documenting transformations and decision rationale

### Learning Goals:
- Participants define canonical schemas and normalization rules (dates, currency, units, taxonomies).
- Participants generate anomaly reports and set acceptance thresholds.
- Participants re-run normalization to verify determinism and document residual variance.
- Participants apply consistent naming/versioning conventions for traceability.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

---

## 4. Redlining & Document Comparison (2:30)
### Description:
Operationalize redlining using Vision and ADA across contracts, policies, SOPs, and structured appendices. Extract clause/table-level diffs, classify risk-bearing edits, and produce executive-ready summaries. Optionally use image generation to produce annotated visual highlights aligned with textual diffs.

### Takeaways:
- Redline diffs and a structured change_summary with risk/impact annotations
- Prompt patterns for section/paragraph/table alignment and comparison
- Optional visual highlights to accelerate stakeholder review

### Learning Goals:
- Participants align comparable sections and extract granular diffs via Vision and ADA.
- Participants classify changes by business risk and escalation triggers.
- Participants produce stakeholder-ready redline briefs with optional visual annotations.
- Participants document assumptions for reflowed text, scanned markups, and embedded images.

### Exercise Description:
Duration: 80 minutes, Debrief: 30 minutes

---

## 5. Knowledge-backed Q&A with Custom GPTs (3:00)
### Description:
Stand up a Custom GPT with Knowledge files for grounded Q&A and correct abstention. Use Custom Instructions to enforce citations, privacy posture, tone, and safety; configure retrieval options. Build a 10-question retrieval QA suite and log outcomes in retrieval_test_log.csv. Introduce no-code Actions via structured outputs for predictable downstream handoffs.

### Takeaways:
- Custom GPT scaffold with Knowledge uploaded and retrieval configured
- 10-question retrieval QA suite with pass/fail, citations, and abstentions logged
- Structured output templates tailored for no-code Actions and downstream consumers

### Learning Goals:
- Participants configure a Custom GPT with Knowledge and enforce citation/abstention rules.
- Participants design and run a retrieval QA suite with quantifiable thresholds.
- Participants produce structured outputs for reliable downstream consumption.
- Participants document tuning levers (chunking, file formats, Knowledge refresh cadence).

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

---

## 6. Browsing, Grounding, and Citations Under Uncertainty (1:45)
### Description:
Enable Browse to incorporate time-sensitive or external evidence within scoped domains. Practice verification steps, decide when to answer versus abstain, and document link provenance and evidence quality. Integrate browsed evidence with Knowledge-backed responses without compromising auditability.

### Takeaways:
- Browse policy template with domain allowlists and source-quality criteria
- Citation exemplars with verification notes and link provenance
- Safe-failure and escalation patterns for ambiguous or out-of-distribution prompts

### Learning Goals:
- Participants configure Browse within constrained domains and capture traceable citations.
- Participants validate sources and record verification steps aligned to governance.
- Participants implement abstention and escalation when evidence is insufficient or stale.
- Participants integrate Browse and Knowledge responses while preserving provenance.

### Exercise Description:
Duration: 70 minutes, Debrief: 35 minutes

---

## 7. Governance, Privacy, and Auditability for Enterprise (3:30)
### Description:
Translate QA metrics into enforceable governance aligned with Teams/Enterprise data controls, Memory policy, GPT Store policies, artifact versioning, and retention. Draft a governance SOP and privacy checklist; define a risk-rating rubric over common document types (contracts, invoices, PHI, IP) and legal escalation triggers. Codify audit trails, timestamp/version conventions, and reviewer sign-offs.

### Takeaways:
- Governance SOP and privacy checklist aligned to enterprise controls
- Audit-trail template and versioning/timestamp conventions
- Risk-rating rubric with sign-off triggers and escalation criteria

### Learning Goals:
- Participants author a governance SOP tied to retrieval QA and normalization thresholds.
- Participants complete a privacy checklist and define retention/versioning conventions.
- Participants apply risk ratings and identify legal/contractual sign-off criteria.
- Participants configure Teams/Enterprise sharing and data controls to meet policy.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

---

## 8. Deployment via Teams/Enterprise and GPT Store (1:45)
### Description:
Operationalize internal sharing and optional publication workflows. Configure Teams/Enterprise org sharing, collections, and permissions; evaluate GPT Store norms for publication where permitted. Establish release cadence, change notes, rollback plans, and a consumer SOP to standardize no-code handoffs.

### Takeaways:
- Deployment plan with scoped access/permissions and release/rollback procedures
- Consumer SOP with stable inputs/outputs and incident response paths
- Readiness checklist for internal-only versus GPT Store publication

### Learning Goals:
- Participants configure Teams/Enterprise sharing and least-privilege permission models.
- Participants prepare versioned releases with change notes and rollback plans.
- Participants draft a consumer SOP for safe, repeatable downstream use.
- Participants assess GPT Store publication options against policy constraints.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

---

## 9. Capstone Build: End-to-End Doc-to-Decision Pipeline (1:30)
### Description:
Integrate Vision/OCR extraction, ADA normalization, redlining, Knowledge-backed Q&A with Browse, and governance into a cohesive pipeline. Produce a decision memo with grounded citations and attach all supporting, versioned artifacts. Validate performance against predefined QA thresholds and governance rules.

### Takeaways:
- Full pipeline run with linked, versioned artifacts and audit trail
- Decision memo with citations and appended governance SOP and privacy checklist
- Self-assessed pass/fail outcome mapped to rubric thresholds

### Learning Goals:
- Participants execute the pipeline on a fresh document pack meeting accuracy/governance thresholds.
- Participants assemble and cross-reference artifacts coherently in a decision memo.
- Participants identify limitations and propose prioritized improvements for deployment.

### Exercise Description:
Duration: 75 minutes, Debrief: 15 minutes

---

## 10. Defense, Assessment, and Handover (0:30)
### Description:
Defend the capstone pipeline with a concise walkthrough of artifacts, QA metrics, and governance posture. Formalize Teams/Enterprise deployment steps and record pass/fail with rationale. Capture peer/facilitator feedback to inform productionization and scaling.

### Takeaways:
- Peer-reviewed feedback and facilitator rubric scores
- Documented pass/fail decision, deployment readiness, and risk mitigations
- Targeted post-course roadmap and recommended follow-ups

### Learning Goals:
- Participants defend design choices using evidence from logs, metrics, and citations.
- Participants finalize deployment readiness including permissions and rollback plans.
- Participants select follow-up modules to deepen retrieval QA and no-code Actions.

### Exercise Description:
Duration: 20 minutes, Debrief: 10 minutes

---

### Course Deliverables (Participant Artifacts)
- Prompt library: ten RTCFCE prompts with A/B scores and selection rationale.
- Document extraction and QA pack: extracted CSV(s) from Vision/OCR dirty docs + error_log.csv + completed 5-point QA checklist.
- ADA normalization report: normalized.csv + anomaly_report.csv + change_log.csv demonstrating reproducibility.
- Custom GPT scaffold with Knowledge files and retrieval_test_log.csv, plus a governance SOP and privacy checklist for the workflow.

---

### Further Resources for Course Organizers (Preparation)
- OpenAI platform status and feature availability: https://status.openai.com
- Advanced Data Analysis (ADA): https://help.openai.com/en/articles/8554397-advanced-data-analysis
- Vision for PDFs/tables/images: https://platform.openai.com/docs/guides/vision
- Browse capability: https://help.openai.com/en/articles/8554400-browsing
- Custom GPTs and Knowledge: https://help.openai.com/en/articles/8554408-custom-gpts
- Teams/Enterprise features and admin: https://openai.com/enterprise
- GPT Store guidelines and policies: https://openai.com/blog/introducing-the-gpt-store
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Accessibility (WCAG 2.1): https://www.w3.org/WAI/standards-guidelines/wcag/

### Further Resources for Participants (Learning)
- OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering
- ReAct prompting pattern: https://arxiv.org/abs/2210.03629
- Evaluating LLMs (test suites and metrics): https://arxiv.org/abs/2307.03109
- Practical data cleaning and normalization: https://library.carleton.ca/guides/data-cleaning
- Responsible AI practices (governance basics): https://ai.google/responsibilities/responsible-ai-practices
- Contract redlining primer: https://www.americanbar.org/groups/business_law/publications/committee_newsletters/CL182000/
- Versioning and audit trails in data projects: https://dvc.org/doc/start

Notes to facilitation:
- Explicitly name and demonstrate the following tools/features in each lab as applicable: Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, Memory/Custom Instructions, Custom GPTs with Knowledge and no-code Actions, GPT Store, and Teams/Enterprise controls.
- Maintain a strict no-code policy while leveraging structured outputs, checklists, and rubrics to ensure accuracy, grounded citations, and reproducibility.