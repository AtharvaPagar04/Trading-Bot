from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)


@dataclass
class RuntimeIntegrityReport:
    valid: bool

    issues: list[str]


def validate_runtime_integrity(
    runtime: RuntimeState,
) -> RuntimeIntegrityReport:

    issues = []

    if (
        runtime.session
        .current_capital < 0
    ):
        issues.append(
            "Negative capital detected"
        )

    if (
        not runtime.session
        .session_id
    ):
        issues.append(
            "Missing session ID"
        )

    if runtime.market_state is None:
        issues.append(
            "Missing market state"
        )

    if runtime.risk_state is None:
        issues.append(
            "Missing risk state"
        )

    if not isinstance(
        runtime.active_events,
        list,
    ):
        issues.append(
            "Active events "
            "must be list"
        )

    if not isinstance(
        runtime.event_history,
        list,
    ):
        issues.append(
            "Event history "
            "must be list"
        )

    return RuntimeIntegrityReport(
        valid=len(issues) == 0,
        issues=issues,
    )