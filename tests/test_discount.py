import pytest
from pricing.discount import percent_off


@pytest.mark.l4("C-424b9938")
def test_percent_off_rounds_half_up():
    assert percent_off(250, 15) == 38


@pytest.mark.l4("C-c79fb63b")
def test_percent_off_nothing_off():
    assert percent_off(250, 0) == 0
    assert percent_off(200, 25) == 50


@pytest.mark.l4("C-04d600ea")
def test_percent_off_rejects_percent_above_100():
    with pytest.raises(ValueError):
        percent_off(100, 101)
