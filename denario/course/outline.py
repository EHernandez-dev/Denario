import re
from pathlib import Path
import cmbagent

from .key_manager import KeyManager
from denario.prompts.course_outline import course_outline_planner_prompt, course_outline_researcher_prompt
from .utils import create_work_dir, get_task_result


class CourseOutline:
    """
    This class is used to develop a course outline based on a course idea.

    It uses the `researcher` agent to create a structured course outline with:
    - Modules organized from foundational to advanced concepts
    - Description, Takeaways, and Learning Goals for each module
    - Exercise duration estimates

    Args:
        course_idea: The course idea including topic, target audience, and duration.
        keys: KeyManager instance with API keys.
        work_dir: Working directory for output files.
        researcher_model: LLM model for the researcher agent.
        planner_model: LLM model for the planner agent.
        plan_reviewer_model: LLM model for the plan reviewer agent.
        orchestration_model: LLM model for orchestration.
        formatter_model: LLM model for formatting responses.
    """

    def __init__(self,
                 course_idea: str,
                 keys: KeyManager,
                 work_dir: str | Path,
                 researcher_model: str = "gpt-4.1-2025-04-14",
                 planner_model: str = "gpt-4.1-2025-04-14",
                 plan_reviewer_model: str = "o3-mini",
                 orchestration_model: str = "gpt-4.1",
                 formatter_model: str = "o3-mini",
                ):

        self.researcher_model = researcher_model
        self.planner_model = planner_model
        self.plan_reviewer_model = plan_reviewer_model
        self.orchestration_model = orchestration_model
        self.formatter_model = formatter_model
        self.api_keys = keys

        self.outline_dir = create_work_dir(work_dir, "course_outline")

        # Set prompts with course_idea formatted in
        self.planner_append_instructions = course_outline_planner_prompt.format(course_idea=course_idea)
        self.researcher_append_instructions = course_outline_researcher_prompt.format(course_idea=course_idea)

    def generate(self, course_description: str = "") -> str:
        """
        Generates the course outline based on the course idea.

        Args:
            course_description: Optional additional description or context for the course.
                               If empty, uses the course idea alone.

        Returns:
            str: The generated course outline in markdown format.
        """

        # If no additional description provided, use a minimal placeholder
        if not course_description:
            course_description = "Generate the course outline based on the course idea provided above."

        results = cmbagent.planning_and_control_context_carryover(
            course_description,
            n_plan_reviews=1,
            max_n_attempts=4,
            max_plan_steps=6,
            researcher_model=self.researcher_model,
            planner_model=self.planner_model,
            plan_reviewer_model=self.plan_reviewer_model,
            plan_instructions=self.planner_append_instructions,
            researcher_instructions=self.researcher_append_instructions,
            work_dir=self.outline_dir,
            api_keys=self.api_keys,
            default_llm_model=self.orchestration_model,
            default_formatter_model=self.formatter_model
        )

        chat_history = results['chat_history']

        try:
            task_result = get_task_result(chat_history, 'researcher_response_formatter')
        except Exception as e:
            raise e

        # Extract markdown content from code block if present
        MD_CODE_BLOCK_PATTERN = r"```[ \t]*(?:markdown)?[ \t]*\r?\n(.*)\r?\n[ \t]*```"
        matches = re.findall(MD_CODE_BLOCK_PATTERN, task_result, flags=re.DOTALL)

        if matches:
            extracted_outline = matches[0]
            # Remove any HTML comments
            clean_outline = re.sub(r'^<!--.*?-->\s*\n', '', extracted_outline)
        else:
            # If no markdown code block, use the result as-is
            clean_outline = task_result

        return clean_outline
