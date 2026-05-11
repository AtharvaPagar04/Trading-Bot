from datetime import datetime

from src.events.event import (
    EventType,
    RuntimeEvent,
)


def create_event(
    event_type: EventType,
    message: str,
) -> RuntimeEvent:
    return RuntimeEvent(
        event_type=event_type,

        timestamp=datetime.utcnow(),

        message=message,
    )