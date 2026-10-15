# Proposal: Taxed total as text

## Why
The receipt prints the taxed total as an amount.

## What Changes
- Add `pricing.discount.taxed_total_text(amounts, percent, rate_percent)`: the `str` of
  `pricing.money.from_cents(taxed_total(amounts, percent, rate_percent))` (changes `add-taxed-total`,
  `add-money-format`).

## Capabilities

### New Capabilities
- `taxed-text`: the taxed total as text.

### Modified Capabilities

## Impact
`src/pricing/discount.py`, tests under `tests/`. It depends on the change `add-taxed-total`.
