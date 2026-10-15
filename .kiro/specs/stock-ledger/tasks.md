# Implementation Plan

- [x] 1. Implement receiving, shipping and the count on hand
  - [x] 1.1 Create the ledger module with StockLedger.receive, ship and on_hand, and unit tests
    - _Requirements: 1.1, 1.2, 1.3_

- [ ] 2. Reject invalid movements
  - [ ] 2.1 Reject quantities below 1 and shipments above the count on hand, with unit tests
    - _Requirements: 2.1, 2.2_

- [ ] 3. List the SKUs
  - [ ] 3.1 Add StockLedger.skus returning the sorted SKUs, with a unit test
    - _Requirements: 3.1_
