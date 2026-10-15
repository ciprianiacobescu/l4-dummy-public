# Proposal: SKU normalization

## Why
SKUs typed by hand carry spaces and lower case; the ledger needs one spelling.

## What Changes
- Add `inventory.sku.normalize(sku)`: the SKU with surrounding spaces removed and in upper case. An SKU that is empty
  after the spaces are removed raises `ValueError`.

## Capabilities

### New Capabilities
- `sku`: one spelling of a SKU.

### Modified Capabilities

## Impact
`src/inventory/sku.py` (new), tests under `tests/`. It depends on no other change.
