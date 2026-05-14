import json
from dataclasses import asdict
from pathlib import Path

from src.events.event import (
    RuntimeEvent,
)


EVENT_LOG_PATH = (
    "data/runtime/runtime_events.json"
)


def persist_runtime_events(
    events: list[RuntimeEvent],
) -> None:
    path = Path(EVENT_LOG_PATH)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    existing_data = []

    if path.exists():
        with open(path, "r") as file:
            try:
                existing_data = json.load(
                    file
                )
            except json.JSONDecodeError:
                existing_data = []

    serialized_events = []

    for event in events:
        event_dict = asdict(event)

        event_dict["emitted_at"] = (
            event.emitted_at.isoformat()
        )

        serialized_events.append(
            event_dict
        )

    existing_data.extend(
        serialized_events
    )

    with open(path, "w") as file:
        json.dump(
            existing_data,
            file,
            indent=4,
        )