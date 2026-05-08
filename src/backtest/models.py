from dataclasses import dataclass
from src.strategy.diagnostics_models import (
    StrategyDiagnostics,
)

@dataclass
class BacktestResult:
    total_trades: int
    diagnostics: StrategyDiagnostics

    final_capital: float

    pnl_percent: float

    win_rate: float

    equity_curve: list[float]

    max_drawdown_percent: float