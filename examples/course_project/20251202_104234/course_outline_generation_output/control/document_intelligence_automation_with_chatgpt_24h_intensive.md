<!-- filename: document_intelligence_automation_with_chatgpt_24h_intensive.md -->
# Document Intelligence & Automation with ChatGPT — 24-hour Intensive (No-Code)

### Overview:
This hands-on intensive equips professionals to turn messy PDFs and scans into accurate, auditable decisions without writing code. Across ten scaffolded modules, participants master Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads and multi-file analysis, Memory/Custom Instructions, and Custom GPTs with Knowledge and no-code Actions, plus GPT Store and Teams/Enterprise features. The capstone delivers a validated doc-to-decision workflow with grounded citations, QA metrics, and a governance SOP ready for team deployment.

## 1. Prompting & Context Foundations + Environment Setup (2:30)
### Description:
Set the prompting discipline and platform posture that anchor the pipeline. Calibrate RTCFCE (Role, Task, Context, Format, Constraints, Examples), ReAct, checklist prompts, and A/B prompt versioning for testable improvements and reproducibility. Configure Memory and Custom Instructions for privacy posture, grounded citations, tone, and escalation. Verify access to Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, and the Custom GPT builder.

### Takeaways:
- Seeded RTCFCE/ReAct prompt library with A/B variants and selection rationale.
- Memory/Custom Instructions that enforce privacy and citation standards.
- A/B evaluation checklist and logging template to reduce variance.

### Learning Goals:
- Participants design RTCFCE prompts and run A/B comparisons with logged outcomes.
- Participants configure Memory/Custom Instructions to constrain privacy, tone, and citation behavior.
- Participants verify access to ADA, Browse, Vision, image generation, and multi-file uploads.
- Participants define pass/fail criteria and versioning rules for prompt evolution.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

Artifacts Produced:
- prompt_library.csv (10 RTCFCE prompts with A/B scores and selection notes)
- custom_instructions.md (privacy and citation controls)

Instructor Note (Fallback):
- Primary features: ChatGPT Memory, Custom Instructions, file uploads/multi-file analysis.
- Fallback if Memory unavailable: use session preambles saved in prompt_library.csv; paste into each chat.

---

## 2. Vision/OCR for Messy PDFs, Tables, and Images (4:00)
### Description:
Develop resilient extraction workflows for dirty scans and heterogeneous PDFs using Vision for PDFs/tables/images and multi-file uploads. Address page segmentation, multi-page tables, stamps/handwriting, and mixed bundles. Implement structured error logging and a 5-point QA checklist to triage defects and drive remediation.

### Takeaways:
- Extracted CSV(s) plus error logging and QA triage.
- Stable prompt patterns for tables/forms and page-level triage.
- Remediation rubric for re-scan, batching, or manual corrections.

### Learning Goals:
- Participants batch-upload PDFs/images and extract tabular/form data using Vision.
- Participants log OCR anomalies (split/merged cells, header loss, misreads) in error_log.csv.
- Participants apply a 5-point QA checklist to decide remediation priorities.
- Participants design fallback prompts and batching strategies for problematic pages.

### Exercise Description:
Duration: 150 minutes, Debrief: 30 minutes

Artifacts Produced:
- extracted.csv (per document set), error_log.csv, QA_checklist.md (completed)
- ocr_prompt_patterns.md (tables/forms/page triage)

Instructor Note (Fallback):
- Primary features: Vision for PDFs/tables/images, file uploads/multi-file analysis.
- Fallback if Vision degrades: use ADA file preview and constrained parsing prompts; supply pre-OCR’d snapshots if scans are unreadable.

---

## 3. ADA Normalization & Reproducibility (3:00)
### Description:
Normalize extracted data in ADA to a canonical schema with typing, unit harmonization, controlled vocabularies, and schema validation. Produce anomaly_report.csv and change_log.csv so every transformation is auditable and reproducible. Emphasize deterministic re-runs and versioned filenames for governance.

### Takeaways:
- normalized.csv with canonical fields/types/units.
- anomaly_report.csv capturing outliers, missingness, and schema violations.
- change_log.csv documenting transformation steps and rationale.

### Learning Goals:
- Participants define canonical schemas and normalization rules (dates, currency, units, taxonomies).
- Participants generate anomaly reports and set acceptance thresholds.
- Participants re-run normalization to verify determinism and document residual variance.
- Participants apply versioning conventions for traceable artifacts.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

Artifacts Produced:
- normalized.csv, anomaly_report.csv, change_log.csv
- normalization_schema.md (field definitions, accepted values)

Instructor Note (Fallback):
- Primary features: Advanced Data Analysis (ADA), file uploads.
- Fallback if ADA unavailable: use a spreadsheet with data validation; document steps in change_log.csv.

---

