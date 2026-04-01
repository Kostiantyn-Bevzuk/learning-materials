#!/usr/bin/env python3
"""
Deterministic Python project scaffolder.

Usage:
    python scaffold.py --name my-project --type webapp --deps fastapi,uvicorn
    python scaffold.py --name ml-experiment --type ds
    python scaffold.py --name etl-pipeline --type de --deps polars,dbt-core,airflow
    python scaffold.py --name my-lib --type lib
"""

import argparse
import json
import os
import sys
from pathlib import Path
from textwrap import dedent

# ──────────────────────────────────────────────
# Project type definitions
# ──────────────────────────────────────────────

PROJECT_TYPES = {
    "webapp": {
        "label": "Web Application (FastAPI)",
        "default_deps": ["fastapi", "uvicorn[standard]", "pydantic-settings"],
    },
    "ds": {
        "label": "Data Science / ML",
        "default_deps": ["jupyter", "pandas", "scikit-learn", "matplotlib"],
    },
    "de": {
        "label": "Data Engineering",
        "default_deps": [],
    },
    "lib": {
        "label": "Library / Package",
        "default_deps": [],
    },
}

DEV_DEPS = [
    "ruff>=0.8",
    "pre-commit>=4.0",
    "python-dotenv>=1.0",
]

# ──────────────────────────────────────────────
# File generators
# ──────────────────────────────────────────────


def generate_pyproject(name: str, project_type: str, deps: list[str]) -> str:
    all_deps = PROJECT_TYPES[project_type]["default_deps"] + deps
    deps_lines = "\n".join(f'    "{d}",' for d in sorted(set(all_deps)))
    dev_deps_lines = "\n".join(f'    "{d}",' for d in DEV_DEPS)

    lines = [
        "[project]",
        f'name = "{name}"',
        'version = "0.1.0"',
        'description = ""',
        'requires-python = ">=3.12"',
        "dependencies = [",
        deps_lines,
        "]",
        "",
        "[project.optional-dependencies]",
        "dev = [",
        dev_deps_lines,
        "]",
        "",
        "[tool.ruff]",
        'target-version = "py312"',
        "line-length = 100",
        "",
        "[tool.ruff.lint]",
        "select = [",
        '    "E",    # pycodestyle errors',
        '    "W",    # pycodestyle warnings',
        '    "F",    # pyflakes',
        '    "I",    # isort',
        '    "UP",   # pyupgrade',
        '    "B",    # flake8-bugbear',
        '    "SIM",  # flake8-simplify',
        "]",
    ]

    if project_type == "lib":
        lines += [
            "",
            "[build-system]",
            'requires = ["hatchling"]',
            'build-backend = "hatchling.build"',
        ]

    return "\n".join(lines) + "\n"


def generate_precommit_config() -> str:
    return dedent("""\
        repos:
          - repo: https://github.com/astral-sh/ruff-pre-commit
            rev: v0.8.6
            hooks:
              - id: ruff
                args: [--fix]
              - id: ruff-format
          - repo: https://github.com/pre-commit/pre-commit-hooks
            rev: v5.0.0
            hooks:
              - id: trailing-whitespace
              - id: end-of-file-fixer
              - id: check-yaml
              - id: check-added-large-files
    """)


def generate_ci() -> str:
    return dedent("""\
        name: CI

        on:
          push:
            branches: [main]
          pull_request:

        jobs:
          lint-and-test:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v4
              - uses: astral-sh/setup-uv@v5
              - run: uv python install 3.12
              - run: uv sync --dev
              - run: uv run ruff check .
              - run: uv run ruff format --check .
    """)


def generate_gitignore(project_type: str) -> str:
    base = dedent("""\
        __pycache__/
        *.py[cod]
        *.egg-info/
        dist/
        build/
        .eggs/
        .venv/
        .env
        *.egg
        .pytest_cache/
        .ruff_cache/
        .mypy_cache/
    """)

    if project_type in ("ds", "de"):
        base += dedent("""\
            data/
            *.csv
            *.parquet
            *.pkl
            models/
            wandb/
            mlruns/
        """)

    return base


