course_outline_planner_prompt = r"""
{course_idea}

Instruction for planning:

Given this course idea, including the topic, target audience, and duration, we want to design a comprehensive course outline.
The goal of the task is to write a plan that will be used to generate a detailed, structured course outline with modules, learning goals, and takeaways.

- Start by requesting the *researcher* to analyze the course idea and identify the core competencies and skills participants should develop.
- Ask the *researcher* to determine what participants need to know before the course (prerequisites).
- Request the *researcher* to propose 4-8 main modules that logically build upon each other, progressing from foundational to advanced concepts.
- For each module, ask the *researcher* to write: a description of what the session covers, key takeaways (what participants leave with), and specific learning goals written as "Participants [action verb]...".
- Ask the *researcher* to include exercise duration estimates for hands-on modules.
- This can be done in multiple steps.
- The focus should be strictly on the course structure, learning goals, and takeaways. **Do not include** actual lesson slides, scripts, or full exercise materials.
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
- Each module must have: a Description, Takeaways, and Learning Goals
- Write learning goals as "Participants [action verb] [specific measurable outcome]."
- Use action verbs: identify, describe, apply, compare, evaluate, create, demonstrate, formulate, distinguish, explain, navigate, select, verify, recognize
- Ensure logical flow where each module builds on previous ones
- Include exercise duration estimates where appropriate
- **Do not include** actual lesson slides, detailed scripts, or full exercise materials

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
[Continue for all takeaways - create 3-5 takeaways depending on the length of the module]
### Learning Goals:
- Participants [action verb] [specific measurable outcome].
- Participants [action verb] [specific measurable outcome].
- Participants [action verb] [specific measurable outcome].
[Continue for all learning goals - create 3-8 learning goals depending on the length of the module]
### Exercise Description:
Duration: [X] minutes, Debrief: [Y] minutes

## 2. [Module Title]
### Description:
[...]
### Takeaways:
[...]
### Learning Goals:
[...]

[Continue for all modules - create 6-12 modules depending on course duration]

Each module should have 3-5 learning goals. The full course outline should be roughly 1000-1500 words.
"""
