# discounted-total Specification

## Purpose
The total after a percentage off.

## Requirements

### Requirement: Discounted total
`pricing.discount.discounted_total(amounts: list[int], percent: int)` SHALL return the `int`
`sum(amounts) - pricing.discount.percent_off(sum(amounts), percent)`, always calling `percent_off`, so a `ValueError` of
`percent_off` SHALL be raised unchanged even for an empty list; an empty list with a valid percent SHALL give `0`.

#### Scenario: Two lines at 15 percent
- **WHEN** a basket asks for `pricing.discount.discounted_total([100, 150], 15)`
- **THEN** it returns exactly `212`

#### Scenario: An empty basket
- **WHEN** a basket asks for `pricing.discount.discounted_total([], 15)`
- **THEN** it returns exactly `0`

#### Scenario: An empty basket with a percent above 100
- **WHEN** a basket asks for `pricing.discount.discounted_total([], 101)`
- **THEN** it raises `ValueError`
