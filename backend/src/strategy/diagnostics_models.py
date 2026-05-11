from dataclasses import dataclass


@dataclass
class StrategyDiagnostics:

    buy_signals: int

    sell_signals: int

    hold_signals: int

    executed_trades: int

    suppressed_signals: int