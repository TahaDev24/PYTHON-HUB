.PHONY: install test lint format-check typecheck check web

install:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

format-check:
	ruff format --check .

typecheck:
	mypy src/python_hub

check: lint format-check typecheck test

web:
	python -m http.server 5173 --directory apps/web
