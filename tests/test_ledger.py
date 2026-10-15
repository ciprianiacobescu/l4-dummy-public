import pytest

from inventory.ledger import StockLedger


@pytest.mark.l4("C-d8b024d8")
def test_receive_reports_units_on_hand():
    ledger = StockLedger()
    ledger.receive("sku-1", 5)
    assert ledger.on_hand("sku-1") == 5


@pytest.mark.l4("C-0c0ba66b")
def test_receive_then_ship_reports_remaining_on_hand():
    ledger = StockLedger()
    ledger.receive("sku-1", 5)
    ledger.ship("sku-1", 2)
    assert ledger.on_hand("sku-1") == 3


@pytest.mark.l4("C-64e536b9", "C-d8b024d8")
def test_never_received_sku_reports_zero_on_hand():
    ledger = StockLedger()
    assert ledger.on_hand("sku-x") == 0
    ledger.receive("sku-x", 4)
    assert ledger.on_hand("sku-x") == 4
