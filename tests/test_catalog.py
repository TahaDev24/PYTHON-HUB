from python_hub.catalog.categories import get_categories, get_category


def test_category_ids_are_unique_and_stable() -> None:
    categories = get_categories()
    ids = [item.id for item in categories]

    assert len(categories) >= 15
    assert len(ids) == len(set(ids))
    assert all(item.id == item.id.lower() for item in categories)


def test_category_lookup_normalizes_input() -> None:
    category = get_category("  CODE-QUALITY ")

    assert category is not None
    assert category.name == "Code Quality"


def test_unknown_category_returns_none() -> None:
    assert get_category("not-a-real-category") is None
