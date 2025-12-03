# Course Creation Architecture

This document describes the complete agent workflow for generating courses from topic to slides.

## Overview

```
Topic + Audience + Duration
         │
         ▼
┌─────────────────┐
│  PHASE 1: IDEA  │  idea_maker + idea_hater
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PHASE 2: OUTLINE│  researcher (web search) -> TODO: ADD DEEP RESEARCH? Check OpenAI cookbook
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PHASE 3: SLIDES │  6 agents (architect, researcher, engineer,
└────────┬────────┘  content_creator, reviewer, refiner)
         │
         ▼
   Slidev Presentation
```

---

## Phase 1: Idea Generation

**Class:** `CourseIdea` (`denario/course/idea.py`)

**Input:** topic, audience, duration

```
Step 1: idea_maker → Generate 5 initial ideas
    │
    ▼
Step 2: idea_hater → Critique & rank all 5 ideas
    │
    ▼
Step 3: idea_maker → Improve top 2 ideas based on feedback
    │
    ▼
Step 4: idea_hater → Final critique, select best idea
    │
    ▼
Step 5: idea_maker → Polish final idea
    │
    ▼
Step 6: formatter → Format as markdown
```

**Output:** `idea.md` (refined course concept)

### Agents

| Agent | Model (default) | Role |
|-------|-----------------|------|
| idea_maker | gpt-4o | Generate and refine course ideas |
| idea_hater | o3-mini | Critique ideas, identify weaknesses |
note: it may be recommendable to use gpt-5 and gpt-5-mini for idea generation and critique
---

## Phase 2: Outline Generation

**Class:** `CourseOutline` (`denario/course/outline.py`)

**Input:** course idea

```
researcher (web search enabled) →
    │
    ├── Research topic, audience needs, prerequisites
    ├── Structure modules with learning goals
    ├── Add exercises, takeaways, further resources
    └── Generate supporting documents
```

**Outputs:**
```
{work_dir}/
├── input_files/
│   └── outline.md              # Structured course outline
└── course_outline_generation_output/
    └── control/
        ├── {Course}_Competencies.md      # Skills & tool mapping
        ├── {Course}_Prerequisites.md     # Background requirements
        └── {Course}_ProfessionalGuide.md # Expanded descriptions
```

### Agents

| Agent | Model (default) | Role |
|-------|-----------------|------|
| researcher | gpt-4.1 | Research content, structure modules (web search enabled) |
note: using gpt-5 takes ~3 hours while gpt-4.1 takes ~10 minutes
---

## Phase 3: Slide Generation

**Class:** `CourseSlides` (`denario/course/slides.py`)

**Input:** course outline + research context

### Workflow

```
STEP 1: ARCHITECTURE
  slide_architect → JSON structure
      ├── modules[] with folder_name, title, estimated_time
      ├── slides[] per module (section_title, learning_goals, content...)
      └── breaks[] with timing

STEP 2: MODULE-BY-MODULE CONTENT
┌─────────────────── FOR EACH MODULE ───────────────────┐
│                                                       │
│  [if deep_research=True]                              │
│      │                                                │
│      ▼                                                │
│  2a. slide_researcher (web search)                    │
│      ├── Fetch Further Resources URLs                 │
│      ├── Additional web searches                      │
│      └── Output: enriched_content + technical_reqs[]  │
│      │                                                │
│      ▼                                                │
│  2b. slides_engineer (if technical_reqs exist)        │
│      ├── Code examples (with Slidev highlighting)     │
│      ├── Mermaid diagrams                             │
│      └── Output: generated_assets[]                   │
│                                                       │
│      ▼                                                │
│  2c. slide_content_creator                            │
│      └── Output: Slidev markdown for module           │
│      │                                                │
│      ▼                                                │
│  2d. slide_reviewer                                   │
│      └── Critique: density, notes, timing, variety    │
│      │                                                │
│      ▼                                                │
│  2e. slide_refiner                                    │
│      └── Output: improved slides.md                   │
│                                                       │
└───────────────────────────────────────────────────────┘

STEP 3: FINAL REVIEW
  slide_reviewer → Quality check all modules

STEP 4: ASSEMBLY
  slide_architect → main.md (imports + breaks)
```

