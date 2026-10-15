# Design Document

## Overview

A new module `src/billing/invoice.py` (with `src/billing/__init__.py`) with one function.

## Components and Interfaces

### `src/billing/invoice.py`

**Function:** `invoice_line(ledger: StockLedger, sku: str, qty: int, unit_price_cents: int, rate_percent: int) -> dict`

- The checks run in this order, each raising `ValueError`: `qty` below 1; `unit_price_cents` below 0; `qty` above
  `ledger.on_hand(sku)` (0 for a SKU never received). Then `net` is `qty * unit_price_cents`, `vat` is
  `pricing.vat.vat_cents(net, rate_percent)` (its `ValueError` for a negative rate is raised unchanged), `gross` is
  `net + vat`.
- The result is a `dict` with exactly the keys `sku`, `qty`, `net`, `vat`, `gross`: `sku` and `qty` as given, the three
  amounts as the `str` that `pricing.money.from_cents` returns.
- It only reads the ledger (`on_hand`); it never changes it.

## Testing Strategy

Unit tests in `tests/test_invoice.py`, one per acceptance criterion.
