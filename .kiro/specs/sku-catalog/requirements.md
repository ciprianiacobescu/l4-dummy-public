# Requirements Document

## Introduction

The shop sells items by SKU at a unit price that can be finer than a cent (screws cost `0.125` each). This feature
adds an in-memory SKU catalog, `inventory.catalog.SkuCatalog`, that registers SKUs with a unit price and looks them
up, and a shared pytest fixture `sku_catalog` that every test of the repository can request. It depends on no other
spec.

Prices are `decimal.Decimal` amounts in currency units, stored exactly as given (no rounding). SKUs are compared
exactly as given: no trimming, case kept.

Already on the base branch: the root `conftest.py` (next to `pyproject.toml`) exists and holds only a docstring;
pytest reads it for every test under `tests/`, and `pyproject.toml` puts `src/` on the import path.

## Requirements

### Requirement 1: Register and Look Up

**User Story:** As a shop clerk, I need to register each SKU with its unit price so that totals can read the price.

#### Acceptance Criteria

1. WHEN `A-1` is registered at `Decimal("2.50")` in a new catalog, THEN `unit_price("A-1")` SHALL return `Decimal("2.50")`.

2. WHEN `B-2` is registered at `Decimal("0.125")`, THEN `unit_price("B-2")` SHALL return `Decimal("0.125")`, not rounded.

3. WHEN `F-0` is registered at `Decimal("0")`, THEN the system SHALL accept it and `unit_price("F-0")` SHALL return `Decimal("0")`.

4. WHEN `B-2` and then `A-1` are registered, THEN `skus()` SHALL return `["A-1", "B-2"]` (sorted); for a new catalog it SHALL return `[]`.

### Requirement 2: Invalid Registrations

**User Story:** As a shop clerk, I need wrong registrations rejected so that no total uses a wrong price.

#### Acceptance Criteria

1. WHEN a SKU is registered at a negative or non-finite price (e.g., `Decimal("-0.01")`, `Decimal("NaN")`, `Decimal("Infinity")`), THEN the system SHALL raise `ValueError` and `skus()` SHALL not list that SKU.

2. WHEN `A-1`, registered at `Decimal("2.50")`, is registered again at any `Decimal` price (e.g., `Decimal("3.00")`), THEN the system SHALL raise `ValueError` naming `A-1`, and `unit_price("A-1")` SHALL still return `Decimal("2.50")`.

3. WHEN the SKU is empty or only whitespace (e.g., `""`, `"   "`, `"\t"`) and the price is a valid `Decimal`, THEN the system SHALL raise `ValueError` and the catalog SHALL stay unchanged.

4. WHEN the price is not a `decimal.Decimal` (e.g., the float `2.5`, the int `250` or the str `"2.50"`), THEN the system SHALL raise `TypeError` and the catalog SHALL stay unchanged.

### Requirement 3: Unknown SKU

**User Story:** As a shop clerk, I need a clear error for a SKU that is not in the catalog so that no price is guessed.

#### Acceptance Criteria

1. WHEN `unit_price` is asked for a SKU that was never registered (e.g., `Z-9`), THEN the system SHALL raise `KeyError` whose message contains `Z-9`.

### Requirement 4: Shared Test Catalog

**User Story:** As a developer, I need one ready catalog for tests so that tests of other features share the same sample prices.

#### Acceptance Criteria

1. WHEN a test requests the pytest fixture `sku_catalog`, THEN it SHALL receive a `SkuCatalog` whose `skus()` is `["A-1", "B-2"]`, with `unit_price("A-1") == Decimal("2.50")` and `unit_price("B-2") == Decimal("0.125")`.