def generate_env_example(project_type: str) -> str:
    lines = ["# Copy this file to .env and fill in the values"]

    if project_type == "webapp":
        lines.append("# DATABASE_URL=postgresql://user:password@localhost:5432/dbname")
        lines.append("# SECRET_KEY=change-me")
        lines.append("# DEBUG=true")
    elif project_type == "ds":
        lines.append("# DATA_DIR=./data")
        lines.append("# WANDB_API_KEY=your-key-here")
    elif project_type == "de":
        lines.append("# DATABASE_URL=postgresql://user:password@localhost:5432/dbname")
        lines.append("# WAREHOUSE_URL=your-warehouse-url")
        lines.append("# API_KEY=your-key-here")
    else:
        lines.append("# API_KEY=your-key-here")

    return "\n".join(lines) + "\n"


def generate_readme(name: str, project_type: str) -> str:
    label = PROJECT_TYPES[project_type]["label"]

    run_section = {
        "webapp": "uv run uvicorn app.main:app --reload",
        "ds": "uv run jupyter lab",
        "de": "uv run python -m pipelines.example_pipeline",
        "lib": "uv run python -c \"import {pkg}\"".format(pkg=name.replace("-", "_")),
    }

    return dedent(f"""\
        # {name}

        {label} project.

        ## Setup

        ```bash
        uv sync --dev
        uv run pre-commit install
        cp .env.example .env
        ```

        ## Run

        ```bash
        {run_section[project_type]}
        ```

        ## Lint

        ```bash
        uv run ruff check .
        uv run ruff format .
        ```
    """)


# ──────────────────────────────────────────────
# Type-specific directory structures
# ──────────────────────────────────────────────


def create_webapp_structure(root: Path, name: str) -> None:
    app = root / "app"
    for subdir in ["routers", "models", "schemas"]:
        (app / subdir).mkdir(parents=True, exist_ok=True)
        (app / subdir / "__init__.py").touch()

    (app / "__init__.py").touch()

    (app / "main.py").write_text(dedent(f"""\
        from fastapi import FastAPI

        app = FastAPI(title="{name}")


        @app.get("/health")
        async def health():
            return {{"status": "ok"}}
    """))

    (app / "config.py").write_text(dedent("""\
        from pydantic_settings import BaseSettings


        class Settings(BaseSettings):
            debug: bool = False

            model_config = {"env_file": ".env"}


        settings = Settings()
    """))


def create_ds_structure(root: Path) -> None:
    (root / "notebooks").mkdir(exist_ok=True)
    (root / "data").mkdir(exist_ok=True)
    (root / "data" / ".gitkeep").touch()

    src = root / "src"
    src.mkdir(exist_ok=True)
    (src / "__init__.py").touch()

    (src / "data.py").write_text(dedent("""\
        \"\"\"Data loading utilities.\"\"\"
    """))

    (src / "features.py").write_text(dedent("""\
        \"\"\"Feature engineering.\"\"\"
    """))

    (src / "train.py").write_text(dedent("""\
        \"\"\"Training entrypoint.\"\"\"
    """))


def create_de_structure(root: Path) -> None:
    pipelines = root / "pipelines"
    pipelines.mkdir(exist_ok=True)
    (pipelines / "__init__.py").touch()

    (pipelines / "example_pipeline.py").write_text(dedent("""\
        \"\"\"Example pipeline — replace with your own.\"\"\"
    """))

    src = root / "src"
    src.mkdir(exist_ok=True)
    (src / "__init__.py").touch()

    (src / "extract.py").write_text(dedent("""\
        \"\"\"Extract stage.\"\"\"
    """))

    (src / "transform.py").write_text(dedent("""\
        \"\"\"Transform stage.\"\"\"
    """))

    (src / "load.py").write_text(dedent("""\
        \"\"\"Load stage.\"\"\"
    """))

    configs = root / "configs"
    configs.mkdir(exist_ok=True)
    (configs / "pipeline_config.yaml").write_text(dedent("""\
        # Pipeline configuration
        pipeline:
          name: example
          schedule: null
    """))


