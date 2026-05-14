from src.core.event_bus import (
    EventBus,
)

from src.core.events import (
    RuntimeEvent,
)


class RuntimeEventBus(EventBus):
    """
    Deprecated compatibility wrapper.

    Canonical event bus:
    src.core.event_bus.EventBus
    """

    def publish(
        self,
        event_type,
        payload=None,
    ):
        if payload is None:
            # New typed dataclass events
            event = event_type
            event_name = type(event).__name__
            # Wrap into a RuntimeEvent for compatibility, or just publish directly if super expects RuntimeEvent
            # Actually super().publish expects a RuntimeEvent with an event_type string.
            # I can convert dataclass to RuntimeEvent here or just broadcast it.
            super().publish(
                RuntimeEvent(
                    event_type=event_name,
                    payload=event.__dict__,
                    emitted_at=None,
                )
            )
            return


        if isinstance(
            payload,
            RuntimeEvent,
        ):

            super().publish(
                payload
            )

            return

        event = RuntimeEvent(
            event_type=event_type,
            payload=payload,
            emitted_at=None,
        )

        super().publish(event)