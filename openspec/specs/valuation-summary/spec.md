# valuation-summary Specification

## Purpose
The one-line stock value of the daily mail.

## Requirements

### Requirement: One-line summary
`inventory.summary.valuation_summary(ledger, price_cents: dict[str, int], rate_percent: int)` SHALL return the `str`
`net <net> | vat <vat> | gross <gross>`, with the three amounts of `inventory.valuation.stock_value` for the same
arguments. A `ValueError` of `stock_value` (a SKU on hand without a price, a negative rate) SHALL be raised unchanged:
`valuation_summary` catches nothing and adds no check of its own.

#### Scenario: Two SKUs at 10 percent
- **GIVEN** a `StockLedger` that received 2 of `a` and 3 of `b`, prices `{"a": 150, "b": 200}`
- **WHEN** the daily mail asks for `valuation_summary(ledger, prices, 10)`
- **THEN** it returns exactly `net 9.00 | vat 0.90 | gross 9.90`

#### Scenario: Nothing on hand
- **GIVEN** an empty `StockLedger`, prices `{}`
- **WHEN** the daily mail asks for `valuation_summary(ledger, {}, 10)`
- **THEN** it returns exactly `net 0.00 | vat 0.00 | gross 0.00`

#### Scenario: A SKU on hand without a price
- **GIVEN** a `StockLedger` that received 1 of `c`, prices `{}`
- **WHEN** the daily mail asks for `valuation_summary(ledger, {}, 10)`
- **THEN** it raises `ValueError`
