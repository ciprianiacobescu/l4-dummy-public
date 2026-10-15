# Design Document

## Overview

A new module `src/inventory/ledger.py` with the class `StockLedger`.

## Components and Interfaces

### `src/inventory/ledger.py`

**Class:** `StockLedger()`

- `receive(sku: str, qty: int) -> None` adds `qty` to the SKU; `qty` below 1 raises `ValueError`.
- `ship(sku: str, qty: int) -> None` removes `qty`; `qty` below 1, or above the count on hand, raises `ValueError` and
  changes nothing.
- `on_hand(sku: str) -> int` is the count on hand, 0 for a SKU never received.
- `skus() -> list[str]` lists every SKU ever received, sorted.

## Testing Strategy

Unit tests in `tests/test_ledger.py`, one per acceptance criterion.
