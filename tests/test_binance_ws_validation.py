import pytest

from src.runtime.async_event_bus import (
    AsyncEventBus,
)

from src.market.binance_ws import (
    BinanceWebsocketClient,
)


@pytest.mark.asyncio
async def test_binance_client_creation():

    bus = AsyncEventBus()

    client = BinanceWebsocketClient(
        event_bus=bus,
        symbol="btcusdt",
    )

    assert (
        client.symbol
        ==
        "btcusdt"
    )

    assert (
        client.running
        is False
    )


@pytest.mark.asyncio
async def test_binance_client_stop():

    bus = AsyncEventBus()

    client = BinanceWebsocketClient(
        event_bus=bus,
    )

    client.running = True

    client.stop()

    assert (
        client.running
        is False
    )