**Output:**
```
{work_dir}/slides/
├── main.md                 # Main deck (imports modules)
├── theme/                  # Symlink to Slidev theme
└── src/
    ├── module_01_intro/
    │   ├── slides.md
    │   └── images/
    ├── module_02_core/
    │   └── slides.md
    └── ...
```

### Agents

| Agent | Model (default) | Role |
|-------|-----------------|------|
| slide_architect | gpt-4o | Create JSON structure, assemble main.md |
| slide_researcher | gpt-4.1 | Enrich content via web search (deep_research only) |
| slides_engineer | gpt-4.1 | Generate code, diagrams, tables (deep_research only) |
| slide_content_creator | gpt-4.1 | Convert JSON spec → Slidev markdown |
| slide_reviewer | o3-mini | Quality check (density, timing, notes) |
| slide_refiner | gpt-4.1 | Improve slides based on feedback |

---

## Agent Responsibilities

### slide_architect
- **Input:** Course outline markdown
- **Output:** JSON structure mapping modules to slides
- Determines slide types: `section_title`, `learning_goals`, `content`, `exercise`, `takeaways`
- Suggests layouts: `default`, `twocols`
- Plans breaks based on course duration

### slide_researcher (deep_research only)
- **Input:** Module spec + Further Resources URLs
- **Output:** Enriched content JSON + technical_requirements[]
- Fetches curated URLs from outline
- Performs additional web searches for gaps
- Identifies content needing code/visualizations

### slides_engineer (deep_research only)
- **Input:** technical_requirements[] from researcher
- **Output:** generated_assets[] (code, diagrams, tables)
- Creates code examples with Slidev line highlighting
- Generates mermaid diagrams for workflows
- Produces markdown comparison tables

### slide_content_creator
- **Input:** Module JSON spec (+ enriched_content + assets if deep_research)
- **Output:** Valid Slidev markdown
- Converts JSON to slide format
- Adds speaker notes with timing
- Applies layouts, image placeholders

### slide_reviewer
- **Input:** Slidev markdown
- **Output:** Critique with issues and recommendations
- Checks: text density (max 6 bullets), speaker notes, timing, visual variety
- Validates Slidev syntax

### slide_refiner
- **Input:** Original slides + reviewer feedback
- **Output:** Improved Slidev markdown
- Splits dense slides
- Adds missing speaker notes
- Fixes layout issues

---

## Usage

```python
from denario.course import CourseCreator

creator = CourseCreator(project_dir="./my_course")

# Phase 1: Idea
creator.set_topic("Python for Data Science", "Beginners", "2 days")
creator.generate_idea()
creator.show_idea()

# Phase 2: Outline
creator.generate_outline()
creator.show_outline()

# Phase 3: Slides
creator.generate_slides(deep_research=True)   # Full research pipeline
# or
creator.generate_slides(deep_research=False)  # Faster, reuses outline research

creator.show_slides()
```

### deep_research Flag

| Value | Behavior |
|-------|----------|
| `False` (default) | Fast generation using existing outline research |
| `True` | Rich content with web search + code/diagram generation |

Use `deep_research=True` for:
- Final production slides
- Technical/code-heavy courses
- High-stakes training

Use `deep_research=False` for:
- Quick prototypes
- Internal team updates
- Iteration/testing

---

## File Structure

```
{project_dir}/
├── {timestamp}/                          # Run directory
│   ├── input_files/
│   │   ├── topic.md
│   │   ├── idea.md
│   │   └── outline.md
│   ├── idea_generation_output/
│   │   └── control/
│   │       ├── ideas_*.json              # Idea snapshots
│   │       └── chats/
│   ├── course_outline_generation_output/
│   │   └── control/
│   │       ├── {Course}_Competencies.md
│   │       ├── {Course}_Prerequisites.md
│   │       └── {Course}_ProfessionalGuide.md
│   └── slides/
│       ├── main.md
│       ├── theme/
│       └── src/
│           └── module_*/slides.md
```
