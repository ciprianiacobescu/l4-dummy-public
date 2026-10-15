# Proposal: Percent off

## Why
Promotions take a percentage off an amount in cents, rounded the same way everywhere.

## What Changes
- Add `pricing.discount.percent_off(cents, percent)`: the discount in cents, `cents * percent / 100` rounded half up.
  A negative amount, or a percent outside 0 to 100, raises `ValueError`.

## Capabilities

### New Capabilities
- `discount`: the discount on an amount.

### Modified Capabilities

## Impact
`src/pricing/discount.py` (new), tests under `tests/`. It depends on no other change.
