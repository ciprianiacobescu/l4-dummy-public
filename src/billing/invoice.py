"""Invoice line helpers of the eval base project."""

from inventory.ledger import StockLedger
from pricing import money, vat


def invoice_line(
    ledger: StockLedger,
    sku: str,
    qty: int,
    unit_price_cents: int,
    rate_percent: int,
) -> dict:
    """One invoice line with its net, VAT and gross amounts."""
    if qty < 1:
        raise ValueError(f"quantity must be at least 1: {qty}")
    if unit_price_cents < 0:
        raise ValueError(f"unit_price_cents must be non-negative: {unit_price_cents}")
    if qty > ledger.on_hand(sku):
        raise ValueError(f"cannot invoice {qty} of {sku}: {ledger.on_hand(sku)} on hand")
    net = qty * unit_price_cents
    vat_cents = vat.vat_cents(net, rate_percent)
    gross = net + vat_cents
    return {
        "sku": sku,
        "qty": qty,
        "net": money.from_cents(net),
        "vat": money.from_cents(vat_cents),
        "gross": money.from_cents(gross),
    }


def invoice_lines(
    ledger: StockLedger,
    items: list[tuple[str, int, int]],
    rate_percent: int,
) -> list[dict]:
    """Every line of an invoice, in the order of the items."""
    return [
        invoice_line(ledger, sku, qty, unit_price_cents, rate_percent)
        for sku, qty, unit_price_cents in items
    ]
