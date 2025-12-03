<!-- filename: chatgpt_pro_power_user_24hr_intensive.md -->
# ChatGPT Pro Power User: No-Code Productivity and Analysis — Revised 24-Hour Intensive

### Overview:
This hands-on, end-to-end intensive is for cross-functional professionals who want to operationalize ChatGPT Pro without writing code. Across eight scaffolded modules (three hours each), participants progress from prompt and context fundamentals to applied capabilities with Custom Instructions/Memory, Browse, Advanced Data Analysis (ADA), Vision, Image Generation, Custom GPT Builder with Knowledge (and a no-code Actions concept), GPT Store considerations, and Teams/Enterprise governance. Emphasis is on reproducibility, evidence grounding, accessibility, privacy-by-design, feature-availability fallbacks, and artifact-based checkpoints—culminating in a governance-ready, SOP-backed capstone.

## 1. LLM Fundamentals & Prompt Mechanics
### Description:
Establish a robust prompting discipline using the RTCFCE structure (Role, Task, Context, Format, Constraints, Evaluation). The session normalizes A/B trials of prompt variants, quantifies response quality, and demonstrates how constraints steer tone, structure, and fidelity. This methodological base is essential for subsequent context engineering and multimodal work.

### Takeaways:
- A reusable RTCFCE template and scoring rubric
- A replicable A/B prompt evaluation workflow
- Practical levers to control style, structure, and fidelity

### Learning Goals:
- Participants draft six RTCFCE prompts (three domain-specific, three general), each with explicit constraints and evaluation criteria, saved as prompt_set.xlsx.
- Participants run vA/vB trials and score outputs for correctness, clarity, and constraint adherence in prompt_set.xlsx.
- Participants select winning variants and document rationale, enabling peer reuse and audit.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes  
Tools and features: ChatGPT (base chat), RTCFCE prompting, Custom Instructions (preview)

## 2. Context Engineering & Memory/Custom Instructions
### Description:
Operationalize Custom Instructions/Memory for personalization and file-based context to enforce terminology and output structure. Compare CI-on vs CI-off for the same task, reference a glossary by exact filename (glossary.csv), and apply a feature-availability decision path: if Memory is disabled, store profile/output preferences as Knowledge in a Custom GPT (previewed further in Module 7).

### Takeaways:
- Production-ready Custom Instructions and output preferences
- Measurable CI-on vs CI-off impact on tone, structure, and terminology
- A validated fallback path using Knowledge in a Custom GPT

### Learning Goals:
- Participants configure Custom Instructions, exporting CI_template.txt (profile and output preferences).
- Participants run CI-on vs CI-off trials on the same task and log measurable deltas (tone, structure, terminology) in before_after_log.csv.
- Participants upload and reference glossary.csv by exact filename; record terminology alignment evidence in before_after_log.csv.
- Participants apply the CI/Knowledge decision path when Memory is disabled and document the chosen path/rationale in before_after_log.csv.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes  
Tools and features: Custom Instructions/Memory, File uploads, Custom GPT Builder + Knowledge (fallback)  
Checkpoint rubric applies

## 3. Web-Grounded Research with Browse
### Description:
Implement a defensible research workflow that prioritizes recency, credibility, and cross-verification using Browse. Cite only opened sources with access dates, use inline bracketed citations, and maintain a structured source log to ensure auditability in enterprise contexts.

### Takeaways:
- Transparent, auditable web research workflow with verifiable citations
- Practical heuristics for recency, credibility, and relevance
- Structured source logging aligned with stakeholder review norms

### Learning Goals:
- Participants open and evaluate at least three reputable sources (≤12 months) and extract quotes with metadata into sources.csv.
- Participants produce a one-page brief with inline bracketed citations and a references list including access dates, saved as brief.docx.
- Participants validate one-to-one mapping between every inline citation in brief.docx and entries in sources.csv.

### Exercise Description:
Duration: 80 minutes, Debrief: 20 minutes  
Tools and features: Browse (web-enabled), inline bracketed citations, link inspection, references with access dates

## 4. Advanced Data Analysis (ADA) for Pros
### Description:
Use ADA to analyze multi-file CSVs: join, compute KPIs, visualize, and deliver a concise narrative stating assumptions and flagging outliers. If ADA is unavailable, execute a spreadsheet-based fallback (pseudo-calculations + visual spec) to preserve rigor and reproducibility.

### Takeaways:
- A reproducible join–transform–visualize pipeline
- Portable KPI tables and charts for stakeholders
- An assumption-transparent narrative with outlier detection

### Learning Goals:
- Participants join sales_q1_q4.csv with targets.csv on quarter and export kpi_table.csv with revenue variance and units per product.
- Participants render a KPI bar chart with correct labels and currency formatting, exported as chart.png.
- Participants author a 150-word maximum summary with assumptions and outliers (>2 SD), saved as summary.txt.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes  
Tools and features: Advanced Data Analysis (code interpreter), Multi-file uploads, CSV export; spreadsheet fallback (pseudo-calculations + visual spec)  
Checkpoint rubric applies

## 5. Document & Table Intelligence (Vision)
### Description:
Apply Vision to locate, extract, and normalize tables from PDFs and images; validate numeric integrity with ADA. Emphasize OCR/structure error handling, clarifying questions for ambiguous cells, and crop/re-upload for skewed inputs; produce a five-check QA report.

