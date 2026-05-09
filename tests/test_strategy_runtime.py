from datetime import datetime

from src.core.strategy_runtime import (
    execute_strategy_cycle,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)
from src.strategy.strategy_state import (
    StrategyState,
)
from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.market.market_data import (
    Candle,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

exchange = PaperExchange(
    starting_capital=2000
)

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

candle = Candle(
    timestamp=
    datetime.utcnow(),

    open=120,

    high=124,

    low=118,

    close=122,

    volume=2500,
)

result = (
    execute_strategy_cycle(
        runtime=runtime,

        exchange=exchange,

        snapshot=snapshot,

        candle=candle,
        state=StrategyState(),
    )
)

print("SIGNAL")
print(result.signal)

print("\nEXECUTED")
print(result.executed)

print("\nBALANCE")
print(exchange.balance)

print("\nPOSITIONS")
print(exchange.positions)