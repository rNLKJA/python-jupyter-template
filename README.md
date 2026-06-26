<div align="center">

# Python Jupyter Template

A clean, opinionated starting point for Python data-science projects — structured folders, logging, tests, and CI ready to go.

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/python_test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## Overview

This repository is a reusable template for data-science work in Python and Jupyter. Instead of starting every project from an empty folder, clone this and you already have a sensible layout, a configured logger, a test harness, and a CI workflow — so you can spend your time on the analysis, not the scaffolding.

It is deliberately small. The point is structure and good defaults, not a heavy framework.

## Highlights

- **Structured layout** — separate homes for source code (`src/`), notebooks (`notebooks/`), data (`data/`), scripts (`scripts/`), tests (`tests/`), and docs (`docs/`).
- **Logging out of the box** — `src/logger.py` writes to both the console and `logs/app.log`; see [`docs/logging_usage.md`](docs/logging_usage.md) for how to use it.
- **Tests + CI** — a sample `unittest` suite under `tests/`, wired to a GitHub Actions workflow that runs across Python 3.9–3.11.
- **Environment files** — both `pip` (`envs/requirements.txt`) and Conda (`envs/environment.yml`) starting points.

## Tech Stack

| Area         | Tools                                     |
| ------------ | ----------------------------------------- |
| Language     | Python 3.9+                               |
| Notebooks    | JupyterLab / Jupyter Notebook             |
| Data science | NumPy, pandas, scikit-learn, Matplotlib   |
| Testing      | `unittest` (swap in `pytest` if you like) |
| CI           | GitHub Actions                            |
| Packaging    | `setuptools` (`setup.py`)                 |

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/rNLKJA/python-jupyter-template.git
   cd python-jupyter-template
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

3. **Install dependencies** (pip or Conda)

   ```bash
   pip install -r envs/requirements.txt
   # or
   conda env create -f envs/environment.yml
   ```

4. **Explore the notebooks**

   ```bash
   jupyter lab        # then open the notebooks/ directory
   ```

5. **Run the tests**

   ```bash
   python -m unittest discover -s tests
   ```

## Repo Structure

```
python-jupyter-template/
├── src/            # Project source code (incl. logger.py)
├── notebooks/      # Jupyter notebooks (exploratory/ + final/)
├── scripts/        # Standalone task scripts
├── tests/          # Automated tests
├── docs/           # Documentation
├── data/           # raw/ (immutable) + processed/
├── logs/           # Application logs
├── envs/           # requirements.txt + environment.yml
├── .github/        # CI workflows + issue templates
├── setup.py        # Packaging
└── LICENSE         # MIT
```

## Using This Template

Clone it, then make it yours:

- Update the project name, author, and URL in [`setup.py`](setup.py).
- Fill `envs/requirements.txt` (and `envs/environment.yml`) with your real dependencies.
- Replace the sample module, script, and test with your own.

## License

Released under the [MIT License](LICENSE).
