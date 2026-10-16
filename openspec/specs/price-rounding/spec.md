# price-rounding Specification

## Purpose
Money amounts finer than a cent, rounded half up to whole cents in one agreed way for every total.

## Requirements

### Requirement: Half-up rounding to cents
`pricing.rounding.round_cents(amount: decimal.Decimal)` SHALL return the `int` number of cents nearest to `amount`
(currency units), with a tie rounded away from zero.

#### Scenario: A tie rounds up
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("0.125"))`
- **THEN** it returns exactly `13`

#### Scenario: Below a tie rounds down
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("0.124"))`
- **THEN** it returns exactly `12`

#### Scenario: A sum of fine prices
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("5.375"))`
- **THEN** it returns exactly `538`

#### Scenario: Whole cents stay
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("12.34"))`
- **THEN** it returns exactly `1234`

#### Scenario: A negative tie rounds away from zero
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("-0.125"))`
- **THEN** it returns exactly `-13`

#### Scenario: Zero
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("0"))`
- **THEN** it returns exactly `0`

#### Scenario: A negative amount below a tie
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("-0.124"))`
- **THEN** it returns exactly `-12`

#### Scenario: The context's rounding mode does not matter
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("0.125"))` inside `decimal.localcontext()` with `rounding=decimal.ROUND_DOWN`
- **THEN** it returns exactly `13`

### Requirement: Decimal amounts only
`pricing.rounding.round_cents` SHALL raise `TypeError` for an amount that is not a `decimal.Decimal` and `ValueError`
for a non-finite one.

#### Scenario: A float
- **WHEN** a total asks for `pricing.rounding.round_cents(0.125)`
- **THEN** it raises `TypeError`

#### Scenario: An int, a bool or a str
- **WHEN** a total asks for `pricing.rounding.round_cents(250)`, `pricing.rounding.round_cents(True)` or `pricing.rounding.round_cents("0.125")`
- **THEN** each raises `TypeError`

#### Scenario: Not a number
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("NaN"))` or `pricing.rounding.round_cents(Decimal("sNaN"))`
- **THEN** each raises `ValueError`

#### Scenario: Infinity
- **WHEN** a total asks for `pricing.rounding.round_cents(Decimal("Infinity"))` or `pricing.rounding.round_cents(Decimal("-Infinity"))`
- **THEN** each raises `ValueError`
