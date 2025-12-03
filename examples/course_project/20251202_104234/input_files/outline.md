# Document Intelligence & Automation with ChatGPT — 24-hour Intensive (No-Code)

### Overview:
A hands-on, no-code intensive for professionals who must convert messy PDFs, scans, and mixed document bundles into accurate, auditable decisions. The course scaffolds from prompting/context foundations through Vision/OCR extraction, ADA-based normalization/QA, redlining, retrieval-grounded Q&A with Browse, governance, and enterprise deployment. Participants explicitly use Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads and multi-file analysis, Memory/Custom Instructions, and Custom GPTs with Knowledge and no-code Actions, plus GPT Store and Teams/Enterprise features.

## 1. Prompting & Context Foundations + Environment Setup (2:30)
### Description:
Establish a reproducible prompting discipline and secure platform posture that anchor the pipeline. Calibrate RTCFCE (Role, Task, Context, Format, Constraints, Examples), ReAct, checklist prompts, and A/B prompt versioning to achieve measurable, testable improvements. Configure Memory and Custom Instructions to encode privacy posture, grounded citation norms, and domain tone. Verify access to ADA, Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, and the Custom GPT builder.

### Takeaways:
- Seeded RTCFCE/ReAct prompt library with A/B variants and selection rationale.
- Memory/Custom Instructions that enforce privacy and citation standards.
- A/B evaluation checklist and logging template to reduce variance.

### Learning Goals:
- Participants design RTCFCE and ReAct prompts and run A/B evaluations with logged outcomes.
- Participants configure Memory/Custom Instructions to constrain privacy, tone, and citations.
- Participants verify access to ADA, Browse, Vision, image generation, and multi-file uploads.
- Participants define pass/fail criteria and versioning rules for prompt evolution.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

Instructor Note (Fallback):
- Primary features: Memory, Custom Instructions, file uploads/multi-file analysis.
- Fallback if Memory is unavailable: paste a standardized “preamble” into each session; store preamble text in the prompt_library.

---

## 2. Vision/OCR for Messy PDFs, Tables, and Images (4:00)
### Description:
Engineer resilient extraction for dirty scans and heterogeneous PDFs using Vision for PDFs/tables/images with multi-file uploads. Address page segmentation, multi-page tables, skew/low contrast, stamps/handwriting, and mixed bundles. Implement error logging and a 5-point QA checklist to triage defects and guide remediation.

### Takeaways:
- Extracted CSV(s) with error_log.csv and a completed 5-point QA checklist.
- Stable prompt patterns for tables/forms and page-level triage.
- Remediation rubric for re-scan, batching, or manual correction.

### Learning Goals:
- Participants batch-upload PDFs/images and extract tables/forms using Vision.
- Participants log OCR anomalies (split/merged cells, header loss, misreads) in error_log.csv.
- Participants apply the 5-point QA checklist to set remediation priorities.
- Participants design fallback prompts and batching strategies for problematic pages.

### Exercise Description:
Duration: 150 minutes, Debrief: 30 minutes

Instructor Note (Fallback):
- Primary features: Vision for PDFs/tables/images, file uploads/multi-file analysis.
- Fallback if Vision degrades: use ADA file preview to ingest text; apply constrained table parsing prompts; provide pre-OCR’d snapshots if required.

---

## 3. ADA Normalization & Reproducibility (3:00)
### Description:
Normalize extracted data to a canonical schema in ADA. Enforce typing, unit harmonization, controlled vocabularies, and schema validation; produce anomaly_report.csv and maintain change_log.csv so every transformation is auditable and reproducible. Emphasize deterministic re-runs and versioned filenames.

### Takeaways:
- normalized.csv with canonical fields/types/units.
- anomaly_report.csv capturing outliers, missingness, and schema violations.
- change_log.csv documenting transformation steps and rationale.

