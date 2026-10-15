# Design Document

## Overview

A new function in `src/billing/invoice.py`, next to `invoice_line`.

## Components and Interfaces

### `src/billing/invoice.py`

**Function:** `invoice_lines(ledger: StockLedger, items: list[tuple[str, int, int]], rate_percent: int) -> list[dict]`

- `items` is a `list` of `(sku, qty, unit_price_cents)` tuples. An empty list raises `ValueError` before the ledger is
  read.
- Before any line is made, the quantities of each SKU are summed over all items; a sum above `ledger.on_hand(sku)`
  raises `ValueError` naming the SKU.
- Then it returns `[invoice_line(ledger, sku, qty, price, rate_percent) for each item]`, in the order of `items`, as a
  `list`. A `ValueError` of `invoice_line` is raised unchanged and no list is returned.
- It never changes the ledger.

## Testing Strategy

Unit tests in `tests/test_invoice_lines.py`, one per acceptance criterion.
