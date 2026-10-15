# Proposal: summary currency

## Why
The daily mail goes to a team that works in more than one currency, so the summary names it.

## What Changes
- Change `inventory.summary.valuation_summary` (added by the change `add-valuation-summary`) to take
  `currency: str | None = None`. With a currency it puts the currency after each amount
  (`net 9.00 EUR | vat 0.90 EUR | gross 9.90 EUR`); without one the summary is unchanged, so existing callers and tests
  keep working.

## Capabilities

### New Capabilities
- `summary-currency`: the currency in the one-line stock value.

### Modified Capabilities

## Impact
`src/inventory/summary.py` and its tests. It depends on the change `add-valuation-summary` (it changes the function that
change adds) and on nothing else.
