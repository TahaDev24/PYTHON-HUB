from python_hub.localization.catalog import supported_locales, translate


def test_english_is_the_default_locale() -> None:
    assert translate("app.name") == "PYTHON HUB"


def test_persian_messages_are_available() -> None:
    assert translate("nav.overview", "fa") == "نمای کلی"


def test_unknown_key_falls_back_to_key() -> None:
    assert translate("missing.key") == "missing.key"


def test_locale_metadata_includes_rtl_information() -> None:
    locales = {item["code"]: item for item in supported_locales()}
    assert locales["en"]["rtl"] is False
    assert locales["fa"]["rtl"] is True
