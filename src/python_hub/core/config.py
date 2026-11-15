"""Application configuration with safe environment-based overrides."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from python_hub.core.errors import ConfigurationError
from python_hub.core.paths import get_data_dir


@dataclass(frozen=True, slots=True)
class AppConfig:
    """Small, immutable configuration object for the application shell."""

    locale: str = "en"
    theme: str = "dark"
    data_dir: Path = get_data_dir()

    @classmethod
    def from_environment(cls) -> AppConfig:
        """Build configuration from supported environment variables."""
        locale = os.getenv("PYTHON_HUB_LOCALE", "en").strip().lower()
        theme = os.getenv("PYTHON_HUB_THEME", "dark").strip().lower()
        data_dir_value = os.getenv("PYTHON_HUB_DATA_DIR")

        if locale not in {"en", "fa"}:
            raise ConfigurationError("PYTHON_HUB_LOCALE must be 'en' or 'fa'")
        if theme not in {"dark"}:
            raise ConfigurationError("Only the dark theme is currently supported")

        data_dir = Path(data_dir_value).expanduser() if data_dir_value else get_data_dir()
        return cls(locale=locale, theme=theme, data_dir=data_dir)
