# Implementation Plan

- [ ] 1. Implement the order total
  - [x] 1.1 Add order_total_cents summing qty times unit_price exactly and rounding the sum once with round_cents, with unit tests using the sku_catalog fixture
    - _Requirements: 1.1, 1.2, 1.3_
  - [ ] 1.2 Return 0 for an empty order without calling the catalog, with a unit test
    - _Requirements: 2.1_

- [ ] 2. Reject bad orders
  - [ ] 2.1 Check every quantity before calling the catalog: TypeError for a non-int or bool, ValueError below 1, each naming the SKU, with unit tests
    - _Requirements: 3.1, 3.2_
  - [ ] 2.2 Let the KeyError of unit_price for an unknown SKU through unchanged, with a unit test
    - _Requirements: 4.1_
