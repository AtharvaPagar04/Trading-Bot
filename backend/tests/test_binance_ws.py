import asyncio

from src.market.binance_ws import (
    BinanceWebsocketClient,
)

from src.runtime.async_event_bus import (
    AsyncEventBus,
)


async def market_handler(
    event,
):

    print(
        "LIVE MARKET EVENT"
    )

    print(event)


async def main():

    bus = AsyncEventBus()

    bus.subscribe(
        "MARKET_TICK",
        market_handler,
    )

    client = (
        BinanceWebsocketClient(
            event_bus=bus,

            symbol="btcusdt",
        )
    )

    websocket_task = (
        asyncio.create_task(
            client.connect()
        )
    )

    await asyncio.sleep(10)

    client.stop()

    await websocket_task


asyncio.run(main())