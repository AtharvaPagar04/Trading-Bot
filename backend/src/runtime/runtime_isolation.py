from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)

class RuntimeIsolationError(
    RuntimeError
):

    def __init__(
        self,
        subsystem: str,
        original_exception: Exception,
    ):

        self.subsystem = subsystem

        self.original_exception = (
            original_exception
        )

        super().__init__(
            f"[{subsystem}] "
            f"{type(original_exception).__name__}: "
            f"{original_exception}"
        )


def isolate_runtime_failure(
    subsystem: str,
    operation,
):
    try:

        return operation()

    except Exception as exc:
        runtime_log(
            level=LogLevel.ERROR,
            category=LogCategory.ISOLATION,
            message=(
                f"Isolation failure in "
                f"{subsystem}: "
                f"{type(exc).__name__} - "
                f"{exc}"
            ),
        )

        raise RuntimeIsolationError(
            subsystem=subsystem,
            original_exception=exc,
        ) from exc