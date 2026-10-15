# Spec Delta

## Purpose
The currency in the one-line stock value.

## ADDED Requirements

### Requirement: Currency in the summary
`inventory.summary.valuation_summary(ledger, price_cents, rate_percent, currency: str | None = None)` SHALL put a space
and `currency` after each of the three amounts when `currency` is given, and SHALL return the summary unchanged when it
is not.

#### Scenario: A currency
- **GIVEN** a `StockLedger` that received 2 of `a` and 3 of `b`, prices `{"a": 150, "b": 200}`
- **WHEN** the daily mail asks for `valuation_summary(ledger, prices, 10, currency="RON")`
- **THEN** it returns exactly `net 9.00 RON | vat 0.90 RON | gross 9.90 RON`

#### Scenario: No currency
- **GIVEN** the same ledger and prices
- **WHEN** the daily mail asks for `valuation_summary(ledger, prices, 10)`
- **THEN** it returns exactly `net 9.00 | vat 0.90 | gross 9.90`, as before
