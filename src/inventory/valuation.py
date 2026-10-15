"""Stock valuation helpers of the eval base project."""

from pricing.money import from_cents
from pricing.vat import vat_cents


def stock_value(ledger, price_cents: dict[str, int], rate_percent: int):
    net = 0
    for sku in ledger.skus():
        on_hand = ledger.on_hand(sku)
        if on_hand <= 0:
            continue
        if sku not in price_cents:
            raise ValueError(f"missing price for SKU: {sku}")
        net += on_hand * price_cents[sku]
    vat = vat_cents(net, rate_percent)
    gross = net + vat
    return {
        "net": from_cents(net),
        "vat": from_cents(vat),
        "gross": from_cents(gross),
    }
