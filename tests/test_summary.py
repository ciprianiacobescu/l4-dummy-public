import pytest

from inventory.ledger import StockLedger
from inventory.summary import valuation_summary


@pytest.mark.l4("C-7214c7b7")
def test_valuation_summary_two_skus_at_ten_percent():
    ledger = StockLedger()
    ledger.receive("a", 2)
    ledger.receive("b", 3)
    assert valuation_summary(ledger, {"a": 150, "b": 200}, 10) == (
        "net 9.00 | vat 0.90 | gross 9.90"
    )


@pytest.mark.l4("C-93fbabbf")
def test_valuation_summary_nothing_on_hand():
    ledger = StockLedger()
    assert valuation_summary(ledger, {}, 10) == "net 0.00 | vat 0.00 | gross 0.00"
    ledger.receive("a", 2)
    assert valuation_summary(ledger, {"a": 150}, 10) == "net 3.00 | vat 0.30 | gross 3.30"


@pytest.mark.l4("C-f8f4d33e")
def test_valuation_summary_sku_on_hand_without_price_raises():
    ledger = StockLedger()
    ledger.receive("c", 1)
    with pytest.raises(ValueError):
        valuation_summary(ledger, {}, 10)
    assert valuation_summary(ledger, {"c": 250}, 10) == (
        "net 2.50 | vat 0.25 | gross 2.75"
    )


@pytest.mark.l4("C-ef2fe9ee")
def test_valuation_summary_currency_after_each_amount():
    ledger = StockLedger()
    ledger.receive("a", 2)
    ledger.receive("b", 3)
    assert valuation_summary(ledger, {"a": 150, "b": 200}, 10, currency="RON") == (
        "net 9.00 RON | vat 0.90 RON | gross 9.90 RON"
    )


@pytest.mark.l4("C-53560ac2")
def test_valuation_summary_without_currency_unchanged():
    ledger = StockLedger()
    ledger.receive("a", 2)
    ledger.receive("b", 3)
    assert valuation_summary(ledger, {"a": 150, "b": 200}, 10) == (
        "net 9.00 | vat 0.90 | gross 9.90"
    )
