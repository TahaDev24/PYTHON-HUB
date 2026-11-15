# Development Guide

## Environment

Use Python 3.11 or newer. Create an isolated environment and install the development extra:

~~~bash
python -m venv .venv
python -m pip install -e ".[dev]"
~~~

## Project conventions

- Add Python runtime code under src/python_hub.
- Keep tests under tests and name files test_*.py.
- Prefer small modules with one clear responsibility.
- Add type annotations to public functions and data models.
- Use immutable dataclasses for stable metadata where appropriate.
- Raise domain exceptions for expected application failures.
- Keep optional dependencies optional.
- Avoid import-time side effects, network calls, and filesystem writes.

## Quality commands

~~~bash
ruff check .
ruff format --check .
mypy src/python_hub
pytest
~~~

Run the full set before submitting changes. If a check fails, fix the issue rather than disabling the rule without explanation.

## Testing strategy

- Unit tests cover domain logic and error conditions.
- Contract tests verify plugin adapters against shared expectations.
- API tests should use a test client and never contact external services.
- Frontend tests should cover search, language direction, keyboard use, and responsive states as the UI grows.
- Integration tests should be deterministic and use temporary directories.

## Dependency policy

Before adding a dependency, consider whether the standard library or an existing dependency is sufficient. For every new runtime dependency, document its capability, minimum supported version, license and maintenance status, import and startup impact, security, and platform implications.

Keep large data-science and machine-learning frameworks out of the base installation. They should be optional, isolated integrations.

## Public contracts

Changes to tool metadata, plugin interfaces, configuration keys, or API response shapes should include tests and documentation. Breaking changes must be called out in the changelog and discussed before merge.
