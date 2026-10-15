# taxed-text Specification

## Purpose
The taxed total as text.

## Requirements

### Requirement: Taxed total text
`pricing.discount.taxed_total_text(amounts: list[int], percent: int, rate_percent: int)` SHALL return the `str` of
`pricing.money.from_cents(pricing.discount.taxed_total(amounts, percent, rate_percent))`; a `ValueError` SHALL be raised
unchanged.

#### Scenario: Two lines, 15 percent off, 19 percent VAT
- **WHEN** the receipt asks for `pricing.discount.taxed_total_text([100, 150], 15, 19)`
- **THEN** it returns exactly `"2.52"`

#### Scenario: An empty basket
- **WHEN** the receipt asks for `pricing.discount.taxed_total_text([], 15, 19)`
- **THEN** it returns exactly `"0.00"`
