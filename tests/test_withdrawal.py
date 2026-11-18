import pytest
from src.wallet_withdrawal import withdraw

@pytest.mark.parametrize(("balance_cents", "amount_cents", "expected"), [
    pytest.param(1000, 700, 300, id="amount_below_balance"),
    pytest.param(1000, 1000, 0, id="amount_equals_balance"),
])

def test_valid_withdrawal_returns_remaining_balance(balance_cents, amount_cents, expected):
    assert withdraw(balance_cents, amount_cents) == expected


@pytest.mark.parametrize(("balance_cents", "amount_cents"), [
    pytest.param(500, 0, id="zero_amount"), # Zero withdrawal
    pytest.param(1000, 1200, id="amount_exceeds_balance"), # Withdrawal exceeds balanace
    pytest.param(500, -100, id="negative_amount"), # Negative withdrawal
    pytest.param(-500, 100, id="negative_balance"), # Negative balance
])

def test_invalid_withdrawal_raises_error(balance_cents, amount_cents):
    with pytest.raises(ValueError):
            withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(("balance_cents", "amount_cents"), [
    pytest.param(1000, 600.0, id="float"),
    pytest.param(1000, "600", id="numeric_string"),
    pytest.param(1000, None, id="none"),
    pytest.param(1000, True, id="bool"),
])

def test_unsupported_withdraw_amt_type_raises_error(balance_cents, amount_cents):
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(("balance_cents", "amount_cents"), [
    pytest.param(600.0, 500, id="float"),
    pytest.param("600", 500, id="numeric_string"),
    pytest.param(None, 500, id="none"),
    pytest.param(True, 500, id="bool"),
])

def test_unsupported_balance_amt_type_raises_error(balance_cents, amount_cents):
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)
