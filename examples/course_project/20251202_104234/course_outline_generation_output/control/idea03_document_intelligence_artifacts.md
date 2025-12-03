<!-- filename: idea03_document_intelligence_artifacts.md -->
<code>
competency_id,competency_name,modules,deliverable_evidence,rubric_metric,one_line_rationale
C01,Prompt engineering with RTCFCE/ReAct/checklists and A/B versioning,M1,"prompt_library","A/B tests logged with selection rationale; chosen prompt demonstrates measurable improvement and adherence to constraints","Prompt discipline and versioned testing are foundational for reliable downstream performance"
C02,Configure Memory and Custom Instructions for privacy/style/citations,M1,"governance_SOP + privacy_checklist","Custom Instructions fields completed; privacy/citation policies enforced; Memory use aligned with policy","Configuration embeds governance into every interaction"
C03,Multi-file uploads and Vision for PDFs/tables/images extraction,M2,"extraction_QA_pack","OCR/table extraction coverage meets target; extracted CSV present; files and steps logged","Robust extraction from heterogeneous documents unlocks automation"
C04,OCR error logging and 5-point QA triage,M2,"extraction_QA_pack","error_log.csv complete; QA checklist.md completed; triage decisions documented","Systematic QA reduces hidden errors and informs remediation"
C05,ADA normalization to canonical schema (typing/units/taxonomies),M3,"normalized_pack","normalized.csv conforms to schema; typing/units harmonized; schema validation passes","Normalization enables consistent analytics and comparisons"
C06,Anomaly detection and reproducible change logging in ADA,M3,"normalized_pack","anomaly_report.csv populated; change_log.csv complete; re-run yields consistent outputs within tolerance","Reproducibility and anomaly control support auditability"
C07,Redlining and document comparison with risk classification,M4,"redline_brief","Change detection accurate; risk categories assigned; stakeholder summary clear","Redlining turns raw diffs into actionable risk signals"
C08,Build a Custom GPT with Knowledge for grounded Q&A,M5,"custom_gpt_scaffold + retrieval_test_log","Custom GPT created; Knowledge loaded; retrieval functioning with citations","Knowledge-backed Q&A anchors decisions to documented evidence"
C09,Retrieval QA with correct abstention and citation quality,M5,"custom_gpt_scaffold + retrieval_test_log","Retrieval test_log.csv shows grounded answers meeting threshold; appropriate abstentions; valid citations","Quantified retrieval QA ensures trust under governance"
C10,Constrained Browse with source vetting and provenance logging,M6,"browse_policy + citations","Browse policy documented; citations include provenance and verification notes; abstain on insufficient evidence","Browsing expands coverage while preserving auditability"
C11,Structured outputs design for no-code Actions handoffs,M5,"deployment_plan + consumer_SOP","Schema documented in consumer SOP; sample outputs validate against schema; handoff steps clear","Stable schemas enable reliable downstream automation without code"
C12,Governance SOP and privacy checklist (data minimization/retention/consent),M7,"governance_SOP + privacy_checklist","SOP meets required controls; privacy checklist complete; retention rules specified","Governance operationalizes risk controls and compliance"
C13,Audit trail, versioning, and timestamp conventions,M7,"governance_SOP + privacy_checklist","Artifacts versioned; timestamps follow convention; audit fields complete","Auditability is essential for enterprise acceptance"
C14,Teams/Enterprise deployment (sharing/permissions) and GPT Store norms,M8,"deployment_plan + consumer_SOP","Deployment plan defines access, permissions, release/rollback; GPT Store/Teams settings aligned with policy","Controlled deployment ensures safe adoption"
C15,Consumer SOP for downstream users with rollback/incident response,M8,"deployment_plan + consumer_SOP","Consumer SOP clear; rollback and escalation paths documented; roles/responsibilities assigned","Operational clarity reduces misuse and downtime"
C16,Capstone integration: end-to-end doc-to-decision with citations,M9,"capstone_decision_memo","Decision memo links all artifacts; meets accuracy/governance thresholds; evidence cited","Integration demonstrates readiness for team deployment"
C17,Risk rating rubric and legal escalation triggers,M7,"governance_SOP + privacy_checklist","Rubric applied to sample docs; escalation thresholds identified; sign-off points defined","Early risk identification prevents policy violations"
C18,Visual annotation via image generation for redline highlights (optional),M4,"redline_brief","If used, visual marks match textual diffs; improves stakeholder comprehension","Visuals accelerate stakeholder review when appropriate"
</code>


<!-- filename: ./artifacts/idea03/prerequisites_checklist.md -->
<code>
# Prerequisites Checklist — Document Intelligence & Automation with ChatGPT (No-Code)

Status keys: [ ] not started, [~] in progress, [x] complete

## 1) Accounts and Licenses
- [ ] ChatGPT Plus or ChatGPT Teams/Enterprise account provisioned for all participants
- [ ] Features enabled in org/admin settings:
  - [ ] Advanced Data Analysis (ADA)
  - [ ] Browse
  - [ ] Vision for PDFs/tables/images
  - [ ] Image generation
  - [ ] File uploads and multi-file analysis
  - [ ] Memory and Custom Instructions
  - [ ] Custom GPTs with Knowledge
  - [ ] GPT Store visibility (if permitted) or internal-only sharing via Teams/Enterprise

## 2) Feature Access Validation (pre-flight checks)
- [ ] ADA opens and can import a CSV; basic dataframe preview works
- [ ] Vision loads a multi-page PDF and extracts a simple table
- [ ] Browse returns results from approved domains with citations
- [ ] Image generation produces a simple annotated image (watermarked if policy requires)
- [ ] Custom GPT builder accessible; Knowledge files uploadable; retrieval produces citations
- [ ] Memory/Custom Instructions save and apply across sessions

