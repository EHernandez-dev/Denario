# AI-Assisted Legacy Code Deep-Dive: Explain → Test → Refactor

### Overview:
This one-day, hands-on course is designed for STEM professionals who routinely encounter legacy scientific code and want to leverage AI tools for rapid understanding, safe testing, and robust refactoring. Participants will use Copilot Chat and ChatGPT within VS Code to explain, test, and modernize real-world legacy code, with a focus on numerical correctness, maintainability, and reproducibility. The course emphasizes practical workflows, guardrails, and measurable outcomes, making it accessible to mixed-skill teams.

---

## 1. Introduction & Motivation: The Legacy Code Challenge

### Description:
Introduces the unique challenges of legacy code in STEM, such as lack of documentation, missing or inadequate tests, and the risks of refactoring numerically sensitive algorithms. Frames the course objectives and sets expectations for AI-assisted workflows.

### Takeaways:
- Awareness of common legacy code pitfalls in STEM
- Understanding the value and limitations of AI assistance
- Clarity on course structure and deliverables

### Learning Goals:
- Participants articulate the main risks and pain points of legacy code in STEM.
- Participants identify scenarios where AI can accelerate legacy code workflows.
- Participants outline the end-to-end workflow: explain → test → refactor.

### Exercise Description:
Duration: 10 minutes, Debrief: 5 minutes

---

## 2. Environment Setup & Tooling Primer

### Description:
Participants configure a prebuilt development environment (VS Code, devcontainer, Poetry, requirements) and receive a guided tour of Copilot Chat, ChatGPT, pytest, mypy, and ruff. The session ensures all tools are functional and introduces best practices for AI-assisted coding.

### Takeaways:
- Ready-to-use, reproducible development environment
- Familiarity with Copilot Chat and ChatGPT integration in VS Code
- Understanding of Python testing and linting tools

### Learning Goals:
- Participants launch and navigate the preconfigured devcontainer.
- Participants use Copilot Chat and ChatGPT for code queries.
- Participants run pytest, mypy, and ruff on provided code.

### Exercise Description:
Duration: 15 minutes, Debrief: 5 minutes

---

## 3. Rapid Code Comprehension with AI

### Description:
Focuses on using AI to generate summaries, docstrings, and high-level explanations for unfamiliar legacy code. Emphasizes prompt engineering, hallucination guardrails, and verifying AI outputs.

### Takeaways:
- Techniques for extracting accurate explanations from AI
- Prompt templates for safe code summarization
- Strategies for validating AI-generated documentation

### Learning Goals:
- Participants generate function-level summaries using Copilot Chat.
- Participants apply prompt templates to minimize hallucinations.
- Participants cross-check AI explanations against code logic.

### Exercise Description:
Duration: 20 minutes, Debrief: 5 minutes

---

## 4. Golden-Master Test Generation

### Description:
Participants learn to create golden-master (characterization) tests using AI, capturing the current behavior of legacy code with seeded random number generators and realistic tolerances. The session covers test scaffolding, fixture management, and the importance of reproducibility.

### Takeaways:
- Ability to generate robust golden-master tests with AI
- Understanding of test fixtures and seeded RNGs for reproducibility
- Awareness of numerical tolerances and invariants

### Learning Goals:
- Participants scaffold golden-master tests using Copilot Chat.
- Participants implement seeded RNGs and fixture data.
- Participants set and justify numerical tolerances (e.g., atol=1e-9).

### Exercise Description:
Duration: 25 minutes, Debrief: 5 minutes

---

## 5. Coverage, Linting, and Static Analysis

### Description:
Introduces code coverage measurement (pytest-cov), static type checking (mypy), and linting (ruff). Participants learn to interpret results, identify untested or problematic code, and use AI to suggest targeted improvements.

### Takeaways:
- Skills in measuring and improving test coverage
- Proficiency with mypy and ruff for code quality
- AI-assisted identification of coverage and style gaps

### Learning Goals:
- Participants run and interpret pytest-cov, mypy, and ruff reports.
- Participants use Copilot Chat to suggest coverage and style fixes.
- Participants prioritize improvements based on analysis results.

