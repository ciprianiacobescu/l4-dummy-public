"""In-memory SKU catalog."""

from decimal import Decimal


class SkuCatalog:
    def __init__(self) -> None:
        self._prices: dict[str, Decimal] = {}

    def register(self, sku: str, unit_price: Decimal) -> None:
        if not isinstance(unit_price, Decimal):
            raise TypeError("unit_price must be a decimal.Decimal")
        if not sku.strip():
            raise ValueError("sku must not be empty")
        if not unit_price.is_finite() or unit_price < 0:
            raise ValueError("unit_price must be finite and not negative")
        if sku in self._prices:
            raise ValueError(f"sku {sku!r} is already registered")
        self._prices[sku] = unit_price

    def unit_price(self, sku: str) -> Decimal:
        return self._prices[sku]

    def skus(self) -> list[str]:
        return sorted(self._prices)
