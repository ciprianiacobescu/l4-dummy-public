import pytest

from billing.invoice import invoice_lines
from inventory.ledger import StockLedger


@pytest.mark.l4("C-c9886635")
def test_invoice_lines_all_lines_in_item_order():
    ledger = StockLedger()
    ledger.receive("a", 5)
    ledger.receive("b", 5)
    result = invoice_lines(ledger, [("a", 1, 100), ("b", 3, 50)], 10)
    assert result == [
        {"sku": "a", "qty": 1, "net": "1.00", "vat": "0.10", "gross": "1.10"},
        {"sku": "b", "qty": 3, "net": "1.50", "vat": "0.15", "gross": "1.65"},
    ]
