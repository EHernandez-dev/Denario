import os
import re
import json
from pathlib import Path
import cmbagent

from .key_manager import KeyManager
from denario.prompts.course_slides import (
    course_slides_planner_prompt,
    course_slides_deep_research_planner_prompt,
    slide_architect_prompt,
    slide_content_creator_prompt,
    slide_reviewer_prompt,
    slide_refiner_prompt,
    slide_researcher_prompt,
    slides_engineer_prompt,
    MAIN_DECK_TEMPLATE,
    MODULE_IMPORT_TEMPLATE,
    BREAK_SLIDE_TEMPLATE,
)
from .utils import create_work_dir, get_task_result


class CourseSlides:
    """
    This class generates Slidev presentations from course outlines.

    It uses six types of agents:
    - `slide_architect`: Creates JSON structure mapping outline to slides
    - `slide_researcher`: Researches and expands module content (web search enabled)
    - `slides_engineer`: Generates code examples, visualizations, and diagrams
    - `slide_content_creator`: Generates Slidev markdown per module
    - `slide_reviewer`: Quality checks slides for text density, timing, etc.
    - `slide_refiner`: Improves slides based on reviewer feedback

    The workflow:
    1. slide_architect analyzes outline → JSON structure
    2. [If deep_research=True] For each module:
       - slide_researcher enriches content + identifies technical needs
       - slides_engineer generates code/visualizations (if needed)
    3. For each module: content_creator → reviewer → refiner
    4. slide_architect assembles main.md

    Args:
        course_outline: The course outline in markdown format.
        keys: KeyManager instance with API keys.
        work_dir: Working directory for output files.
        theme_path: Path to Slidev theme (for symlinking).
        architect_model: LLM for the slide architect agent.
        content_creator_model: LLM for content creation.
        reviewer_model: LLM for reviewing slides.
        refiner_model: LLM for refining slides.
        researcher_model: LLM for content research (web search enabled).
        engineer_model: LLM for generating code and visualizations.
        planner_model: LLM for the planner agent.
        plan_reviewer_model: LLM for the plan reviewer.
        orchestration_model: LLM for orchestration.
        formatter_model: LLM for formatting responses.
        deep_research: If True, run slide_researcher and slides_engineer
                       for richer content. If False, use existing outline
                       research only.
    """

    def __init__(self,
                 course_outline: str,
                 keys: KeyManager,
                 work_dir: str | Path,
                 theme_path: str | Path = "/Users/elenahernandez/projects/llm-power-user-training/theme",
                 architect_model: str = "gpt-4o",
                 content_creator_model: str = "gpt-4.1",
                 reviewer_model: str = "o3-mini",
                 refiner_model: str = "gpt-4.1",
                 researcher_model: str = "gpt-4.1",
                 engineer_model: str = "gpt-4.1",
                 planner_model: str = "gpt-4o",
                 plan_reviewer_model: str = "o3-mini",
                 orchestration_model: str = "gpt-4.1",
                 formatter_model: str = "o3-mini",
                 deep_research: bool = False,
                 ):

        self.course_outline = course_outline
        self.theme_path = Path(theme_path)
        self.architect_model = architect_model
        self.content_creator_model = content_creator_model
        self.reviewer_model = reviewer_model
        self.refiner_model = refiner_model
        self.researcher_model = researcher_model
        self.engineer_model = engineer_model
        self.planner_model = planner_model
        self.plan_reviewer_model = plan_reviewer_model
        self.orchestration_model = orchestration_model
        self.formatter_model = formatter_model
        self.deep_research = deep_research
        self.api_keys = keys

        self.slides_output_dir = create_work_dir(work_dir, "slides")
        self.work_dir = Path(work_dir)

        # Set prompts based on deep_research mode
        if deep_research:
            self.planner_append_instructions = course_slides_deep_research_planner_prompt.format(
                course_outline=course_outline
            )
        else:
            self.planner_append_instructions = course_slides_planner_prompt.format(
                course_outline=course_outline
            )
        self.slide_architect_instructions = slide_architect_prompt
        self.slide_content_creator_instructions = slide_content_creator_prompt
        self.slide_reviewer_instructions = slide_reviewer_prompt
        self.slide_refiner_instructions = slide_refiner_prompt
        self.slide_researcher_instructions = slide_researcher_prompt
        self.slides_engineer_instructions = slides_engineer_prompt

        # Will be populated during generation
        self.slide_structure: dict = {}
        self.slides_dir: Path | None = None
        self.enriched_content: dict = {}  # Research results per module
        self.generated_assets: dict = {}  # Engineer outputs per module

    def generate(self) -> Path:
        """
        Generates the Slidev presentation from the course outline.

        Returns:
            Path: Path to the slides/ directory containing the presentation.
        """

        if self.deep_research:
            print("Generating slides with deep research (researcher + engineer)...")
        else:
            print("Generating slide structure...")

        # Build agent parameters
        agent_params = {
            "slide_architect_model": self.architect_model,
            "slide_content_creator_model": self.content_creator_model,
            "slide_reviewer_model": self.reviewer_model,
            "slide_refiner_model": self.refiner_model,
            "planner_model": self.planner_model,
            "plan_reviewer_model": self.plan_reviewer_model,
            "plan_instructions": self.planner_append_instructions,
            "slide_architect_instructions": self.slide_architect_instructions,
            "slide_content_creator_instructions": self.slide_content_creator_instructions,
            "slide_reviewer_instructions": self.slide_reviewer_instructions,
            "slide_refiner_instructions": self.slide_refiner_instructions,
            "work_dir": self.slides_output_dir,
            "api_keys": self.api_keys,
            "default_llm_model": self.orchestration_model,
            "default_formatter_model": self.formatter_model,
        }

        # Add researcher and engineer if deep_research is enabled
        if self.deep_research:
            agent_params.update({
                "slide_researcher_model": self.researcher_model,
                "slides_engineer_model": self.engineer_model,
                "slide_researcher_instructions": self.slide_researcher_instructions,
                "slides_engineer_instructions": self.slides_engineer_instructions,
                "max_plan_steps": 20,  # More steps for research workflow
            })
        else:
            agent_params["max_plan_steps"] = 12  # Standard workflow

        results = cmbagent.planning_and_control_context_carryover(
            self.course_outline,
            n_plan_reviews=1,
            max_n_attempts=4,
            **agent_params
        )

        chat_history = results['chat_history']

        # Extract slide structure JSON from architect
        try:
            architect_result = get_task_result(chat_history, 'slide_architect_response_formatter')
            self.slide_structure = self._parse_json_structure(architect_result)
        except Exception as e:
            print(f"Warning: Could not extract slide structure: {e}")
            self.slide_structure = {}

        # Extract research and engineering outputs if deep_research was enabled
        if self.deep_research:
            self._extract_research_outputs(chat_history)

        # Create slides directory structure
        self.slides_dir = self._create_slides_folder()

        # Symlink the theme
        self._symlink_theme()

        # Extract and save module slides
        self._save_module_slides(chat_history)

        # Create main.md
        self._create_main_deck()

        print(f"Slides generated at: {self.slides_dir}")
        return self.slides_dir

    def _parse_json_structure(self, text: str) -> dict:
        """Extract JSON from text that may contain markdown code blocks."""
        # Try to find JSON in code block
        json_pattern = r"```(?:json)?\s*\n(.*?)\n```"
        matches = re.findall(json_pattern, text, flags=re.DOTALL)

        if matches:
            try:
                return json.loads(matches[0])
            except json.JSONDecodeError:
                pass

        # Try parsing the whole text as JSON
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {}

    def _create_slides_folder(self) -> Path:
        """Create the slides directory structure."""
        slides_dir = self.work_dir / "slides"
        src_dir = slides_dir / "src"

        os.makedirs(slides_dir, exist_ok=True)
        os.makedirs(src_dir, exist_ok=True)

        # Create module folders
        if self.slide_structure and "modules" in self.slide_structure:
            for module in self.slide_structure["modules"]:
                folder_name = module.get("folder_name", f"module_{module.get('module_num', 0):02d}")
                module_dir = src_dir / folder_name
                os.makedirs(module_dir, exist_ok=True)
                os.makedirs(module_dir / "images", exist_ok=True)

        return slides_dir

    def _symlink_theme(self) -> None:
        """Create symlink to the theme folder."""
        if not self.slides_dir:
            return

        theme_link = self.slides_dir / "theme"

        # Remove existing symlink if present
        if theme_link.exists() or theme_link.is_symlink():
            theme_link.unlink()

        # Create symlink if theme exists
        if self.theme_path.exists():
            os.symlink(self.theme_path, theme_link)
            print(f"Theme linked: {theme_link} -> {self.theme_path}")
        else:
            print(f"Warning: Theme path not found: {self.theme_path}")

    def _save_module_slides(self, chat_history: list) -> None:
        """Extract and save module slides from chat history."""
        if not self.slides_dir or not self.slide_structure:
            return

        src_dir = self.slides_dir / "src"

        # Try to extract slides for each module from chat history
        for module in self.slide_structure.get("modules", []):
            folder_name = module.get("folder_name", f"module_{module.get('module_num', 0):02d}")
            module_dir = src_dir / folder_name

            # Look for content creator output for this module
            # The agent name pattern may vary, try common patterns
            module_num = module.get("module_num", 0)
            possible_names = [
                f"slide_content_creator_module_{module_num}",
                f"slide_refiner_module_{module_num}",
                "slide_content_creator_response_formatter",
                "slide_refiner_response_formatter",
            ]

            slides_content = None
            for name in possible_names:
                try:
                    slides_content = get_task_result(chat_history, name)
                    if slides_content:
                        break
                except:
                    continue

            # If we found content, save it
            if slides_content:
                slides_path = module_dir / "slides.md"
                # Clean up markdown code blocks if present
                slides_content = self._extract_markdown(slides_content)
                with open(slides_path, 'w') as f:
                    f.write(slides_content)
            else:
                # Create placeholder
                slides_path = module_dir / "slides.md"
                placeholder = self._create_placeholder_slides(module)
                with open(slides_path, 'w') as f:
                    f.write(placeholder)

    def _extract_markdown(self, text: str) -> str:
        """Extract markdown from text that may be wrapped in code blocks."""
        # Try to find markdown in code block
        md_pattern = r"```(?:markdown|md)?\s*\n(.*?)\n```"
        matches = re.findall(md_pattern, text, flags=re.DOTALL)

        if matches:
            return matches[0]

        # Return as-is if no code block found
        return text

    def _create_placeholder_slides(self, module: dict) -> str:
        """Create placeholder slides for a module."""
        title = module.get("title", "Module")
        return f'''---
layout: Section
---
<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    {title}
  </div>
</div>

---

## Learning Goals

- [TODO: Add learning goals]

<!--
- Time: 1 minute
- Introduce module objectives
-->

---

## [Content Title]

- [TODO: Add content]

<!--
- Time: 3 minutes
- Key talking points
-->

---

## Key Takeaways

- [TODO: Add takeaways]

<!--
- Time: 2 minutes
- Summarize main points
-->
'''

    def _extract_research_outputs(self, chat_history: list) -> None:
        """Extract enriched content and generated assets from deep research workflow."""
        # Try to extract researcher outputs for each module
        for module in self.slide_structure.get("modules", []):
            module_num = module.get("module_num", 0)

            # Look for researcher output
            researcher_patterns = [
                f"slide_researcher_module_{module_num}",
                f"slide_researcher_response_formatter",
            ]
            for pattern in researcher_patterns:
                try:
                    researcher_result = get_task_result(chat_history, pattern)
                    if researcher_result:
                        parsed = self._parse_json_structure(researcher_result)
                        if parsed:
                            self.enriched_content[module_num] = parsed
                            break
                except Exception:
                    continue

            # Look for engineer output
            engineer_patterns = [
                f"slides_engineer_module_{module_num}",
                f"slides_engineer_response_formatter",
            ]
            for pattern in engineer_patterns:
                try:
                    engineer_result = get_task_result(chat_history, pattern)
                    if engineer_result:
                        parsed = self._parse_json_structure(engineer_result)
                        if parsed:
                            self.generated_assets[module_num] = parsed
                            break
                except Exception:
                    continue

        # Save research outputs for reference
        if self.enriched_content or self.generated_assets:
            research_dir = self.slides_output_dir / "control" / "research"
            os.makedirs(research_dir, exist_ok=True)

            if self.enriched_content:
                with open(research_dir / "enriched_content.json", 'w') as f:
                    json.dump(self.enriched_content, f, indent=2)

            if self.generated_assets:
                with open(research_dir / "generated_assets.json", 'w') as f:
                    json.dump(self.generated_assets, f, indent=2)

            print(f"Research outputs saved to: {research_dir}")

    def _create_main_deck(self) -> None:
        """Create the main.md file that assembles all modules."""
        if not self.slides_dir or not self.slide_structure:
            return

        course_title = self.slide_structure.get("course_title", "Course")
        tag = self.slide_structure.get("tag", "Training")
        presenter = self.slide_structure.get("presenter", "[Instructor Name]")

        # Build module imports with breaks
        module_imports = []
        breaks = {b["after_module"]: b for b in self.slide_structure.get("breaks", [])}

        for module in self.slide_structure.get("modules", []):
            folder_name = module.get("folder_name", f"module_{module.get('module_num', 0):02d}")
            module_num = module.get("module_num", 0)

            # Add module import
            module_imports.append(MODULE_IMPORT_TEMPLATE.format(folder_name=folder_name))

            # Add break after this module if specified
            if module_num in breaks:
                break_info = breaks[module_num]
                break_slide = BREAK_SLIDE_TEMPLATE.format(
                    break_type=break_info.get("type", "Break"),
                    duration=break_info.get("duration", "10 minutes")
                )
                module_imports.append(break_slide)

        # Assemble main.md
        main_content = MAIN_DECK_TEMPLATE.format(
            course_title=course_title,
            tag=tag,
            presenter=presenter,
            module_imports="\n".join(module_imports)
        )

        main_path = self.slides_dir / "main.md"
        with open(main_path, 'w') as f:
            f.write(main_content)

        # Save structure JSON for reference
        structure_path = self.slides_output_dir / "control" / "slide_structure.json"
        os.makedirs(structure_path.parent, exist_ok=True)
        with open(structure_path, 'w') as f:
            json.dump(self.slide_structure, f, indent=2)
