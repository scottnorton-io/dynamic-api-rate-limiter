# Contributing to `api-ratelimiter`

First off, thank you for considering contributing! 🎉  
This project aims to provide a clean, reliable, dynamic API rate limiter with per-API configurations (Notion, Vanta, Fieldguide, and more).

This document outlines how to get set up locally, propose changes, and open pull requests.

---

## 📦 Getting Started

### 1. Fork and clone

1. Fork the repository on GitHub.
2. Clone your fork:
```bash

git clone https://github.com/<your-username>/api-ratelimiter.git
cd api-ratelimiter

```

### 2. Create a virtual environment (recommended)
```bash

python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.venv\Scripts\activate      # Windows

```

### 3. Install dependencies
Install the package in editable mode and basic dev tools:

```bash

pip install -e .
pip install pytest ruff

```

## 🧪 Running Checks Locally

Before opening a pull request, please run:

### Lint (ruff)

```bash

ruff check api_ratelimiter examples

```

### Tests (pytest)

```bash

pytest

```

Currently the project may not have a full test suite; feel free to add tests for any new functionality you introduce.

## 🧩 Project Structure

```text

api_ratelimiter/
    __init__.py
    dynamic_ratelimiter.py   # Adaptive token-bucket rate limiter (AIMD-style)
    api_rate_config.py       # Centralized API configuration table
    clients.py               # Dynamic API client + factory

examples/
    example_notion.py
    example_vanta.py
    example_fieldguide.py

```

- `dynamic_ratelimiter.py`: The core algorithm (rate + cooldown logic).
- `api_rate_config.py`: Registry for known API configurations.
- `clients.py`: HTTP client abstraction that applies the limiter and handles 429s.

If you’re adding a new integration or API:

1. Add a new `ApiRateConfig` entry in `api_rate_config.py`.
2. (Optionally) add an example script under `examples/`.

## ✅ What Makes a Good PR?
- Focused: one logical change per PR (bugfix, new feature, or refactor).
- Typed: use type hints where practical.
- Documented:
  - Public functions/classes should have short docstrings.
  - If you add new configuration fields or behavior, update README.md.

- Tested:
  - Add or update tests when introducing new behavior.
  - Ensure ruff and pytest both pass.

## 🧱 Code Style
We aim for:
- Readable, straightforward Python.
- Type hints for function signatures and complex structures.
- Minimal external dependencies (currently: requests + optional dev tools).

Suggested tools (not strictly enforced, but helpful):
- `ruff` for linting and basic style checks.
- `black` for code formatting (optional).

## 🐛 Reporting Issues
If you encounter a bug or want to request a feature:

1. Check if an issue already exists.
2. If not, open a new issue with:
  - What you were trying to do.
  - What you expected to happen.
  - What actually happened (traceback if applicable).
  - Example code or steps to reproduce, if possible.

## 🔁 Pull Request Process
1. Create a feature branch from main:
```bash

git checkout -b feature/my-new-feature

```

2. Make your changes.

3. Run `ruff` and `pytest`.

4. Commit with a clear message:
```bash

git commit -am "Add dynamic config for <SomeAPI>"

```

5. Push your branch and open a PR against `main`:
```bash

git push origin feature/my-new-feature

```

6. Fill out the PR template (if present) and describe:
  - What changed.
  - Why it changed.
  - Any breaking behavior or migration notes.

## 🙏 Thanks
Your contributions help make this library more robust and useful for everyone building integrations with Notion, Vanta, Fieldguide, and beyond. Thank you! 💛
