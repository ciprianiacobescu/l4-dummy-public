# Design Document

## Overview

A new module `src/billing/order.py` with one function. It reads prices only through `SkuCatalog.unit_price` (Kiro
spec `sku-catalog`) and rounds only through `pricing.rounding.round_cents` (OpenSpec change `add-price-rounding`).

## Components and Interfaces

### `src/billing/order.py`

**Function:** `order_total_cents(catalog: SkuCatalog, items: list[tuple[str, int]]) -> int`

- `items` is a `list` of `(sku, qty)` tuples, in any order; a SKU may appear more than once.
- First every quantity is checked, in the order of `items`, before the catalog is called: a `qty` that is not an `int`,
  or is a `bool`, raises `TypeError` naming the SKU; a `qty` below 1 raises `ValueError` naming the SKU.
- Then it sums `qty * catalog.unit_price(sku)` as an exact `Decimal` (starting from `Decimal("0")`) and returns
  `round_cents(total)`. A `KeyError` of `unit_price` is raised unchanged.
- An empty `items` returns `0` without calling the catalog.
- It never changes the catalog.

## Testing Strategy

Unit tests in `tests/test_order.py`, one per acceptance criterion. They take the shared fixture `sku_catalog` as a
parameter for the sample catalog. The "without calling the catalog" criteria use a small catalog object whose
`unit_price` raises `AssertionError`.
