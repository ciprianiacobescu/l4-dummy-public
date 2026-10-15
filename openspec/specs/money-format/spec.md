# money-format Specification

## Purpose
The printed form of an amount in cents.

## Requirements

### Requirement: Amount from cents
`pricing.money.from_cents(cents: int)` SHALL return the `str` amount with exactly two decimals, and a leading `-` when
`cents` is negative.

#### Scenario: Whole and fractional parts
- **WHEN** a report asks for `pricing.money.from_cents(1234)`
- **THEN** it returns exactly `12.34`

#### Scenario: A small negative amount
- **WHEN** a report asks for `pricing.money.from_cents(-5)`
- **THEN** it returns exactly `-0.05`

#### Scenario: Zero
- **WHEN** a report asks for `pricing.money.from_cents(0)`
- **THEN** it returns exactly `0.00`
