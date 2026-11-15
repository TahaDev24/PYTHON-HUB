<div align="center">

# PYTHON HUB
### One Ecosystem. Every Python Tool.

A unified, modular workspace for exploring and using the Python ecosystem — from code quality and testing to data, AI, APIs, automation, and more.

[Documentation](docs/README.md) · [Getting Started](docs/GETTING_STARTED.md) · [Roadmap](docs/ROADMAP.md) · [Contributing](CONTRIBUTING.md)

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-Responsive-00C8D7)
![Languages](https://img.shields.io/badge/Languages-English%20%7C%20Persian-7567F8)
![Status](https://img.shields.io/badge/Status-Early%20Development-orange)

</div>

---

## Vision

PYTHON HUB is being built as a single destination for the tools, workflows, and integrations that make the Python ecosystem productive. It brings independently maintained capabilities into a consistent experience instead of attempting to reimplement every mature Python project.

- **One workspace:** a discoverable home for tools across the Python ecosystem.
- **Composable by design:** a modular core, explicit tool contracts, and an extensible plugin system.
- **Works across screens:** a responsive experience for phones, tablets, and desktop computers.
- **Accessible to more developers:** English by default, with Persian localization and right-to-left support.

## What is in this repository?

| Area | Foundation |
|---|---|
| Python core | Package layout, configuration, paths, logging, and domain errors |
| Command line | CLI with diagnostics and catalog commands |
| Catalog | Structured categories for the wider Python ecosystem |
| Extensions | Typed tool contracts and an in-process registry |
| API | Optional FastAPI health and catalog endpoints |
| Web interface | Responsive, dark-first, bilingual interface shell |
| Quality | Tests, Ruff configuration, CI, and dependency automation |
| Governance | Contribution, security, support, and issue-reporting guidance |

The catalog describes ecosystem domains. A category appearing in the interface does **not** mean every tool in that domain has already been integrated.

## Project status

PYTHON HUB is in early development. This branch establishes the project structure and initial foundations. Tool integrations, execution isolation, accounts, synchronization, desktop packaging, and the full marketplace are planned work — not completed features.

Follow the [roadmap](docs/ROADMAP.md) for the intended delivery sequence.

## Quick start

Requirements: Python 3.11 or newer.

~~~bash
git clone https://github.com/TahaDev24/PYTHON-HUB.git
cd PYTHON-HUB
python -m venv .venv
# Activate the environment, then:
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m python_hub --help
python -m python_hub doctor
python -m python_hub catalog list
pytest
~~~

Optional HTTP API:

~~~bash
python -m pip install -e ".[api]"
python -m uvicorn python_hub.api.app:app --reload
~~~

The API exposes metadata endpoints and interactive documentation at /docs. It does not execute tools.

Preview the current web interface:

~~~bash
python -m http.server 5173 --directory apps/web
~~~

## Repository layout

~~~text
PYTHON-HUB/
├── .github/                 Workflows and contribution templates
├── apps/web/                Responsive web interface foundation
├── docs/                    Product and engineering documentation
├── src/python_hub/
│   ├── api/                 Optional HTTP API
│   ├── catalog/             Ecosystem category models
│   ├── cli/                 Command-line interface
│   ├── core/                Shared application foundations
│   ├── localization/        English and Persian resources
│   └── plugins/             Tool contracts and registry
└── tests/                   Automated test suite
~~~

## Design and language

The interface uses a dark visual foundation with electric-blue and cyan accents, responsive layouts, keyboard-friendly controls, and reduced-motion support. English is the default language; Persian is available with RTL layout support.

## Security

The current registry is an in-process foundation, not a security sandbox. Do not load untrusted plugins. Read [SECURITY.md](SECURITY.md) and the [security model](docs/SECURITY_MODEL.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), open an issue for substantial changes, and include tests and documentation with behavior changes.

## License

A license has not yet been selected. Until a license is added, no permission to redistribute or create derivative works should be assumed. License selection is an explicit project decision.
