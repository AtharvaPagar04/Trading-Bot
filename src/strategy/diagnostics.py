from src.strategy.diagnostics_models import (
    StrategyDiagnostics,
)

from src.strategy.models import (
    TradeSignal,
)


def update_strategy_diagnostics(
    diagnostics: StrategyDiagnostics,

    signal: TradeSignal,

    executed: bool,
) -> StrategyDiagnostics:

    if signal == TradeSignal.BUY:

        diagnostics.buy_signals += 1

    elif signal == TradeSignal.SELL:

        diagnostics.sell_signals += 1

    elif signal == TradeSignal.HOLD:

        diagnostics.hold_signals += 1

    if executed:

        diagnostics.executed_trades += 1

    else:

        diagnostics.suppressed_signals += 1

    return diagnostics