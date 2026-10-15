import pytest

from inventory.shelf import shelf_code


@pytest.mark.l4("C-7dc9fae5")
def test_shelf_code_is_zero_padded():
    assert shelf_code(3, 7) == "A03-S07"


@pytest.mark.l4("C-fa2e5d61")
def test_shelf_code_rejects_aisle_below_one():
    with pytest.raises(ValueError):
        shelf_code(0, 7)