### Learning Goals:
- Participants define canonical schemas and normalization rules (dates, currency, units, taxonomies).
- Participants generate anomaly reports and set acceptance thresholds.
- Participants re-run normalization to verify determinism and document residual variance.
- Participants apply naming/versioning conventions for traceable artifacts.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

Instructor Note (Fallback):
- Primary features: ADA, file uploads.
- Fallback if ADA is unavailable: use a spreadsheet with validation/filters; replicate steps and justifications in change_log.csv.

---

## 4. Redlining & Document Comparison (2:30)
### Description:
Operationalize redlining using Vision and ADA across contracts, policies, SOPs, and structured appendices. Extract clause/table-level diffs, classify risk-bearing edits, and produce executive-ready summaries. Optionally leverage image generation for annotated highlights aligned with textual diffs.

### Takeaways:
- Redline diffs and a structured change_summary with risk/impact annotations.
- Prompt patterns for section/paragraph/table alignment and comparison.
- Optional visual highlights to accelerate stakeholder review.

### Learning Goals:
- Participants align comparable sections and extract granular diffs via Vision and ADA.
- Participants classify changes by business risk and escalation triggers.
- Participants produce stakeholder-ready redline briefs with optional visual annotations.
- Participants document assumptions for reflowed text and scanned markups.

### Exercise Description:
Duration: 80 minutes, Debrief: 30 minutes

Instructor Note (Fallback):
- Primary features: Vision, ADA, image generation.
- Fallback if image generation is disabled: provide textual diff tables; note highlight coordinates for manual annotation.

---

## 5. Knowledge-backed Q&A with Custom GPTs (3:00)
### Description:
Stand up a Custom GPT with Knowledge files for grounded Q&A and correct abstention. Use Custom Instructions to enforce citations, privacy posture, tone, and safety; configure retrieval options (e.g., chunking/metadata). Build a 10-question retrieval QA suite and log outcomes in retrieval_test_log.csv. Introduce no-code Actions via structured outputs for predictable handoffs.

### Takeaways:
- Custom GPT scaffold with Knowledge uploaded and retrieval tuned for grounded answers.
- A retrieval QA suite with pass/fail results, citations, and abstentions.
- Structured output templates suitable for no-code Actions.

### Learning Goals:
- Participants configure a Custom GPT with Knowledge and enforce citation/abstention rules.
- Participants design and run a retrieval QA suite with quantifiable thresholds.
- Participants produce structured outputs for reliable downstream consumption.
- Participants document tuning levers (chunking, file formats, Knowledge refresh cadence).

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

Instructor Note (Fallback):
- Primary features: Custom GPT builder, Knowledge, Custom Instructions.
- Fallback if builder is unavailable: emulate with ChatGPT + file uploads in-session; maintain retrieval_test_log.csv manually.

---

## 6. Browsing, Grounding, and Citations Under Uncertainty (1:45)
### Description:
Enable Browse to incorporate time-sensitive or external evidence within scoped domains. Practice verification steps, decide when to answer versus abstain, and document link provenance and evidence quality. Integrate browsed evidence with Knowledge-backed responses while preserving auditability.

### Takeaways:
- Browse policy template with domain allowlists and source-quality criteria.
- Citation exemplars with verification notes and link provenance.
- Safe-failure and escalation patterns for ambiguous or out-of-distribution prompts.

### Learning Goals:
- Participants configure Browse within constrained domains and capture traceable citations.
- Participants validate sources and record verification steps aligned to governance.
- Participants implement abstention and escalation when evidence is insufficient or stale.
- Participants integrate Browse and Knowledge responses while preserving provenance.

### Exercise Description:
Duration: 70 minutes, Debrief: 35 minutes

Instructor Note (Fallback):
- Primary features: Browse.
- Fallback if Browse is disabled: use archived pages or pre-downloaded snapshots; log provenance and verification steps manually.

---

