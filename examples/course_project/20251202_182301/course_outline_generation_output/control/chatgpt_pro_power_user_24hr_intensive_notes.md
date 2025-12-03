<!-- filename: chatgpt_pro_power_user_24hr_intensive_notes.md -->
# ChatGPT Pro Power User: No-Code Productivity and Analysis — Revised 24-Hour Intensive

### Overview:
A hands-on, end-to-end intensive for cross-functional professionals seeking reproducible, no-code AI workflows with ChatGPT Pro. Across eight scaffolded modules (three hours each), participants progress from prompt/context fundamentals to applied capabilities across Custom Instructions/Memory, Browse, Advanced Data Analysis (ADA), Vision, Image Generation, Custom GPT Builder with Knowledge (and a no-code Actions concept), GPT Store considerations, and Teams/Enterprise governance. Emphasis is on evidence grounding, accessibility, privacy-by-design, feature-availability fallbacks, and artifact-based checkpoints—culminating in a governance-ready, SOP-backed capstone.

## 1. LLM Fundamentals & Prompt Mechanics
### Description:
Standardizes prompt practice using the RTCFCE structure (Role, Task, Context, Format, Constraints, Evaluation). Participants A/B test prompt variants and quantify how constraints and formats steer tone, structure, and fidelity—establishing a methodological base for later context engineering and multimodal work. Tools explicitly named: ChatGPT (base chat), RTCFCE prompting pattern, Custom Instructions (preview).

### Takeaways:
- Reusable RTCFCE prompt template and scoring rubric
- Replicable A/B prompt evaluation workflow
- Practical levers to control style, structure, and fidelity

### Learning Goals:
- Participants author six RTCFCE prompts (three domain-specific, three general) with explicit constraints and evaluation criteria, saved to prompt_set.xlsx.
- Participants run vA/vB trials and score outputs for correctness, clarity, and constraint adherence in prompt_set.xlsx.
- Participants select winning variants and document rationale enabling peer replication.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes

## 2. Context Engineering & Memory/Custom Instructions
### Description:
Operationalizes Custom Instructions/Memory for personalization and file-based context to enforce terminology. Participants compare CI-on vs CI-off outcomes, reference glossary.csv by exact filename, and apply a feature-availability decision path: if Memory is disabled, store profile/output preferences as Knowledge in a Custom GPT. Tools explicitly named: Custom Instructions/Memory, File uploads (CSV), Custom GPT Builder + Knowledge (fallback).

### Takeaways:
- Production-ready Custom Instructions and output preferences
- Measured evidence of CI impact on tone/structure/terminology
- Validated fallback path using Knowledge in a Custom GPT

### Learning Goals:
- Participants configure Custom Instructions and export CI_template.txt capturing profile and output preferences.
- Participants run CI-on vs CI-off trials for a single task and log measurable deltas (tone, structure, terminology) in before_after_log.csv.
- Participants upload and reference glossary.csv by exact filename; record terminology alignment in before_after_log.csv.
- Participants apply the CI/Knowledge decision path when Memory is disabled and document the chosen path in before_after_log.csv.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 3. Web-Grounded Research with Browse
### Description:
Implements a defensible Browse workflow that prioritizes recency, credibility, and cross-verification. Participants cite only opened sources with access dates, use inline bracketed citations, and maintain a structured source log. Tools explicitly named: Browse (web-enabled ChatGPT), inline bracketed citations, link inspection, references with access dates.

### Takeaways:
- Transparent, auditable research workflow with verifiable citations
- Practical heuristics for recency, credibility, and relevance
- Structured source logging aligned to enterprise norms

### Learning Goals:
- Participants open and evaluate at least three reputable sources (≤12 months) and record quotes/metadata in sources.csv.
- Participants produce a one-page brief with inline bracketed citations and a references list including access dates, saved as brief.docx.
- Participants verify one-to-one mapping between every inline citation in brief.docx and entries in sources.csv.

### Exercise Description:
Duration: 80 minutes, Debrief: 20 minutes

