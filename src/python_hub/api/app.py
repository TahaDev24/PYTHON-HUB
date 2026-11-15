"""Optional FastAPI application exposing the initial catalog API."""

from __future__ import annotations

from dataclasses import asdict

from python_hub import __version__
from python_hub.catalog.categories import get_categories


def create_app():
    """Create the API application.

    FastAPI is an optional dependency. Install the API extra before importing
    this module.
    """
    try:
        from fastapi import FastAPI
    except ImportError as exc:
        raise RuntimeError(
            "FastAPI is optional. Install PYTHON HUB with the 'api' extra."
        ) from exc

    application = FastAPI(
        title="PYTHON HUB API",
        version=__version__,
        description="Initial API for PYTHON HUB platform metadata.",
    )

    @application.get("/api/v1/health", tags=["system"])
    def health() -> dict[str, str]:
        return {"status": "ok", "version": __version__}

    @application.get("/api/v1/catalog/categories", tags=["catalog"])
    def categories() -> dict[str, object]:
        return {"items": [asdict(item) for item in get_categories()]}

    return application


app = create_app()
