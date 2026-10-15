import pytest
from pricing.money import from_cents, to_cents


def test_to_cents():
    assert to_cents("12.34") == 1234
    assert to_cents("-0.05") == -5


def test_to_cents_rejects_a_missing_fraction():
    with pytest.raises(ValueError):
        to_cents("12")


@pytest.mark.l4("C-81dc0f07")
def test_from_cents_whole_and_fractional_parts():
    assert from_cents(1234) == "12.34"


@pytest.mark.l4("C-23b9bbc0")
def test_from_cents_small_negative_amount():
    assert from_cents(-5) == "-0.05"


@pytest.mark.l4("C-f6b8aea8")
def test_from_cents_zero():
    assert from_cents(0) == "0.00"
