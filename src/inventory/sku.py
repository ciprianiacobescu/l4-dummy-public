"""SKU helpers of the eval base project."""


def normalize(sku: str) -> str:
    """Return `sku` with the surrounding spaces removed, in upper case."""
    normalized = sku.strip().upper()
    if not normalized:
        raise ValueError("SKU is empty after removing surrounding spaces")
    return normalized
