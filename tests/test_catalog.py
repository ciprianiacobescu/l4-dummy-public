from decimal import Decimal

import pytest

from inventory.catalog import SkuCatalog


@pytest.mark.l4("C-7185884e")
def test_register_and_look_up_a_price():
    catalog = SkuCatalog()
    catalog.register("A-1", Decimal("2.50"))
    assert catalog.unit_price("A-1") == Decimal("2.50")


@pytest.mark.l4("C-e94711be")
def test_register_keeps_sub_cent_price_exact():
    catalog = SkuCatalog()
    catalog.register("B-2", Decimal("0.125"))
    assert catalog.unit_price("B-2") == Decimal("0.125")


@pytest.mark.l4("C-d2545444")
def test_register_accepts_zero_price():
    catalog = SkuCatalog()
    catalog.register("F-0", Decimal("0"))
    catalog.register("G-7", Decimal("0.125"))
    assert catalog.unit_price("F-0") == Decimal("0")
    assert catalog.unit_price("G-7") == Decimal("0.125")


@pytest.mark.l4("C-3b21b3b3")
def test_skus_are_sorted_and_new_catalog_is_empty():
    empty = SkuCatalog()
    assert empty.skus() == []
    catalog = SkuCatalog()
    catalog.register("B-2", Decimal("0.125"))
    catalog.register("A-1", Decimal("2.50"))
    assert catalog.skus() == ["A-1", "B-2"]
