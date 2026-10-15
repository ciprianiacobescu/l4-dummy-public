import pytest

from inventory.sku import normalize


@pytest.mark.l4("C-dfed5b51")
def test_normalize_strips_surrounding_spaces_and_upper_cases():
    assert normalize("  ab-12 ") == "AB-12"


@pytest.mark.l4("C-3c7d5cfa", "C-dfed5b51")
def test_normalize_rejects_whitespace_only_sku():
    assert normalize("  ab-12 ") == "AB-12"
    with pytest.raises(ValueError):
        normalize("   ")
