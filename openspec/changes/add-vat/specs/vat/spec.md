# Spec Delta

## Purpose
The VAT on a net amount.

## ADDED Requirements

### Requirement: VAT in cents
`pricing.vat.vat_cents(net_cents: int, rate_percent: int)` SHALL return the `int` VAT `net_cents * rate_percent / 100`
rounded half up, and SHALL raise `ValueError` when `net_cents` or `rate_percent` is negative.

#### Scenario: Rounded half up
- **WHEN** an invoice asks for `pricing.vat.vat_cents(1999, 19)`
- **THEN** it returns exactly `380`

#### Scenario: An exact amount
- **WHEN** an invoice asks for `pricing.vat.vat_cents(250, 10)`
- **THEN** it returns exactly `25`

#### Scenario: A negative rate is rejected
- **WHEN** an invoice asks for `pricing.vat.vat_cents(100, -1)`
- **THEN** it raises `ValueError`
