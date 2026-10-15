# Proposal: stock valuation

## Why
Finance needs the value of the stock on hand, net, VAT and gross.

## What Changes
- Add `inventory.valuation.stock_value(ledger, price_cents, rate_percent)`. For every SKU of the ledger it multiplies
  `ledger.on_hand(sku)` by `price_cents[sku]` and sums the products into the net amount. It adds VAT on the net amount
  with `pricing.vat.vat_cents`. It returns `{"net": ..., "vat": ..., "gross": ...}`, each formatted with
  `pricing.money.from_cents`. A SKU with stock but no price raises `ValueError`.

## Capabilities

### New Capabilities
- `stock-valuation`: the value of the stock on hand.

### Modified Capabilities

## Impact
`src/inventory/valuation.py` (new), tests under `tests/`. It depends on three other changes: it reads the count on
hand from `inventory.ledger.StockLedger` (Kiro spec `stock-ledger`), computes VAT with `pricing.vat.vat_cents` (change
`add-vat`) and formats with `pricing.money.from_cents` (change `add-money-format`).
