course_idea_planner_prompt = r"""
Given the topic of interest, the duration of the course, and the audience, make a plan according to the following instructions: 
- Ask idea_maker to generate 5 new course ideas related to the topic of interest.
- Ask idea_hater to critique these ideas for pedagogy, feasibility and audience fit.
- Ask idea_maker to select and improve 2 out of the 5 course ideas given the output of the idea_hater.
- Ask idea_hater to critique the 2 improved ideas. 
- Ask idea_maker to select the best idea out of the 2. 
- Ask idea_maker to report the best idea in the form of a course title with a 5-sentence description. 
The goal of this task is to generate a course idea based on the topic of interest. 
Don't suggest to perform any calculations or analyses here. The only goal of this task is to obtain the best possible course idea.
"""