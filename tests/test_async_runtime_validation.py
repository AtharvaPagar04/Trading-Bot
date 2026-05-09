import pytest

from src.runtime.async_event_bus import (
    AsyncEventBus,
)


async def sample_handler(event):

    sample_handler.called = True


sample_handler.called = False


@pytest.mark.asyncio
async def test_async_event_publish():

    bus = AsyncEventBus()

    bus.subscribe(
        "TEST_EVENT",
        sample_handler,
    )

    await bus.publish(
        event_type="TEST_EVENT",

        payload={
            "status": "ok"
        },
    )

    assert (
        sample_handler.called
        is True
    )