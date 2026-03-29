# Anvil Dataset Benchmark
This repository contains a collection of 10  tasks, fully structured and validated using the **Anvil CLI**. 

## Project Milestones
- **Status:** Dataset Validated Locally.
- **Task Count:** 10 unique DSA instances (Arrays, Linked Lists, Trees, etc.).
- **Validation:** Successfully passed `anvil validate-dataset`.
- **Infrastructure:** Dockerfiles and configuration scripts are ready for containerization.

## Repository Structure
- `my-dsa-dataset/`: The core dataset containing task configurations.
- `task-1/` to `task-10/`: Individual task environments, including:
  - `solution.py`: The reference implementation.
  - `task_tests.py`: Pytest-based validation logic.
  - `problem.md`: Detailed task descriptions.
- `setup-anvil.bat`: Automation script for environment initialization.

## Technical Highlights
- **Environment:** Isolated Python 3.12 virtual environment.
- **Testing:** Comprehensive test suites for each task using `pytest`.
- **Tooling:** Leveraged the **Anvil Tooling** for dataset lifecycle management.

## How to Validate (Local)
1. Ensure the Python `venv` is active.
2. Ensure Docker Desktop is running.
3. Run the validation command:
   ```bash
   anvil validate-dataset --dataset my-dsa-dataset
