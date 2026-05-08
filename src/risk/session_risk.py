from enum import Enum


class SessionRiskState(str, Enum):
    NORMAL = "NORMAL"
    REDUCE_RISK = "REDUCE_RISK"
    DISABLE_ENTRIES = "DISABLE_ENTRIES"
    STOP_SESSION = "STOP_SESSION"
    EMERGENCY_LIQUIDATION = (
        "EMERGENCY_LIQUIDATION"
    )


def classify_session_risk(
    session_pnl_percent: float,
) -> SessionRiskState:
    if session_pnl_percent <= -4:
        return (
            SessionRiskState
            .EMERGENCY_LIQUIDATION
        )

    if session_pnl_percent <= -3:
        return (
            SessionRiskState
            .STOP_SESSION
        )

    if session_pnl_percent <= -2:
        return (
            SessionRiskState
            .DISABLE_ENTRIES
        )

    if session_pnl_percent <= -1:
        return (
            SessionRiskState
            .REDUCE_RISK
        )

    return SessionRiskState.NORMAL