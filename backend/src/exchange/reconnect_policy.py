from src.exchange.reconnect_state import (
    ReconnectState,
)


def should_reconnect(
    state: ReconnectState,
):

    return (
        state.reconnect_attempts
        <
        state.reconnect_limit
    )
