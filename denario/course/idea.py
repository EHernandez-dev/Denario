import os
import re
from pathlib import Path
import cmbagent

from .key_manager import KeyManager
from denario.prompts.course_idea import course_idea_planner_prompt
from .utils import create_work_dir, get_task_result

DELIBERATION_REPORT_FILE = "deliberation_report.md"

class CourseIdea:
    """
    This class is used to develop a course idea based on topic, audience, and duration.
    It makes use of two types of agents:

    - `idea_maker`: to generate new course ideas.
    - `idea_hater`: to critique ideas for pedagogy, feasibility, and audience fit.

    The LLMs are provided the following instructions:

    - Ask `idea_maker` to generate 5 new course ideas related to the topic.
    - Ask `idea_hater` to critique these ideas.
    - Ask `idea_maker` to select and improve 2 out of the 5 course ideas given the output of the `idea_hater`.
    - Ask `idea_hater` to critique the 2 improved ideas.
    - Ask `idea_maker` to select the best idea out of the 2.
    - Ask `idea_maker` to report the best idea in the form of a course title with a 5-sentence description.

    Args:
        keys: KeyManager instance with API keys.
        work_dir: Working directory for output files.
    """
    def __init__(self, 
                 keys: KeyManager,
                 work_dir: str | Path,
                 idea_maker_model = "gpt-4o", 
                 idea_hater_model = "o3-mini",
                 planner_model = "gpt-4o",
                 plan_reviewer_model = "o3-mini",
                 orchestration_model = "gpt-4.1",
                 formatter_model = "o3-mini",
                ):
        
        self.idea_maker_model = idea_maker_model
        self.idea_hater_model = idea_hater_model
        self.planner_model = planner_model
        self.plan_reviewer_model = plan_reviewer_model
        self.orchestration_model = orchestration_model
        self.formatter_model = formatter_model
        self.api_keys = keys

        self.idea_dir = create_work_dir(work_dir, "idea")

        # Set prompt
        self.planner_append_instructions = course_idea_planner_prompt
        
    def generate(self, course_description: str) -> tuple[str, str]:
        """
        Generates a course idea based on the course description.

        Args:
            course_description: Description including topic, target audience, and duration.

        Returns:
            tuple[T]: A tuple containing:
                - The generated course idea with title and description
                - The deliberation report summarizing all ideas and selection rationale
        """

        results = cmbagent.planning_and_control_context_carryover(course_description,
                              n_plan_reviews = 1,
                              max_plan_steps = 7,
                              idea_maker_model = self.idea_maker_model,
                              idea_hater_model = self.idea_hater_model,
                              plan_instructions=self.planner_append_instructions,
                              planner_model=self.planner_model,
                              plan_reviewer_model=self.plan_reviewer_model,
                              work_dir = self.idea_dir,
                              api_keys = self.api_keys,
                              default_llm_model = self.orchestration_model,
                              default_formatter_model = self.formatter_model
                             )

        chat_history = results['chat_history']

        # Extract the final course idea
        try:
            task_result = get_task_result(chat_history,'idea_maker_nest')
        except Exception as e:
            raise e

        pattern = r'\*\*Ideas\*\*\s*\n- Idea 1:'
        replacement = "Course Idea:"
        task_result = re.sub(pattern, replacement, task_result)

        ### Extract the deliberation report from formatter
        ##try:
        ##    deliberation_report = get_task_result(chat_history, 'formatter_nest')
        ##except Exception:
        ##    deliberation_report = "Deliberation report not available."

        ### Save the deliberation report to file
        ##report_path = os.path.join(self.idea_dir, DELIBERATION_REPORT_FILE)
        ##with open(report_path, 'w') as f:
        ##    f.write(deliberation_report)

        return task_result ##, deliberation_report
