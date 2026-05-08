from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)


@dataclass
class ExecutionPermission:
    allowed: bool

    reason: str


def evaluate_execution_permission(
    runtime: RuntimeState,
) -> ExecutionPermission:

    if runtime.safe_mode:
        return ExecutionPermission(
            allowed=False,
            reason=(
                "Runtime operating "
                "in safe mode"
            ),
        )

    if (
        not runtime.market_state
        .allow_entries
    ):
        return ExecutionPermission(
            allowed=False,
            reason=(
                "Market regime "
                "blocked entries"
            ),
        )

    if (
        not runtime.session
        .entries_enabled
    ):
        return ExecutionPermission(
            allowed=False,
            reason=(
                "Session entries "
                "disabled"
            ),
        )

    if (
        not runtime.risk_state
        .entries_allowed
    ):
        return ExecutionPermission(
            allowed=False,
            reason=(
                "Risk state "
                "blocked entries"
            ),
        )

    return ExecutionPermission(
        allowed=True,
        reason="Execution allowed",
    )