# Implementation Plan

## 1. Catalog module `src/inventory/catalog.py`

- [ ] 1. Implement the SKU catalog
  - [x] 1.1 Add SkuCatalog with register, unit_price and skus, with unit tests
    - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - [x] 1.2 Reject negative or non-finite prices, a SKU registered twice, a blank SKU and a price that is not a Decimal, leaving the catalog unchanged, with unit tests
    - _Requirements: 2.1, 2.2, 2.3, 2.4_
  - [ ] 1.3 Raise KeyError naming a SKU that was never registered, with a unit test
    - _Requirements: 3.1_

## 2. Root `conftest.py`

- [ ] 2. Share a sample catalog with every test
  - [ ] 2.1 Add the function-scoped fixture sku_catalog returning a new SkuCatalog with A-1 at Decimal("2.50") and B-2 at Decimal("0.125"), with a unit test that obtains it by name
    - _Requirements: 4.1_
