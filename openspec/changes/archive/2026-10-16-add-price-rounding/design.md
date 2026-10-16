# Design: Price rounding

## Context
`pricing.vat.vat_cents(net_cents, rate_percent)` already rounds half up, but on integer cents (`(n * r + 50) // 100`)
and stays as it is. Prices finer than a cent are `decimal.Decimal` amounts in currency units, so they need their own
rounding.

## Interface
`round_cents(amount: Decimal) -> int` in the new module `src/pricing/rounding.py`:
- `amount * 100` quantized to `Decimal("1")` with `decimal.ROUND_HALF_UP` (a tie goes away from zero), returned as an
  `int`. The result does not depend on the current `decimal` context's rounding mode.
- Checks, in this order: an `amount` that is not a `decimal.Decimal` (a `float`, an `int`, a `bool`, a `str`) raises
  `TypeError`; a non-finite `amount` (`NaN`, `sNaN`, `Infinity`, `-Infinity`) raises `ValueError`.

## Decisions
- `Decimal` only: a `float` cannot hold `0.125`-style prices exactly, and accepting an `int` would leave open whether
  it means units or cents.
- Ties away from zero, also for negative amounts (`-0.125` is `-13`), as `decimal.ROUND_HALF_UP` does.
- A new module instead of `pricing/money.py`, so the formatting helpers there stay unchanged.
