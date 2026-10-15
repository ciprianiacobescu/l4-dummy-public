# Requirements Document

## Introduction

The warehouse records stock movements per SKU. This feature adds an in-memory stock ledger. It depends on no other
spec.

## Requirements

### Requirement 1: Receive and Ship

**User Story:** As a stock clerk, I need to record goods received and shipped so that the count on hand is right.

#### Acceptance Criteria

1. WHEN 5 units of `sku-1` are received into a new ledger, THEN the system SHALL report 5 on hand for `sku-1`.

2. WHEN 5 units of `sku-1` are received and 2 are shipped, THEN the system SHALL report 3 on hand for `sku-1`.

3. WHEN a SKU was never received, THEN the system SHALL report 0 on hand for it.

### Requirement 2: Invalid Movements

**User Story:** As a stock clerk, I need impossible movements rejected so that the count never goes wrong.

#### Acceptance Criteria

1. WHEN a quantity below 1 is received or shipped, THEN the system SHALL raise `ValueError`.

2. WHEN more units are shipped than are on hand (e.g., 4 shipped with 3 on hand), THEN the system SHALL raise `ValueError` and the count SHALL stay 3.

### Requirement 3: Listing

**User Story:** As a stock clerk, I need the SKUs of the ledger so that reports can walk them.

#### Acceptance Criteria

1. WHEN `sku-b` and then `sku-a` are received, THEN the system SHALL list the SKUs as `["sku-a", "sku-b"]` (sorted).
