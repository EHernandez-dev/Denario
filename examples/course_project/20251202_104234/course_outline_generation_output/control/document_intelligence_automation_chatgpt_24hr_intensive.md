<!-- filename: document_intelligence_automation_chatgpt_24hr_intensive.md -->
# Document Intelligence & Automation with ChatGPT — 24-hour Intensive (No-Code)

### Overview:
A hands-on, no-code intensive for professionals who must convert messy PDFs, scans, and mixed document bundles into accurate, auditable decisions. The course scaffolds from prompting/context foundations to Vision/OCR extraction, ADA-based normalization/QA, redlining, knowledge-backed Q&A with Browse, governance, and enterprise deployment. Participants explicitly use Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads and multi-file analysis, Memory/Custom Instructions, and Custom GPTs with Knowledge and no-code Actions, plus GPT Store and Teams/Enterprise features.

## 1. Prompting & Context Foundations + Environment Setup
### Description:
Establish a reproducible prompting discipline and secure platform posture that anchor the pipeline. Calibrate RTCFCE (Role, Task, Context, Format, Constraints, Examples), ReAct, checklist prompts, and A/B prompt versioning to produce measurable, testable improvements. Configure Memory and Custom Instructions to encode privacy posture, grounded citation norms, and domain tone. Verify access to Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, and the Custom GPT builder.
### Takeaways:
- A seeded RTCFCE/ReAct prompt library with A/B variants and selection rationale.
- Memory/Custom Instructions that enforce privacy posture and citation style.
- An A/B evaluation checklist and logging template for stable iteration.
### Learning Goals:
- Participants design RTCFCE and ReAct prompts and run A/B evaluations with logged outcomes.
- Participants configure Memory/Custom Instructions to constrain privacy, tone, and citations.
- Participants verify access to ADA, Browse, Vision for PDFs/tables/images, image generation, and multi-file uploads.
- Participants define pass/fail criteria and versioning rules for prompt evolution.
### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

## 2. Vision/OCR for Messy PDFs, Tables, and Images
### Description:
Engineer resilient extraction for degraded, heterogeneous sources using Vision for PDFs/tables/images with file uploads and multi-file analysis. Address page segmentation, multi-page tables, skew/low contrast, stamps/handwriting, and mixed bundles. Implement structured error logging and a 5-point QA checklist to triage defects and guide remediation.
### Takeaways:
- Extracted CSV(s) from Vision/OCR with error_log.csv and a completed 5-point QA checklist.
- Stable prompt patterns for tables/forms and page-level triage across document types.
- A remediation rubric for re-scan, batching, or manual correction.
### Learning Goals:
- Participants batch-upload PDFs/images and extract table/form data using Vision for PDFs/tables/images.
- Participants log OCR anomalies (split/merged cells, header loss, misreads) in error_log.csv with examples.
- Participants apply the 5-point QA checklist to decide re-scan versus remediation.
- Participants design fallback prompts and batching strategies for problematic pages.
### Exercise Description:
Duration: 150 minutes, Debrief: 30 minutes

## 3. ADA Normalization & Reproducibility
### Description:
Normalize extracted data to a canonical schema in ADA, enforcing data typing, unit harmonization, controlled vocabularies, and schema validation. Produce anomaly_report.csv and maintain change_log.csv so every transformation is auditable and reproducible. Emphasize deterministic re-runs and versioned filenames.
### Takeaways:
- normalized.csv with canonical fields/types/units.
- anomaly_report.csv capturing outliers, missingness, and schema violations.
- change_log.csv documenting transformation steps and decision rationale.
### Learning Goals:
- Participants define canonical schemas and normalization rules (dates, currency, units, taxonomies).
- Participants generate anomaly reports and set acceptance thresholds.
- Participants re-run normalization to verify determinism and document residual variance.
- Participants apply naming/versioning conventions for traceable artifacts.
### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 4. Redlining & Document Comparison
### Description:
Operationalize redlining using Vision and ADA across contracts, policies, SOPs, and structured appendices. Extract clause/table-level diffs, classify risk-bearing edits, and produce executive-ready change summaries. Optionally use image generation to create annotated visual highlights aligned with textual diffs.
### Takeaways:
- Redline diffs and a structured change_summary with risk/impact annotations.
- Prompt patterns for section/paragraph/table alignment and comparison.
- Optional visual highlights to accelerate stakeholder review.
### Learning Goals:
- Participants align comparable sections and extract granular diffs via Vision and ADA.
- Participants classify material changes by business risk and escalation triggers.
- Participants produce stakeholder-ready redline summaries with optional visual highlights.
- Participants document assumptions for reflowed text, scanned markups, and embedded images.
### Exercise Description:
Duration: 80 minutes, Debrief: 30 minutes

