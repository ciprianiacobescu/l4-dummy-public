# Requirements Document

## Introduction

An invoice line shows the quantity, net, VAT and gross amount of one SKU. It depends on three other specs: it checks
the stock with `inventory.ledger.StockLedger` (Kiro spec `stock-ledger`), computes VAT with `pricing.vat.vat_cents`
(OpenSpec change `add-vat`, half-up rounding) and formats amounts with `pricing.money.from_cents` (OpenSpec change
`add-money-format`).

## Requirements

### Requirement 1: Line Amounts

**User Story:** As a billing clerk, I need one line per SKU with its amounts so that the invoice is clear.

#### Acceptance Criteria

1. WHEN 3 units of `a` at 250 cents are invoiced at 10 percent and the ledger holds 5 of `a`, THEN the system SHALL return `{"sku": "a", "qty": 3, "net": "7.50", "vat": "0.75", "gross": "8.25"}`.

2. WHEN 1 unit of `a` at 5 cents is invoiced at 50 percent and the ledger holds 5 of `a`, THEN the system SHALL return `{"sku": "a", "qty": 1, "net": "0.05", "vat": "0.03", "gross": "0.08"}` (the VAT of 2.5 cents rounds half up).

3. WHEN a line is made, THEN the system SHALL leave the ledger's count on hand unchanged.

### Requirement 2: Stock Check

**User Story:** As a billing clerk, I need lines for goods we do not hold rejected so that we never bill missing stock.

#### Acceptance Criteria

1. WHEN the quantity is above the ledger's count on hand (e.g., 6 of `a` with 5 on hand), THEN the system SHALL raise `ValueError`.

2. WHEN the quantity equals the count on hand (5 of `a` with 5 on hand), THEN the system SHALL return the line.

3. WHEN the SKU was never received (`on_hand` is 0), THEN the system SHALL raise `ValueError`.

### Requirement 3: Input Check

**User Story:** As a billing clerk, I need impossible lines rejected so that no line bills nothing or a negative amount.

#### Acceptance Criteria

1. WHEN the quantity is below 1 (e.g., 0 or -1), THEN the system SHALL raise `ValueError`, before the stock check.

2. WHEN `unit_price_cents` is below 0, THEN the system SHALL raise `ValueError`, before the stock check.

3. WHEN `rate_percent` is below 0, THEN the system SHALL raise the `ValueError` of `pricing.vat.vat_cents` unchanged.
