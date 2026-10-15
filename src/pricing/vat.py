"""VAT helpers of the eval base project."""


def vat_cents(net_cents: int, rate_percent: int) -> int:
    """The VAT in cents on `net_cents` at `rate_percent`, rounded half up."""
    if net_cents < 0 or rate_percent < 0:
        raise ValueError("net_cents and rate_percent must be non-negative")
    return (net_cents * rate_percent + 50) // 100
