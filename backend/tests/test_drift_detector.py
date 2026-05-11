from src.exchange.drift_detector import (
    detect_balance_drift,
)


def test_detect_balance_drift():

    runtime = {
        "USDT": {
            "total": 1000,
        }
    }

    exchange = {
        "USDT": {
            "total": 900,
        }
    }

    drift = (
        detect_balance_drift(
            runtime,
            exchange,
        )
    )

    assert (
        "USDT"
        in drift
    )

    assert (
        drift["USDT"]["difference"]
        ==
        100
    )
