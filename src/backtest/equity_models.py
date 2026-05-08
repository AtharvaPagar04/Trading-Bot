from dataclasses import dataclass


@dataclass
class EquityCurveReport:
    equity_curve: list[float]

    peak_equity: float

    max_drawdown_percent: float

    final_equity: float