## 5. Knowledge-backed Q&A with Custom GPTs
### Description:
Stand up a Custom GPT with Knowledge files for grounded Q&A and correct abstention. Use Custom Instructions to enforce citations, privacy posture, tone, and safety; configure retrieval options (chunking/metadata). Build a 10-question retrieval QA suite and log outcomes in retrieval_test_log.csv. Introduce no-code Actions via structured outputs for predictable downstream handoffs.
### Takeaways:
- A Custom GPT scaffold with Knowledge uploaded and retrieval tuned for grounded answers.
- A retrieval QA suite with pass/fail results, citations, and abstentions.
- Structured output templates suitable for no-code Actions.
### Learning Goals:
- Participants configure a Custom GPT with Knowledge and enforce citation/abstention rules.
- Participants design and run a retrieval QA suite with quantifiable thresholds.
- Participants produce structured outputs for reliable downstream consumption.
- Participants document tuning levers (chunking strategy, file formats, Knowledge refresh cadence).
### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 6. Browsing, Grounding, and Citations Under Uncertainty
### Description:
Enable Browse to incorporate time-sensitive or external evidence within scoped domains. Practice verification steps, decide when to answer versus abstain, and document link provenance and evidence quality. Integrate browsed evidence with Knowledge-backed responses while preserving auditability.
### Takeaways:
- A browse policy template with domain allowlists and source-quality criteria.
- Citation exemplars with verification notes and link provenance.
- Safe-failure and escalation patterns for ambiguous or out-of-distribution prompts.
### Learning Goals:
- Participants configure Browse within constrained domains and capture traceable citations.
- Participants validate sources and record verification steps aligned to governance.
- Participants implement abstention and escalation when evidence is insufficient or stale.
- Participants integrate Browse and Knowledge responses while preserving provenance.
### Exercise Description:
Duration: 70 minutes, Debrief: 35 minutes

## 7. Governance, Privacy, and Auditability for Enterprise
### Description:
Translate QA metrics into enforceable governance aligned with Teams/Enterprise data controls, Memory policy, GPT Store policies, artifact versioning, and retention. Draft a governance SOP and privacy checklist; define a risk-rating rubric across document types (contracts, invoices, PHI, IP) and legal escalation triggers. Codify audit trails, timestamp/version conventions, and reviewer sign-offs.
### Takeaways:
- A governance SOP and privacy checklist aligned to enterprise controls.
- An audit-trail template and versioning/timestamp conventions.
- A risk-rating rubric with sign-off triggers and escalation criteria.
### Learning Goals:
- Participants author a governance SOP tied to retrieval QA and normalization thresholds.
- Participants complete a privacy checklist and define retention/versioning conventions.
- Participants apply risk ratings and identify legal/contractual sign-off criteria.
- Participants configure Teams/Enterprise sharing and data controls to meet policy.
### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 8. Deployment via Teams/Enterprise and GPT Store
### Description:
Operationalize internal sharing and optional publication workflows. Configure Teams/Enterprise org sharing, collections, and permissions; evaluate GPT Store norms where permitted. Establish release cadence, change notes, rollback plans, and a consumer SOP to standardize no-code handoffs.
### Takeaways:
- A deployment plan with scoped access/permissions and release/rollback procedures.
- A consumer SOP with stable inputs/outputs and incident response paths.
- A readiness checklist for internal-only versus GPT Store publication.
### Learning Goals:
- Participants configure Teams/Enterprise sharing with least-privilege permission models.
- Participants prepare versioned releases with change notes and rollback plans.
- Participants draft a consumer SOP for safe, repeatable downstream use.
- Participants assess GPT Store publication options against policy constraints.
### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

## 9. Capstone Build: End-to-End Doc-to-Decision Pipeline
### Description:
Integrate Vision/OCR extraction, ADA normalization, redlining, Knowledge-backed Q&A with Browse, and governance into a cohesive pipeline. Produce a decision memo with grounded citations and attach all supporting, versioned artifacts. Validate performance against predefined QA thresholds and governance rules.
### Takeaways:
- A full pipeline run with linked, versioned artifacts and an audit trail.
- A decision memo with citations and appended governance SOP and privacy checklist.
- A self-assessed pass/fail outcome mapped to rubric thresholds.
### Learning Goals:
- Participants execute the pipeline on a fresh document pack meeting accuracy/governance thresholds.
- Participants assemble and cross-reference artifacts coherently in a decision memo.
- Participants identify limitations and propose prioritized improvements.
### Exercise Description:
Duration: 75 minutes, Debrief: 15 minutes

## 10. Defense, Assessment, and Handover
### Description:
Defend the capstone pipeline with a concise walkthrough of artifacts, QA metrics, and governance posture. Formalize Teams/Enterprise deployment steps and record pass/fail with rationale. Capture peer/facilitator feedback to inform productionization and scaling.
### Takeaways:
- Peer-reviewed feedback and facilitator rubric scores.
- Documented pass/fail decision, deployment readiness, and risk mitigations.
- A targeted post-course roadmap and recommended follow-ups.
### Learning Goals:
- Participants defend design choices using evidence from logs, metrics, and citations.
- Participants finalize deployment readiness including permissions and rollback plans.
- Participants select follow-up modules to deepen retrieval QA and no-code Actions.
### Exercise Description:
Duration: 20 minutes, Debrief: 10 minutes

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