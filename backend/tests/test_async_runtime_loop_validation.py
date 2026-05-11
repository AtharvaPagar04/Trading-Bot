import asyncio
import pytest

from src.runtime.async_event_bus import (
    AsyncEventBus,
)

from src.runtime.async_runtime_loop import (
    AsyncRuntimeLoop,
)


@pytest.mark.asyncio
async def test_async_runtime_loop_starts_and_stops():

    bus = AsyncEventBus()

    runtime = AsyncRuntimeLoop(
        event_bus=bus
    )

    async def stop_runtime():

        await asyncio.sleep(0.1)

        runtime.stop()

    runtime_task = asyncio.create_task(
        runtime.start()
    )

    stop_task = asyncio.create_task(
        stop_runtime()
    )

    await asyncio.gather(
        runtime_task,
        stop_task,
    )

    assert runtime.running is False