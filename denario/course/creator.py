import os
import shutil
from datetime import datetime

from .key_manager import KeyManager
from .idea import CourseIdea
from .outline import CourseOutline
from .utils import input_check, in_notebook


# Config constants
DEFAULT_PROJECT_NAME = "course_project"
INPUT_FILES = "input_files"
TOPIC_FILE = "topic.md"
IDEA_FILE = "idea.md"
OUTLINE_FILE = "outline.md"


class CourseCreator:
    """
    CourseCreator main class. Orchestrates the course creation workflow:

    1. Set topic, audience, and duration
    2. Generate course idea using idea_maker/idea_hater agents
    3. Generate course outline using researcher agent

    Uses cmbagent backend for detailed planning and control.

    Each run creates a timestamped subfolder within the project directory,
    preserving all outputs from previous runs.

    Args:
        project_dir: Directory for project outputs. If None, creates a 'course_project' folder.
        clear_project_dir: Clear all files in project directory when initializing if True.

    Attributes:
        project_dir: The root project directory.
        work_dir: The timestamped directory for this run (e.g., project_dir/20251126_143000/).

    Example:
        ```python
        from denario.course import CourseCreator

        creator = CourseCreator(project_dir="./my_course")
        # Creates: ./my_course/20251126_143000/
        creator.set_topic("Python for Data Science", "Beginners", "2 days")
        creator.generate_idea()
        creator.show_idea()
        creator.generate_outline()
        creator.show_outline()
        ```
    """

    def __init__(self,
                 project_dir: str | None = None,
                 clear_project_dir: bool = False,
                 ):

        if project_dir is None:
            project_dir = os.path.join(os.getcwd(), DEFAULT_PROJECT_NAME)
        if not os.path.exists(project_dir):
            os.mkdir(project_dir)

        self.clear_project_dir = clear_project_dir

        if os.path.exists(project_dir) and clear_project_dir:
            shutil.rmtree(project_dir)
            os.makedirs(project_dir, exist_ok=True)
        self.project_dir = project_dir

        # Create timestamped work directory for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.work_dir = os.path.join(project_dir, timestamp)
        os.makedirs(self.work_dir, exist_ok=True)
        print(f"Run directory: {self.work_dir}")

        self._setup_input_files()

        # Get keys from environment
        self.keys = KeyManager()
        self.keys.get_keys_from_env()

        self.run_in_notebook = in_notebook()

        # Initialize state
        self.topic: str = ""
        self.audience: str = ""
        self.duration: str = ""
        self.idea: str = ""
        self.outline: str = ""

        # Try to load existing files
        self._load_existing()

    def _setup_input_files(self) -> None:
        """Create input files directory."""
        input_files_dir = os.path.join(self.work_dir, INPUT_FILES)
        os.makedirs(input_files_dir, exist_ok=True)

    def _load_existing(self) -> None:
        """Load existing files if present in the working directory."""
        # Load topic description
        try:
            topic_path = os.path.join(self.work_dir, INPUT_FILES, TOPIC_FILE)
            with open(topic_path, 'r') as f:
                self._topic_description = f.read()
        except FileNotFoundError:
            self._topic_description = ""

        # Load idea
        try:
            idea_path = os.path.join(self.work_dir, INPUT_FILES, IDEA_FILE)
            with open(idea_path, 'r') as f:
                self.idea = f.read()
        except FileNotFoundError:
            pass

        # Load outline
        try:
            outline_path = os.path.join(self.work_dir, INPUT_FILES, OUTLINE_FILE)
            with open(outline_path, 'r') as f:
                self.outline = f.read()
        except FileNotFoundError:
            pass

    # ---
    # Setters
    # ---

    def set_topic(self, topic: str, audience: str, duration: str) -> None:
        """
        Set the course topic, target audience, and duration.

        Args:
            topic: The subject/topic of the course (e.g., "Python for Data Science")
            audience: Target audience (e.g., "Beginners", "Intermediate developers")
            duration: Course duration (e.g., "2 days", "1 week", "8 hours")
        """
        self.topic = topic
        self.audience = audience
        self.duration = duration

        # Create the topic description that will be passed to agents
        self._topic_description = f"""
Topic: {topic}
Target Audience: {audience}
Duration: {duration}
"""

        # Save to file
        topic_path = os.path.join(self.work_dir, INPUT_FILES, TOPIC_FILE)
        with open(topic_path, 'w') as f:
            f.write(self._topic_description)

    def set_idea(self, idea: str | None = None) -> None:
        """
        Manually set a course idea.

        Args:
            idea: Course idea as a string or path to markdown file.
                  If None, tries to load from idea.md in work directory.
        """
        if idea is None:
            idea_path = os.path.join(self.work_dir, INPUT_FILES, IDEA_FILE)
            with open(idea_path, 'r') as f:
                idea = f.read()
        else:
            idea = input_check(idea)

        self.idea = idea

        # Save to file
        idea_path = os.path.join(self.work_dir, INPUT_FILES, IDEA_FILE)
        with open(idea_path, 'w') as f:
            f.write(idea)

    def set_outline(self, outline: str | None = None) -> None:
        """
        Manually set a course outline.

        Args:
            outline: Course outline as a string or path to markdown file.
                     If None, tries to load from outline.md in work directory.
        """
        if outline is None:
            outline_path = os.path.join(self.work_dir, INPUT_FILES, OUTLINE_FILE)
            with open(outline_path, 'r') as f:
                outline = f.read()
        else:
            outline = input_check(outline)

        self.outline = outline

        # Save to file
        outline_path = os.path.join(self.work_dir, INPUT_FILES, OUTLINE_FILE)
        with open(outline_path, 'w') as f:
            f.write(outline)

    # ---
    # Printers
    # ---

    def _printer(self, content: str) -> None:
        """Display content based on execution environment (notebook vs script)."""
        if self.run_in_notebook:
            from IPython.display import display, Markdown
            display(Markdown(content))
        else:
            print(content)

    def show_topic(self) -> None:
        """Show the topic description."""
        self._printer(self._topic_description)

    def show_idea(self) -> None:
        """Show the generated or set course idea."""
        if not self.idea:
            print("No idea generated yet. Run generate_idea() first.")
            return
        self._printer(self.idea)

    def show_outline(self) -> None:
        """Show the generated or set course outline."""
        if not self.outline:
            print("No outline generated yet. Run generate_outline() first.")
            return
        self._printer(self.outline)

    # ---
    # Generators
    # ---

    def generate_idea(self,
                      idea_maker_model: str = "gpt-4o",
                      idea_hater_model: str = "o3-mini",
                      planner_model: str = "gpt-4o",
                      plan_reviewer_model: str = "o3-mini",
                      orchestration_model: str = "gpt-4.1",
                      formatter_model: str = "o3-mini",
                      ) -> None:
        """
        Generate a course idea based on the topic, audience, and duration.

        Args:
            idea_maker_model: LLM for the idea maker agent.
            idea_hater_model: LLM for the idea hater/critic agent.
            planner_model: LLM for the planner agent.
            plan_reviewer_model: LLM for the plan reviewer agent.
            orchestration_model: LLM for orchestration.
            formatter_model: LLM for formatting responses.
        """
        if not self._topic_description:
            raise ValueError("No topic set. Call set_topic() first.")

        print("Generating course idea...")

        course_idea = CourseIdea(
            keys=self.keys,
            work_dir=self.work_dir,
            idea_maker_model=idea_maker_model,
            idea_hater_model=idea_hater_model,
            planner_model=planner_model,
            plan_reviewer_model=plan_reviewer_model,
            orchestration_model=orchestration_model,
            formatter_model=formatter_model,
        )

        self.idea = course_idea.generate(self._topic_description)

        # Save to file
        idea_path = os.path.join(self.work_dir, INPUT_FILES, IDEA_FILE)
        with open(idea_path, 'w') as f:
            f.write(self.idea)

        print("Course idea generated successfully.")

    def generate_outline(self,
                         researcher_model: str = "gpt-4.1-2025-04-14",
                         planner_model: str = "gpt-4.1-2025-04-14",
                         plan_reviewer_model: str = "o3-mini",
                         orchestration_model: str = "gpt-4.1",
                         formatter_model: str = "o3-mini",
                         ) -> None:
        """
        Generate a course outline based on the course idea.

        Args:
            researcher_model: LLM for the researcher agent.
            planner_model: LLM for the planner agent.
            plan_reviewer_model: LLM for the plan reviewer agent.
            orchestration_model: LLM for orchestration.
            formatter_model: LLM for formatting responses.
        """
        if not self.idea:
            raise ValueError("No course idea available. Call generate_idea() or set_idea() first.")

        print("Generating course outline...")

        course_outline = CourseOutline(
            course_idea=self.idea,
            keys=self.keys,
            work_dir=self.work_dir,
            researcher_model=researcher_model,
            planner_model=planner_model,
            plan_reviewer_model=plan_reviewer_model,
            orchestration_model=orchestration_model,
            formatter_model=formatter_model,
        )

        self.outline = course_outline.generate()

        # Save to file
        outline_path = os.path.join(self.work_dir, INPUT_FILES, OUTLINE_FILE)
        with open(outline_path, 'w') as f:
            f.write(self.outline)

        print("Course outline generated successfully.")

    def run(self,
            idea_maker_model: str = "gpt-4o",
            idea_hater_model: str = "o3-mini",
            researcher_model: str = "gpt-4.1-2025-04-14",
            planner_model: str = "gpt-4o",
            plan_reviewer_model: str = "o3-mini",
            orchestration_model: str = "gpt-4.1",
            formatter_model: str = "o3-mini",
            ) -> None:
        """
        Run the full course creation workflow: generate idea then generate outline.

        Args:
            idea_maker_model: LLM for the idea maker agent.
            idea_hater_model: LLM for the idea hater/critic agent.
            researcher_model: LLM for the researcher agent (outline generation).
            planner_model: LLM for the planner agent.
            plan_reviewer_model: LLM for the plan reviewer agent.
            orchestration_model: LLM for orchestration.
            formatter_model: LLM for formatting responses.
        """
        self.generate_idea(
            idea_maker_model=idea_maker_model,
            idea_hater_model=idea_hater_model,
            planner_model=planner_model,
            plan_reviewer_model=plan_reviewer_model,
            orchestration_model=orchestration_model,
            formatter_model=formatter_model,
        )

        self.generate_outline(
            researcher_model=researcher_model,
            planner_model=planner_model,
            plan_reviewer_model=plan_reviewer_model,
            orchestration_model=orchestration_model,
            formatter_model=formatter_model,
        )
