"""VAT helpers of the eval base project."""


def vat_cents(net_cents: int, rate_percent: int) -> int:
    """The VAT in cents on `net_cents` at `rate_percent`, rounded half up."""
    raise NotImplementedError
