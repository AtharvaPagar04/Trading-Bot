from src.events.event import (
    EventType,
)

from src.events.event_factory import (
    create_event,
)

events = [
    (
        EventType.SESSION_STARTED,
        "Trading session initialized",
    ),

    (
        EventType.TRADE_EXECUTED,
        "Grid trade executed",
    ),

    (
        EventType.RISK_ESCALATED,
        "Session risk increased",
    ),
]

for event_type, message in events:
    event = create_event(
        event_type=event_type,
        message=message,
    )

    print(event)