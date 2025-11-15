# Release & Publishing Guide

This document describes how to cut a new release of `dynamic-api-rate-limiter`
and publish it to PyPI.

The project follows **Semantic Versioning**:

- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes

---

## 1. Pre-release checklist

- [ ] All tests pass locally: `pytest`
- [ ] Lint passes: `ruff check api_ratelimiter examples`
- [ ] `README.md`, `USAGE.md`, and other docs are up to date
- [ ] `CHANGELOG.md` has an entry for the new version
- [ ] `__version__` in `api_ratelimiter/__init__.py` is updated
- [ ] `version` in `pyproject.toml` is updated

Example version bump (to 0.2.0):

- In `pyproject.toml`:

  ```toml
  version = "0.2.0"
  ```

- In `api_ratelimiter/__init__.py`:

  ```python
  __version__ = "0.2.0"
  ```

- In `CHANGELOG.md`, add a new section:

  ```markdown
  ## [0.2.0] - YYYY-MM-DD
  ```

---

## 2. Build the distribution

Upgrade build tools (once):

```bash
python -m pip install --upgrade build twine
```

Build the package:

```bash
python -m build
```

This will create `dist/` with `.tar.gz` and `.whl` files.

---

## 3. Test upload to TestPyPI (optional but recommended)

```bash
twine upload --repository testpypi dist/*
```

If everything looks good, proceed to real PyPI.

---

## 4. Upload to PyPI

Make sure you have a `PYPI_API_TOKEN` with publish rights.

```bash
twine upload dist/*
```

After upload, verify:

- The project page on PyPI is correct
- Installation works via:

  ```bash
  pip install dynamic-api-rate-limiter
  ```

---

## 5. Tag the release in Git

```bash
git tag -a v0.2.0 -m "Release 0.2.0"
git push origin v0.2.0
```

If you configure GitHub Actions to publish on tag, this tag will trigger
the workflow.

---

## 6. Post-release

- [ ] Update `CHANGELOG.md` `[Unreleased]` section with any future plans
- [ ] Announce the release (GitHub Releases, social, etc.)
- [ ] Create issues for any follow-up work discovered during release
