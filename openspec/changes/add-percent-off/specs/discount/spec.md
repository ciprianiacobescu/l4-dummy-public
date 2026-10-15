# Spec Delta

## Purpose
The discount on an amount.

## ADDED Requirements

### Requirement: Percent off in cents
`pricing.discount.percent_off(cents: int, percent: int)` SHALL return the `int` discount `cents * percent / 100` rounded
half up, and SHALL raise `ValueError` when `cents` is negative or `percent` is below 0 or above 100.

#### Scenario: Rounded half up
- **WHEN** a promotion asks for `pricing.discount.percent_off(250, 15)`
- **THEN** it returns exactly `38`

#### Scenario: Nothing off
- **WHEN** a promotion asks for `pricing.discount.percent_off(250, 0)`
- **THEN** it returns exactly `0`

#### Scenario: A percent above 100 is rejected
- **WHEN** a promotion asks for `pricing.discount.percent_off(100, 101)`
- **THEN** it raises `ValueError`
