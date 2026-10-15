# Proposal: VAT amount

## Why
Valuations and invoices add VAT to a net amount in cents, rounded the same way everywhere.

## What Changes
- Add `pricing.vat.vat_cents(net_cents, rate_percent)`: the VAT in cents, `net_cents * rate_percent / 100` rounded half
  up (`1999` at 19 gives `380`, `250` at 10 gives `25`, any amount at 0 gives `0`). A negative net amount or rate
  raises `ValueError`.

## Capabilities

### New Capabilities
- `vat`: the VAT on a net amount.

### Modified Capabilities

## Impact
`src/pricing/vat.py` (new), tests under `tests/`. It depends on no other change.
