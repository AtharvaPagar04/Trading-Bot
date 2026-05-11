from src.db.database import (
    SessionLocal,
)

from src.db.models import (
    CandleEntity,
)

from src.db.models import (
    CompletedTradeEntity,
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

class CompletedTradeRepository:

    def __init__(self):

        self.session = (
            SessionLocal()
        )

    def save_completed_trade(
        self,
        symbol: str,
        quantity: float,
        entry_price: float,
        exit_price: float,
        realized_pnl: float,
        fees_paid: float,
        opened_at,
        closed_at,
    ):

        trade = (
            CompletedTradeEntity(
                symbol=symbol,

                quantity=quantity,

                entry_price=
                entry_price,

                exit_price=
                exit_price,

                realized_pnl=
                realized_pnl,

                fees_paid=
                fees_paid,

                opened_at=
                opened_at,

                closed_at=
                closed_at,
            )
        )

        self.session.add(
            trade
        )

        self.session.commit()

    def get_all_completed_trades(
        self,
    ):

        return (
            self.session.query(
                CompletedTradeEntity
            ).all()
        )