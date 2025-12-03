<!-- filename: doc-intelligence-automation-chatgpt-24hr-intensive.md -->
# Document Intelligence & Automation with ChatGPT — 24-hour Intensive (No-Code)

### Overview:
This one-day, hands-on intensive is designed for analysts, operations leads, and knowledge workers who need to turn messy PDFs and scanned documents into accurate, auditable decisions—without writing code. Across ten scaffolded modules, participants learn to use ChatGPT’s Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, file uploads and multi-file analysis, image generation, Memory/Custom Instructions, and Custom GPTs with Knowledge and no-code Actions, plus GPT Store and Teams/Enterprise features. The course culminates in a validated doc-to-decision workflow with governance, citations, and an SOP that is ready for team deployment.

## 1. Prompting & Context Foundations + Environment Setup (2:30)
### Description:
Establish the baseline prompting discipline and environment that will carry through the pipeline. Calibrate RTCFCE (Role, Task, Context, Format, Constraints, Examples), ReAct, checklist prompts, and A/B prompt versioning. Configure ChatGPT with Memory and Custom Instructions; confirm access to Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, and file uploads/multi-file analysis. This session ensures deterministic habits, traceable experiments, and reproducibility.

### Takeaways:
- A working prompt library template and initial five RTCFCE prompt pairs with version notes.
- Custom Instructions tuned for the participant’s domain and data sensitivity.
- A/B prompt testing checklist and logging template for consistent evaluation.

### Learning Goals:
- Participants formulate RTCFCE prompts and execute A/B comparisons with documented selection rationale.
- Participants configure Memory and Custom Instructions to enforce role, style, and citation norms.
- Participants enable and verify access to ADA, Browse, Vision, image generation, and multi-file analysis.
- Participants create a prompt evaluation checklist to reduce variance and codify acceptance criteria.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

## 2. Vision/OCR for Messy PDFs, Tables, and Images (4:00)
### Description:
Build robust extraction habits from “dirty” inputs using Vision for PDFs/tables/images and multi-file uploads. Cover page segmentation, table extraction, handwriting/low contrast handling, and error triage. Introduce error logging and a 5-point QA checklist to capture systematic failures and inform normalization.

### Takeaways:
- Extracted CSVs from OCR/parsed tables with associated error_log and QA checklist.
- Repeatable prompt patterns for table extraction and page-level triage.
- A prioritized remediation list for recurring OCR issues.

### Learning Goals:
- Participants upload multi-file PDF/image sets and apply Vision to extract structured data from tables and forms.
- Participants detect and log OCR anomalies (misreads, split cells, missing headers) using a standardized error_log.
- Participants apply a 5-point QA checklist to decide when re-scans or manual interventions are required.
- Participants design fallback prompts for low-quality scans to maximize salvageable data.

### Exercise Description:
Duration: 150 minutes, Debrief: 30 minutes

## 3. ADA Normalization & Reproducibility (3:00)
### Description:
Normalize and validate the extracted data in Advanced Data Analysis (ADA). Define canonical schemas, controlled vocabularies, and consistent types; run anomaly detection and generate change logs that make transformations auditable. Emphasize reproducibility, file versioning, and deterministic re-runs.

### Takeaways:
- normalized.csv with harmonized fields and types.
- anomaly_report.csv capturing outliers, missingness, and schema violations.
- change_log.csv documenting transformations and decisions for auditability.

### Learning Goals:
- Participants specify normalization rules (e.g., currency, dates, units, taxonomies) and implement them in ADA.
- Participants generate anomaly reports and establish acceptance thresholds for key metrics.
- Participants maintain a change_log.csv that supports end-to-end reproducibility and re-run verification.
- Participants re-run normalization to prove determinism and document any residual variance.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 4. Redlining & Document Comparison (2:30)
### Description:
Operationalize redlining using Vision and ADA to compare document versions (e.g., contract revisions, policy updates). Generate difference summaries, highlight risk-bearing changes, and produce review-ready outputs. Optionally use image generation to render visual annotations for stakeholder clarity.

### Takeaways:
- Redline diffs and a structured change summary with risk notes.
- A prompt pattern for consistent diffing (headings, clauses, tables).
- Optional annotated visuals highlighting key differences.

