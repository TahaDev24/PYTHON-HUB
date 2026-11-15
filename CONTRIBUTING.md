# Contributing to PYTHON HUB

Thank you for considering a contribution. The project aims to make the Python ecosystem easier to discover and use without sacrificing quality, security, or the identity of integrated tools.

## Before you start

1. Read the [architecture](docs/ARCHITECTURE.md) and [roadmap](docs/ROADMAP.md).
2. Search existing issues and pull requests.
3. Open an issue before substantial features or architectural changes.
4. Never submit secrets, private data, or code copied from a project whose license does not permit its use.

## Development setup

Python 3.11 or newer is required.

~~~bash
git clone https://github.com/TahaDev24/PYTHON-HUB.git
cd PYTHON-HUB
python -m venv .venv
python -m pip install -e ".[dev]"
~~~

## Quality checks

~~~bash
ruff check .
ruff format --check .
mypy src/python_hub
pytest
~~~

Behavior changes should include tests. Public interfaces, configuration keys, plugin contracts, and user-visible behavior should be documented.

## Pull request expectations

- Keep each pull request focused and reasonably sized.
- Explain the problem and the reasoning behind the change.
- Link related issues.
- Include tests for new behavior and regression fixes.
- Update documentation and examples when behavior changes.
- Avoid unrelated formatting or file moves.
- Explain new runtime dependencies.
- Do not claim an integration is complete unless it has been implemented and tested end to end.

## Tool integration requirements

Every proposed integration should identify its upstream project, license, supported versions, installation source, platform support, permissions, execution model, and maintenance status. Prefer official APIs and supported interfaces over scraping or brittle shell commands.

## Security reports

Do not report vulnerabilities in public issues. Follow the private reporting instructions in [SECURITY.md](SECURITY.md).

## License and contributions

The project license has not yet been selected. Until licensing terms are published, do not assume contributions or repository contents may be redistributed under a particular open-source license.
