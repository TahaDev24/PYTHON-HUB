"""Small application message catalog for English and Persian."""

from __future__ import annotations

from typing import Literal

LocaleCode = Literal["en", "fa"]

_MESSAGES: dict[str, dict[str, str]] = {
    "en": {
        "app.name": "PYTHON HUB",
        "nav.overview": "Overview",
        "nav.catalog": "Ecosystem",
        "nav.favorites": "Favorites",
        "nav.settings": "Settings",
        "search.placeholder": "Search tools and categories...",
        "status.foundation": "Platform foundation",
    },
    "fa": {
        "app.name": "پایتون هاب",
        "nav.overview": "نمای کلی",
        "nav.catalog": "اکوسیستم",
        "nav.favorites": "علاقه‌مندی‌ها",
        "nav.settings": "تنظیمات",
        "search.placeholder": "جست‌وجوی ابزارها و دسته‌بندی‌ها...",
        "status.foundation": "زیرساخت اولیه پلتفرم",
    },
}


def translate(key: str, locale: LocaleCode = "en") -> str:
    """Return a translated message, falling back to English and then the key."""
    language = _MESSAGES.get(locale, _MESSAGES["en"])
    return language.get(key, _MESSAGES["en"].get(key, key))


def supported_locales() -> list[dict[str, str | bool]]:
    """Return public locale metadata for CLI and API consumers."""
    return [
        {"code": "en", "name": "English", "native_name": "English", "rtl": False},
        {"code": "fa", "name": "Persian", "native_name": "فارسی", "rtl": True},
    ]
