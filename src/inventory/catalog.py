"""In-memory SKU catalog."""

from decimal import Decimal


class SkuCatalog:
    def register(self, sku: str, unit_price: Decimal) -> None:
        raise NotImplementedError

    def unit_price(self, sku: str) -> Decimal:
        raise NotImplementedError

    def skus(self) -> list[str]:
        raise NotImplementedError
