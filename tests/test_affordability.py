import pytest
from src.wallet_affordability import can_afford


@pytest.mark.parametrize(("balance_cents", "price_cents", "expected"), [
    pytest.param(1000, 700, True, id="price_below_balance"),
    pytest.param(1000, 1000, True, id="price_equals_balance"),
    pytest.param(1000, 1200, False, id="price_exceeds_balance"),
    pytest.param(500, 0, True, id="zero_price_positive_balance"),
    pytest.param(0, 0, True, id="zero_price_zero_balance"),
])
def test_valid_purchase_returns_expected(balance_cents, price_cents, expected):
    assert can_afford(balance_cents, price_cents) is expected

@pytest.mark.parametrize(("balance_cents", "price_cents"), [
    pytest.param(500, -100, id="negative_price"),
    pytest.param(-500, 200, id="negative_balance"),
])

def test_invalid_purchase_raises_error(balance_cents, price_cents):
    with pytest.raises(ValueError):
        can_afford(balance_cents, price_cents)

@pytest.mark.parametrize(("balance_cents", "price_cents"), [
    pytest.param(1000, 600.0, id="float"),
    pytest.param(1000, "600", id="numeric_string"),
    pytest.param(1000, None, id="none"),
    pytest.param(1000, True, id="bool"),
])

def test_unsupported_purchase_price_type_raises_error(balance_cents, price_cents):
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)


@pytest.mark.parametrize(("balance_cents", "price_cents"), [
    pytest.param(600.0, 500, id="float"),
    pytest.param("600", 500, id="numeric_string"),
    pytest.param(None, 500, id="none"),
    pytest.param(True, 500, id="bool"),
])
def test_unsupported_balance_amt_type_raises_error(balance_cents, price_cents):
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)
        