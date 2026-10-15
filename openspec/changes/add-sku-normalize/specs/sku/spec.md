# Spec Delta

## Purpose
One spelling of a SKU.

## ADDED Requirements

### Requirement: Normalized SKU
`inventory.sku.normalize(sku: str)` SHALL return `sku` with the surrounding spaces removed, in upper case, and SHALL
raise `ValueError` when nothing is left after the spaces are removed.

#### Scenario: Spaces and lower case
- **WHEN** a clerk enters `inventory.sku.normalize("  ab-12 ")`
- **THEN** it returns exactly `"AB-12"`

#### Scenario: Only spaces
- **WHEN** a clerk enters `inventory.sku.normalize("   ")`
- **THEN** it raises `ValueError`
