"""In-memory SKU catalog."""

from decimal import Decimal


class SkuCatalog:
    def __init__(self) -> None:
        self._prices: dict[str, Decimal] = {}

    def register(self, sku: str, unit_price: Decimal) -> None:
        self._prices[sku] = unit_price

    def unit_price(self, sku: str) -> Decimal:
        return self._prices[sku]

    def skus(self) -> list[str]:
        return sorted(self._prices)
