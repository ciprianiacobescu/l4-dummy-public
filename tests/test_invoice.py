import pytest

from billing.invoice import invoice_line
from inventory.ledger import StockLedger


@pytest.mark.l4("C-47c7a274")
def test_invoice_line_three_units_amounts():
    ledger = StockLedger()
    ledger.receive("a", 5)
    result = invoice_line(ledger, "a", 3, 250, 10)
    assert result == {
        "sku": "a",
        "qty": 3,
        "net": "7.50",
        "vat": "0.75",
        "gross": "8.25",
    }


@pytest.mark.l4("C-bd29d7e5")
def test_invoice_line_vat_rounds_half_up():
    ledger = StockLedger()
    ledger.receive("a", 5)
    result = invoice_line(ledger, "a", 1, 5, 50)
    assert result == {
        "sku": "a",
        "qty": 1,
        "net": "0.05",
        "vat": "0.03",
        "gross": "0.08",
    }


@pytest.mark.l4("C-4c441964", "C-47c7a274")
def test_invoice_line_leaves_ledger_unchanged():
    ledger = StockLedger()
    ledger.receive("a", 5)
    result = invoice_line(ledger, "a", 3, 250, 10)
    assert result == {
        "sku": "a",
        "qty": 3,
        "net": "7.50",
        "vat": "0.75",
        "gross": "8.25",
    }
    assert ledger.on_hand("a") == 5
