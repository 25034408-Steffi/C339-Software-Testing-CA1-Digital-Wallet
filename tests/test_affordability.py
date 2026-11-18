import pytest
from src.wallet_affordability import can_afford


@pytest.mark.parametrize(("balance_cents", "price_cents", "expected"), [
    (1000, 700, True),
    (1000, 1000, True),
    (1000, 1200, False),
    (500, 0, True),
    (0, 0, True)
])
def test_valid_purchase_returns_expected(balance_cents, price_cents, expected):
    assert can_afford(balance_cents, price_cents) is expected

@pytest.mark.parametrize(("balance_cents", "price_cents"), [
    (500, -100), # Negative purchase price
    (-500, 200) # Negative balance
])

def test_invalid_purchase_raises_error(balance_cents, price_cents):
    with pytest.raises(ValueError):
        can_afford(balance_cents, price_cents)

@pytest.mark.parametrize(("balance_cents", "price_cents"), [
    (1000, 600.0), 
    (1000, "600"),
    (1000, None), 
    (1000, True)
])

def test_unsupported_purchase_price_type_raises_error(balance_cents, price_cents):
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)


@pytest.mark.parametrize(("balance_cents", "price_cents"), [
    (600.0, 500), 
    ("600", 500),
    (None, 500), 
    (True, 500)
])
def test_unsupported_balance_amt_type_raises_error(balance_cents, price_cents):
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)