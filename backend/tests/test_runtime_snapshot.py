from src.core.runtime_builder import (
    build_runtime_state,
)

from src.core.runtime_update import (
    process_runtime_trade,
)

from src.events.event_dispatcher import (
    dispatch_runtime_events,
)

from src.persistence.runtime_snapshot import (
    persist_runtime_snapshot,
)
from src.strategy.strategy_state import (
    StrategyState,
)

from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)

from src.risk.drawdown_tracker import (
    DrawdownState,
)

runtime = build_runtime_state(
    capital=2000,
    timeframe="15m",
    adx_value=18,
    atr_percent=1.5,
)

trade_results = [
    40,
    -50,
    -100,
]

for pnl in trade_results:
    runtime = process_runtime_trade(
        runtime=runtime,
        realized_pnl=pnl,
    )

runtime = dispatch_runtime_events(
    runtime
)

persist_runtime_snapshot(
    runtime=runtime,

    strategy_state=
    StrategyState(),

    portfolio=
    PaperPortfolio(),

    drawdown_state=
    DrawdownState(
        peak_equity=1000.0,
        current_drawdown_percent=0.0,
    ),
)

print("Runtime snapshot persisted")