from dataclasses import dataclass

from src.core.session import (
    TradingSession,
)

from src.risk.exposure import (
    drawdown_size_multiplier,
)

from src.risk.session_risk import (
    SessionRiskState,
    classify_session_risk,
)


@dataclass
class RiskSyncState:
    risk_state: SessionRiskState

    entries_allowed: bool

    size_multiplier: float


def synchronize_risk_state(
    session: TradingSession,
) -> RiskSyncState:
    risk_state = (
        classify_session_risk(
            session.session_pnl_percent
        )
    )

    entries_allowed = (
        risk_state
        not in [
            SessionRiskState
            .STOP_SESSION,

            SessionRiskState
            .EMERGENCY_LIQUIDATION,
        ]
    )

    drawdown = abs(
        min(
            session.session_pnl_percent,
            0,
        )
    )

    size_multiplier = (
        drawdown_size_multiplier(
            drawdown
        )
    )

    return RiskSyncState(
        risk_state=risk_state,

        entries_allowed=
        entries_allowed,

        size_multiplier=
        size_multiplier,
    )