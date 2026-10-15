import pytest
from pricing.discount import (
    discounted_total,
    percent_off,
    taxed_total,
    taxed_total_text,
)


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


@pytest.mark.l4("C-cc44872e")
def test_percent_off_everything_off():
    assert percent_off(250, 100) == 250


@pytest.mark.l4("C-42af1607")
def test_discounted_total_two_lines_at_15_percent():
    assert discounted_total([100, 150], 15) == 212


@pytest.mark.l4("C-2120d6c2")
def test_discounted_total_empty_basket():
    assert discounted_total([], 15) == 0
    assert discounted_total([100], 15) == 85


@pytest.mark.l4("C-c5658d1c")
def test_discounted_total_empty_basket_rejects_percent_above_100():
    assert discounted_total([200], 25) == 150
    with pytest.raises(ValueError):
        discounted_total([], 101)


@pytest.mark.l4("C-0853868a")
def test_taxed_total_two_lines_at_15_percent_with_19_percent_vat():
    assert taxed_total([100, 150], 15, 19) == 252


@pytest.mark.l4("C-fac6bef2", "C-0853868a")
def test_taxed_total_empty_basket_and_single_line():
    assert taxed_total([], 15, 19) == 0
    assert taxed_total([100], 15, 19) == 101


@pytest.mark.l4("C-67e2f81d")
def test_taxed_total_text_two_lines_at_15_percent_with_19_percent_vat():
    assert taxed_total_text([100, 150], 15, 19) == "2.52"


@pytest.mark.l4("C-ed97191c")
def test_taxed_total_text_empty_basket():
    assert taxed_total_text([], 15, 19) == "0.00"
