from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)


def validate_runtime_dependencies(
    exchange,
    websocket,
    runtime_monitor,
    event_bus,
):

    dependencies = {
        "exchange": exchange,
        "websocket": websocket,
        "runtime_monitor": runtime_monitor,
        "event_bus": event_bus,
    }

    for name, dependency in (
        dependencies.items()
    ):

        if dependency is None:

            raise RuntimeError(
                f"{name} dependency missing"
            )

    runtime_log(
        level=LogLevel.INFO,

        category=LogCategory.RUNTIME,

        message=(
            "Runtime dependency "
            "validation passed"
        ),
    )