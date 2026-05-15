from src.core.runtime import RuntimeState

from src.core.runtime_state_machine import (
    evaluate_runtime_state,
)


def get_operating_state(
    runtime: RuntimeState,
) -> str:

    return (
        evaluate_runtime_state(runtime)
        .state
        .value
    )