def create_lib_structure(root: Path, name: str) -> None:
    pkg_name = name.replace("-", "_")
    pkg_dir = root / "src" / pkg_name
    pkg_dir.mkdir(parents=True, exist_ok=True)

    (pkg_dir / "__init__.py").write_text(f'"""Top-level package for {name}."""\n')
    (pkg_dir / "py.typed").touch()


# ──────────────────────────────────────────────
# Main scaffold logic
# ──────────────────────────────────────────────

TYPE_STRUCTURE_BUILDERS = {
    "webapp": lambda root, name: create_webapp_structure(root, name),
    "ds": lambda root, name: create_ds_structure(root),
    "de": lambda root, name: create_de_structure(root),
    "lib": lambda root, name: create_lib_structure(root, name),
}


def scaffold(name: str, project_type: str, deps: list[str], output_dir: str | None = None) -> Path:
    """Create the full project structure. Returns the project root path."""

    if output_dir:
        root = Path(output_dir) / name
    else:
        root = Path.cwd() / name

    if root.exists():
        print(f"Error: directory '{root}' already exists.", file=sys.stderr)
        sys.exit(1)

    root.mkdir(parents=True)

    # Core files
    (root / "pyproject.toml").write_text(generate_pyproject(name, project_type, deps))
    (root / ".pre-commit-config.yaml").write_text(generate_precommit_config())
    (root / ".gitignore").write_text(generate_gitignore(project_type))
    (root / ".env.example").write_text(generate_env_example(project_type))
    (root / "README.md").write_text(generate_readme(name, project_type))

    # CI
    ci_dir = root / ".github" / "workflows"
    ci_dir.mkdir(parents=True)
    (ci_dir / "ci.yml").write_text(generate_ci())

    # Type-specific structure
    TYPE_STRUCTURE_BUILDERS[project_type](root, name)

    return root


def print_tree(path: Path, prefix: str = "") -> None:
    """Print a directory tree, skipping hidden dirs except .github."""
    entries = sorted(path.iterdir(), key=lambda e: (not e.is_dir(), e.name))
    visible = [e for e in entries if not e.name.startswith(".") or e.name in (".github", ".env.example", ".gitignore", ".pre-commit-config.yaml")]

    for i, entry in enumerate(visible):
        connector = "└── " if i == len(visible) - 1 else "├── "
        print(f"{prefix}{connector}{entry.name}")
        if entry.is_dir():
            extension = "    " if i == len(visible) - 1 else "│   "
            print_tree(entry, prefix + extension)


def main():
    parser = argparse.ArgumentParser(description="Scaffold a Python project")
    parser.add_argument("--name", required=True, help="Project name (used for directory and package name)")
    parser.add_argument(
        "--type",
        required=True,
        choices=list(PROJECT_TYPES.keys()),
        help="Project type: webapp, ds (data science), de (data engineering), lib (library)",
    )
    parser.add_argument(
        "--deps",
        default="",
        help="Comma-separated extra dependencies (e.g., 'polars,dbt-core,apache-airflow')",
    )
    parser.add_argument("--output-dir", default=None, help="Parent directory for the project (default: cwd)")

    args = parser.parse_args()

    extra_deps = [d.strip() for d in args.deps.split(",") if d.strip()]

    root = scaffold(
        name=args.name,
        project_type=args.type,
        deps=extra_deps,
        output_dir=args.output_dir,
    )

    label = PROJECT_TYPES[args.type]["label"]
    print(f"\n✅ Created {label} project: {root}\n")
    print_tree(root)
    print(f"\nNext steps:")
    print(f"  cd {args.name}")
    print(f"  uv sync --dev")
    print(f"  uv run pre-commit install")
    print(f"  cp .env.example .env")


if __name__ == "__main__":
    main()
