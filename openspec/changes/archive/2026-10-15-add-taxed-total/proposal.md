# Proposal: Taxed basket total

## Why
The till shows the basket total after the promotion and with VAT.

## What Changes
- Add `pricing.discount.taxed_total(amounts, percent, rate_percent)`: `net = pricing.discount.discounted_total(amounts,
  percent)` (change `add-discounted-total`), plus `pricing.vat.vat_cents(net, rate_percent)` (change `add-vat`, half-up
  rounding). Their `ValueError` is raised unchanged.

## Capabilities

### New Capabilities
- `taxed-total`: the basket total with VAT.

### Modified Capabilities

## Impact
`src/pricing/discount.py`, tests under `tests/`. It depends on the changes `add-discounted-total` and `add-vat`.
