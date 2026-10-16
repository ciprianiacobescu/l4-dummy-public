from decimal import ROUND_DOWN, Decimal, localcontext

import pytest

from pricing.rounding import round_cents


@pytest.mark.l4("C-ca83ff85")
def test_tie_rounds_up():
    assert round_cents(Decimal("0.125")) == 13


@pytest.mark.l4("C-d01b956c")
def test_below_a_tie_rounds_down():
    assert round_cents(Decimal("0.124")) == 12


@pytest.mark.l4("C-7f99705c")
def test_sum_of_fine_prices():
    assert round_cents(Decimal("5.375")) == 538


@pytest.mark.l4("C-2c898feb")
def test_whole_cents_stay():
    assert round_cents(Decimal("12.34")) == 1234


@pytest.mark.l4("C-f0177631")
def test_negative_tie_rounds_away_from_zero():
    assert round_cents(Decimal("-0.125")) == -13


@pytest.mark.l4("C-544c4d18", "C-ca83ff85")
def test_zero():
    assert round_cents(Decimal("0")) == 0
    assert round_cents(Decimal("0.125")) == 13


@pytest.mark.l4("C-4337d0d3")
def test_negative_amount_below_a_tie():
    assert round_cents(Decimal("-0.124")) == -12


@pytest.mark.l4("C-acdaa231")
def test_context_rounding_mode_does_not_matter():
    with localcontext() as context:
        context.rounding = ROUND_DOWN
        assert round_cents(Decimal("0.125")) == 13


@pytest.mark.l4("C-e03de5d9")
def test_float_raises_type_error():
    assert round_cents(Decimal("0.125")) == 13
    with pytest.raises(TypeError):
        round_cents(0.125)


@pytest.mark.l4("C-67550744")
def test_int_bool_str_raise_type_error():
    assert round_cents(Decimal("2.50")) == 250
    with pytest.raises(TypeError):
        round_cents(250)
    with pytest.raises(TypeError):
        round_cents(True)
    with pytest.raises(TypeError):
        round_cents("0.125")


@pytest.mark.l4("C-5948ccfa")
def test_nan_raises_value_error():
    assert round_cents(Decimal("1.00")) == 100
    with pytest.raises(ValueError):
        round_cents(Decimal("NaN"))
    with pytest.raises(ValueError):
        round_cents(Decimal("sNaN"))


@pytest.mark.l4("C-89184fc1")
def test_infinity_raises_value_error():
    assert round_cents(Decimal("1.00")) == 100
    with pytest.raises(ValueError):
        round_cents(Decimal("Infinity"))
    with pytest.raises(ValueError):
        round_cents(Decimal("-Infinity"))


@pytest.mark.l4("C-e03de5d9")
def test_float_amount_is_rejected_with_type_error():
    assert round_cents(Decimal("0.125")) == 13
    with pytest.raises(TypeError):
        round_cents(0.125)


@pytest.mark.l4("C-67550744")
def test_int_bool_str_amounts_are_rejected_with_type_error():
    assert round_cents(Decimal("12.34")) == 1234
    with pytest.raises(TypeError):
        round_cents(250)
    with pytest.raises(TypeError):
        round_cents(True)
    with pytest.raises(TypeError):
        round_cents("0.125")


@pytest.mark.l4("C-5948ccfa")
def test_nan_amounts_are_rejected_with_value_error():
    assert round_cents(Decimal("2.50")) == 250
    with pytest.raises(ValueError):
        round_cents(Decimal("NaN"))
    with pytest.raises(ValueError):
        round_cents(Decimal("sNaN"))


@pytest.mark.l4("C-89184fc1")
def test_infinite_amounts_are_rejected_with_value_error():
    assert round_cents(Decimal("2.50")) == 250
    with pytest.raises(ValueError):
        round_cents(Decimal("Infinity"))
    with pytest.raises(ValueError):
        round_cents(Decimal("-Infinity"))
