from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_governance_loop import (
    GovernanceCycleResult,
    execute_governance_cycle,
)

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.market.market_state_pipeline import (
    generate_market_state,
)


@dataclass
class LiveGovernanceResult:
    runtime: RuntimeState

    market_state: object


def execute_live_governance_cycle(
    runtime: RuntimeState,

    snapshot: MarketDataSnapshot,
) -> LiveGovernanceResult:

    market_state = (
        generate_market_state(
            snapshot
        )
    )

    governance = (
        execute_governance_cycle(
            runtime=runtime,

            adx_value=
            market_state.adx,

            atr_percent=
            market_state.atr_percent,

            stable_closes=2,
        )
    )

    runtime = governance.runtime

    runtime.market_state = (
        market_state
    )

    return LiveGovernanceResult(
        runtime=runtime,

        market_state=
        market_state,
    )