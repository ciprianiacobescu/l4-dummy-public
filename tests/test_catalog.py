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


@pytest.mark.l4("C-a7f447fb")
@pytest.mark.parametrize(
    "bad_price",
    [Decimal("-0.01"), Decimal("NaN"), Decimal("Infinity"), Decimal("-Infinity")],
)
def test_register_rejects_negative_or_non_finite_price(bad_price):
    catalog = SkuCatalog()
    catalog.register("K-1", Decimal("2.50"))
    with pytest.raises(ValueError):
        catalog.register("N-1", bad_price)
    assert catalog.skus() == ["K-1"]


@pytest.mark.l4("C-3006b46a")
def test_register_rejects_duplicate_sku_and_keeps_first_price():
    catalog = SkuCatalog()
    catalog.register("A-1", Decimal("2.50"))
    with pytest.raises(ValueError) as excinfo:
        catalog.register("A-1", Decimal("3.00"))
    assert "A-1" in str(excinfo.value)
    assert catalog.unit_price("A-1") == Decimal("2.50")
    assert catalog.skus() == ["A-1"]


@pytest.mark.l4("C-5541dd3b")
@pytest.mark.parametrize("bad_sku", ["", "   ", "\t"])
def test_register_rejects_blank_sku(bad_sku):
    catalog = SkuCatalog()
    catalog.register("A-1", Decimal("2.50"))
    with pytest.raises(ValueError):
        catalog.register(bad_sku, Decimal("2.50"))
    assert catalog.skus() == ["A-1"]


@pytest.mark.l4("C-59fd7246")
@pytest.mark.parametrize("bad_price", [2.5, 250, "2.50"])
def test_register_rejects_non_decimal_price(bad_price):
    catalog = SkuCatalog()
    catalog.register("A-1", Decimal("2.50"))
    with pytest.raises(TypeError):
        catalog.register("N-1", bad_price)
    assert catalog.skus() == ["A-1"]