## 4. Redlining & Document Comparison (2:30)
### Description:
Operationalize redlining with Vision and ADA across contracts, policies, SOPs, and structured appendices. Extract clause/table-level diffs, classify risk-bearing edits, and generate executive-ready change summaries. Optionally use image generation for annotated visual highlights aligned with textual diffs.

### Takeaways:
- Redline diffs and change_summary.md with risk/impact annotations.
- Prompt patterns for section/paragraph/table alignment and comparison.
- Optional visuals to accelerate stakeholder review.

### Learning Goals:
- Participants align comparable sections and extract granular diffs via Vision and ADA.
- Participants classify changes by business risk and escalation triggers.
- Participants produce stakeholder-ready redline summaries with optional visual highlights.
- Participants document assumptions for reflowed text, scanned markups, and embedded images.

### Exercise Description:
Duration: 80 minutes, Debrief: 30 minutes

Artifacts Produced:
- redline_diffs.md, change_summary.md, optional annotated_images.zip
- redline_prompt_patterns.md

Instructor Note (Fallback):
- Primary features: Vision, ADA, image generation.
- Fallback if image generation disabled: produce textual diff tables; note highlight coordinates for manual annotation.

---

## 5. Knowledge-backed Q&A with Custom GPTs (3:00)
### Description:
Stand up a Custom GPT with Knowledge files for grounded Q&A and correct abstention. Use Custom Instructions to enforce citation requirements, privacy posture, tone, and safety; configure retrieval options (chunking, metadata). Build a 10-question retrieval QA suite and log outcomes in retrieval_test_log.csv; introduce no-code Actions via structured outputs for predictable handoffs.

### Takeaways:
- Custom GPT scaffold with Knowledge uploaded and retrieval options tuned.
- 10-question retrieval QA suite with logged pass/fail, citations, and abstentions.
- Structured output templates for no-code Actions.

### Learning Goals:
- Participants configure a Custom GPT with Knowledge and enforce citation/abstention rules.
- Participants design and run a retrieval QA suite with quantifiable thresholds.
- Participants produce structured outputs for reliable downstream handoffs.
- Participants document tuning levers (chunking, file formats, Knowledge refresh cadence).

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

Artifacts Produced:
- custom_gpt_config.md, knowledge_files_list.md
- retrieval_test_log.csv (scores, citations, abstentions), structured_output_template.md

Instructor Note (Fallback):
- Primary features: Custom GPT builder, Knowledge, Memory/Custom Instructions.
- Fallback if Custom GPT builder unavailable: use standard ChatGPT with files uploaded per chat; emulate retrieval QA and log outcomes.

---

## 6. Browsing, Grounding, and Citations Under Uncertainty (1:45)
### Description:
Enable Browse to incorporate time-sensitive or external evidence within constrained domains. Practice verification steps, decide when to answer versus abstain, and document link provenance and evidence quality. Integrate browsed evidence with Knowledge-backed responses while preserving auditability.

### Takeaways:
- Browse policy template with domain allowlists and source-quality criteria.
- Citation exemplars with verification notes and link provenance.
- Safe-failure patterns for ambiguous or out-of-distribution prompts.

### Learning Goals:
- Participants configure Browse within scoped domains and capture traceable citations.
- Participants validate sources and record verification steps aligned to governance.
- Participants implement abstention and escalation when evidence is insufficient or stale.
- Participants integrate Browse and Knowledge responses while preserving provenance.

### Exercise Description:
Duration: 70 minutes, Debrief: 35 minutes

Artifacts Produced:
- browse_policy.md, citation_examples.md, browse_verification_log.md

Instructor Note (Fallback):
- Primary features: Browse.
- Fallback if Browse unavailable: provide archived pages or pre-downloaded snapshots; require manual provenance logging.

---

## 7. Governance, Privacy, and Auditability for Enterprise (3:30)
### Description:
Translate QA metrics into enforceable governance aligned with Teams/Enterprise data controls, Memory policy, GPT Store policies, artifact versioning, and retention. Draft a governance SOP and privacy checklist; define a risk-rating rubric across document types (contracts, invoices, PHI, IP) and legal escalation triggers. Codify audit trails, timestamp/version conventions, and reviewer sign-offs.

### Takeaways:
- Governance SOP and privacy checklist covering data minimization, retention, consent.
- Audit-trail template and timestamp/versioning conventions.
- Risk-rating rubric with sign-off triggers and legal escalation points.

### Learning Goals:
- Participants author a governance SOP tied to retrieval QA and normalization thresholds.
- Participants complete a privacy checklist and define retention/versioning conventions.
- Participants apply risk ratings and identify legal/contractual sign-off criteria.
- Participants configure Teams/Enterprise sharing and data controls to meet policy expectations.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