## 4. Advanced Data Analysis (ADA) for Pros
### Description:
Applies ADA to multi-file CSV analysis: join on quarter, compute KPIs, visualize, and produce a concise narrative with explicit assumptions and outlier flags. Spreadsheet fallback (pseudo-calculations + visual spec) preserves rigor if ADA is unavailable. Tools explicitly named: Advanced Data Analysis (code interpreter), Multi-file uploads, CSV export; spreadsheet fallback.

### Takeaways:
- Reproducible join–transform–visualize pipeline
- Portable KPI tables and charts for stakeholders
- Assumption-transparent narrative with outlier detection

### Learning Goals:
- Participants join sales_q1_q4.csv with targets.csv on quarter and export kpi_table.csv including revenue variance and units per product.
- Participants generate a labeled KPI bar chart with currency formatting, exported as chart.png.
- Participants author a ≤150-word domain-tailored summary with assumptions and outliers (>2 SD), saved as summary.txt.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 5. Document & Table Intelligence (Vision)
### Description:
Uses Vision to locate, extract, and normalize tables from PDFs and images; validates numeric integrity with ADA. Emphasizes OCR/structure error handling, clarifying questions for ambiguous cells, and crop/re-upload for skewed inputs; culminates in a five-check QA report. Tools explicitly named: Vision (PDF/image table extraction), ADA (validation), image preprocessing (crop/re-upload).

### Takeaways:
- Reliable Vision extraction and normalization workflow
- Practical numeric validation and reconciliation via ADA
- Transparent QA/error logging suitable for audit

### Learning Goals:
- Participants extract the “Coverage limits” table from policy_handbook.pdf and table_screenshot.png and export coverage_limits.csv preserving header names.
- Participants validate totals/ranges with ADA and record issues, corrections, and decisions in qa_report.txt (≥5 checks).
- Participants apply crop/re-upload when OCR fidelity is low and document interventions in qa_report.txt.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 6. Image Generation & Multimodal Workflows
### Description:
Combines Vision-based brand parsing with Image Generation to deliver on-brief assets that satisfy brand and accessibility constraints. Participants generate three comps, refine to two finals, verify color contrast ratios, author alt-text, and write a concise rationale. Tools explicitly named: Image Generation (ChatGPT), Vision (Brand_Guide.pdf parsing), accessibility checks (contrast ratios, alt-text).

### Takeaways:
- Lightweight brand-to-asset multimodal pipeline
- Accessibility-first review (contrast ratios, alt-text)
- Rationale discipline linking visuals to brand rules

### Learning Goals:
- Participants reflect the extracted palette/constraints from Brand_Guide.pdf in two final images (hero_v1.png; hero_v2.png).
- Participants compile accessibility_checklist.txt with contrast notes and alt-text for each image.
- Participants produce a 120-word rationale linking design choices to brand rules, saved as rationale.txt.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes

## 7. Custom GPTs: Builder, Knowledge, No-Code Actions (simulated)
### Description:
Builds a task-specific assistant using Custom GPT Builder with a precise RTCFCE system prompt and Knowledge files, enforcing Knowledge-only citations and explicit “I don’t know” behavior. Simulates a no-code Action via a structured JSON output pattern and drafts a GPT Store listing. Base-ChatGPT simulation path applies if Builder is unavailable. Tools explicitly named: Custom GPT Builder, Knowledge files (upload/retrieval), structured JSON outputs, GPT Store (mock); base ChatGPT + file uploads (fallback).

### Takeaways:
- Working Custom GPT scaffold with guardrails and Knowledge-only citations
- Retrieval QA/testing log with citation integrity and confidence reporting
- Parseable JSON output pattern enabling lightweight automation

