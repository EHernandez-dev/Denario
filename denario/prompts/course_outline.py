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
