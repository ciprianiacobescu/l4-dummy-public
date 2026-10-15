import pytest


@pytest.mark.l4("C-de0b5996")
def test_low_stock_message_returns_restock_message_below_threshold():
    from inventory.alerts import low_stock_message

    result = low_stock_message("bolts", 2)
    assert result == "Restock bolts: 2 left"


@pytest.mark.l4("C-79953eae", "C-de0b5996")
def test_low_stock_message_returns_none_at_threshold():
    from inventory.alerts import low_stock_message

    # Test at threshold (5) - should return None
    result_at = low_stock_message("widgets", 5)
    assert result_at is None

    # Also test that the function actually returns messages for low values
    # This ensures the test fails on zero-value stubs (not vacuous)
    result_low = low_stock_message("widgets", 3)
    assert result_low == "Restock widgets: 3 left"


@pytest.mark.l4("C-79953eae", "C-de0b5996")
def test_low_stock_message_returns_none_above_threshold():
    from inventory.alerts import low_stock_message

    # Test above threshold (12) - should return None
    result_above = low_stock_message("gadgets", 12)
    assert result_above is None

    # Also test that the function actually returns messages for low values
    # This ensures the test fails on zero-value stubs (not vacuous)
    result_low = low_stock_message("gadgets", 4)
    assert result_low == "Restock gadgets: 4 left"


@pytest.mark.l4("C-2fec7147")
def test_low_stock_message_returns_restock_message_at_zero():
    from inventory.alerts import low_stock_message

    result = low_stock_message("bolts", 0)
    assert result == "Restock bolts: 0 left"


@pytest.mark.l4("C-ce9e7997")
def test_low_stock_message_raises_value_error_for_negative_on_hand():
    from inventory.alerts import low_stock_message

    with pytest.raises(ValueError, match="on_hand must be non-negative"):
        low_stock_message("bolts", -1)


@pytest.mark.l4("C-ce9e7997")
def test_low_stock_message_raises_value_error_for_various_negative_values():
    from inventory.alerts import low_stock_message

    # Test multiple negative values to ensure validation is robust
    with pytest.raises(ValueError, match="on_hand must be non-negative"):
        low_stock_message("widgets", -5)

    with pytest.raises(ValueError, match="on_hand must be non-negative"):
        low_stock_message("gadgets", -100)


@pytest.mark.l4("C-357020b8")
def test_low_stock_message_uses_env_threshold(monkeypatch):
    """WHEN LOW_STOCK_THRESHOLD is set THEN use its value instead of hard-coded 5."""
    from inventory.alerts import low_stock_message

    monkeypatch.setenv("LOW_STOCK_THRESHOLD", "10")

    # With threshold 10, on_hand=8 should trigger low stock
    result_low = low_stock_message("widgets", 8)
    assert result_low == "Restock widgets: 8 left"

    # With threshold 10, on_hand=10 should return None (at threshold)
    result_at = low_stock_message("widgets", 10)
    assert result_at is None

    # With threshold 10, on_hand=11 should return None (above threshold)
    result_above = low_stock_message("widgets", 11)
    assert result_above is None


@pytest.mark.l4("C-ea291e36")
def test_low_stock_message_defaults_to_5_when_env_not_set(monkeypatch):
    """WHEN LOW_STOCK_THRESHOLD is not set THEN continue to behave as before (threshold 5)."""
    from inventory.alerts import low_stock_message

    # Ensure the env var is not set
    monkeypatch.delenv("LOW_STOCK_THRESHOLD", raising=False)

    # Default threshold is 5, so on_hand=4 should trigger low stock
    result_low = low_stock_message("gadgets", 4)
    assert result_low == "Restock gadgets: 4 left"

    # At threshold 5, should return None
    result_at = low_stock_message("gadgets", 5)
    assert result_at is None

    # Above threshold 5, should return None
    result_above = low_stock_message("gadgets", 6)
    assert result_above is None
