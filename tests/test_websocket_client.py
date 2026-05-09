from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
)

from src.market_data.market_data_router import (
    MarketDataRouter,
)

from src.market_data.websocket_client import (
    WebSocketClient,
)
from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)

def test_websocket_client_initial_state():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    router = MarketDataRouter(
        runtime
    )

    client = WebSocketClient(
        router
    )

    assert client.connected is False


def test_websocket_connect():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    router = MarketDataRouter(
        runtime
    )

    client = WebSocketClient(
        router
    )

    client.connect()

    assert client.connected is True


def test_websocket_disconnect():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    router = MarketDataRouter(
        runtime
    )

    client = WebSocketClient(
        router
    )

    client.connect()

    client.disconnect()

    assert client.connected is False

def test_websocket_tick_updates_market_health():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    router = MarketDataRouter(
        runtime
    )

    client = WebSocketClient(
        router
    )

    before = (
        runtime.market_data_health
        .last_update
    )

    client.receive_tick(
        symbol="BTCUSDT",
        price=100000.0,
        exchange="binance",
    )

    after = (
        runtime.market_data_health
        .last_update
    )

    assert after >= before


def test_websocket_reconnect():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    router = MarketDataRouter(
        runtime
    )

    client = WebSocketClient(
        router
    )

    result = client.reconnect()

    assert result is True

    assert client.connected is True

    assert (
        client.reconnect_attempts
        == 1
    )

def test_websocket_reconnect_limit():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    router = MarketDataRouter(
        runtime
    )

    client = WebSocketClient(
        router
    )

    client.reconnect_attempts = 5

    result = client.reconnect()

    assert result is False

    assert (
        runtime.state.status
        ==
        RuntimeStatus.EMERGENCY_STOP
    )

    assert (
        runtime.state.emergency_reason
        ==
        EmergencyReason
        .HEARTBEAT_FAILURE
    )

    assert (
        runtime.execution_allowed()
        is False
    )