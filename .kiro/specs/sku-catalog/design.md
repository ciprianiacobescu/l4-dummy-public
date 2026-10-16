# Design Document

## Overview

A new module `src/inventory/catalog.py` with the class `SkuCatalog`, and a new fixture `sku_catalog` in the root
`conftest.py`, which exists on the base branch with only a docstring.

## Components and Interfaces

### `src/inventory/catalog.py`

**Class:** `SkuCatalog()`, an empty catalog.

- `register(sku: str, unit_price: Decimal) -> None` stores the price exactly as given. It checks, in this order: a
  `unit_price` that is not a `decimal.Decimal` raises `TypeError`; a `sku` that is empty after `strip()` raises
  `ValueError`; a `unit_price` that is negative or not finite (`NaN`, `Infinity`) raises `ValueError`; a `sku` already
  registered raises `ValueError` naming it. On any error the catalog is unchanged. `Decimal("0")` is accepted.
- `unit_price(sku: str) -> Decimal` returns the registered price; a SKU never registered raises `KeyError` whose
  message contains the SKU.
- `skus() -> list[str]` lists the registered SKUs, sorted; `[]` for a new catalog.

SKUs are compared exactly as given (no trimming, case kept). Other features read prices only through `unit_price`.

### Root `conftest.py`

**Fixture:** `sku_catalog() -> SkuCatalog`, function scope (pytest's default, so each test gets a new catalog and a
test that registers more SKUs changes only its own). It returns a new `SkuCatalog` with `A-1` registered at
`Decimal("2.50")` and `B-2` at `Decimal("0.125")`. The existing docstring stays; the fixture and its imports are
added after it.

## Testing Strategy

Unit tests in `tests/test_catalog.py`, one per acceptance criterion. The test of Requirement 4 obtains the fixture with
`request.getfixturevalue("sku_catalog")`, takes `pytest.FixtureLookupError` as "no catalog" (`None`) and then asserts
on the catalog's SKUs and prices: before the fixture exists it fails by assertion instead of erroring at setup.
