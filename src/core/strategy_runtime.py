from dataclasses import dataclass

from src.core.autonomous_runtime import (
    AutonomousCycleResult,
    execute_autonomous_cycle,
)

from src.core.runtime import (
    RuntimeState,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

from src.market.market_data import (
    Candle,
    MarketDataSnapshot,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.models import (
    TradeSignal,
)
from src.strategy.strategy_state import (
    StrategyState,
)

@dataclass
class StrategyRuntimeResult:
    runtime: RuntimeState

    executed: bool

    signal: TradeSignal
    state: StrategyState


def execute_strategy_cycle(
    runtime: RuntimeState,
    exchange: PaperExchange,
    snapshot: MarketDataSnapshot,
    candle: Candle,
    state: StrategyState,
) -> StrategyRuntimeResult:

    strategy = (
        MeanReversionStrategy()
    )

    signal = (
        strategy.generate_signal(
            snapshot
        )
    )

    MIN_CONFIDENCE = 0.65

    if (
        signal.confidence
        <
        MIN_CONFIDENCE
    ):

        return StrategyRuntimeResult(
            runtime=runtime,
            executed=False,
            signal=signal.signal,
            state=state,
        )

    side = None
    if (
        state.last_signal
        ==
        signal.signal
    ):

        return StrategyRuntimeResult(
            runtime=runtime,
            executed=False,
            signal=signal.signal,
            state=state,
        )

    has_position = (
        len(exchange.positions)
        > 0
    )

    if (
        signal.signal
        ==
        TradeSignal.BUY
        and
        not has_position
    ):

        side = "BUY"

    elif (
        signal.signal
        ==
        TradeSignal.SELL
        and
        has_position
    ):

        side = "SELL"

    if side is None:

        return StrategyRuntimeResult(
            runtime=runtime,
            executed=False,
            signal=signal.signal,
            state=state,
        )
        
    state.last_signal = (
        signal.signal
    )

    autonomous: AutonomousCycleResult = (
        execute_autonomous_cycle(
            runtime=runtime,
            exchange=exchange,
            snapshot=snapshot,
            candle=candle,
            trade_side=side,
        )
    )

    return StrategyRuntimeResult(
        runtime=autonomous.runtime,
        executed=autonomous.executed,
        signal=signal.signal,
        state=state,
    )