### Learning Goals:
- Participants compare versions using Vision and extract changes at clause/table levels.
- Participants classify and summarize changes by potential impact and required escalation.
- Participants generate stakeholder-ready redline briefs with optional visual annotations.

### Exercise Description:
Duration: 80 minutes, Debrief: 30 minutes

## 5. Knowledge-backed Q&A with Custom GPTs (3:00)
### Description:
Create a Custom GPT with Knowledge files, tuned via Custom Instructions for domain grounding and correct abstention. Configure retrieval settings and test suites for accuracy, completeness, and citation quality. Introduce no-code Actions conceptually and structured outputs for downstream handoffs.

### Takeaways:
- A Custom GPT scaffold with Knowledge files uploaded and retrieval options set.
- A 10-question retrieval test suite and a retrieval test_log.csv with scores, citations, and abstentions.
- A governance-aligned instruction set (e.g., privacy posture, “do not speculate,” citation format).

### Learning Goals:
- Participants build a Custom GPT with Knowledge and evaluate retrieval quality against a test suite.
- Participants set and measure thresholds for grounded answers and correct abstentions.
- Participants tune Custom Instructions to enforce citation formats and safety constraints.
- Participants pilot a JSON-like structured response pattern as a precursor to no-code Actions.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 6. Browsing, Grounding, and Citations Under Uncertainty (1:45)
### Description:
Enable Browse to supplement Knowledge when external citations are needed or content is time-sensitive. Practice crafting prompts that constrain browsing scope, verify sources, and handle out-of-distribution queries safely. Establish citation and abstention policies that satisfy governance.

### Takeaways:
- A browse policy template with domain boundaries and source quality guidelines.
- Citation exemplars with verification steps.
- A mitigation plan for ambiguous or OOD queries (safe failure and escalation paths).

### Learning Goals:
- Participants configure Browse and constrain search behavior for precise, auditable citations.
- Participants validate citations and document verification steps for the audit trail.
- Participants implement abstention patterns and escalation when evidence is insufficient.

### Exercise Description:
Duration: 70 minutes, Debrief: 35 minutes

## 7. Governance, Privacy, and Auditability for Enterprise (3:30)
### Description:
Translate QA and performance thresholds into governance. Build a governance SOP and privacy checklist aligned with Teams/Enterprise data controls, Memory policy, GPT Store policies, and artifact versioning. Define risk rating for document types (e.g., contracts, invoices, PHI) and legal/contractual escalation triggers.

### Takeaways:
- A governance SOP and privacy checklist covering data minimization, retention, and consent.
- An audit-trail template and versioning scheme for all artifacts.
- A risk-rating rubric with example application to provided document types.

### Learning Goals:
- Participants author a governance SOP with measurable pass/fail rules tied to QA metrics.
- Participants complete a privacy checklist and define retention/versioning conventions.
- Participants apply a risk-rating rubric to determine when legal sign-off is mandatory.
- Participants configure Teams/Enterprise sharing and data controls to meet policy requirements.

### Exercise Description:
Duration: 120 minutes, Debrief: 30 minutes

## 8. Deployment via Teams/Enterprise and GPT Store (1:45)
### Description:
Operationalize sharing and deployment pathways: Teams/Enterprise org sharing, collections, permissions, and GPT Store publishing norms. Establish versioning, release notes, and rollback plans; define a consumer SOP for downstream teams using no-code handoffs.

### Takeaways:
- A deployment plan with access controls, sharing scopes, and versioning cadence.
- A consumer SOP for downstream users and a rollback/incident response outline.
- A readiness checklist for internal-only vs GPT Store publication.

### Learning Goals:
- Participants configure sharing within Teams/Enterprise and document permission models.
- Participants prepare a versioned release with change notes and rollback plans.
- Participants draft a consumer SOP to ensure safe, consistent downstream use.

### Exercise Description:
Duration: 75 minutes, Debrief: 30 minutes

## 9. Capstone Build: End-to-End Doc-to-Decision Pipeline (1:30)
### Description:
Integrate all components—Vision/OCR, ADA normalization, redlining, Knowledge-backed Q&A with Browse, and governance—into a coherent pipeline. Produce a decision memo with grounded citations, attach supporting artifacts, and validate against defined QA thresholds.

