# Spec Delta

## Purpose
The total after a percentage off.

## ADDED Requirements

### Requirement: Discounted total
`pricing.discount.discounted_total(amounts: list[int], percent: int)` SHALL return the `int`
`sum(amounts) - pricing.discount.percent_off(sum(amounts), percent)`; an empty list SHALL give `0`, and a `ValueError`
of `percent_off` SHALL be raised unchanged.

#### Scenario: Two lines at 15 percent
- **WHEN** a basket asks for `pricing.discount.discounted_total([100, 150], 15)`
- **THEN** it returns exactly `212`

#### Scenario: An empty basket
- **WHEN** a basket asks for `pricing.discount.discounted_total([], 15)`
- **THEN** it returns exactly `0`
