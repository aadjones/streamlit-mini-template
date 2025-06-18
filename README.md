# Streamlit Mini Template

Cookiecutter template for a lightweight Streamlit dashboard with optional tests, Black + isort pre-commit hooks, and a Makefile that bootstraps everything in one command.

---

## Quick use

Make sure Cookiecutter is installed

```bash
pipx install cookiecutter           
```
Generate a project (interactive prompts)
```bash
cookiecutter gh:aadjones/streamlit-mini-template
```

Bootstrap and run
```bash
cd <project_slug>
make setup        # env + deps + git init + pre-commit
make dev          # open the Streamlit app
```

## One-liners
| Task                     | Command                                                              |
| ------------------------ | -------------------------------------------------------------------- |
| Non-interactive defaults | `cookiecutter gh:aadjones/streamlit-mini-template --no-input`        |
| Use a specific tag       | `cookiecutter gh:aadjones/streamlit-mini-template --checkout v0.1.0` |