Artifacts Produced:
- governance_SOP.md, privacy_checklist.md, audit_trail_template.csv, risk_rubric.md

Instructor Note (Fallback):
- Primary features: Teams/Enterprise admin controls, Memory policy settings.
- Fallback if Teams/Enterprise unavailable: simulate with shared folders and manual permission logs; still apply SOP and audit templates.

---

## 8. Deployment via Teams/Enterprise and GPT Store (1:45)
### Description:
Operationalize internal sharing and optional publication workflows. Configure Teams/Enterprise org sharing, collections, and permissions; evaluate GPT Store norms for publication if permitted. Establish release cadence, change notes, rollback plans, and a consumer SOP to standardize no-code handoffs.

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

Artifacts Produced:
- deployment_plan.md, consumer_SOP.md, release_notes.md, rollback_plan.md

Instructor Note (Fallback):
- Primary features: Teams/Enterprise org sharing, GPT Store.
- Fallback if GPT Store access restricted: finalize internal-only deployment; document deferred publication steps.

---

## 9. Capstone Build: End-to-End Doc-to-Decision Pipeline (1:30)
### Description:
Integrate Vision/OCR extraction, ADA normalization, redlining, Knowledge-backed Q&A with Browse, and governance into a cohesive pipeline. Produce a decision memo with grounded citations and append all supporting artifacts (extractions, normalized.csv, anomaly_report.csv, change_log.csv, retrieval_test_log.csv, governance SOP, privacy checklist). Validate performance against predefined QA thresholds.

### Takeaways:
- Full pipeline run with linked, versioned artifacts and audit trail.
- Decision memo with citations, SOP, and privacy checklist attached.
- Self-assessed pass/fail outcome mapped to rubric thresholds.

### Learning Goals:
- Participants execute the complete pipeline on a fresh document pack meeting accuracy/governance thresholds.
- Participants assemble and cross-reference artifacts coherently in a decision memo.
- Participants identify limitations and propose prioritized improvements for deployment.

### Exercise Description:
Duration: 75 minutes, Debrief: 15 minutes

Artifacts Produced:
- decision_memo.md/pdf, capstone_artifacts_index.md (links to all versioned files)

Instructor Note (Fallback):
- Primary features: Vision, ADA, Custom GPT with Knowledge, Browse, Teams/Enterprise.
- Fallback: substitute module-specific fallbacks; document impacts and mitigations in decision_memo.md.

---

## 10. Defense, Assessment, and Handover (0:30)
### Description:
Defend the capstone pipeline with a concise walkthrough of artifacts, QA metrics, and governance posture. Formalize Teams/Enterprise deployment steps and record pass/fail with rationale; capture peer/facilitator feedback to guide productionization and scaling. Select targeted next steps to deepen retrieval QA and no-code Actions.

### Takeaways:
- Peer-reviewed feedback and facilitator rubric scores.
- Documented pass/fail decision, deployment readiness, and risk mitigations.
- Targeted post-course roadmap and recommended follow-ups.

### Learning Goals:
- Participants defend design choices using evidence from logs, metrics, and citations.
- Participants finalize deployment readiness including permissions and rollback plans.
- Participants select follow-up modules in retrieval QA and no-code Actions.

### Exercise Description:
Duration: 20 minutes, Debrief: 10 minutes

Artifacts Produced:
- assessment_rubric_scores.csv, feedback_notes.md, deployment_readiness.md

Instructor Note (Fallback):
- Primary features: Teams/Enterprise sharing and review workflows.
- Fallback: use shared drives with access logs and manual sign-off if Teams/Enterprise unavailable.

---

## Assessment Checkpoints and Rubric Thresholds
- Vision/OCR extraction:
  - Field-level accuracy at or above 95% on a labeled subset; missing header rate documented.
  - error_log.csv completeness: all anomalies categorized with remediation actions.
- ADA normalization and reproducibility:
  - Unresolved anomaly rate at or below 2% after remediation.
  - change_log.csv: 100% of transformations recorded with timestamp and rationale; deterministic re-run confirmed.
- Redlining and comparison:
  - High recall on risk-bearing edits; risk classifications with rationale in change_summary.md.
- Knowledge-backed Q&A and Browse:
  - Retrieval QA: at or above 95% grounded answers on a 10-question suite; correct abstention on out-of-distribution prompts per browse_policy.md.
  - Citations present and verifiable for all grounded answers.
- Governance and privacy:
  - governance_SOP.md and privacy_checklist.md complete; risk rubric applied with sign-off points; audit_trail_template.csv adopted.
- Capstone pass:
  - End-to-end run meets all thresholds and produces a decision memo with linked, versioned artifacts.

---