### Takeaways:
- A complete, reproducible pipeline run with supporting artifacts linked.
- A decision memo with citations, a governance SOP, and privacy checklist appended.
- A clear pass/fail assessment against the rubric.

### Learning Goals:
- Participants execute the full pipeline on a new document pack, meeting accuracy and governance thresholds.
- Participants assemble artifacts coherently and cross-reference them in the memo.
- Participants identify limitations and propose next-step improvements.

### Exercise Description:
Duration: 75 minutes, Debrief: 15 minutes

## 10. Defense, Assessment, and Handover (0:30)
### Description:
Conduct concise defenses of the capstone pipelines, reviewing artifacts, QA metrics, and governance posture. Formalize handover steps for team deployment and record pass/fail outcomes with selection rationale.

### Takeaways:
- Peer-reviewed feedback and facilitator rubric scores.
- Documented pass/fail and readiness notes for deployment.
- Personalized next-step recommendations.

### Learning Goals:
- Participants defend design choices using evidence from logs and artifacts.
- Participants document deployment readiness and risk mitigations.
- Participants select follow-up learning paths.

### Exercise Description:
Duration: 20 minutes, Debrief: 10 minutes

---

### Deliverables Produced Across the Course
- Prompt library: 10 RTCFCE prompts with A/B scores and selection rationale.
- Document extraction and QA pack: extracted CSV(s) from Vision/OCR dirty docs + error_log.csv + 5-point QA checklist.md.
- ADA normalization report: normalized.csv + anomaly_report.csv + change_log.csv demonstrating reproducibility.
- Custom GPT scaffold with Knowledge files and retrieval test_log.csv, plus a governance SOP and privacy checklist for the workflow.

### Recommended Next Steps (Optional Follow-ups)
- Advanced Knowledge Retrieval QA (2 hours): Configure multi-file Knowledge sets and achieve ≥95% grounded answers with correct abstention; build a 10-question retrieval QA suite with pass/fail criteria.
- No-Code Actions via Structured Outputs (3 hours): Design stable JSON schemas for handoffs, validate schema conformance, and document a mock “consumer” SOP for downstream tools.

---

### Resources for Course Organizers (Preparation)
- OpenAI platform status and features: https://status.openai.com
- ChatGPT Advanced Data Analysis (overview/how-to): https://help.openai.com/en/articles/8554397-advanced-data-analysis
- Vision with PDFs/tables/images: https://platform.openai.com/docs/guides/vision
- Browse (with citation behavior): https://help.openai.com/en/articles/8554400-browsing
- Custom GPTs and Knowledge: https://help.openai.com/en/articles/8554408-custom-gpts
- Teams/Enterprise features and admin: https://openai.com/enterprise
- GPT Store guidelines and policies: https://openai.com/blog/introducing-the-gpt-store
- Data privacy and retention: https://openai.com/policies/privacy-policy
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Accessibility guidance (WCAG 2.1 summary): https://www.w3.org/WAI/standards-guidelines/wcag/

### Resources for Participants (Further Learning)
- Prompting patterns (ReAct, chain-of-thought caution): https://arxiv.org/abs/2210.03629
- OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering
- Evaluating LLMs (intro to test suites and metrics): https://arxiv.org/abs/2307.03109
- Data cleaning and normalization concepts (practical guide): https://library.carleton.ca/guides/data-cleaning
- Responsible AI playbook (governance basics): https://ai.google/responsibilities/responsible-ai-practices
- Contract redlining basics (domain primer): https://www.americanbar.org/groups/business_law/publications/committee_newsletters/CL182000/
- Versioning and audit trails in data projects (best practices): https://dvc.org/doc/start

Notes on tools and features: Throughout the course, participants explicitly use Advanced Data Analysis (ADA), Browse, Vision for PDFs/tables/images, image generation, file uploads and multi-file analysis, Memory/Custom Instructions, and Custom GPTs with Knowledge and no-code Actions, plus GPT Store and Teams/Enterprise features. The design adheres to a strict no-code policy while enabling structured outputs for downstream interoperability.