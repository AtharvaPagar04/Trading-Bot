from src.core.runtime import (
    RuntimeState,
)


def clear_runtime_safe_mode(
    runtime: RuntimeState,
) -> RuntimeState:

    runtime.safe_mode = False

    runtime.session.entries_enabled = (
        True
    )

    return runtime