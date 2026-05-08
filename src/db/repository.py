from src.db.database import (
    SessionLocal,
)

from src.db.models import (
    CandleEntity,
)


class CandleRepository:

    def __init__(self):

        self.session = (
            SessionLocal()
        )

    def save_candle(
        self,
        symbol: str,
        timeframe: str,
        open_price: float,
        high_price: float,
        low_price: float,
        close_price: float,
        volume: float,
    ):

        candle = CandleEntity(
            symbol=symbol,

            timeframe=timeframe,

            open=open_price,

            high=high_price,

            low=low_price,

            close=close_price,

            volume=volume,
        )

        self.session.add(
            candle
        )

        self.session.commit()

    def get_all_candles(self):

        return (
            self.session.query(
                CandleEntity
            ).all()
        )