"""Price rounding helpers of the eval base project."""

from decimal import Decimal


def round_cents(amount: Decimal) -> int:
    """The whole cents nearest to `amount` (currency units), ties away from zero."""
    raise NotImplementedError
