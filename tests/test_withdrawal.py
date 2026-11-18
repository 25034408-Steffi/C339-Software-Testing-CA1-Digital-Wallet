import pytest
from src.wallet_withdrawal import withdraw

@pytest.mark.parametrize(("balance_cents", "amount_cents", "expected"), [
    (1000, 700, 300),
    (1000, 1000, 0)
])

def test_valid_withdrawal_returns_remaining_balance(balance_cents, amount_cents, expected):
    assert withdraw(balance_cents, amount_cents) == expected


@pytest.mark.parametrize(("balance_cents", "amount_cents"), [
    (500, 0), # Zero withdrawal
    (1000, 1200), # Withdrawal exceeds balanace
    (500, -100), # Negative withdrawal
    (-500, 100)  # Negative balance
])

def test_invalid_withdrawal_raises_error(balance_cents, amount_cents):
    with pytest.raises(ValueError):
            withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(("balance_cents", "amount_cents"), [
    (1000, 600.0),
    (1000, "600"),
    (1000, None),
    (1000, True)
])

def test_unsupported_withdraw_amt_type_raises_error(balance_cents, amount_cents):
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(("balance_cents", "amount_cents"), [
    (600.0, 500),
    ("600", 500),
    (None, 500),
    (True, 500)
])

def test_unsupported_balance_amt_type_raises_error(balance_cents, amount_cents):
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)
