import json
from dataclasses import asdict
from pathlib import Path

from src.core.runtime import (
    RuntimeState,
)


SNAPSHOT_PATH = (
    "data/runtime/runtime_snapshot.json"
)


def persist_runtime_snapshot(
    runtime: RuntimeState,
) -> None:
    path = Path(SNAPSHOT_PATH)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    snapshot = asdict(runtime)

    snapshot["session"][
        "start_time"
    ] = (
        runtime.session.start_time
        .isoformat()
    )

    for event in (
        snapshot["active_events"]
        +
        snapshot["event_history"]
    ):
        event["timestamp"] = (
            event["timestamp"]
            .isoformat()
        )

    with open(path, "w") as file:
        json.dump(
            snapshot,
            file,
            indent=4,
        )