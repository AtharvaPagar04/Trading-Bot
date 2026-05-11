from src.core.live_governance import (
    execute_live_governance_cycle,
)

from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

result = (
    execute_live_governance_cycle(
        runtime=runtime,

        snapshot=snapshot,
    )
)

print("MARKET STATE")
print(result.market_state)

print("\nOPERATING STATE")
print(
    result.runtime
    .operating_state
)

print("\nEVENTS")
for event in (
    result.runtime
    .active_events
):
    print(event)