### Learning Goals:
- Participants create an unlisted “Team FAQ Assistant” requiring Knowledge-only citations with page/line and explicit “I don’t know” behavior.
- Participants upload Product_FAQ.docx, Policy_Guide.pdf, and glossary.csv; test at least five questions; log retrieval fidelity in test_log.csv.
- Participants produce both a human-readable answer and a JSON block {answer, citations, confidence}; prepare a store listing mock in store_listing.txt.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 8. Teams/Enterprise Governance & Capstone
### Description:
Operationalizes Teams/Enterprise data controls, retention, and workspace sharing. Executes an end-to-end capstone integrating at least three tools (e.g., Vision + ADA + Browse) using only synthetic/redacted data. Delivers a formal SOP, governance checklist, RACI, and measurable acceptance criteria. Tools explicitly named: Teams/Enterprise settings, Browse, ADA, Vision, Image Generation, Custom Instructions/Memory, Custom GPTs.

### Takeaways:
- Governance-compliant, SOP-backed end-to-end workflow
- RACI and acceptance criteria enabling replication and sign-off
- Privacy-by-design posture for ongoing enterprise use

### Learning Goals:
- Participants document relevant Teams/Enterprise settings (retention, data controls, workspace sharing) within the SOP in capstone_pack.zip.
- Participants execute a cross-tool workflow using at least three tools and synthetic/redacted inputs; include all artifacts within capstone_pack.zip.
- Participants include a governance checklist, RACI, and measurable acceptance criteria in capstone_pack.zip and document any fallbacks used.

### Exercise Description:
Duration: 110 minutes, Debrief: 30 minutes

---

### Assessment touchpoints and capstone expectations
- Practical checkpoints after Modules 2, 4, 5, and 7 using the rubric (scale 1–4): Correctness; Clarity/Structure; Grounding/Citations (if relevant); Reproducibility; Compliance (privacy/brand). Passing requires average at least three with no criterion below two.
- Capstone rubric (Module 8): End-to-end completeness; Tool integration (≥3 tools); Evidence grounding; Governance/SOP quality; Business relevance. Passing requires average at least three and Governance at least three.
- Feature-availability fallbacks (document in artifacts and SOP): Memory disabled → Knowledge-as-profile in a Custom GPT; ADA unavailable → spreadsheet pseudo-calculations + visual spec; Builder disabled → simulate in base ChatGPT with file uploads and strict system prompt; Vision OCR degraded → crop/re-upload and annotate manual corrections. Always use synthetic/redacted data.

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

---

Deliverables are provided below as three files. Save or export them to the specified paths.

### 1) course_outline.md
<code># ChatGPT Pro Power User: No-Code Productivity and Analysis — Revised 24-Hour Intensive

### Overview:
A hands-on, end-to-end intensive for cross-functional professionals seeking reproducible, no-code AI workflows with ChatGPT Pro. Across eight scaffolded modules (three hours each), participants progress from prompt/context fundamentals to applied capabilities across Custom Instructions/Memory, Browse, Advanced Data Analysis (ADA), Vision, Image Generation, Custom GPT Builder with Knowledge (and a no-code Actions concept), GPT Store considerations, and Teams/Enterprise governance. Emphasis is on evidence grounding, accessibility, privacy-by-design, feature-availability fallbacks, and artifact-based checkpoints—culminating in a governance-ready, SOP-backed capstone.

