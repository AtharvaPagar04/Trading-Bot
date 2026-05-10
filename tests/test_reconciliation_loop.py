from src.exchange.reconciliation_loop import (
    ReconciliationLoop,
)


def test_reconciliation_loop():

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

    loop = (
        ReconciliationLoop(
            runtime,
            exchange,
        )
    )

    drift = (
        loop.run_cycle()
    )

    assert (
        "USDT"
        in drift
    )
