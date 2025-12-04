
Course Idea:
	* Idea 1: Spec-to-Ship with AI Pair Programming (VS Code + Copilot + ChatGPT)
		- What it is: Build a small, production-ready Python library from a plain-English spec using Copilot/ChatGPT; include tests, docs, typing, and CI.
		- Strengths: End-to-end workflow mirroring real engineering; strong process (Spec-Plan-Implement-Test).
		- Critique highlights: Too ambitious for 1 day; high setup friction (Copilot, CI, permissions); cognitive load from juggling multiple deliverables; needs prebuilt templates and tighter scope.

- Idea 2:
	* Idea 2: AI-Accelerated Data Analysis and Simulation (Jupyter + Copilot/Tabnine + ChatGPT)
		- What it is: Use AI to speed up notebooks, vectorize hotspots, fix bottlenecks, and generate reports; optional notebook-to-package conversion.
		- Strengths: Highly relevant to STEM analysts; practical optimization and profiling focus.
		- Critique highlights: Over-broad topic list; risky speedup promises; toolchain confusion (multiple assistants); should focus on profiling + AI-suggested refactors with curated examples and a single primary assistant.

- Idea 3:
	* Idea 3: AI-Assisted Refactoring and Porting of Legacy STEM Code
		- What it is: Explain legacy code with AI, generate golden-master tests, refactor safely, optionally port a small component with parity checks.
		- Strengths: Addresses a ubiquitous pain point; solid guardrails (golden-master, interface-first prompts).
		- Critique highlights: Full porting unrealistic in 1 day; licensing/validation pitfalls; should center on a small self-contained function with curated snippets and emphasize AI for explanation/test generation.

- Idea 4:
	* Idea 4: Ship a Scientific API in a Day with AI (FastAPI + Copilot + ChatGPT)
		- What it is: Wrap a scientific model as a REST API with validation, tests, and container packaging; AI scaffolds endpoints, tests, and docs.
		- Strengths: Concrete deliverable (containerized API); clear contract-first approach; strong relevance for model serving.
		- Critique highlights: Requires prework (Docker, web basics); CI and load testing likely excessive; potential infra blockers; narrow to 1 endpoint and provide templates/fallbacks.

- Idea 5:
	* Idea 5: AI-Driven Test-First Development (Property-Based + Mocks)
		- What it is: Practice AI-accelerated TDD with property-based tests, then implement robust algorithms; measure coverage/mutation.
		- Strengths: Teaches powerful testing techniques for numerical/stochastic code; disciplined pipeline.
		- Critique highlights: Heavy for 1 day; mutation testing may overwhelm; needs 1–2 focused katas, simplified toolchain, and property template library.

- Idea 6:
	* Idea 6: Improved Idea — AI-Assisted Scientific Microservice in a Day (FastAPI + Copilot Chat + ChatGPT)
		- Improvements made: Narrowed to a single endpoint (+/health), contract-first prompting, negative tests, and optional read-only CI demo; preconfigured starter repo with Poetry/Makefile; single primary AI (Copilot Chat) plus ChatGPT for contract drafting.
		- Sample scenario: POST /simulate/sir with strict Pydantic validation; tests (pytest+HTTPX); Dockerfile provided; smoke tests via curl.
		- Feasibility tweaks from critique: Time-boxed labs; removed heavy CI; added AI-unavailable fallbacks; acceptance checks simplified to practical goals.
		- Remaining risks and mitigations: AI access variability (provide offline scaffolds); infra blockers (prework checklist); cognitive load (minute-by-minute schedule).

- Idea 7:
	* Idea 7: Improved Idea — AI-Assisted Legacy Code Deep-Dive: Explain → Test → Refactor (Optional Port)
		- Improvements made: Curated 150-line legacy snippet; golden-master fixtures; prompt templates (hallucination guardrails: “cite the line before changing logic”); realistic tolerances (e.g., atol=1e-9); preconfigured environment (devcontainer/requirements).
		- Labs: AI-generated summaries/docstrings; characterization tests with seeded RNG; safe refactors under test; optional minimal port with parity checks and PSD invariants.
		- Feasibility tweaks from critique: Porting optional; numeric tolerances realistic; instructor check-ins; dedicated segment on mitigating AI hallucinations.
		- Measurable outcomes: 75–85% line coverage; all golden-master tests pass; mypy/ruff clean; 20–40% cyclomatic complexity reduction; parity within atol=1e-9.

- Idea 8:
	* Idea 8: Final Selection Rationale — Why the Legacy Deep-Dive Won
		- Best alignment: Directly targets common STEM pain (understanding/refactoring legacy code) without web/Docker overhead; strongest fit for mixed-skill participants.
		- Lower friction: Fewer infrastructure dependencies and fewer corporate IT blockers than API/Docker; primarily code–test–prompt workflows inside VS Code.
		- Strong guardrails: Golden-master tests, typed refactors, and explicit hallucination guardrails keep AI assistance safe and verifiable.
		- Quantifiable benefits: Participants deliver docstrings for 100% functions, 75–85% coverage, 20–40% complexity reduction, parity within atol=1e-9, and 40–60% faster time-to-understand (via a short comprehension quiz); AI assist acceptance rate ≥50%.
		- Day-one success likelihood: Curated snippets, prebuilt fixtures, and optional porting ensure most participants finish with a high-quality, tested module.

- Idea 9:
	* Idea 9: Reflections and Themes Influencing the Final Choice
		- Scope discipline wins: Narrow, end-to-end deliverables (single endpoint, single legacy snippet) proved most feasible for a 1-day arc.
		- Toolchain simplicity: Choosing one primary assistant (Copilot Chat) and preconfigured environments reduces cognitive and setup load.
		- Guardrails are essential: Contract-first specs, golden-master tests, and hallucination guardrails consistently improved safety and outcomes.
		- Measurable outcomes matter: Coverage, complexity reduction, performance/parity tolerances, and comprehension metrics made impact tangible and guided selection.
		- STEM specificity: Numerical correctness, validation, and reproducibility needs shaped the emphasis on tests, tolerances, and invariants over broader devops topics.

        