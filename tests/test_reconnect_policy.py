from src.exchange.reconnect_policy import (
    should_reconnect,
)

from src.exchange.reconnect_state import (
    ReconnectState,
)


def test_should_reconnect():

    state = ReconnectState(
        reconnect_attempts=1,
        reconnect_limit=5,
    )

    assert (
        should_reconnect(
            state
        )
        is True
    )
