# Proposal: Discounted total

## Why
A basket total after a promotion, from the line amounts in cents.

## What Changes
- Add `pricing.discount.discounted_total(amounts, percent)`: the sum of `amounts` minus
  `pricing.discount.percent_off(sum, percent)` (change `add-percent-off`). An empty list gives `0`; a `ValueError` of
  `percent_off` is raised unchanged.

## Capabilities

### New Capabilities
- `discounted-total`: the total after a percentage off.

### Modified Capabilities

## Impact
`src/pricing/discount.py` (the module of `add-percent-off`), tests under `tests/`. It depends on the change
`add-percent-off`.