## Modules Summary Table
| Module | Duration | Tools/Features | Hands-on minutes | Primary Artifacts |
|---|---|---|---|---|
| 1. LLM Fundamentals & Prompt Mechanics | 03:00 | ChatGPT (base chat), RTCFCE prompting pattern, Custom Instructions (preview) | 90 | prompt_set.xlsx |
| 2. Context Engineering & Memory/Custom Instructions | 03:00 | Custom Instructions/Memory, File uploads (CSV), Custom GPT Builder + Knowledge (fallback) | 90 | CI_template.txt; before_after_log.csv |
| 3. Web-Grounded Research with Browse | 03:00 | Browse, inline bracketed citations, link inspection | 80 | brief.docx; sources.csv |
| 4. Advanced Data Analysis (ADA) for Pros | 03:00 | Advanced Data Analysis (code interpreter), Multi-file uploads; spreadsheet fallback | 100 | kpi_table.csv; chart.png; summary.txt |
| 5. Document & Table Intelligence (Vision) | 03:00 | Vision (PDF/image), ADA (validation), crop/re-upload | 100 | coverage_limits.csv; qa_report.txt |
| 6. Image Generation & Multimodal Workflows | 03:00 | Image Generation, Vision (brand parsing), accessibility checks | 90 | hero_v1.png; hero_v2.png; rationale.txt; accessibility_checklist.txt |
| 7. Custom GPTs: Builder, Knowledge, No-Code Actions (simulated) | 03:00 | Custom GPT Builder, Knowledge files, structured JSON output, GPT Store (mock) | 100 | Custom GPT (unlisted); test_log.csv; store_listing.txt |
| 8. Teams/Enterprise Governance & Capstone | 03:00 | Teams/Enterprise settings, Browse, ADA, Vision, Image Gen, CI/Memory, Custom GPTs | 110 | capstone_pack.zip |

## 1. LLM Fundamentals & Prompt Mechanics
### Description:
Standardizes prompting with the RTCFCE structure (Role, Task, Context, Format, Constraints, Evaluation) and normalizes A/B prompt trials. Participants quantify how constraints and formats steer tone, structure, and fidelity—foundational for later context and multimodal work. Tools: ChatGPT (base chat), RTCFCE pattern, Custom Instructions (preview).

### Takeaways:
- Reusable RTCFCE prompt template and scoring rubric
- Replicable A/B evaluation workflow
- Practical levers to control style, structure, and fidelity

### Learning Goals:
- Participants author six RTCFCE prompts (three domain-specific, three general) with explicit constraints and evaluation criteria, saved to prompt_set.xlsx.
- Participants run vA/vB trials and score correctness, clarity, and constraint adherence in prompt_set.xlsx.
- Participants select winning variants and document rationale within prompt_set.xlsx for peer reuse.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes

## 2. Context Engineering & Memory/Custom Instructions
### Description:
Operationalizes Custom Instructions/Memory for personalization and file-based context to enforce terminology. Participants compare CI-on vs CI-off outcomes, reference glossary.csv by exact filename, and follow a feature-availability decision tree (Memory disabled → store profile as Knowledge in a Custom GPT). Tools: Custom Instructions/Memory, File uploads, Custom GPT Builder + Knowledge (fallback).

### Takeaways:
- Production-ready Custom Instructions and output preferences
- Measured evidence of CI impact on tone/structure/terminology
- Validated fallback path using Knowledge files

### Learning Goals:
- Participants configure Custom Instructions and export CI_template.txt (profile + output preferences).
- Participants run CI-on vs CI-off trials and log measurable deltas (tone, structure, terminology) in before_after_log.csv.
- Participants upload and reference glossary.csv by exact filename; record terminology alignment in before_after_log.csv.
- Participants document the decision path (CI vs Knowledge) and rationale in before_after_log.csv.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 3. Web-Grounded Research with Browse
### Description:
Implements a defensible Browse workflow prioritizing recency, credibility, and cross-verification. Participants cite only opened sources with access dates and maintain a structured source log for auditability. Tools: Browse (web-enabled), inline bracketed citations, link inspection, references with access dates.

### Takeaways:
- Transparent, auditable research workflow
- Practical heuristics for recency, credibility, relevance
- Structured source logging aligned to enterprise norms

### Learning Goals:
- Participants open and evaluate ≥3 reputable sources (≤12 months) and record quotes/metadata in sources.csv.
- Participants produce a one-page brief with inline bracketed citations and a references list with access dates, saved as brief.docx.
- Participants verify one-to-one mapping between inline citations in brief.docx and entries in sources.csv.

### Exercise Description:
Duration: 80 minutes, Debrief: 20 minutes

## 4. Advanced Data Analysis (ADA) for Pros
### Description:
Applies ADA to multi-file CSV analysis: join on quarter, compute KPIs, visualize, and write a concise, assumption-transparent narrative with outlier flags. Spreadsheet fallback applies (pseudo-calculations + visual spec) if ADA is unavailable. Tools: Advanced Data Analysis, Multi-file uploads, CSV export; spreadsheet fallback.

