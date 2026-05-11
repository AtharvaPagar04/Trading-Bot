from src.db.database import (
    Base,
)

from src.db.database import (
    engine,
)

from src.db.repository import (
    CandleRepository,
)

Base.metadata.create_all(
    bind=engine
)

repo = (
    CandleRepository()
)

repo.save_candle(
    symbol="BTCUSDT",

    timeframe="1m",

    open_price=100,

    high_price=105,

    low_price=99,

    close_price=103,

    volume=12,
)

candles = (
    repo.get_all_candles()
)

for candle in candles:

    print(candle.symbol)

    print(candle.close)