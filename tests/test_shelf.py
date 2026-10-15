import pytest

from inventory.shelf import shelf_code, shelf_label


@pytest.mark.l4("C-7dc9fae5")
def test_shelf_code_is_zero_padded():
    assert shelf_code(3, 7) == "A03-S07"


@pytest.mark.l4("C-fa2e5d61")
def test_shelf_code_rejects_aisle_below_one():
    with pytest.raises(ValueError):
        shelf_code(0, 7)


@pytest.mark.l4("C-70ccb449")
def test_shelf_label_combines_code_and_stripped_name():
    assert shelf_label(3, 7, " bolts ") == "A03-S07 bolts"


@pytest.mark.l4("C-87d7c93e", "C-70ccb449")
def test_shelf_label_rejects_whitespace_only_name():
    assert shelf_label(3, 7, " bolts ") == "A03-S07 bolts"
    with pytest.raises(ValueError):
        shelf_label(3, 7, "  ")