### Takeaways:
- Reproducible join–transform–visualize pipeline
- Portable KPI tables and charts
- Concise narrative with assumptions and outliers

### Learning Goals:
- Participants join sales_q1_q4.csv with targets.csv and export kpi_table.csv (revenue variance and units per product).
- Participants export a labeled KPI bar chart with currency formatting as chart.png.
- Participants author a ≤150-word summary with assumptions and outliers (>2 SD) saved as summary.txt.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 5. Document & Table Intelligence (Vision)
### Description:
Uses Vision to locate, extract, and normalize tables from PDFs/images; validates numeric integrity with ADA. Emphasizes OCR/structure error handling, clarifying questions, and crop/re-upload strategies for skewed inputs; culminates in a five-check QA report. Tools: Vision (PDF/image), ADA (validation), image preprocessing (crop/re-upload).

### Takeaways:
- Reliable Vision extraction and normalization workflow
- Numeric validation and reconciliation via ADA
- Transparent QA/error logging suitable for audit

### Learning Goals:
- Participants extract the “Coverage limits” table from policy_handbook.pdf and table_screenshot.png and export coverage_limits.csv preserving headers.
- Participants validate totals/ranges with ADA and record issues/corrections in qa_report.txt (≥5 checks).
- Participants apply crop/re-upload and document interventions in qa_report.txt when OCR fidelity is low.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 6. Image Generation & Multimodal Workflows
### Description:
Combines Vision-based brand parsing with Image Generation to produce on-brief assets under brand and accessibility constraints. Participants generate three comps, refine to two finals, verify color contrast, write alt-text, and justify design choices. Tools: Image Generation, Vision (Brand_Guide.pdf parsing), accessibility checks (contrast ratios, alt-text).

### Takeaways:
- Lightweight brand-to-asset creative pipeline
- Accessibility-first checks embedded in review
- Rationale discipline linking visuals to constraints

### Learning Goals:
- Participants reflect Brand_Guide.pdf palette/constraints in two images (hero_v1.png; hero_v2.png) derived from three comps.
- Participants compile accessibility_checklist.txt (contrast notes + alt-text for each image).
- Participants author a 120-word rationale linking design choices to brand rules, saved as rationale.txt.

### Exercise Description:
Duration: 90 minutes, Debrief: 20 minutes

## 7. Custom GPTs: Builder, Knowledge, No-Code Actions (simulated)
### Description:
Builds a task-specific assistant via Custom GPT Builder with an RTCFCE system prompt and Knowledge files, enforcing Knowledge-only citations and “I don’t know” behavior. Simulates a no-code Action through structured JSON output and prepares a GPT Store listing mock; includes base ChatGPT simulation fallback. Tools: Custom GPT Builder, Knowledge files, structured JSON output, GPT Store (mock); base ChatGPT + file uploads (fallback).

### Takeaways:
- Working Custom GPT scaffold with guardrails
- Retrieval QA/testing log with citation integrity
- Parseable JSON output for downstream tools

### Learning Goals:
- Participants create an unlisted “Team FAQ Assistant” requiring Knowledge-only citations with page/line and explicit “I don’t know.”
- Participants upload Product_FAQ.docx, Policy_Guide.pdf, glossary.csv; test ≥5 questions and log retrieval fidelity in test_log.csv.
- Participants produce both a human-readable answer and a JSON block {answer, citations, confidence}; draft store_listing.txt with governance notes.

### Exercise Description:
Duration: 100 minutes, Debrief: 20 minutes
Checkpoint rubric applies

## 8. Teams/Enterprise Governance & Capstone
### Description:
Operationalizes Teams/Enterprise data controls, retention, and workspace sharing. Executes an end-to-end capstone integrating ≥3 tools (e.g., Vision + ADA + Browse) using only synthetic/redacted data. Delivers a formal SOP, governance checklist, RACI, and measurable acceptance criteria. Tools: Teams/Enterprise settings, Browse, ADA, Vision, Image Generation, Custom Instructions/Memory, Custom GPTs.

