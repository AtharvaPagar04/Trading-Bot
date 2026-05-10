from src.exchange.filter_validator import (
    validate_min_notional,
)


def test_validate_min_notional():

    valid = (
        validate_min_notional(
            quantity=0.01,
            price=100000,
            min_notional=10,
        )
    )

    assert (
        valid
        is True
    )
