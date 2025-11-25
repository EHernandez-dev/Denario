⏺ High-Level Overview of Denario

  Denario is an autonomous scientific research assistant built as a multiagent AI system. Its core purpose is to transform raw data descriptions into complete, publication-ready scientific papers with minimal human intervention.

  What It Does

  The system automates the entire scientific research workflow:

  1. Idea Generation - Takes a dataset/tools description and generates novel research hypotheses
  2. Novelty Checking - Searches academic literature (Semantic Scholar) to validate the idea hasn't been done before
  3. Methodology Design - Creates a detailed experimental approach
  4. Experiment Execution - Runs computational experiments, generates code, and produces visualizations
  5. Paper Writing - Generates a complete LaTeX-formatted scientific paper with proper citations

  Architecture

  The system uses a dual-backend architecture:

  | Backend   | Purpose                                 | Speed    |
  |-----------|-----------------------------------------|----------|
  | LangGraph | Fast prototyping and ideation           | Quick    |
  | cmbagent  | Detailed, publication-quality workflows | Thorough |

  Key Components

  - denario.py - Central orchestrator coordinating the entire pipeline
  - research.py - Pydantic data model storing research state (idea, methodology, results, etc.)
  - langgraph_agents/ - Fast workflow with specialized nodes (idea_maker, idea_hater, novelty_decider, etc.)
  - paper_agents/ - Detailed multi-agent workflows using planner/critic patterns
  - prompts/ - LLM prompt templates for various tasks

  Multi-LLM Support

  Supports multiple providers (OpenAI, Anthropic, Google) with configurable models per task - allowing cost optimization by using cheaper models for simple tasks and powerful models for complex ones.

  Output

  Generates LaTeX papers formatted for specific journals:
  - AAS (Astronomical Society)
  - APS (American Physical Society)
  - ICML, NeurIPS (Machine Learning conferences)
  - And more...