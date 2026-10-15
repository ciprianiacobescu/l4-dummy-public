"""Discount helpers of the eval base project."""

from pricing.vat import vat_cents


def percent_off(cents: int, percent: int) -> int:
    """The discount in cents for `percent` off `cents`, rounded half up."""
    if cents < 0 or percent < 0 or percent > 100:
        raise ValueError("cents must be non-negative and percent between 0 and 100")
    return (cents * percent + 50) // 100


def discounted_total(amounts: list[int], percent: int) -> int:
    """The total of `amounts` after `percent` off, in cents."""
    total = sum(amounts)
    return total - percent_off(total, percent)


def taxed_total(amounts: list[int], percent: int, rate_percent: int) -> int:
    """The discounted total of `amounts` with VAT at `rate_percent`, in cents."""
    net = discounted_total(amounts, percent)
    return net + vat_cents(net, rate_percent)


def taxed_total_text(amounts: list[int], percent: int, rate_percent: int) -> str:
    raise NotImplementedError
