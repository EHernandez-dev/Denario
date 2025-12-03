# Course Creator: Implementation Plan

## Goal
Build a wrapper around cmbagent to achieve:
- **Objective 1**: Idea Generation (topic + audience + duration → course idea)
- **Objective 2**: Course Outline Generation (idea → topics, subtopics, learning objectives)

## Configuration
- **Location**: Within Denario on branch `prototype/course-outliner`
- **Models**: Configurable (no hardcoded defaults)
- **Mode**: cmbagent only (no LangGraph fast mode)

---

## Project Structure

```
/Users/elenahernandez/projects/agents/Denario/
├── denario/
│   ├── ... (existing files)
│   ├── course/                     # NEW: Course creator module
│   │   ├── __init__.py
│   │   ├── creator.py              # Main CourseCreator class
│   │   ├── idea.py                 # Idea generation wrapper
│   │   └── outline.py              # Outline generation wrapper
│   └── prompts/
│       ├── ... (existing)
│       ├── course_idea.py          # NEW: Prompts for idea generation
│       └── course_outline.py       # NEW: Prompts for outline generation
├── examples/
│   ├── ... (existing)
│   └── course_creation.py          # NEW: Example usage
└── ... (existing files)
```

---

## Implementation Steps

### Step 1: Create Module Structure
- [ ] Create `denario/course/` directory
- [ ] Create `denario/course/__init__.py`
- [ ] Reuse existing `key_manager.py` and `utils.py` from Denario

### Step 2: Create Idea Generation Prompts (`prompts/course_idea.py`)
- [ ] Write `course_idea_planner_prompt` - instructs planner to:
  - Use idea_maker to generate 3-5 course ideas
  - Use idea_hater to critique for pedagogy, feasibility, audience fit
  - Select and refine the best idea
  - Output: Title + 3-5 sentence description

