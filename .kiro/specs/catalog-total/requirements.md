# Requirements Document

## Introduction

An order lists SKUs with a quantity. This feature computes the order total in whole cents from the catalog prices. It
depends on two units:

- the Kiro spec `sku-catalog`: `inventory.catalog.SkuCatalog.unit_price(sku: str) -> Decimal`, which raises `KeyError`
  (its message contains the SKU) for a SKU never registered, and the pytest fixture `sku_catalog` of the root
  `conftest.py`, a new `SkuCatalog` with `A-1` at `Decimal("2.50")` and `B-2` at `Decimal("0.125")`;
- the OpenSpec change `add-price-rounding`: `pricing.rounding.round_cents(amount: Decimal) -> int`, whole cents with a
  tie rounded away from zero.

The total is `round_cents` of the exact sum of `qty * unit_price(sku)` over the items: it is rounded once, never per
item. In the criteria below, "the sample catalog" is the catalog of the `sku_catalog` fixture.

## Requirements

### Requirement 1: Order Total

**User Story:** As a till clerk, I need the total of an order in cents so that the customer pays the right amount.

#### Acceptance Criteria

1. WHEN the items are `[("A-1", 2), ("B-2", 3)]` with the sample catalog, THEN the system SHALL return `538` (the sum `5.375` rounded half up).

2. WHEN the items are `[("B-2", 1), ("B-2", 1)]` with the sample catalog, THEN the system SHALL return `25` (the sum `0.250`, rounded once; rounding each item would give `26`).

3. WHEN the items are `[("A-1", 1)]` with the sample catalog, THEN the system SHALL return `250`.

### Requirement 2: Empty Order

**User Story:** As a till clerk, I need an empty order to total zero so that an empty basket costs nothing.

#### Acceptance Criteria

1. WHEN the item list is `[]`, THEN the system SHALL return `0` without calling the catalog.

### Requirement 3: Bad Quantities

**User Story:** As a till clerk, I need wrong quantities rejected before any price is read so that no partial total is made.

#### Acceptance Criteria

1. WHEN an item's quantity is below 1 (e.g., `[("A-1", 1), ("B-2", 0)]` or `[("A-1", 1), ("B-2", -1)]`), THEN the system SHALL raise `ValueError` naming `B-2`, without calling the catalog.

2. WHEN an item's quantity is not an `int` or is a `bool` (e.g., `[("A-1", 1.5)]` or `[("A-1", True)]`), THEN the system SHALL raise `TypeError` naming `A-1`, without calling the catalog.

### Requirement 4: Unknown SKU

**User Story:** As a till clerk, I need an order with a SKU that is not in the catalog rejected so that no price is guessed.

#### Acceptance Criteria

1. WHEN the items are `[("A-1", 1), ("Z-9", 1)]` with the sample catalog, THEN the system SHALL raise the `KeyError` of `unit_price` unchanged (its message contains `Z-9`) and return no total.
