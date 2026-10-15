# Proposal: valuation summary

## Why
The daily mail shows the stock value on one line.

## What Changes
- Add `inventory.summary.valuation_summary(ledger, price_cents, rate_percent)`, which returns
  `net <net> | vat <vat> | gross <gross>` from the result of `inventory.valuation.stock_value`.

## Capabilities

### New Capabilities
- `valuation-summary`: the one-line stock value of the daily mail.

### Modified Capabilities

## Impact
`src/inventory/summary.py` (new), tests under `tests/`. It depends on the change `add-stock-valuation`: it calls
`inventory.valuation.stock_value` and uses nothing else from other changes.
