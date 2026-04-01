---
name: python-project-setup
description: >
  Set up a new Python project with a complete, opinionated scaffolding — directory structure,
  dependency management (uv), linting (ruff), pre-commit hooks, CI (GitHub Actions), .env handling,
  and project-type-specific boilerplate. Use this skill whenever the user wants to start a new Python
  project, scaffold a Python codebase, initialize a repo for Python work, or asks things like
  "set up a new project", "create a Python app", "bootstrap a FastAPI service", "init a data pipeline",
  "scaffold an ML project", or any variation of starting fresh with Python code. Also trigger when the
  user asks to add missing scaffolding to an existing project (e.g., "add CI to my project",
  "set up linting", "add pre-commit hooks"). Even if they don't say "Python" explicitly, trigger if the
  context clearly implies Python (e.g., mentions FastAPI, pandas, dbt, airflow, sklearn).
---

# Python Project Setup

Scaffold a production-ready Python project with sensible defaults and consistent structure.
This skill bundles a deterministic scaffold script — use it instead of generating files manually.

## Golden rule: stop when confused

If any of the following are unclear from the user's prompt, **stop and ask before running anything**:

- **Project name** — don't invent one. If the user said "set up a python project" with no name, ask.
- **Project type** — if the prompt could be webapp or de or ds, don't pick one. Ask.
- **Dependencies** — if the user mentions a technology you're unsure how to map to a pip package name (e.g., "Spark" → `pyspark`? `spark`? `apache-spark`?), ask.
- **Conflicting signals** — e.g., "FastAPI data pipeline" could be webapp or de. Ask.
- **Destination** — if it's unclear where to create the project (current dir? specific path?), ask.

Never guess. A wrong scaffold is worse than a 10-second clarification. Ask one clear question that covers all the ambiguities at once, then proceed.

## Workflow

### 1. Parse the user's request

Extract these parameters from the user's prompt:

| Parameter | How to extract | Required |
|-----------|---------------|----------|
| `--name` | Project name from the prompt (e.g., "de-intro", "my-api"). Slugify if needed. | Yes |
| `--type` | Infer from context. One of: `webapp`, `ds`, `de`, `lib` (see table below) | Yes |
| `--deps` | Comma-separated list of technologies mentioned (e.g., "polars,dbt-core,apache-airflow") | No |

**Type inference guide:**

| User says... | Type |
|---|---|
| FastAPI, Flask, API, web app, backend, server | `webapp` |
| ML, machine learning, model, training, experiment, notebook, data science | `ds` |
| pipeline, ETL, ELT, data engineering, dbt, airflow, spark, ingestion | `de` |
| library, package, pip install, publish, PyPI | `lib` |

If ambiguous, ask the user. Don't guess.

### 2. Run the scaffold script

```bash
python <skill-path>/scripts/scaffold.py \
  --name <project-name> \
  --type <project-type> \
  --deps <comma-separated-deps>
```

The script creates the full directory tree deterministically — all files, configs, and boilerplate.
Do not create project files manually. Always use the script.

**Example invocations:**

```bash
# "create for me project de-intro with polars, dbt, airflow, spark tech stack"
python scripts/scaffold.py --name de-intro --type de --deps polars,dbt-core,apache-airflow,pyspark

# "bootstrap a FastAPI service called user-api"
python scripts/scaffold.py --name user-api --type webapp

# "set up an ML project for churn prediction"
python scripts/scaffold.py --name churn-prediction --type ds

# "create a python library called py-utils"
python scripts/scaffold.py --name py-utils --type lib
```

### 3. Initialize the environment

After the script completes, run:

```bash
cd <project-name>
uv sync --dev
uv run pre-commit install
```

This installs dependencies and activates pre-commit hooks. The project is ready to use.

### 4. Report to the user

Show the generated directory tree (the script prints it) and the next steps.
If the user specified deps, confirm which were added.

## What the script generates

### All project types get:

- `pyproject.toml` — project metadata, dependencies, ruff config (line-length=100, py312)
- `.pre-commit-config.yaml` — ruff + standard hooks
- `.github/workflows/ci.yml` — GitHub Actions with uv, ruff check, ruff format
- `.gitignore` — Python-specific (extended for ds/de with data patterns)
- `.env.example` — placeholder env vars relevant to project type
- `README.md` — setup and run instructions using uv

### Type-specific structure:

**webapp** → `app/` with main.py (FastAPI), config.py (pydantic-settings), routers/, models/, schemas/

**ds** → `notebooks/`, `src/` (data.py, features.py, train.py), `data/` (gitignored)

**de** → `pipelines/`, `src/` (extract.py, transform.py, load.py), `configs/`

**lib** → `src/package_name/` with __init__.py and py.typed marker, hatchling build system

## Adapting to existing projects

When the user asks to add scaffolding to an existing project (not create a new one), do NOT run the scaffold script. Instead:

1. Check what already exists in the project directory
2. Offer to add only the missing pieces (e.g., "You have a pyproject.toml but no ruff config — want me to add it?")
3. Add config sections individually — don't overwrite existing files

This is the one case where you generate files manually instead of using the script.

## Optional extras (add only if the user asks)

These are not handled by the script — add them manually when requested:

- **pytest scaffolding**: `tests/` directory, conftest.py, pytest config in pyproject.toml, pytest added to CI
- **Dockerfile**: Multi-stage build with uv for fast installs
- **Makefile**: Common commands (lint, test, run, build)
- **mypy config**: `[tool.mypy]` section in pyproject.toml
- **VS Code settings**: `.vscode/settings.json` with ruff extension config
