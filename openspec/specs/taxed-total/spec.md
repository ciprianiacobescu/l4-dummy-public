# taxed-total Specification

## Purpose
The basket total with VAT.

## Requirements

### Requirement: Taxed total
`pricing.discount.taxed_total(amounts: list[int], percent: int, rate_percent: int)` SHALL return the `int`
`net + pricing.vat.vat_cents(net, rate_percent)` with `net = pricing.discount.discounted_total(amounts, percent)`; a
`ValueError` of either SHALL be raised unchanged.

#### Scenario: Two lines, 15 percent off, 19 percent VAT
- **WHEN** the till asks for `pricing.discount.taxed_total([100, 150], 15, 19)`
- **THEN** it returns exactly `252` (net `212`, VAT `40`)

#### Scenario: An empty basket
- **WHEN** the till asks for `pricing.discount.taxed_total([], 15, 19)`
- **THEN** it returns exactly `0`
