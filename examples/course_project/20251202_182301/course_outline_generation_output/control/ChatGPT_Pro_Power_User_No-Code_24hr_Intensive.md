<!-- filename: chatgpt_pro_power_user_no-code_24hr_intensive.md -->
# ChatGPT Pro Power User: No-Code Productivity and Analysis — Revised 24-Hour Intensive

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

### Assessment touchpoints and capstone expectations
- Practical checkpoints after Modules 2, 4, 5, and 7 using the rubric (scale 1–4): Correctness; Clarity/Structure; Grounding/Citations (if relevant); Reproducibility; Compliance (privacy/brand). Passing requires average at least three with no criterion below two.
- Capstone rubric (Module 8): End-to-end completeness; Tool integration (≥3 tools); Evidence grounding; Governance/SOP quality; Business relevance. Passing requires average at least three and Governance at least three.
- Feature-availability fallbacks (document in artifacts and SOP): Memory disabled → Knowledge-as-profile in a Custom GPT; ADA unavailable → spreadsheet pseudo-calculations + visual spec; Builder disabled → simulate in base ChatGPT with file uploads and strict system prompt; Vision OCR degraded → crop/re-upload and annotate manual corrections. Always use synthetic/redacted data.

---

## Further resources for organizers
- OpenAI Help Center (Teams/Enterprise, ADA, Browse, Vision, Image Generation, Custom GPTs, GPT Store): https://help.openai.com
- OpenAI Policies (privacy, data usage, safety): https://openai.com/policies
- OpenAI Cookbook (prompting patterns, data workflows): https://github.com/openai/openai-cookbook
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- WCAG 2.1 (contrast and alt-text standards): https://www.w3.org/TR/WCAG21/

## Further resources for participants
- Getting started with Browse, ADA, and Vision in ChatGPT: https://help.openai.com
- Prompt engineering basics (OpenAI Cookbook): https://github.com/openai/openai-cookbook
- Responsible use of generative AI in the workplace (OpenAI policies): https://openai.com/policies
- W3C WAI tutorials (contrast and alt-text): https://www.w3.org/WAI/tutorials/
- Purdue OWL (research and citation primer): https://owl.purdue.edu/owl/research_and_citation/overview.html