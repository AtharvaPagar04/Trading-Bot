from src.events.base_event import BaseEvent

def serialize_event(
    event: BaseEvent,
) -> dict:

    event_dict = event.__dict__.copy()
    
    # Remove event_type and emitted_at from the payload body
    event_type = event_dict.pop("event_type", type(event).__name__)
    emitted_at = event_dict.pop("emitted_at", None)

    # Format datetime if present
    if emitted_at is not None:
        emitted_at = emitted_at.isoformat()
        
    # Also we should format any other datetime fields in the payload
    for key, value in event_dict.items():
        if hasattr(value, "isoformat"):
            event_dict[key] = value.isoformat()

    return {
        "event_type": event_type,
        "emitted_at": emitted_at,
        "payload": event_dict,
    }
