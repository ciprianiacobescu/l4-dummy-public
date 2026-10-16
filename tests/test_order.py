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
