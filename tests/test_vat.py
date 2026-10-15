import pytest
from pricing.vat import vat_cents


@pytest.mark.l4("C-2b4aa24a")
def test_vat_cents_rounds_half_up():
    assert vat_cents(1999, 19) == 380


@pytest.mark.l4("C-7c4f5794")
def test_vat_cents_exact_amount():
    assert vat_cents(250, 10) == 25


@pytest.mark.l4("C-a550fd63")
def test_vat_cents_rejects_negative_inputs():
    assert vat_cents(250, 10) == 25
    with pytest.raises(ValueError):
        vat_cents(100, -1)
    with pytest.raises(ValueError):
        vat_cents(-100, 19)