## 7. Governance, Privacy, and Auditability for Enterprise (3:30)
### Description:
Translate QA metrics into enforceable governance aligned with Teams/Enterprise data controls, Memory policy, GPT Store policies, artifact versioning, and retention. Draft a governance SOP and privacy checklist; define a risk-rating rubric across document types and legal escalation triggers. Codify audit trails, timestamp/version conventions, and reviewer sign-offs.

### Takeaways:
- Governance SOP and privacy checklist aligned to enterprise controls.
- Audit-trail template and versioning/timestamp conventions.
- Risk-rating rubric with sign-off triggers and escalation criteria.

### Learning Goals:
- Participants author a governance SOP tied to retrieval QA and normalization thresholds.
- Participants complete a privacy checklist and define retention/versioning conventions.
- Participants apply risk ratings and identify legal/contractual sign-off criteria.
- Participants configure Teams/Enterprise sharing and data controls to meet policy.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

Instructor Note (Fallback):
- Primary features: Teams/Enterprise settings, Memory policy controls.
- Fallback without Teams/Enterprise: simulate with shared drives and manual permission logs; still adopt SOP and audit templates.

---

## 8. Deployment via Teams/Enterprise and GPT Store (1:45)
### Description:
Operationalize internal sharing and optional publication workflows. Configure Teams/Enterprise org sharing, collections, and permissions; evaluate GPT Store norms where publication is permitted. Establish release cadence, change notes, rollback plans, and a consumer SOP to standardize no-code handoffs.

### Takeaways:
- Deployment plan with scoped access/permissions and release/rollback procedures.
- Consumer SOP with stable inputs/outputs and incident response paths.
- Readiness checklist for internal-only versus GPT Store publication.

### Learning Goals:
- Participants configure Teams/Enterprise sharing and least-privilege permission models.
- Participants prepare versioned releases with change notes and rollback plans.
- Participants draft a consumer SOP for safe, repeatable downstream use.
- Participants assess GPT Store publication options against policy constraints.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

Instructor Note (Fallback):
- Primary features: Teams/Enterprise sharing; GPT Store.
- Fallback if GPT Store is not allowed: finalize internal-only deployment; document deferred publication steps.

---

## 9. Capstone Build: End-to-End Doc-to-Decision Pipeline (1:30)
### Description:
Integrate Vision/OCR extraction, ADA normalization, redlining, Knowledge-backed Q&A with Browse, and governance into a cohesive pipeline. Produce a decision memo with grounded citations and attach all versioned artifacts. Validate performance against predefined QA thresholds and governance rules.

### Takeaways:
- Full pipeline run with linked, versioned artifacts and an audit trail.
- Decision memo with citations and appended governance SOP and privacy checklist.
- Self-assessed pass/fail outcome mapped to rubric thresholds.

### Learning Goals:
- Participants execute the pipeline on a fresh document pack meeting accuracy/governance thresholds.
- Participants assemble and cross-reference artifacts coherently in a decision memo.
- Participants identify limitations and propose prioritized improvements.

### Exercise Description:
Duration: 75 minutes, Debrief: 15 minutes

Instructor Note (Fallback):
- Primary features: Vision, ADA, Custom GPT with Knowledge, Browse, Teams/Enterprise.
- Fallback: apply module-specific fallbacks; document impacts and mitigations in the decision memo.

---

## 10. Defense, Assessment, and Handover (0:30)
### Description:
Defend the capstone pipeline with a concise walkthrough of artifacts, QA metrics, and governance posture. Formalize Teams/Enterprise deployment steps and record pass/fail with rationale. Capture peer/facilitator feedback to inform productionization and scaling.

### Takeaways:
- Peer-reviewed feedback and facilitator rubric scores.
- Documented pass/fail decision, deployment readiness, and risk mitigations.
- Targeted post-course roadmap and recommended follow-ups.

### Learning Goals:
- Participants defend design choices using evidence from logs, metrics, and citations.
- Participants finalize deployment readiness including permissions and rollback plans.
- Participants select follow-up modules to deepen retrieval QA and no-code Actions.

### Exercise Description:
Duration: 20 minutes, Debrief: 10 minutes

