"""Portable paths used by the application."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def get_data_dir(app_name: str = "python-hub") -> Path:
    """Return the user-specific data directory without creating it."""
    if not app_name or app_name in {".", ".."} or Path(app_name).name != app_name:
        raise ValueError("app_name must be a single non-empty path segment")

    if sys.platform == "win32":
        root = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    elif sys.platform == "darwin":
        root = Path.home() / "Library" / "Application Support"
    else:
        root = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))

    return root / app_name
