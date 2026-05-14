from src.runtime.event_bus import (
    EventBus,
)


class RuntimeEventBus(EventBus):
    """
    Legacy compatibility wrapper.

    Deprecated:
    Use src.runtime.event_bus.EventBus
    as canonical runtime sync bus.
    """

    pass