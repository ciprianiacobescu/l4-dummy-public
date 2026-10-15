"""One-line stock value summary of the daily mail."""

from inventory.valuation import stock_value


def valuation_summary(
    ledger,
    price_cents: dict[str, int],
    rate_percent: int,
    currency: str | None = None,
) -> str:
    if currency is not None:
        raise NotImplementedError
    value = stock_value(ledger, price_cents, rate_percent)
    return f"net {value['net']} | vat {value['vat']} | gross {value['gross']}"
