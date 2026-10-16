import pytest

from billing.order import order_total_cents
from inventory.catalog import SkuCatalog


@pytest.mark.l4("C-195630bc")
def test_order_total_sums_and_rounds_once(sku_catalog: SkuCatalog):
    assert order_total_cents(sku_catalog, [("A-1", 2), ("B-2", 3)]) == 538


@pytest.mark.l4("C-33b6327b")
def test_order_total_rounds_sum_not_each_item(sku_catalog: SkuCatalog):
    assert order_total_cents(sku_catalog, [("B-2", 1), ("B-2", 1)]) == 25


@pytest.mark.l4("C-eb22bf33")
def test_order_total_single_item(sku_catalog: SkuCatalog):
    assert order_total_cents(sku_catalog, [("A-1", 1)]) == 250


@pytest.mark.l4("C-5511b8fe")
def test_empty_order_returns_zero_without_calling_catalog(sku_catalog: SkuCatalog):
    class _NoCallCatalog:
        def unit_price(self, sku: str):
            raise AssertionError(f"unit_price must not be called, got {sku!r}")

    assert order_total_cents(_NoCallCatalog(), []) == 0
    assert order_total_cents(sku_catalog, [("A-1", 1)]) == 250


class _NoCallCatalog:
    def unit_price(self, sku: str):
        raise AssertionError(f"unit_price must not be called, got {sku!r}")


@pytest.mark.l4("C-0559ea74")
@pytest.mark.parametrize("bad_qty", [0, -1])
def test_quantity_below_one_raises_value_error_naming_sku(bad_qty: int):
    with pytest.raises(ValueError) as excinfo:
        order_total_cents(_NoCallCatalog(), [("A-1", 1), ("B-2", bad_qty)])
    assert "B-2" in str(excinfo.value)


@pytest.mark.l4("C-cdb7a4f0")
@pytest.mark.parametrize("bad_qty", [1.5, True])
def test_non_int_or_bool_quantity_raises_type_error_naming_sku(bad_qty):
    with pytest.raises(TypeError) as excinfo:
        order_total_cents(_NoCallCatalog(), [("A-1", bad_qty)])
    assert "A-1" in str(excinfo.value)
