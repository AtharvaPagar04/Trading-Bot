from src.db.position_repository import (
    PositionRepository,
)


repository = (
    PositionRepository()
)

repository.save_position(
    symbol="BTCUSDT",

    quantity=0.01,

    average_price=81000,

    current_price=81200,

    unrealized_pnl=2.0,

    status="OPEN",
)

positions = (
    repository.get_all_positions()
)

for position in positions:

    print(
        position.symbol,
        position.quantity,
        position.unrealized_pnl,
    )