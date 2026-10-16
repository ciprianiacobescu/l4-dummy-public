# Proposal: Price rounding

## Why
Unit prices can be finer than a cent (`0.125`), so a sum of them is too. A total must become whole cents in one
agreed way.

## What Changes
- Add `pricing.rounding.round_cents(amount)`: a `decimal.Decimal` amount in currency units as an `int` number of
  cents, with a tie (exactly half a cent) rounded away from zero (`decimal.ROUND_HALF_UP`). An amount that is not a
  `decimal.Decimal` raises `TypeError`; a non-finite one (`NaN`, `Infinity`) raises `ValueError`.

## Capabilities

### New Capabilities
- `price-rounding`: amounts finer than a cent rounded half up to whole cents.

### Modified Capabilities

## Impact
`src/pricing/rounding.py` (new), tests under `tests/`. No existing module changes. It depends on no other change; the
Kiro spec `catalog-total` calls `round_cents`.
