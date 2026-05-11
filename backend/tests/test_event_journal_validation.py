from src.runtime.event_journal import (
    EventJournal,
)


def test_event_logging():

    journal = EventJournal()

    journal.log_event(
        event_type="TEST_EVENT",

        payload={
            "status": "ok"
        },
    )

    events = (
        journal.get_events()
    )

    assert len(events) > 0

    latest = events[-1]

    assert (
        latest.event_type
        ==
        "TEST_EVENT"
    )