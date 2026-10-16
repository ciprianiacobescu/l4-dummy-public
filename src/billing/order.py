"""Order total helpers of the eval base project."""

from inventory.catalog import SkuCatalog


def order_total_cents(catalog: SkuCatalog, items: list[tuple[str, int]]) -> int:
    """The whole cents total of an order, rounding the exact sum once."""
    raise NotImplementedError
