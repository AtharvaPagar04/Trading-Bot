from src.exchange.consistency_state import (
    ConsistencyState,
)


def test_consistency_state_defaults():

    state = (
        ConsistencyState()
    )

    assert (
        state.drift_detected
        is False
    )

    assert (
        state.last_reconciliation_successful
        is True
    )
