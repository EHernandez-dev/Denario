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
