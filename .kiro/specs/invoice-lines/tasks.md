# Implementation Plan

- [x] 1. Implement all the lines of an invoice
  - [x] 1.1 Add invoice_lines calling invoice_line for each item in order, with a unit test
    - _Requirements: 1.1_

- [x] 2. Reject an empty invoice
  - [x] 2.1 Raise ValueError for an empty item list before reading the ledger, with a unit test
    - _Requirements: 2.1_

- [x] 3. Check the stock across lines
  - [x] 3.1 Sum the quantities per SKU and raise ValueError naming a SKU whose sum is above its count on hand, with unit tests
    - _Requirements: 3.1, 3.2_

- [ ] 4. Reject a bad line
  - [ ] 4.1 Let a ValueError of invoice_line through with no partial result, with a unit test
    - _Requirements: 4.1_
