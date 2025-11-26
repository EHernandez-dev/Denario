# CMBAgent Bug Report: Gemini reasoning_effort parameter

## Repository
Run this to find the repo URL:
```bash
pip show cmbagent | grep Home
```

Or check: https://github.com/search?q=cmbagent

## Issue Title
`ValidationError: reasoning_effort parameter incorrectly passed to Google/Gemini models`

## Issue Body

### Bug Description
When using Gemini models (e.g., `gemini-2.5-flash`) with `planning_and_control_context_carryover()`,
cmbagent passes `reasoning_effort='medium'` to the LLM config. This parameter is only valid for
OpenAI reasoning models (like o3-mini), not for Google/Gemini models.

### Error Message
```
ValidationError: 1 validation error for _LLMConfig
config_list.0.google.reasoning_effort
  Extra inputs are not permitted [type=extra_forbidden, input_value='medium', input_type=str]
    For further information visit https://errors.pydantic.dev/2.12/v/extra_forbidden
```

### Steps to Reproduce
1. Install cmbagent and denario
2. Use `planning_and_control_context_carryover()` with Gemini models
3. Set model parameters to `gemini-2.5-flash` (or any Gemini model)
4. Error occurs during CMBAgent initialization at `base_agent.py:211`

### Code to Reproduce
```python
import cmbagent

results = cmbagent.planning_and_control_context_carryover(
    "Test task",
    planner_model="gemini-2.5-flash",
    plan_reviewer_model="gemini-2.5-flash",
    default_llm_model="gemini-2.5-flash",
    default_formatter_model="gemini-2.5-flash",
)
```

### Expected Behavior
The `reasoning_effort` parameter should only be added to the config for OpenAI reasoning
models (o3-mini, o1, etc.), not for Google/Gemini models.

### Suggested Fix
In the `get_model_config()` function (or wherever the config is built), add a check to only
include `reasoning_effort` for OpenAI reasoning models:

```python
if "o3" in model_name or "o1" in model_name:
    config["reasoning_effort"] = "medium"
```

### Environment
Run these commands to get version info:
```bash
pip show cmbagent
pip show autogen
python --version
```

- OS: macOS
- Python: 3.12
