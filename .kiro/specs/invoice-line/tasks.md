# Implementation Plan

- [ ] 1. Implement the invoice line
  - [ ] 1.1 Create the billing package and the invoice module with invoice_line returning sku, qty, net, vat and gross, and unit tests
    - _Requirements: 1.1, 1.2, 1.3_

- [ ] 2. Check the stock
  - [ ] 2.1 Reject a quantity above the count on hand, accept one equal to it, reject a SKU never received, with unit tests
    - _Requirements: 2.1, 2.2, 2.3_

- [ ] 3. Check the input
  - [ ] 3.1 Reject a quantity below 1 and a negative price before the stock check, and let the VAT error of a negative rate through, with unit tests
    - _Requirements: 3.1, 3.2, 3.3_