### Step 3: Create Outline Generation Prompts (`prompts/course_outline.py`)
- [ ] Write `course_outline_planner_prompt` - instructs planner to create outline
- [ ] Write `course_outline_researcher_prompt` - instructs researcher to:
  - Structure content hierarchically (topics → subtopics)
  - Define learning objectives per section (Bloom's taxonomy)
  - Estimate duration per topic
  - Output: Structured markdown outline

### Step 4: Implement CourseIdea Class (`course/idea.py`)
- [ ] Create `CourseIdea` class (adapt from `denario/idea.py`)
- [ ] Constructor params: `keys`, `work_dir`, all model params configurable
- [ ] Implement `generate(topic, audience, duration)` method
- [ ] Call `cmbagent.planning_and_control_context_carryover()` with custom prompts

### Step 5: Implement CourseOutline Class (`course/outline.py`)
- [ ] Create `CourseOutline` class (adapt from `denario/method.py`)
- [ ] Constructor params: `course_idea`, `keys`, `work_dir`, all model params configurable
- [ ] Implement `generate()` method
- [ ] Call `cmbagent.planning_and_control_context_carryover()` with custom prompts

### Step 6: Implement Main CourseCreator Class (`course/creator.py`)
- [ ] Create `CourseCreator` orchestrator class
- [ ] Constructor: `project_dir`, `keys` (optional, auto-detect from env)
- [ ] Methods:
  - `set_topic(topic, audience, duration)` - stores input params
  - `generate_idea(**model_kwargs)` → stores idea
  - `generate_outline(**model_kwargs)` → stores outline
  - `show_idea()`, `show_outline()` - display methods
- [ ] All model params passed through to underlying classes

### Step 7: Create Example (`examples/course_creation.py`)
- [ ] Demonstrate full workflow:
  ```python
  from denario.course import CourseCreator

  creator = CourseCreator(project_dir="./my_course")
  creator.set_topic("Python for Data Science", "Beginners", "2 days")
  creator.generate_idea(idea_maker_model="gpt-4o", idea_hater_model="o3-mini")
  creator.show_idea()
  creator.generate_outline(researcher_model="gpt-4o")
  creator.show_outline()
  ```

### Step 8: Test & Iterate
- [ ] Test idea generation with different topics
- [ ] Test outline generation quality
- [ ] Adjust prompts based on output quality

---

## Key Files to Reference (Already in Denario)

| Denario File | Purpose | Action |
|--------------|---------|--------|
| `denario/idea.py` | Idea class pattern | Adapt for CourseIdea |
| `denario/method.py` | Method class pattern | Adapt for CourseOutline |
| `denario/prompts/idea.py` | Prompt structure | Reference for course prompts |
| `denario/utils.py` | `get_task_result()`, `create_work_dir()` | Import directly |
| `denario/key_manager.py` | API key handling | Import directly |

---

## Prompts Overview

### Idea Planner Prompt (Key Points)
```
You are planning a course idea generation workflow.
Available agents: idea_maker, idea_hater

Steps:
1. idea_maker: Generate 3-5 course ideas for {topic}, {audience}, {duration}
2. idea_hater: Critique ideas for pedagogy, feasibility, engagement
3. idea_maker: Refine top 2 ideas based on feedback
4. idea_hater: Final critique
5. idea_maker: Select best idea, format as title + description
```

### Outline Researcher Prompt (Key Points)
```
You are a curriculum designer creating a course outline.

For the course idea: {idea}

Create a structured outline with:
- 4-8 main topics (modules)
- 2-4 subtopics per module
- Learning objectives (use action verbs: explain, implement, analyze)
- Estimated duration per topic
- Prerequisites if any

Format as markdown with clear hierarchy.
```

---

## Success Criteria

| Objective | Success Metric |
|-----------|----------------|
| Idea Generation | Produces focused, audience-appropriate course idea |
| Outline Generation | Hierarchical structure with clear learning objectives |
| Integration | Both steps work in sequence |
| Output Quality | Minimal post-processing needed |

---

## Files to Create

| File | Description |
|------|-------------|
| `denario/course/__init__.py` | Exports CourseCreator, CourseIdea, CourseOutline |
| `denario/course/creator.py` | Main orchestrator class |
| `denario/course/idea.py` | CourseIdea class |
| `denario/course/outline.py` | CourseOutline class |
| `denario/prompts/course_idea.py` | Prompts for idea generation |
| `denario/prompts/course_outline.py` | Prompts for outline generation |
| `examples/course_creation.py` | Example usage script |

## Estimated Effort

| Step | Effort |
|------|--------|
| Steps 1-3 (Setup + Prompts) | ~1-2 hours |
| Steps 4-6 (Core Classes) | ~2-3 hours |
| Steps 7-8 (Example + Testing) | ~1-2 hours |
| **Total** | **~4-7 hours** |

---

# Objective 3: Slidev Slide Generation

## Goal
Extend the course agents to generate presentation slides using [Slidev](https://sli.dev/guide/syntax) (markdown-based presentations).

**Input:** Course outline (from Objective 2)
**Output:** Complete Slidev presentation with per-module slides

---

## Reference Theme

Use the existing theme from: `/Users/elenahernandez/projects/llm-power-user-training`

```
llm-power-user-training/
├── main.md                    # Main deck - assembles modules via src: imports
├── theme/                     # Custom theme
│   ├── layouts/               # Section, cover, twocols, default
│   └── components/            # Box, Grid, Prompt, Imgx, etc.
└── src/                       # Per-module folders
    ├── introduction/slides.md
    ├── prompt_and_context_engineering/slides.md
    └── ...
```

---

## New Agents for Slide Generation

| Agent | Role | Input | Output |
|-------|------|-------|--------|
| **slide_architect** | Designs slide deck structure | Course outline | JSON: modules → slide sequences |
| **slide_content_creator** | Generates Slidev markdown | Slide skeleton + module details | Slidev markdown per module |
| **slide_reviewer** | Critiques slides | Generated slides | Feedback on quality |
| **slide_refiner** | Improves slides | Slides + critique | Polished Slidev markdown |

---

## Slide Generation Workflow (6-Step Process)

```
CourseOutline (from Objective 2)
    ↓
Step 1: slide_architect analyzes outline, creates slide-per-module mapping (JSON)
    ↓
Step 2: slide_content_creator generates slides for MODULE 1
    ↓
Step 3: slide_reviewer critiques MODULE 1 (text density, speaker notes, visuals)
    ↓
Step 4: slide_refiner improves MODULE 1 based on feedback
    ↓
[Repeat Steps 2-4 for each module]
    ↓
Step 5: slide_reviewer final check on all modules
    ↓
Step 6: slide_architect assembles main.md with module imports + breaks
    ↓
Output: Complete Slidev presentation
```

---

## Slidev Format Patterns

### Main Deck (`main.md`)
```markdown
---
theme: ./theme
title: "Course Title"
tag: "Series Name"
mdc: true
---

Presenter Name <span class="font-light">(Role)</span>

---
src: ./src/module_01/slides.md
---

---
layout: Section
---
<div class='absolute top-50%'>
  <div style='text-align: left; font-size: 3rem;'>
    Break (10 minutes)
  </div>
</div>

---
src: ./src/module_02/slides.md
---
```

### Module Slides (`src/module/slides.md`)
```markdown
---
layout: Section
---
<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Module Title
  </div>
</div>

---

## Learning Goals

- Goal 1
- Goal 2
- Goal 3

<!--
- Time: 1 minute
- Briefly cover what participants will learn
-->

---

## Key Concept

Content with bullet points

<!--
- Time: 3 minutes
- Speaker notes with timing cues
-->

---
layout: twocols
---

# Left Column

::right::

# Right Column
```

### Speaker Notes Format
```markdown
<!--
- Time: X minutes
- Key talking point 1
- Key talking point 2
-->
```

---

## Slide Types Per Module

1. **Section title slide** - `layout: Section` with module name
2. **Learning goals slide** - Bullet list (3-5 goals)
3. **Content slides** (3-6) - Key concepts, use twocols where appropriate
4. **Exercise slide** - Activity with duration in speaker notes
5. **Takeaways slide** - Key points to remember

---

## Output Structure

```
course_project/
└── {timestamp}/
    ├── input_files/
    │   ├── topic.md
    │   ├── idea.md
    │   └── outline.md
    ├── slides/                        # NEW: Slidev presentation
    │   ├── main.md                   # Main deck (assembles modules)
    │   ├── theme -> ../../../llm-power-user-training/theme  # Symlink
    │   └── src/
    │       ├── module_01_intro/
    │       │   ├── slides.md
    │       │   └── images/
    │       ├── module_02_topic/
    │       │   └── slides.md
    │       └── ...
    ├── idea_generation_output/
    ├── course_outline_generation_output/
    └── slides_generation_output/      # NEW: Agent logs
        ├── control/
        │   ├── slide_structure.json
        │   └── chats/
        └── context/
```

---

## Implementation Steps

### Step 9: Create Slide Prompts (`prompts/course_slides.py`)
- [ ] Write `course_slides_planner_prompt` - orchestrates the 6-step workflow
- [ ] Write `slide_architect_prompt` - creates JSON structure mapping outline → slides
- [ ] Write `slide_content_creator_prompt` - generates Slidev markdown per module
- [ ] Write `slide_reviewer_prompt` - quality checklist for slides
- [ ] Write `slide_refiner_prompt` - improves based on feedback
- [ ] Add templates: `main_deck_template`, `break_slide_template`, `module_import_template`

### Step 10: Implement CourseSlides Class (`course/slides.py`)
- [ ] Create `CourseSlides` class (similar pattern to CourseOutline)
- [ ] Constructor params: `outline`, `work_dir`, `theme_path`, all model params
- [ ] Implement `generate()` method:
  - Call slide_architect to create structure
  - Loop through modules, generating slides per module
  - Review and refine each module
  - Assemble main.md
- [ ] Implement `_create_module_folder()` - creates src/module_XX/ structure
- [ ] Implement `_symlink_theme()` - links to llm-power-user-training theme

### Step 11: Update CourseCreator Class (`course/creator.py`)
- [ ] Add `generate_slides(**model_kwargs)` method:
  - Validates outline exists
  - Creates CourseSlides instance
  - Calls generate()
  - Saves to slides/ folder
- [ ] Add `show_slides()` method - displays main.md content
- [ ] Update `run()` method - optionally include slide generation

### Step 12: Update Module Exports (`course/__init__.py`)
- [ ] Export `CourseSlides` class
- [ ] Update `__all__` list

### Step 13: Update Example (`examples/course_creation.ipynb`)
- [ ] Add slide generation cell:
  ```python
  creator.generate_slides(
      architect_model="gpt-4o",
      content_model="gpt-4.1",
      reviewer_model="o3-mini",
      refiner_model="gpt-4.1"
  )
  creator.show_slides()
  ```
- [ ] Add cell to view slides per module

### Step 14: Test & Iterate
- [ ] Test with existing course outline
- [ ] Verify Slidev renders correctly (`npx slidev slides/main.md`)
- [ ] Adjust prompts for quality
- [ ] Test theme symlink works

---

## Agent Design Details

### slide_architect
**Purpose:** Map outline structure to slide sequences (per-module)

**Output JSON:**
```json
{
  "course_title": "ChatGPT Bootcamp",
  "tag": "LLM Power User Training",
  "modules": [
    {
      "module_num": 1,
      "folder_name": "module_01_llm_fundamentals",
      "title": "LLM Fundamentals & Prompt Mechanics",
      "estimated_time": "45 min",
      "slides": [
        {"type": "section_title", "title": "LLM Fundamentals"},
        {"type": "learning_goals", "items": ["Goal 1", "Goal 2"]},
        {"type": "content", "title": "What is an LLM?", "has_code": false},
        {"type": "content", "title": "Prompt Patterns", "has_code": true, "layout": "twocols"},
        {"type": "exercise", "title": "Hands-on", "duration": "15 min"},
        {"type": "takeaways", "items": ["Key point 1", "Key point 2"]}
      ]
    }
  ],
  "breaks": [
    {"after_module": 2, "duration": "10 minutes"},
    {"after_module": 4, "duration": "1 hour", "type": "Lunch"}
  ]
}
```

### slide_content_creator
**Guidelines:**
- Max 6 bullet points per slide
- MUST include speaker notes with timing: `<!-- Time: X minutes -->`
- Use layouts: `Section`, `default`, `twocols`
- Code examples: fenced blocks with language
- Image placeholders: `![Description](./images/placeholder_01.png)`

### slide_reviewer
**Quality Checklist:**
- [ ] Text density: Max 6 bullets, 50 words per slide
- [ ] Speaker notes present with timing cues
- [ ] Total module time matches estimate
- [ ] Visual variety (not all bullet lists)
- [ ] Code blocks have syntax highlighting language
- [ ] Image placeholders have descriptive alt text

### slide_refiner
**Actions:**
- Split dense slides into multiple
- Add missing speaker notes with timing
- Convert bullet lists to twocols where appropriate
- Ensure code examples are properly formatted

---

## Files to Create/Modify (Objective 3)

| File | Action | Description |
|------|--------|-------------|
| `denario/prompts/course_slides.py` | Create | All slide agent prompts + templates |
| `denario/course/slides.py` | Create | CourseSlides class |
| `denario/course/creator.py` | Modify | Add `generate_slides()`, `show_slides()` |
| `denario/course/__init__.py` | Modify | Export CourseSlides |
| `examples/course_creation.ipynb` | Modify | Add slide generation example |

---

## Design Decisions

| Question | Decision |
|----------|----------|
| Per-module or all at once? | **Per-module** (incremental generation) |
| Theme | Symlink to `llm-power-user-training/theme` |
| Code highlighting | Yes - proper syntax highlighting |
| Image placeholders | Yes - with descriptive alt text |
| Speaker notes | Yes - with timing cues |

---

## Full Workflow Usage

```python
from denario.course import CourseCreator

# Initialize
creator = CourseCreator(project_dir="./my_course")

# Objective 1: Generate idea
creator.set_topic("ChatGPT for Professionals", "Business users", "1 day")
creator.generate_idea(idea_maker_model="gpt-4o", idea_hater_model="o3-mini")
creator.show_idea()

# Objective 2: Generate outline
creator.generate_outline(researcher_model="gpt-4.1")
creator.show_outline()

# Objective 3: Generate slides (NEW)
creator.generate_slides(
    architect_model="gpt-4o",
    content_model="gpt-4.1",
    reviewer_model="o3-mini",
    refiner_model="gpt-4.1"
)
creator.show_slides()

# Run Slidev to preview
# $ cd my_course/{timestamp}/slides && npx slidev main.md
```

---

## Estimated Effort (Objective 3)

| Step | Effort |
|------|--------|
| Step 9 (Slide Prompts) | ~2-3 hours |
| Step 10 (CourseSlides Class) | ~3-4 hours |
| Steps 11-12 (Integration) | ~1-2 hours |
| Steps 13-14 (Example + Testing) | ~2-3 hours |
| **Total** | **~8-12 hours** |

---

## Combined Effort (All Objectives)

| Objective | Effort |
|-----------|--------|
| Objectives 1-2 (Idea + Outline) | ~4-7 hours |
| Objective 3 (Slides) | ~8-12 hours |
| **Total Course Creator** | **~12-19 hours** |
