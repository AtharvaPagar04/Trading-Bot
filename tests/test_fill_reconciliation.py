from src.exchange.fill_reconciliation import (
    reconcile_fill_event,
)


def test_fill_reconciliation():

    event = {
        "symbol": "BTCUSDT",
        "order_status": "FILLED",
        "execution_type": "TRADE",
    }

    result = (
        reconcile_fill_event(
            event
        )
    )

    assert (
        result["status"]
        ==
        "FILLED"
    )
