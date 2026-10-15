# Requirements Document

## Introduction

An invoice has several lines. This feature makes all the lines of an invoice at once. It depends on the Kiro spec
`invoice-line`: it calls `billing.invoice.invoice_line(ledger, sku, qty, unit_price_cents, rate_percent)`, which
returns `{"sku", "qty", "net", "vat", "gross"}` and raises `ValueError` for a bad line, and it reads
`ledger.on_hand(sku)` of `inventory.ledger.StockLedger`.

## Requirements

### Requirement 1: All Lines

**User Story:** As a billing clerk, I need every line of an invoice in the order of the items so that the invoice reads like the order.

#### Acceptance Criteria

1. WHEN the items are `[("a", 1, 100), ("b", 3, 50)]` at 10 percent and the ledger holds 5 of each, THEN the system SHALL return `[{"sku": "a", "qty": 1, "net": "1.00", "vat": "0.10", "gross": "1.10"}, {"sku": "b", "qty": 3, "net": "1.50", "vat": "0.15", "gross": "1.65"}]`.

### Requirement 2: Empty Invoice

**User Story:** As a billing clerk, I need an invoice without items rejected so that no empty invoice is sent.

#### Acceptance Criteria

1. WHEN the item list is empty, THEN the system SHALL raise `ValueError`, before reading the ledger.

### Requirement 3: Stock Across Lines

**User Story:** As a billing clerk, I need the stock checked for the whole invoice so that two lines of one SKU never bill more than we hold.

#### Acceptance Criteria

1. WHEN the items are `[("a", 4, 100), ("a", 4, 100)]` and the ledger holds 5 of `a`, THEN the system SHALL raise `ValueError` naming `a`, because 8 is above 5.

2. WHEN the items are `[("a", 2, 100), ("a", 3, 100)]` and the ledger holds 5 of `a`, THEN the system SHALL return two lines.

### Requirement 4: A Bad Line

**User Story:** As a billing clerk, I need an invoice with a bad line rejected whole so that no partial invoice is sent.

#### Acceptance Criteria

1. WHEN one item makes `invoice_line` raise `ValueError` (e.g., `("b", 0, 50)` after a good `("a", 1, 100)`), THEN the system SHALL raise that `ValueError` unchanged and return no lines.
