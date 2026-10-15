import pytest

from inventory.stock import units_surplus


@pytest.mark.l4("C-c9bc333b")
def test_units_surplus_returns_remainder():
    assert units_surplus(9, 4) == 5


@pytest.mark.l4("C-7bbe703f", "C-c9bc333b")
def test_units_surplus_is_zero_when_wanted_at_least_on_hand():
    assert units_surplus(3, 4) == 0
    assert units_surplus(9, 4) == 5


@pytest.mark.l4("C-5078cdbe")
def test_units_surplus_rejects_negative_counts():
    with pytest.raises(ValueError):
        units_surplus(-1, 4)
    with pytest.raises(ValueError):
        units_surplus(4, -1)