---

## Assessment Checkpoints and Pass Thresholds
- Vision/OCR extraction (Module 2): error_log.csv complete; 5-point QA checklist completed; stable extraction patterns on a holdout file set.
- ADA normalization (Module 3): normalized.csv present; anomaly_report.csv triage documented; change_log.csv complete; re-run reproduces outputs.
- Redlining (Module 4): material change detection with risk annotations in change_summary; rationale consistent and traceable to source.
- Knowledge-backed Q&A and Browse (Modules 5–6): retrieval_test_log.csv evidences grounded answers with correct abstentions; citations verifiable; browse_policy followed.
- Governance (Module 7): governance SOP and privacy checklist finalized; audit-trail template adopted; Teams/Enterprise sharing documented.
- Capstone (Modules 9–10): decision memo cites sources, links artifacts, and states pass/fail against thresholds with rationale.

---

## Cross-References
- Modules → Deliverables
  - M1: Prompt library (10 RTCFCE prompts with A/B scores and selection rationale).
  - M2: Extraction and QA pack (extracted.csv, error_log.csv, QA_checklist.md).
  - M3: ADA normalization report (normalized.csv, anomaly_report.csv, change_log.csv).
  - M5: Custom GPT scaffold with Knowledge + retrieval_test_log.csv.
  - M7: Governance SOP + privacy checklist.
  - M9: Capstone decision memo + artifact index.

- Modules → Rubric Thresholds
  - M2 → OCR accuracy and QA completeness.
  - M3 → anomaly rate and reproducibility.
  - M4 → material-change recall and risk annotation completeness.
  - M5–M6 → retrieval groundedness, abstention correctness, citation verification.
  - M7 → governance SOP completeness, privacy checklist, audit-trail adoption.
  - M9–M10 → end-to-end capstone pass/fail.

---

## Evaluation & Sign-off Procedure
- Roles: Facilitator evaluates artifacts against rubric thresholds; peer participant provides secondary review; product owner/team lead signs deployment readiness.
- Recording: Store assessment_rubric_scores.csv and deployment_readiness.md in the cohort folder; record pass/fail with rationale and remediation plan if applicable.
- Remediation: Timeboxed rework; corrective actions captured in change_log.csv and an addendum to the decision memo.

---

## Instructor Prep
- Access checks: Confirm Plus/Teams/Enterprise access to ADA, Browse, Vision, image generation, file uploads/multi-file analysis, Memory/Custom Instructions, and the Custom GPT builder with Knowledge; ensure Teams/Enterprise sharing is enabled or stage a shared-drive fallback.
- Sample datasets: Dirty scans (invoices with stamps/handwriting), multi-page tables, contracts with amendments, policy versions; one document pack per learner.
- Templates staged: prompt_library.csv, error_log.csv, QA_checklist.md, anomaly_report.csv, change_log.csv, retrieval_test_log.csv, governance_SOP.md, privacy_checklist.md, audit_trail_template.csv, deployment_plan.md, decision_memo.md.
- Buffers: Reserve slack in Modules 2, 3, and 7 to absorb OCR variability, normalization rework, and SOP drafting.
- Naming/versioning: Use consistent timestamps and versioning (e.g., idea03_M3_normalized_v1.csv; idea03_M5_retrieval_test_log_v1.csv).

---

### Further Resources for Course Organizers (Preparation)
- OpenAI platform status and features: https://status.openai.com
- Advanced Data Analysis (ADA): https://help.openai.com/en/articles/8554397-advanced-data-analysis
- Vision (PDFs/tables/images): https://platform.openai.com/docs/guides/vision
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
- Explicitly name and demonstrate: ADA, Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, Memory/Custom Instructions, Custom GPTs with Knowledge and no-code Actions, GPT Store, and Teams/Enterprise controls.
- Enforce the no-code policy rigorously while leveraging structured outputs, checklists, and rubrics to ensure accuracy, grounded citations, and reproducible workflows.