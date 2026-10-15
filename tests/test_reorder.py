import pytest

from inventory.reorder import reorder_quantity


@pytest.mark.l4("C-97756e71")
def test_stock_below_target_is_topped_up():
    assert reorder_quantity(4, 10) == 6


@pytest.mark.l4("C-2d2a7548", "C-97756e71")
def test_stock_at_or_above_target_is_not_ordered():
    assert reorder_quantity(12, 10) == 0
    assert reorder_quantity(4, 10) == 6
