from dataclasses import dataclass

from src.core.live_governance import (
    LiveGovernanceResult,
    execute_live_governance_cycle,
)

from src.core.runtime import (
    RuntimeState,
)

from src.market.market_data import (
    Candle,
    MarketDataSnapshot,
)


@dataclass
class StreamingRuntimeResult:
    runtime: RuntimeState

    snapshot: MarketDataSnapshot


def process_incoming_candle(
    runtime: RuntimeState,

    snapshot: MarketDataSnapshot,

    candle: Candle,

    max_candles: int = 100,
) -> StreamingRuntimeResult:

    snapshot.candles.append(
        candle
    )

    snapshot.candles = (
        snapshot.candles[
            -max_candles:
        ]
    )

    governance: LiveGovernanceResult = (
        execute_live_governance_cycle(
            runtime=runtime,

            snapshot=snapshot,
        )
    )

    runtime = governance.runtime

    return StreamingRuntimeResult(
        runtime=runtime,

        snapshot=snapshot,
    )