## 3) Sample Data Inventory (for exercises and capstone)
- [ ] Dirty scans (10–15 files):
  - [ ] Mixed-quality PDFs (low contrast, skew, multi-page tables, stamps/handwriting)
  - [ ] Image formats (PNG/JPEG) with receipts/forms
  - [ ] Document types: invoices, purchase orders, contracts, NDAs, lab reports
  - [ ] Known-ground-truth subset identified for QA
- [ ] Clean docs (5–10 files):
  - [ ] Well-structured PDFs (vector text, embedded tables)
  - [ ] Policies/SOPs for retrieval Knowledge base
- [ ] File size and count conform to current platform upload limits; larger sets pre-split into batches
- [ ] Folder structure prepared:
  - [ ] ./datasets/dirty_scans/
  - [ ] ./datasets/clean_docs/
  - [ ] ./artifacts/idea03/ (write-access verified)

## 4) Required Software
- [ ] Modern browser: Chrome, Edge, or Safari (latest stable)
- [ ] Spreadsheet tool: Excel, Google Sheets, or LibreOffice Calc
- [ ] PDF reader (Adobe Acrobat Reader or built-in OS viewer)
- [ ] Archive utility (ZIP) for dataset distribution
- [ ] Optional: checksum tool for file integrity (e.g., shasum)

## 5) Connectivity and Browser Settings
- [ ] Reliable broadband connectivity; VPN exceptions configured if required by org
- [ ] Browser privacy settings allow file uploads to ChatGPT per org policy
- [ ] Pop-up blockers do not interfere with file picker and downloads
- [ ] Cookies/session settings permit authenticated access for duration of the course

## 6) Baseline Skills (participant self-check)
- [ ] Comfortable with spreadsheets and CSV inspection
- [ ] Familiar with basic prompt writing
- [ ] Able to follow a QA checklist and log defects
- [ ] Comfortable reading citations and verifying sources

## 7) No-Code Policy (acknowledgement)
- [ ] No API keys, SDKs, or external code execution
- [ ] Only platform-native capabilities used: ADA, Browse, Vision, image generation, file uploads/multi-file analysis, Memory/Custom Instructions, Custom GPTs with Knowledge, Teams/Enterprise sharing, GPT Store (if allowed)
- [ ] Structured outputs permitted as JSON-like responses for no-code handoffs; no external code integration during course

## 8) Compliance and Data Handling Readiness
- [ ] All datasets are synthetic or de-identified; no PHI/PII without written consent
- [ ] Data usage complies with org and platform privacy policies
- [ ] Retention and deletion plans documented for ./artifacts/idea03/
- [ ] Instructor and facilitators briefed on escalation paths for policy issues
</code>


<!-- filename: ./artifacts/idea03/constraints.md -->
<code>
# Constraints and Assumptions — Document Intelligence & Automation with ChatGPT (No-Code)

## 1) No-Code Rule
- Only platform-native features are allowed: ADA, Browse, Vision (PDFs/tables/images), image generation, file uploads/multi-file analysis, Memory/Custom Instructions, Custom GPTs with Knowledge, Teams/Enterprise, GPT Store (if permitted)
- No external code, APIs, SDKs, or custom scripts; structured outputs allowed solely as text-based JSON-like responses

## 2) Privacy and PII Boundaries
- Use synthetic or de-identified datasets; no PHI/PII unless explicit written consent and legal approval exist
- Apply data minimization: upload only what is necessary; redact sensitive content before upload when feasible
- Memory and Custom Instructions must reflect privacy posture; disable Memory if required by org policy

## 3) Retention, Storage Paths, and Versioning
- All course artifacts stored under ./artifacts/idea03/
- Versioning pattern: filename_v1.ext, filename_v2.ext with timestamps appended as needed
- Timestamp convention: YYYYMMDD_HHMMZ (UTC indicator)
- Retention: keep artifacts until course closeout + defined grace period per org policy; then purge

## 4) Online/Offline Needs
- Active internet connection is required for ADA, Browse, Vision, image generation, and Custom GPTs
- Offline viewing allowed only for local PDFs; no offline model use or local OCR

## 5) Organization Policy Limits
- If Browse or GPT Store is disabled by admin, use internal-only Knowledge and approved sources
- Sharing confined to Teams/Enterprise spaces with least-privilege permissions
- Memory usage must comply with org’s data retention and sharing rules

## 6) Supported OS/Browsers
- OS: Windows 10+ and macOS 12+ (or organization-supported equivalents)
- Browsers: latest stable Chrome, Edge, or Safari
- Accessibility settings enabled as required (captions, zoom, high contrast)

## 7) Content Handling Limits
- Respect current platform limits on file size, page counts, and number of concurrent uploads
- For large PDFs or bundles, pre-split into logical batches before upload
- Do not upload encrypted/password-protected files unless decrypted under policy-compliant conditions

## 8) Auditability and Reproducibility Expectations
- Every transformation logged in change_log.csv; anomaly_report.csv maintained for normalization
- Retrieval runs logged in retrieval_test_log.csv with pass/fail, citations, and abstentions
- Audit trails include artifact IDs, versions, timestamps, source file references, and reviewer sign-offs

## 9) Governance and Legal
- Governance SOP and privacy checklist must be completed before capstone acceptance
- Risk rating rubric applied to each document type; legal escalation triggers documented where applicable
- Teams/Enterprise deployment only after governance pass and permission validation
</code>