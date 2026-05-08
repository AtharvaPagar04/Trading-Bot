import time
from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_governance_loop import (
    GovernanceCycleResult,
    execute_governance_cycle,
)
from src.core.runtime_tick_actions import (
    execute_tick_actions,
)

@dataclass
class TickEngineConfig:
    tick_interval_seconds: int


def start_runtime_tick_engine(
    runtime: RuntimeState,

    config: TickEngineConfig,

    cycles: int,

    adx_value: float,

    atr_percent: float,

    stable_closes: int,
) -> RuntimeState:

    for cycle in range(cycles):

        print(
            f"\n===== "
            f"RUNTIME TICK "
            f"{cycle + 1} "
            f"====="
        )

        result: GovernanceCycleResult = (
            execute_governance_cycle(
                runtime=runtime,

                adx_value=
                adx_value,

                atr_percent=
                atr_percent,

                stable_closes=
                stable_closes,
            )
        )

        runtime = result.runtime
        tick_actions = (
            execute_tick_actions(
                runtime
            )
        )
        print(
            "STATE:",
            runtime.operating_state,
        )

        print(
            "EVENTS:",
            len(runtime.active_events),
        )

        print(
            "PNL:",
            runtime.session
            .session_pnl_percent,
        )
        print(
            "HEARTBEAT:",
            tick_actions.heartbeat
            .runtime_healthy,
        )

        time.sleep(
            config.tick_interval_seconds
        )

    return runtime