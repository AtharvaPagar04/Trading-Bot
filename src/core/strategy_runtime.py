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


@dataclass
class StrategyRuntimeResult:
    runtime: RuntimeState

    executed: bool

    signal: TradeSignal


def execute_strategy_cycle(
    runtime: RuntimeState,
    exchange: PaperExchange,
    snapshot: MarketDataSnapshot,
    candle: Candle,
) -> StrategyRuntimeResult:

    strategy = (
        MeanReversionStrategy()
    )

    signal = (
        strategy.generate_signal(
            snapshot
        )
    )

    side = None

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
    )