from src.exchange.event_reconciliation import (
    requires_reconciliation,
)


def test_requires_reconciliation():

    event = {
        "requires_reconciliation":
        True
    }

    assert (
        requires_reconciliation(
            event
        )
        is True
    )
