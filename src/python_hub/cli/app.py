"""Command-line entry point for PYTHON HUB."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from collections.abc import Sequence

from python_hub import __version__
from python_hub.catalog.categories import get_categories
from python_hub.core.config import AppConfig
from python_hub.core.errors import PythonHubError
from python_hub.core.paths import get_data_dir
from python_hub.localization.catalog import supported_locales


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="python-hub",
        description="A unified workspace for the Python ecosystem.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    commands = parser.add_subparsers(dest="command")

    commands.add_parser("doctor", help="Inspect the local PYTHON HUB environment.")

    catalog = commands.add_parser("catalog", help="Explore the Python ecosystem catalog.")
    catalog_commands = catalog.add_subparsers(dest="catalog_command")
    list_command = catalog_commands.add_parser("list", help="List ecosystem categories.")
    list_command.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    locale = commands.add_parser("locales", help="List supported interface languages.")
    locale.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    commands.add_parser("serve", help="Start the optional local HTTP API.")
    return parser


def _run_doctor() -> int:
    config = AppConfig.from_environment()
    print("PYTHON HUB environment")
    print(f"  Application: {__version__}")
    print(f"  Python:      {platform.python_version()}")
    print(f"  Runtime:     {platform.system()} {platform.machine()}")
    print(f"  Locale:      {config.locale}")
    print(f"  Theme:       {config.theme}")
    print(f"  Data path:   {get_data_dir()}")
    print("  Status:      ready")
    return 0


def _run_catalog(as_json: bool) -> int:
    categories = get_categories()
    if as_json:
        payload = [
            {"id": item.id, "name": item.name, "description": item.description}
            for item in categories
        ]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"Python ecosystem domains ({len(categories)})")
    for item in categories:
        print(f"  {item.id:<22} {item.name} — {item.description}")
    print()
    print("Note: categories describe the ecosystem; integrations are not implied to be complete.")
    return 0


def _run_locales(as_json: bool) -> int:
    locales = supported_locales()
    if as_json:
        print(json.dumps(locales, ensure_ascii=False, indent=2))
        return 0

    for locale in locales:
        direction = "RTL" if locale["rtl"] else "LTR"
        print(f"{locale['code']:<5} {locale['name']:<12} {direction}")
    return 0


def _run_server() -> int:
    try:
        import uvicorn
    except ImportError:
        print(
            "The API extras are not installed. Run: python -m pip install -e '.[api]'",
            file=sys.stderr,
        )
        return 2

    uvicorn.run("python_hub.api.app:app", host="127.0.0.1", port=8000, reload=True)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return a process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "doctor":
            return _run_doctor()
        if args.command == "catalog" and args.catalog_command == "list":
            return _run_catalog(args.json)
        if args.command == "locales":
            return _run_locales(args.json)
        if args.command == "serve":
            return _run_server()
        parser.print_help()
        return 0
    except PythonHubError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
