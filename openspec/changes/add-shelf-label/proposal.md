# Proposal: shelf label

## Why
Shelf labels show the shelf code and the product name together.

## What Changes
- Add `inventory.shelf.shelf_label(aisle, slot, name)`, which returns the existing `shelf_code(aisle, slot)`, a space
  and `name` with surrounding spaces removed (`3, 7, " bolts "` gives `A03-S07 bolts`). An empty name raises
  `ValueError`.

## Capabilities

### New Capabilities
- `shelf-label`: the printed label of a shelf.

### Modified Capabilities

## Impact
`src/inventory/shelf.py` (a new function next to the existing `shelf_code`), tests under `tests/`. It depends on no
other change.
