<!-- filename: prerequisites-for-participants.md -->
## Prerequisites for Participants

### Knowledge and Skills

- **Basic Python Programming:**  
  Participants should be comfortable reading and writing Python code, including functions, control flow, and basic data structures (lists, dicts, etc.). Advanced Python knowledge is not required, but familiarity with function definitions and simple modules is essential.

- **Familiarity with Scientific/Numerical Code:**  
  Some exposure to scientific or numerical computing (e.g., using NumPy, SciPy, or similar libraries) is recommended. Participants should understand the importance of numerical correctness and reproducibility in STEM codebases.

- **Introductory Software Engineering Concepts:**  
  Awareness of concepts such as code refactoring, code readability, and maintainability. Prior experience with code reviews or legacy code is helpful but not mandatory.

### Required Software and Environment Setup

- **VS Code (Visual Studio Code):**  
  Participants must have VS Code installed, with the ability to add extensions.

- **Devcontainer Support:**  
  Either Docker Desktop or a compatible container runtime must be installed to support VS Code devcontainers. This ensures a reproducible, preconfigured environment.

- **Prebuilt Course Repository:**  
  Access to a provided GitHub repository containing the legacy code snippet, preconfigured devcontainer, and all necessary dependencies (e.g., Poetry, requirements.txt).

- **Python 3.9+ Environment:**  
  The devcontainer will provide this, but local Python installation is helpful for troubleshooting.

- **Internet Access:**  
  Required for AI tool integration and package installation.

### Tool Familiarity

- **Copilot Chat for VS Code:**  
  Participants should have Copilot Chat enabled in VS Code. No prior experience is required, but they should be able to sign in and access the chat interface.

- **ChatGPT (Web or API):**  
  Access to ChatGPT (free or paid) for contract drafting and prompt experimentation. Familiarity with basic prompt/response workflows is helpful but not required.

- **pytest:**  
  Basic understanding of running tests with pytest. No advanced test writing experience is necessary; the course will scaffold this skill.

- **mypy and ruff:**  
  No prior experience required. Participants will be introduced to static type checking (mypy) and linting (ruff) during the course.

### Prior Experience

- **No Advanced AI or DevOps Experience Required:**  
  The course is designed for mixed-skill STEM professionals. All AI-assisted workflows and DevOps steps (e.g., using devcontainers) will be introduced from first principles.

- **Optional:**  
  Experience with legacy codebases, code reviews, or scientific computing projects will help participants relate course content to their own work, but is not mandatory.

### Summary Table

| Requirement                | Mandatory | Notes                                                      |
|----------------------------|-----------|------------------------------------------------------------|
| Python basics              | Yes       | Functions, modules, control flow                           |
| VS Code                    | Yes       | With extension support                                     |
| Docker/devcontainer        | Yes       | For reproducible environment                               |
| Copilot Chat in VS Code    | Yes       | Account setup required                                     |
| ChatGPT access             | Yes       | Web or API; free tier sufficient                           |
| pytest familiarity         | Helpful   | Will be taught in course                                   |
| mypy/ruff familiarity      | No        | Will be taught in course                                   |
| Scientific code exposure   | Helpful   | Not strictly required                                      |
| Internet access            | Yes       | For AI tools and package installation                      |

### Prework Checklist for Participants

- Install VS Code and Docker Desktop (or compatible runtime)
- Clone the course repository and open in VS Code
- Ensure Copilot Chat extension is installed and signed in
- Verify access to ChatGPT (web or API)
- Test that the devcontainer launches and all dependencies install
- Confirm internet connectivity

### Rationale

These prerequisites ensure that all participants can fully engage with the hands-on, AI-assisted workflows without being blocked by environment or tool setup. The course is designed to be accessible to a broad range of STEM professionals, with all advanced concepts scaffolded and supported by prebuilt templates and guided exercises.