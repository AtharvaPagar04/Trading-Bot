from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)


def log_runtime_event(
    payload,
):

    runtime_log(
        level=LogLevel.INFO,

        category=LogCategory.RUNTIME,

        message=(
            f"Runtime event: "
            f"{payload}"
        ),
    )