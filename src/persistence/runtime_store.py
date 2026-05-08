import json
from dataclasses import asdict
from pathlib import Path

from src.core.monitoring import (
    RuntimeMetrics,
)


RUNTIME_LOG_PATH = (
    "data/runtime/runtime_metrics.json"
)


def persist_runtime_metrics(
    metrics: RuntimeMetrics,
) -> None:
    path = Path(RUNTIME_LOG_PATH)

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

    existing_data.append(
        asdict(metrics)
    )

    with open(path, "w") as file:
        json.dump(
            existing_data,
            file,
            indent=4,
        )