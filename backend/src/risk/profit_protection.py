from dataclasses import dataclass


@dataclass
class ProfitProtectionState:
    session_peak_percent: float
    protected_threshold_percent: float
    protection_triggered: bool


def evaluate_profit_protection(
    session_peak_percent: float,
    current_pnl_percent: float,
    protection_ratio: float = 0.70,
) -> ProfitProtectionState:
    protected_threshold = (
        session_peak_percent
        * protection_ratio
    )

    protection_triggered = (
        current_pnl_percent
        < protected_threshold
    )

    return ProfitProtectionState(
        session_peak_percent=
        session_peak_percent,

        protected_threshold_percent=
        round(protected_threshold, 4),

        protection_triggered=
        protection_triggered,
    )