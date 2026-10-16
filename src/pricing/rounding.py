"""Price rounding helpers of the eval base project."""

from decimal import ROUND_HALF_UP, Decimal, localcontext


def round_cents(amount: Decimal) -> int:
    """The whole cents nearest to `amount` (currency units), ties away from zero."""
    if not isinstance(amount, Decimal):
        raise TypeError(f"amount must be a Decimal, got {type(amount).__name__}")
    if not amount.is_finite():
        raise ValueError(f"amount must be finite, got {amount}")
    with localcontext() as context:
        context.prec = max(context.prec, 28)
        return int((amount * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
