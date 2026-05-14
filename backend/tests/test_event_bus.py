from datetime import datetime

from src.core.event_bus import EventBus

from src.core.events import (
    RuntimeEvent,
    MARKET_TICK,
)


def test_event_publish():

    bus = EventBus()

    results = []

    def handler(event):
        results.append(event.payload)

    bus.subscribe(
        MARKET_TICK,
        handler,
    )

    event = RuntimeEvent(
        event_type=MARKET_TICK,
        payload={
            "price": 50000,
        },
        emitted_at=datetime.utcnow(),
    )

    bus.publish(event)

    assert len(results) == 1

    assert results[0]["price"] == 50000