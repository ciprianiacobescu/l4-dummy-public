# Tasks

## 1. Half-up rounding

- [ ] 1.1 Add `pricing.rounding.round_cents(amount)` returning whole cents with ties away from zero (`decimal.ROUND_HALF_UP`)

## 2. Bad amounts

- [ ] 2.1 Raise `TypeError` from `round_cents` for an amount that is not a `decimal.Decimal`
- [ ] 2.2 Raise `ValueError` from `round_cents` for a non-finite `decimal.Decimal` (`NaN`, `Infinity`)
