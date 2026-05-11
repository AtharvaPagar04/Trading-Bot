from src.db.database import (
    Base,
)

from src.db.database import (
    engine,
)

from src.exchange.execution_engine import (
    ExecutionEngine,
)

Base.metadata.create_all(
    bind=engine
)

engine_instance = (
    ExecutionEngine()
)

position = (
    engine_instance.open_position(
        symbol="BTCUSDT",

        side="BUY",

        quantity=1,

        entry_price=100,
    )
)

execution = (
    engine_instance.close_position(
        position_id=
        position.id,

        exit_price=110,
    )
)

print("POSITIONS")

for p in (
    engine_instance
    .get_positions()
):

    print(
        p.symbol,
        p.status,
    )

print()

print("EXECUTIONS")

for e in (
    engine_instance
    .get_executions()
):

    print(
        e.symbol,
        e.realized_pnl,
    )