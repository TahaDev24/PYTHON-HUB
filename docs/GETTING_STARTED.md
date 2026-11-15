# Getting Started

This guide covers the current repository foundation. It does not describe future integrations as if they were already available.

## Requirements

- Python 3.11 or newer.
- Git.
- A terminal.
- Node.js is not required for the current static web preview.

## Clone and install

~~~bash
git clone https://github.com/TahaDev24/PYTHON-HUB.git
cd PYTHON-HUB
python -m venv .venv
~~~

Activate the environment.

~~~bash
# Linux or macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
~~~

Install the package and developer tools.

~~~bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
~~~

## First commands

~~~bash
python -m python_hub --help
python -m python_hub --version
python -m python_hub doctor
python -m python_hub catalog list
python -m python_hub catalog list --json
python -m python_hub locales
~~~

The installed console command is also available as python-hub.

## Optional HTTP API

~~~bash
python -m pip install -e ".[api]"
python -m uvicorn python_hub.api.app:app --reload
~~~

Available endpoints: GET /api/v1/health, GET /api/v1/catalog/categories, and GET /docs for interactive OpenAPI documentation. The API currently exposes metadata only. It does not execute tools.

## Web interface preview

~~~bash
python -m http.server 5173 --directory apps/web
~~~

Search, navigation, favorites, and language controls are local interface behaviors; the current shell is not yet connected to the Python API.

## Run the test suite

~~~bash
pytest
ruff check .
ruff format --check .
mypy src/python_hub
~~~

## Configuration

| Variable | Accepted values | Default |
|---|---|---|
| PYTHON_HUB_LOCALE | en, fa | en |
| PYTHON_HUB_THEME | dark | dark |
| PYTHON_HUB_DATA_DIR | Filesystem path | Platform-specific data directory |

Invalid locale or theme values produce a configuration error rather than silently changing the user's preference.
