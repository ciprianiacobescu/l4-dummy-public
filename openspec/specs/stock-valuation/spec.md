# stock-valuation Specification

## Purpose
The value of the stock on hand.

## Requirements

### Requirement: Stock value
`inventory.valuation.stock_value(ledger, price_cents: dict[str, int], rate_percent: int)` SHALL return a `dict` with the
keys `net`, `vat` and `gross`: `net` is the sum of `ledger.on_hand(sku) * price_cents[sku]` over the SKUs of
`ledger.skus()` whose `ledger.on_hand(sku)` is above 0, `vat` is `pricing.vat.vat_cents(net, rate_percent)`, `gross` is
`net + vat`, each as the `str` of `pricing.money.from_cents`.

#### Scenario: Two SKUs at 10 percent
- **GIVEN** a `StockLedger` that received 2 of `a` and 3 of `b`, prices `{"a": 150, "b": 200}`
- **WHEN** finance asks for `stock_value(ledger, prices, 10)`
- **THEN** it returns `{"net": "9.00", "vat": "0.90", "gross": "9.90"}`

#### Scenario: Nothing on hand
- **GIVEN** an empty `StockLedger`, prices `{}`
- **WHEN** finance asks for `stock_value(ledger, {}, 10)`
- **THEN** it returns `{"net": "0.00", "vat": "0.00", "gross": "0.00"}`

### Requirement: Missing prices
`stock_value` SHALL raise `ValueError`, naming the SKU, when a SKU with stock on hand has no price, and never
`KeyError`. A SKU whose count on hand is 0 SHALL be skipped without a price lookup. A `ValueError` of
`pricing.vat.vat_cents` (a negative rate) SHALL be raised unchanged.

#### Scenario: A SKU without a price
- **GIVEN** a `StockLedger` that received 1 of `c`, prices `{}`
- **WHEN** finance asks for `stock_value(ledger, {}, 10)`
- **THEN** it raises `ValueError`

#### Scenario: A SKU shipped out has no price
- **GIVEN** a `StockLedger` that received 2 of `a`, received 1 of `c` and shipped 1 of `c`, prices `{"a": 150}`
- **WHEN** finance asks for `stock_value(ledger, prices, 10)`
- **THEN** it returns `{"net": "3.00", "vat": "0.30", "gross": "3.30"}`
