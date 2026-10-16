"""Shared pytest fixtures of the shop's tests (pytest reads this file for every test under tests/)."""

from decimal import Decimal

import pytest

from inventory.catalog import SkuCatalog


@pytest.fixture
def sku_catalog() -> SkuCatalog:
    catalog = SkuCatalog()
    catalog.register("A-1", Decimal("2.50"))
    catalog.register("B-2", Decimal("0.125"))
    return catalog