### Takeaways:
- Reliable Vision extraction and normalization workflow
- Practical numeric validation and reconciliation via ADA
- Transparent QA/error logging suitable for audit

### Learning Goals:
- Participants extract the “Coverage limits” table from policy_handbook.pdf and table_screenshot.png and export coverage_limits.csv preserving header names.
- Participants validate totals/ranges with ADA and record issues, corrections, and decisions in qa_report.txt with at least five checks.
- Participants apply crop/re-upload for skewed images and document interventions in qa_report.txt.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes  
Tools and features: Vision (PDF/image), ADA (validation), image preprocessing (crop/re-upload)  
Checkpoint rubric applies

## 6. Image Generation & Multimodal Workflows
### Description:
Combine Vision-based brand guide parsing with Image Generation to produce on-brief assets that satisfy brand and accessibility constraints. Generate and refine comps, verify color contrast ratios, write alt-text, and provide rationale linking design choices to brand rules.

### Takeaways:
- Lightweight brand-to-asset multimodal pipeline
- Accessibility-first checks (contrast ratios, alt-text) embedded in review
- Rationale discipline linking visuals to constraints

### Learning Goals:
- Participants use Vision to extract palette and constraints from Brand_Guide.pdf, reflected in two final images: hero_v1.png and hero_v2.png.
- Participants compile accessibility_checklist.txt with contrast notes and alt-text for each image.
- Participants produce a 120-word rationale linking design choices to brand rules, saved as rationale.txt.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes  
Tools and features: Image Generation (ChatGPT), Vision (brand parsing), accessibility checks (contrast ratios, alt-text)

## 7. Custom GPTs: Builder, Knowledge, No-Code Actions (simulated)
### Description:
Create a task-specific assistant using Custom GPT Builder with a precise RTCFCE system prompt and Knowledge files, enforcing Knowledge-only citations and explicit “I don’t know” behavior. Simulate a no-code Action via structured JSON outputs usable by downstream tools. Prepare a GPT Store listing mock. If Builder is unavailable, simulate in base ChatGPT with file uploads.

### Takeaways:
- Working Custom GPT scaffold with guardrails and Knowledge-only citations
- Retrieval QA/testing log with citation integrity and confidence reporting
- Parseable JSON output pattern enabling lightweight automation

### Learning Goals:
- Participants create an unlisted “Team FAQ Assistant” requiring Knowledge-only citations with page/line and “I don’t know” when absent.
- Participants upload Product_FAQ.docx, Policy_Guide.pdf, and glossary.csv; test at least five questions; log retrieval fidelity in test_log.csv.
- Participants produce both a human-readable answer and a JSON block {answer, citations, confidence}; draft store_listing.txt with governance notes.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes  
Tools and features: Custom GPT Builder, Knowledge files (upload/retrieval), structured JSON output (no-code Actions concept), GPT Store (mock); base ChatGPT + file uploads (fallback)  
Checkpoint rubric applies

## 8. Teams/Enterprise Governance & Capstone
### Description:
Operationalize privacy, data controls, and workspace sharing in Teams/Enterprise. Execute an end-to-end capstone integrating at least three tools (for example, Vision + ADA + Browse) using synthetic/redacted data. Deliver a formal SOP, governance checklist, RACI, and measurable acceptance criteria suitable for enterprise review.

### Takeaways:
- Governance-compliant, SOP-backed end-to-end workflow
- RACI and acceptance criteria enabling replication and sign-off
- Practical privacy/compliance posture for ongoing team use

### Learning Goals:
- Participants review and document relevant Teams/Enterprise settings (retention, data controls, workspace sharing) in the SOP within capstone_pack.zip.
- Participants execute a cross-tool workflow using at least three tools with synthetic/redacted inputs and include all artifacts in capstone_pack.zip.
- Participants include a governance checklist, RACI, and measurable acceptance criteria in capstone_pack.zip, noting any fallbacks used.

### Exercise Description:
Duration: 110 minutes, Debrief: 30 minutes  
Tools and features: Teams/Enterprise settings (data controls, retention, workspace sharing), Browse, ADA, Vision, Image Generation, Custom Instructions/Memory, Custom GPTs

---

Further resources for organizers:
- OpenAI Help Center (Teams/Enterprise, ADA, Browse, Vision, Image Generation, Custom GPTs, GPT Store): https://help.openai.com
- OpenAI Policies (privacy, data usage, safety): https://openai.com/policies
- OpenAI Cookbook (prompting patterns, data workflows): https://github.com/openai/openai-cookbook
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- WCAG 2.1 (contrast and alt-text standards): https://www.w3.org/TR/WCAG21/

Further resources for participants:
- Getting started with Browse, ADA, and Vision in ChatGPT: https://help.openai.com
- Prompt engineering basics (OpenAI Cookbook): https://github.com/openai/openai-cookbook
- Responsible use of generative AI in the workplace (OpenAI policies): https://openai.com/policies
- W3C WAI tutorials (contrast and alt-text): https://www.w3.org/WAI/tutorials/
- Purdue OWL (research and citation primer): https://owl.purdue.edu/owl/research_and_citation/overview.html