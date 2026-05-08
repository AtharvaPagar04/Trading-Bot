from src.db.database import (
    Base,
)

from src.db.database import (
    engine,
)

from src.runtime.event_journal import (
    EventJournal,
)

Base.metadata.create_all(
    bind=engine
)

journal = (
    EventJournal()
)

journal.log_event(
    event_type=
    "MARKET_TICK",

    payload={
        "symbol":
        "BTCUSDT",

        "price":
        100000,
    },
)

journal.log_event(
    event_type=
    "SIGNAL_GENERATED",

    payload={
        "signal":
        "BUY",

        "confidence":
        0.8,
    },
)

events = (
    journal.get_events()
)

for event in events:

    print()

    print(
        event.event_type
    )

    print(
        event.event_payload
    )