### Takeaways:
- Governance-compliant, SOP-backed end-to-end workflow
- RACI and acceptance criteria enabling replication
- Practical privacy/compliance posture for ongoing use

### Learning Goals:
- Participants document relevant Teams/Enterprise settings in the SOP within capstone_pack.zip.
- Participants execute a cross-tool workflow (≥3 tools) using synthetic/redacted inputs and include all artifacts in capstone_pack.zip.
- Participants include a governance checklist, RACI, and measurable acceptance criteria in capstone_pack.zip and note any fallbacks used.

### Exercise Description:
Duration: 110 minutes, Debrief: 30 minutes

### Assessment touchpoints and capstone expectations
- Practical checkpoints after Modules 2, 4, 5, and 7 using the rubric (scale 1–4): Correctness; Clarity/Structure; Grounding/Citations (if relevant); Reproducibility; Compliance (privacy/brand). Passing requires average at least three with no criterion below two.
- Capstone rubric (Module 8): End-to-end completeness; Tool integration (≥3 tools); Evidence grounding; Governance/SOP quality; Business relevance. Passing requires average at least three and Governance at least three.
- Feature-availability fallbacks: Memory disabled → Knowledge-as-profile in a Custom GPT; ADA unavailable → spreadsheet pseudo-calculations + visual spec; Builder disabled → simulate in base ChatGPT with file uploads and strict system prompt; Vision OCR degraded → crop/re-upload and annotate manual corrections. Always use synthetic/redacted data.
</code>

Saved to: /Users/elenahernandez/projects/agents/Denario/examples/course_project/20251202_182301/course_outline_generation_output/control/course_outline.md

---

### 2) syllabus_crosswalk.csv
<code>course_title,total_hours,module_number,module_title,duration_hh:mm,objectives,tools_covered,assessment_artifact
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",1,"LLM Fundamentals & Prompt Mechanics","03:00","Apply RTCFCE prompt patterns; A/B test six prompts; select winners with rationale.","ChatGPT (base chat); RTCFCE prompting; Custom Instructions (preview)","prompt_set.xlsx"
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",2,"Context Engineering & Memory/Custom Instructions","03:00","Configure Custom Instructions; run CI-on vs CI-off; reference glossary.csv by filename; document decision path if Memory disabled. Checkpoint rubric applies","Custom Instructions/Memory; File uploads (CSV); Custom GPT Builder + Knowledge (fallback)","CI_template.txt; before_after_log.csv"
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",3,"Web-Grounded Research with Browse","03:00","Use Browse to collect and cross-verify ≥3 recent reputable sources; produce 1-page brief with inline citations and access dates; maintain sources log.","Browse; Inline bracketed citations; Link inspection","brief.docx; sources.csv"
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",4,"Advanced Data Analysis (ADA) for Pros","03:00","Analyze multi-file CSVs (join on quarter); compute revenue variance; export KPI CSV, chart PNG, and ≤150-word narrative; flag outliers. Checkpoint rubric applies","Advanced Data Analysis (code interpreter); Multi-file uploads; Spreadsheet fallback","kpi_table.csv; chart.png; summary.txt"
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",5,"Document & Table Intelligence (Vision)","03:00","Extract targeted table from PDF/image; normalize to CSV; validate with ADA; produce QA report with ≥5 checks. Checkpoint rubric applies","Vision (PDF/image); ADA (validation); Crop/re-upload","coverage_limits.csv; qa_report.txt"
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",6,"Image Generation & Multimodal Workflows","03:00","Parse brand guide with Vision; generate and refine 2 images; provide 120-word rationale; deliver accessibility checklist (alt-text, contrast).","Image Generation; Vision (brand parsing); Accessibility checks","hero_v1.png; hero_v2.png; rationale.txt; accessibility_checklist.txt"
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",7,"Custom GPTs: Builder, Knowledge, No-Code Actions (simulated)","03:00","Create unlisted ‘Team FAQ Assistant’ with Knowledge-only citations; test 5 queries; output JSON block; prepare mock store listing. Checkpoint rubric applies","Custom GPT Builder; Knowledge files; Structured JSON outputs; GPT Store (mock)","test_log.csv; store_listing.txt"
"ChatGPT Pro Power User: No-Code Productivity and Analysis","24:00",8,"Teams/Enterprise Governance & Capstone","03:00","Configure data controls and workspace sharing; execute an end-to-end flow using ≥3 tools with synthetic/redacted data; deliver SOP, governance checklist, RACI, acceptance criteria.","Teams/Enterprise settings; Browse; ADA; Vision; Image Generation; CI/Memory; Custom GPTs","capstone_pack.zip"
</code>

