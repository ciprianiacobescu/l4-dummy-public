"""Invoice line helpers of the eval base project."""

from inventory.ledger import StockLedger


def invoice_line(
    ledger: StockLedger,
    sku: str,
    qty: int,
    unit_price_cents: int,
    rate_percent: int,
) -> dict:
    """One invoice line with its net, VAT and gross amounts."""
    raise NotImplementedError