### Exercise Description:
Duration: 15 minutes, Debrief: 5 minutes

---

## 6. Safe Refactoring with AI Guidance

### Description:
Participants apply AI-assisted refactoring to reduce code complexity, improve readability, and modernize interfaces—while ensuring all golden-master tests pass. The session covers prompt templates for safe changes, interface-first refactoring, and complexity metrics.

### Takeaways:
- Methods for safe, incremental refactoring with AI
- Use of cyclomatic complexity metrics to guide improvements
- Guardrails to prevent logic-altering hallucinations

### Learning Goals:
- Participants refactor functions using Copilot Chat with explicit prompts.
- Participants measure and reduce cyclomatic complexity.
- Participants validate refactors by running golden-master tests.

### Exercise Description:
Duration: 25 minutes, Debrief: 5 minutes

---

## 7. Parity Checks and Numerical Validation

### Description:
Addresses the critical need for numerical parity and correctness in STEM code. Participants use AI to generate parity checks, compare outputs before and after refactoring, and set realistic tolerances for floating-point results.

### Takeaways:
- Techniques for automated parity checking
- Understanding of numerical invariants and tolerances
- Confidence in refactored code correctness

### Learning Goals:
- Participants implement parity checks using pytest and AI-generated assertions.
- Participants set and document numerical tolerances.
- Participants interpret and resolve parity discrepancies.

### Exercise Description:
Duration: 15 minutes, Debrief: 5 minutes

---

## 8. Optional: Minimal Porting and Interface Modernization

### Description:
For advanced participants, this session explores porting a small, self-contained function to a new interface or language (e.g., NumPy, Cython), using AI for translation and parity validation. The focus is on safe, incremental migration.

### Takeaways:
- Experience with AI-assisted code porting
- Strategies for interface modernization
- Awareness of licensing and validation pitfalls

### Learning Goals:
- Participants port a function using Copilot Chat and validate with golden-master tests.
- Participants document interface changes and migration steps.
- Participants identify and mitigate common porting risks.

### Exercise Description:
Duration: 20 minutes, Debrief: 5 minutes

---

## 9. Best Practices, Pitfalls, and Hallucination Mitigation

### Description:
Synthesizes best practices for AI-assisted legacy code work, including prompt engineering, hallucination guardrails, and reproducibility. Participants review common pitfalls and how to avoid them.

### Takeaways:
- Checklist of best practices for AI-assisted workflows
- Strategies for prompt refinement and output validation
- Awareness of reproducibility and documentation standards

### Learning Goals:
- Participants apply a checklist to review their workflow.
- Participants identify and correct AI-induced errors.
- Participants document their process for future reference.

### Exercise Description:
Duration: 10 minutes, Debrief: 5 minutes

---

## 10. Wrap-Up, Outcomes, and Next Steps

### Description:
The final session recaps key learning outcomes, reviews measurable achievements (coverage, complexity reduction, parity), and provides guidance for further self-study and organizational adoption. Participants share reflections and plan next steps.

### Takeaways:
- Clear understanding of personal and team progress
- Resources for continued learning and adoption
- Action plan for applying skills to real-world codebases

### Learning Goals:
- Participants summarize their achievements using course metrics.
- Participants identify areas for further improvement.
- Participants access curated resources for ongoing development.

### Exercise Description:
Duration: 10 minutes, Debrief: 10 minutes

---

## Further Resources for Course Organizers

- [VS Code Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [Copilot Chat for VS Code](https://docs.github.com/en/copilot/getting-started-with-github-copilot/about-github-copilot-chat)
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [mypy Type Checker](https://mypy-lang.org/)
- [ruff Linter](https://docs.astral.sh/ruff/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Cyclomatic Complexity in Python](https://radon.readthedocs.io/en/latest/)

## Further Resources for Participants

- [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [Type Checking With mypy](https://realpython.com/python-type-checking/)
- [AI-Assisted Code Refactoring: Best Practices](https://github.com/features/copilot)
- [Numerical Issues in Scientific Computing](https://numpy.org/doc/stable/user/misc.html#numerical-issues)
- [Reproducible Research in Python](https://reproducible-science-curriculum.github.io/)

---