## Cross-Reference: Modules to Deliverables
- Prompt library (10 RTCFCE prompts with A/B scores and selection rationale): Module 1.
- Document extraction and QA pack (extracted CSVs + error_log.csv + 5-point QA checklist): Module 2.
- ADA normalization report (normalized.csv + anomaly_report.csv + change_log.csv): Module 3.
- Custom GPT scaffold with Knowledge + retrieval_test_log.csv: Module 5.
- Governance SOP and privacy checklist: Module 7.
- Capstone decision memo and artifact index: Module 9 (defense in Module 10).

---

## Cross-Reference: Modules to Rubric Thresholds
- Module 2 → OCR accuracy and QA completeness thresholds.
- Module 3 → anomaly rate and reproducibility thresholds.
- Module 4 → redlining recall and risk annotation completeness.
- Modules 5–6 → retrieval groundedness, abstention correctness, and citation verification.
- Module 7 → governance SOP completeness, privacy checklist, and audit trail adoption.
- Modules 9–10 → capstone end-to-end pass/fail against all thresholds.

---

## Evaluation and Sign-off Procedure
- Roles:
  - Facilitator evaluates artifacts against rubric thresholds; peer participant provides secondary review.
  - Product owner or team lead signs off on deployment readiness for the capstone.
- Recording pass/fail:
  - Store assessment_rubric_scores.csv and a signed deployment_readiness.md in the cohort folder.
  - Pass/fail status and rationale recorded prior to and after the capstone to trace remediation decisions.
- Remediation:
  - If any threshold is unmet, schedule rework within a timebox and document corrective actions in change_log.csv and a decision_memo.md addendum.

---

## Instructor Prep
- Access checks:
  - Confirm participant access to ADA, Browse, Vision, image generation, file uploads/multi-file analysis, Memory/Custom Instructions, Custom GPT builder with Knowledge (Plus or Teams/Enterprise).
  - Verify Teams/Enterprise sharing permissions or provision shared drives for fallback.
- Sample datasets:
  - Dirty scans (invoices with stamps/handwriting), multi-page tables, contracts with amendments, policy versions; ensure one full document pack per learner.
- Templates:
  - Provide blank copies of prompt_library.csv, error_log.csv, QA_checklist.md, anomaly_report.csv, change_log.csv, retrieval_test_log.csv, governance_SOP.md, privacy_checklist.md, audit_trail_template.csv, deployment_plan.md, decision_memo.md.
- Timeboxing:
  - Maintain buffers in Modules 2, 3, and 7 to absorb OCR and normalization variability.
- Naming/versioning:
  - Use versioned filenames with timestamps (e.g., idea03_M3_normalized_v1.csv, idea03_M5_retrieval_test_log_v1.csv).

---

## Delivery Readiness Checklist
- Accounts and features:
  - ChatGPT Plus or Teams/Enterprise accounts provisioned; ADA, Browse, Vision for PDFs/tables/images, image generation, file uploads/multi-file analysis, Memory/Custom Instructions, and Custom GPT builder with Knowledge enabled.
- Datasets:
  - Dirty scans and mixed bundles accessible; legal approval for use; PII exposure within permitted scope.
- Environment:
  - Stable connectivity; supported browsers; accessibility supports verified (screen readers, keyboard navigation).
- Governance and ethics:
  - Privacy/PII rules reviewed; retention policy defined; consent documented for real documents.
- Contingencies:
  - Fallback datasets (pre-OCR’d), offline web snapshots for Browse, spreadsheet alternative to ADA, manual review plan for Vision/ADA degradation.
- Operations:
  - Shared storage with write access; templates pre-staged; facilitator-to-learner ratio planned for OCR labs.

---

## Milestone Status Pre-Capstone
- Scope:
  - Modules 1–8 complete; artifacts compiled and versioned; governance SOP drafted; retrieval QA thresholds verified.
- Readiness:
  - All learners have working extraction, normalization, redlining, Knowledge-backed Q&A with Browse, and governance bundles ready to integrate.
- Risks:
  - Unresolved Vision/OCR edge cases; Browse restrictions on enterprise networks; incomplete audit trails.
- Decisions:
  - Final acceptance of thresholds by product owner; internal-only vs GPT Store publication scope.
- Status:
  - Pass/Fail with brief rationale and remediation plan if applicable.

---

## Recommended Next Steps (Follow-up Modules)
- Advanced Knowledge Retrieval QA (2 hours)
  - Learning outcomes: configure multi-file Knowledge sets; achieve at least 95% grounded answers with correct abstention; build and run a 10-question retrieval QA suite with pass/fail criteria; diagnose failures via chunking/metadata tuning.
- No-Code Actions via Structured Outputs (3 hours)
  - Learning outcomes: design stable JSON-like schemas for handoffs; validate schema conformance using structured-output prompts; document a mock consumer SOP for downstream tools; establish error-handling and versioning practices for schema evolution.

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