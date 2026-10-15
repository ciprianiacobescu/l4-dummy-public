# Spec Delta

## Purpose
The printed label of a shelf.

## ADDED Requirements

### Requirement: Shelf label
`inventory.shelf.shelf_label(aisle: int, slot: int, name: str)` SHALL return `shelf_code(aisle, slot)`, a space and the
stripped `name`, and SHALL raise `ValueError` when the stripped name is empty.

#### Scenario: A label
- **WHEN** the label printer asks for `inventory.shelf.shelf_label(3, 7, " bolts ")`
- **THEN** it returns exactly `A03-S07 bolts`

#### Scenario: An empty name
- **WHEN** the label printer asks for `inventory.shelf.shelf_label(3, 7, "  ")`
- **THEN** it raises `ValueError`
