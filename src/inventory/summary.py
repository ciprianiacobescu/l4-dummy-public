"""One-line stock value summary of the daily mail."""

from inventory.valuation import stock_value


def valuation_summary(
    ledger,
    price_cents: dict[str, int],
    rate_percent: int,
    currency: str | None = None,
) -> str:
    value = stock_value(ledger, price_cents, rate_percent)
    suffix = f" {currency}" if currency is not None else ""
    return (
        f"net {value['net']}{suffix} | "
        f"vat {value['vat']}{suffix} | "
        f"gross {value['gross']}{suffix}"
    )
