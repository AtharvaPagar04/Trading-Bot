from src.core.runtime_tick_engine import (
    TickEngineConfig,
    start_runtime_tick_engine,
)

from src.core.safe_mode import (
    apply_safe_mode,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

runtime = apply_safe_mode(
    runtime
)

config = TickEngineConfig(
    tick_interval_seconds=1
)

runtime = start_runtime_tick_engine(
    runtime=runtime,

    config=config,

    cycles=3,

    adx_value=18,

    atr_percent=1.5,

    stable_closes=2,
)