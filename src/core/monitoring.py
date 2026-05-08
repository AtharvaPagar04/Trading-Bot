from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)


@dataclass
class RuntimeMetrics:
    current_capital: float

    session_pnl_percent: float

    peak_pnl_percent: float

    entries_enabled: bool

    risk_state: str

    size_multiplier: float

    active_event_count: int

    archived_event_count: int


def generate_runtime_metrics(
    runtime: RuntimeState,
) -> RuntimeMetrics:
    return RuntimeMetrics(
        current_capital=
        runtime.session.current_capital,

        session_pnl_percent=
        runtime.session
        .session_pnl_percent,

        peak_pnl_percent=
        runtime.session
        .peak_pnl_percent,

        entries_enabled=
        runtime.session
        .entries_enabled,

        risk_state=
        runtime.risk_state
        .risk_state.value,

        size_multiplier=
        runtime.risk_state
        .size_multiplier,

        active_event_count=len(
            runtime.active_events
        ),

        archived_event_count=len(
            runtime.event_history
        ),
    )