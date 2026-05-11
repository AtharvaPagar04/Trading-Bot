from dataclasses import dataclass


@dataclass
class PerformanceReport:
    total_trades: int

    winning_trades: int

    losing_trades: int

    win_rate: float

    total_realized_pnl: float

    average_trade_pnl: float

    best_trade: float

    worst_trade: float