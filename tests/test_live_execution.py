import asyncio

from src.market.binance_ws import (
    BinanceWebsocketClient,
)

from src.runtime.async_event_bus import (
    AsyncEventBus,
)

from src.runtime.handlers.strategy_handler import (
    handle_strategy_event,
)


async def main():

    bus = AsyncEventBus()

    bus.subscribe(
        "MARKET_TICK",
        handle_strategy_event,
    )

    client = (
        BinanceWebsocketClient(
            event_bus=bus,

            symbol="btcusdt",
        )
    )

    task = (
        asyncio.create_task(
            client.connect()
        )
    )

    await asyncio.sleep(30)

    client.stop()

    await task


asyncio.run(main())