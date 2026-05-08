from src.core.runtime import (
    RuntimeState,
)

from src.events.event import (
    EventType,
)

def dispatch_runtime_events(
    runtime: RuntimeState,
) -> RuntimeState:
    processed_events = []

    for event in runtime.active_events:

        if (
            event.event_type
            ==
            EventType.COOLDOWN_STARTED
        ):
            runtime.session.entries_enabled = (
                False
            )

        if (
            event.event_type
            ==
            EventType
            .EMERGENCY_LIQUIDATION
        ):
            runtime.session.entries_enabled = (
                False
            )

        processed_events.append(event)

    runtime.event_history.extend(
        processed_events
    )

    runtime.active_events = []

    return runtime