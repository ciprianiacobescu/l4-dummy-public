# Proposal: money format

## Why
Reports and invoices print amounts that the code keeps as integer cents.

## What Changes
- Add `pricing.money.from_cents(cents)`, the inverse of the existing `to_cents`: it returns the amount as a `str` with
  exactly two decimals and a leading `-` for a negative amount (`1234` gives `12.34`, `-5` gives `-0.05`, `0` gives
  `0.00`).

## Capabilities

### New Capabilities
- `money-format`: the printed form of an amount in cents.

### Modified Capabilities

## Impact
`src/pricing/money.py` (a new function next to `to_cents`), tests under `tests/`. It depends on no other change.
