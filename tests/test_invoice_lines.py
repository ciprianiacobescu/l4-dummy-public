import pytest

from billing.invoice import invoice_lines
from inventory.ledger import StockLedger


class _LedgerThatMustNotBeRead:
    """A ledger that fails loudly if the empty-list check lets a read happen."""

    def on_hand(self, sku: str) -> int:
        raise AssertionError("the ledger must not be read for an empty invoice")


@pytest.mark.l4("C-0e717055")
def test_invoice_lines_rejects_empty_items_before_reading_ledger():
    with pytest.raises(ValueError):
        invoice_lines(_LedgerThatMustNotBeRead(), [], 10)


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


@pytest.mark.l4("C-0d8e49e7")
def test_invoice_lines_rejects_total_of_one_sku_above_stock():
    ledger = StockLedger()
    ledger.receive("a", 5)
    with pytest.raises(ValueError) as caught:
        invoice_lines(ledger, [("a", 4, 100), ("a", 4, 100)], 10)
    assert "a" in str(caught.value)


@pytest.mark.l4("C-2f895644")
def test_invoice_lines_accepts_split_sku_quantities_within_stock():
    ledger = StockLedger()
    ledger.receive("a", 5)
    result = invoice_lines(ledger, [("a", 2, 100), ("a", 3, 100)], 10)
    assert result == [
        {"sku": "a", "qty": 2, "net": "2.00", "vat": "0.20", "gross": "2.20"},
        {"sku": "a", "qty": 3, "net": "3.00", "vat": "0.30", "gross": "3.30"},
    ]