Saved to: /Users/elenahernandez/projects/agents/Denario/examples/course_project/20251202_182301/course_outline_generation_output/control/syllabus_crosswalk.csv

---

### 3) facilitation_notes.pdf
<code>Page 1 — Module 1: LLM Fundamentals & Prompt Mechanics
- Start phrase: Standardize prompting via RTCFCE and quantify impact through disciplined A/B trials; this anchors subsequent modules.
- Demo checklist: Walk RTCFCE anatomy; run vA/vB on a short policy; score with rubric; discuss how constraints shift tone/structure.
- Common pitfall: Vague constraints and missing evaluation criteria leading to unscorable outputs.
- Fallback step: If time is constrained, evaluate three prompts synchronously and assign the remaining three asynchronously with rubric.
- Assessment cue: Confirm prompt_set.xlsx includes six prompts, vA/vB scores, and rationale for winners.

Page 2 — Module 2: Context Engineering & Memory/Custom Instructions
- Start phrase: Operationalize personalization—measure CI-on vs CI-off and lock in a durable context path.
- Demo checklist: Enable Custom Instructions; paste profile/output prefs; upload glossary.csv; run identical task with CI-on and CI-off; compare.
- Common pitfall: Referencing glossary terms without naming the file; overly generic CI text.
- Fallback step: If Memory disabled, store profile as Knowledge in a Custom GPT and re-run the comparison within that GPT.
- Assessment cue: Verify CI_template.txt specificity and before_after_log.csv captures measurable deltas and chosen decision path. Checkpoint rubric applies.

Page 3 — Module 3: Web-Grounded Research with Browse
- Start phrase: Research must be recent, credible, and transparent—cite only what you actually opened.
- Demo checklist: Start browsing-enabled chat; open two reputable sources; extract quotes; add bracketed citations; compile references with access dates.
- Common pitfall: Citing unseen or outdated sources; missing access dates.
- Fallback step: If Browse blocked, use an instructor-curated source pack and model cross-verification manually.
- Assessment cue: Ensure brief.docx uses inline [1], [2], [3] mapping exactly to sources.csv entries.

Page 4 — Module 4: Advanced Data Analysis (ADA) for Pros
- Start phrase: Join, compute, visualize—defend KPIs with assumptions and outlier flags.
- Demo checklist: Upload sales_q1_q4.csv and targets.csv; join on quarter; compute variance; render bar chart; export CSV/PNG; write ≤150-word narrative.
- Common pitfall: Misaligned quarters and inconsistent currency formatting; ignoring outliers.
- Fallback step: If ADA unavailable, execute pseudo-calculations and a visual spec; validate figures in a spreadsheet.
- Assessment cue: Review kpi_table.csv, chart.png, and summary.txt for correctness, readability, and outlier documentation. Checkpoint rubric applies.

