import asyncio

from src.runtime.async_event_bus import (
    AsyncEventBus,
)

from src.runtime.async_runtime_loop import (
    AsyncRuntimeLoop,
)

from src.runtime.handlers.market_handler import (
    handle_market_tick,
)


async def main():

    bus = AsyncEventBus()

    bus.subscribe(
        "MARKET_TICK",
        handle_market_tick,
    )

    runtime = AsyncRuntimeLoop(
        event_bus=bus
    )

    runtime_task = (
        asyncio.create_task(
            runtime.start()
        )
    )

    await asyncio.sleep(5)

    runtime.stop()

    await runtime_task


asyncio.run(main())