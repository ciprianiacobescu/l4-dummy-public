# Proposal: Discounted total

## Why
A basket total after a promotion, from the line amounts in cents.

## What Changes
- Add `pricing.discount.discounted_total(amounts, percent)`: the sum of `amounts` minus
  `pricing.discount.percent_off(sum, percent)` (change `add-percent-off`). `percent_off` is always called, so its `ValueError` for a
  bad percent is raised unchanged, even for an empty list; an empty list with a valid percent gives `0`.

## Capabilities

### New Capabilities
- `discounted-total`: the total after a percentage off.

### Modified Capabilities

## Impact
`src/pricing/discount.py` (the module of `add-percent-off`), tests under `tests/`. It depends on the change
`add-percent-off`.