Page 5 — Module 5: Document & Table Intelligence (Vision)
- Start phrase: Extract, normalize, validate—Vision plus ADA to tame OCR uncertainty.
- Demo checklist: Upload policy_handbook.pdf and table_screenshot.png; locate/extract the Coverage limits table; export CSV; validate totals/ranges in ADA; log corrections.
- Common pitfall: Accepting OCR output without QA; lost headers during extraction.
- Fallback step: Crop skewed regions and re-upload; if fidelity remains low, apply manual corrections and annotate them.
- Assessment cue: Confirm coverage_limits.csv preserves headers and qa_report.txt lists ≥5 checks with pass/fail and clarifications. Checkpoint rubric applies.

Page 6 — Module 6: Image Generation & Multimodal Workflows
- Start phrase: Translate brand constraints into accessible assets—contrast and alt-text matter.
- Demo checklist: Parse Brand_Guide.pdf with Vision; generate three comps; refine to two finals; note contrast; author alt-text; write rationale.
- Common pitfall: Palette violations or photorealistic people where prohibited; missing accessibility details.
- Fallback step: If Image Generation constrained, produce visual briefs/specs and complete accessibility and rationale artifacts for external production.
- Assessment cue: Validate hero_v1.png, hero_v2.png, rationale.txt, and accessibility_checklist.txt for brand fit and WCAG considerations.

Page 7 — Module 7: Custom GPTs: Builder, Knowledge, No-Code Actions (simulated)
- Start phrase: Codify guardrails—Knowledge-only citations and parseable outputs for downstream tools.
- Demo checklist: Open GPT Builder; set RTCFCE system prompt with “cite only from Knowledge”; upload Product_FAQ.docx, Policy_Guide.pdf, glossary.csv; test 5 questions; require JSON block; draft store listing.
- Common pitfall: Hallucinated citations or omitting the JSON block; missing “I don’t know” handling.
- Fallback step: If Builder disabled, simulate in base ChatGPT with attached files and a strict system prompt; maintain JSON requirement.
- Assessment cue: Inspect test_log.csv for retrieval fidelity and store_listing.txt for governance notes; confirm JSON structure. Checkpoint rubric applies.

Page 8 — Module 8: Teams/Enterprise Governance & Capstone
- Start phrase: Integrate ≥3 tools under governance—deliver an SOP that peers can run.
- Demo checklist: Walk through Teams settings (data controls, retention, sharing); execute chosen end-to-end flow (e.g., Vision + ADA + Browse) with synthetic/redacted data; compile SOP, governance checklist, RACI, acceptance criteria.
- Common pitfall: Using non-synthetic or confidential data; undocumented fallbacks.
- Fallback step: If any feature is unavailable, trigger the decision path and record alternates in the SOP; maintain artifact integrity.
- Assessment cue: Inspect capstone_pack.zip for SOP completeness, governance checklist, RACI, acceptance criteria, and cross-tool artifacts.
</code>

Saved to: /Users/elenahernandez/projects/agents/Denario/examples/course_project/20251202_182301/course_outline_generation_output/control/facilitation_notes.pdf

---

Final save paths for all three deliverables:
- /Users/elenahernandez/projects/agents/Denario/examples/course_project/20251202_182301/course_outline_generation_output/control/course_outline.md
- /Users/elenahernandez/projects/agents/Denario/examples/course_project/20251202_182301/course_outline_generation_output/control/syllabus_crosswalk.csv
- /Users/elenahernandez/projects/agents/Denario/examples/course_project/20251202_182301/course_outline_generation_output/control/facilitation_notes.pdf

Disregard previously mis-saved files (e.g., chatgpt_pro_power_user_24hr_intensive.md, ChatGPT_Pro_Power_User_24hr_Intensive.md, chatgpt_pro_power_user_24hr_syllabus.md, ChatGPT_Pro_Power_User_NoCode_24hr_Curriculum.md, ChatGPT_Pro_Power_User_No-Code_Productivity_and_Analysis_24hr_Intensive.md, ChatGPT_Pro_Power_User_No-Code_Productivity_24hr_Intensive.md, ChatGPT_Pro_Power_User_No-Code_24hr_Intensive.md, chatgpt_pro_power_user_no-code_24hr_intensive.md).</code>