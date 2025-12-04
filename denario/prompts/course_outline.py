course_outline_planner_prompt = r"""
{course_idea}

Instruction for planning:

Given this course idea, including the topic, target audience, and duration, we want to design a comprehensive course outline.
The goal of the task is to write a plan that will be used to generate a detailed, structured course outline with modules, learning goals, and takeaways.

- Start by requesting the *researcher* to analyze the course idea and identify the core competencies and skills participants should develop.
- Ask the *researcher* to determine what participants need to know before the course (prerequisites).
- Request the *researcher* to propose around 8-10 main modules that logically build upon each other, progressing from foundational to advanced concepts.
- For each module, ask the *researcher* to write: a description of what the session covers, key takeaways (what participants leave with), and specific learning goals written as "Participants [action verb]...".
- Ask the *researcher* to include exercise duration estimates for hands-on modules.
- This can be done in multiple steps.
- The focus should be strictly on the course structure, learning goals, and takeaways. **Do not include** actual lesson slides, scripts, or full exercise materials.
- In the overview of each module, explicitly name the tools and features that participants learn to use.
- The description should be written as if it were a senior researcher explaining to her research assistant how the course should be performed.

The final step of the plan must be entirely dedicated to writing the full Course Outline in structured markdown format.

The only agent involved in this workflow is the researcher.

In this task we do not create lesson content or materials, only outline the course structure.
"""

course_outline_researcher_prompt = r"""
{course_idea}

Given this course idea, we want to design a comprehensive course outline.
The goal of the task is to develop a detailed, pedagogically-sound course structure.

Guidelines for creating the outline:
- Organize content from foundational to advanced concepts (scaffolded learning progression)
- Ensure logical flow where each module builds on previous ones
- Include exercise duration estimates where appropriate
- For each module be thorough on which tools and features participants will learn to use.
- **Do not include** actual lesson slides, detailed scripts, or full exercise materials
- The course outline should be written as if it were a senior AI researcher explaining to her research assistant how to perform the course.

CRITICAL CONTENT REQUIREMENTS:
- You MUST explicitly name specific tools and features.

The course outline MUST be written in markdown format with the following structure:

# [Course Title]
### Overview:
[2-3 sentence description: what the course covers, who it's for, what participants will learn. Example: "This one-day, hands-on course is designed for professionals who want to integrate [topic] into their daily work. No technical background is required. Across X focused blocks, participants will learn how to..."]

## 1. [Module Title]
### Description:
[2-4 sentences explaining what this session covers and why it matters to participants]
### Takeaways:
- [Practical benefit participants leave with]
- [Practical benefit participants leave with]
- [Practical benefit participants leave with]
[...]
### Learning Goals:
- Participants [action verb] [specific measurable outcome].
- Participants [action verb] [specific measurable outcome].
- Participants [action verb] [specific measurable outcome].
[...]
### Exercise Description:
Duration: [X] minutes, Debrief: [Y] minutes

## 2. [Module Title]
### Description:
[...]
### Takeaways:
[...]
### Learning Goals:
[...]

[Continue for all modules] 

Create around 8-10 modules or more depending on course duration

Each module should have 3-8 learning goals.
Each module should have 3-5 takeaways.

At the end of the outline, include links to further resources that the course organizer can use to prepare the course.
Also include links to resources that participants can use to learn further
"""


# Extended outline prompts (instructor-focused with deep research)

extended_outline_planner_prompt = r"""
{course_idea}

Instruction for planning:

Given this course idea and the outline provided with learning goals and module structure, we want to create an EXTENDED INSTRUCTOR OUTLINE.
This outline helps speakers/instructors prepare and teach the course effectively.

- Start by requesting the *researcher* to analyze the student outline's modules and learning goals
- For EACH MODULE, ask the *researcher* to write:
  1. Do DEEP RESEARCH on each topic using web search to find current, authoritative resources
  2. A detailed description (2-4 paragraphs) explaining topics covered and their implications
  3. Instructor knowledge requirements (what they need to know to teach this module)
  4. Teaching tips and common pitfalls to avoid
  5. 3-5 instructor resources with real URLs (found via web search)
  6. Exercise description with duration estimates

- The *researcher* MUST use web search to find current, authoritative resources for instructor preparation
- IMPORTANT: Follow the SAME module structure as the student outline
- If after the research you would propose different modules, add it as a brief comment at the end of the outline and justify why
- Focus on what the INSTRUCTOR needs to know and prepare, not just student-facing content
- Be thorough about tools, features, and concepts the instructor must understand deeply

The final step of the plan must produce the complete Extended Instructor Outline in structured markdown format.

The only agent involved in this workflow is the researcher.

In this task we create an instructor preparation guide with deep research, not student-facing materials.
"""

extended_outline_researcher_prompt = r"""
{course_idea}

Create an EXTENDED INSTRUCTOR OUTLINE to help speakers/instructors prepare and teach this course effectively.

CRITICAL: You MUST use web search to find real, current resources for each module. This is essential for instructor preparation.

Guidelines for creating the extended outline:
- Organize content from foundational to advanced concepts (scaffolded learning progression)
- Ensure logical flow where each module builds on previous ones
- Focus on what the INSTRUCTOR needs to know to teach this material well
- Use web search to find authoritative, current resources for instructor preparation
- Be thorough about which tools and features the instructor must understand deeply
- Include common student questions and how to address them

The extended outline MUST be written in markdown format with the following structure:
"""