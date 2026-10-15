import pytest

from inventory.ledger import StockLedger
from inventory.valuation import stock_value


@pytest.mark.l4("C-4ab2ef17")
def test_stock_value_two_skus_at_ten_percent():
    ledger = StockLedger()
    ledger.receive("a", 2)
    ledger.receive("b", 3)
    assert stock_value(ledger, {"a": 150, "b": 200}, 10) == {
        "net": "9.00",
        "vat": "0.90",
        "gross": "9.90",
    }


@pytest.mark.l4("C-0151315f")
def test_stock_value_nothing_on_hand():
    ledger = StockLedger()
    assert stock_value(ledger, {}, 10) == {
        "net": "0.00",
        "vat": "0.00",
        "gross": "0.00",
    }
    ledger.receive("a", 2)
    assert stock_value(ledger, {"a": 150}, 10) == {
        "net": "3.00",
        "vat": "0.30",
        "gross": "3.30",
    }


@pytest.mark.l4("C-3b801c40")
def test_stock_value_sku_on_hand_without_price_raises():
    ledger = StockLedger()
    ledger.receive("c", 1)
    with pytest.raises(ValueError) as excinfo:
        stock_value(ledger, {}, 10)
    assert "c" in str(excinfo.value)
    assert stock_value(ledger, {"c": 250}, 10) == {
        "net": "2.50",
        "vat": "0.25",
        "gross": "2.75",
    }


@pytest.mark.l4("C-b333d8d8")
def test_stock_value_skipped_sku_without_price():
    ledger = StockLedger()
    ledger.receive("a", 2)
    ledger.receive("c", 1)
    ledger.ship("c", 1)
    assert stock_value(ledger, {"a": 150}, 10) == {
        "net": "3.00",
        "vat": "0.30",
        "gross": "3.30",
    }
