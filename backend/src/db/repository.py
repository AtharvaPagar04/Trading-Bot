
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
        session_id: int | None,
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

                session_id=
                session_id,
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
    
    def get_trade_analytics(
        self,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            trades = (
                db.query(
                    CompletedTradeEntity
                ).all()
            )

            total_trades = (
                len(trades)
            )

            if total_trades == 0:

                return {
                    "total_trades": 0,
                    "winning_trades": 0,
                    "losing_trades": 0,
                    "win_rate": 0.0,
                    "total_realized_pnl": 0.0,
                    "average_trade_pnl": 0.0,
                    "best_trade_pnl": 0.0,
                    "worst_trade_pnl": 0.0,
                }

            winning_trades = sum(
                1
                for trade
                in trades
                if trade.realized_pnl > 0
            )

            losing_trades = sum(
                1
                for trade
                in trades
                if trade.realized_pnl < 0
            )

            total_realized_pnl = sum(
                trade.realized_pnl
                for trade in trades
            )

            average_trade_pnl = (
                total_realized_pnl
                / total_trades
            )

            best_trade_pnl = max(
                trade.realized_pnl
                for trade in trades
            )

            worst_trade_pnl = min(
                trade.realized_pnl
                for trade in trades
            )

            return {
                "total_trades":
                total_trades,

                "winning_trades":
                winning_trades,

                "losing_trades":
                losing_trades,

                "win_rate":
                round(
                    (
                        winning_trades
                    /
                    total_trades
                    ) * 100,
                    2,
                ),

                "total_realized_pnl":
                total_realized_pnl,

                "average_trade_pnl":
                average_trade_pnl,

                "best_trade_pnl":
                best_trade_pnl,

                "worst_trade_pnl":
                worst_trade_pnl,
            }

        finally:

            db.close()
    
    def get_trades_for_session(
        self,
        session_id: int,
    ):

        return (
            self.session.query(
                CompletedTradeEntity
            ).filter(
                CompletedTradeEntity.session_id == session_id
            ).all()
        )
        
    def get_closed_trades_for_session(
        self,
        session_id: int,
    ):

        return (
            self.session.query(
                CompletedTradeEntity
            ).filter(
                CompletedTradeEntity.session_id == session_id,
                CompletedTradeEntity.closed_at.isnot(None),
            ).all()
        )
        
    def get_session_trade_analytics(
        self,
        session_id: int,
    ):

        trades = (
            self.get_trades_for_session(
                session_id
            )
        )

        total_trades = (
            len(trades)
        )

        if total_trades == 0:

            return {
                "total_trades": 0,
                "winning_trades": 0,
                "losing_trades": 0,
                "win_rate": 0.0,
                "total_realized_pnl": 0.0,
                "average_trade_pnl": 0.0,
                "best_trade_pnl": 0.0,
                "worst_trade_pnl": 0.0,
            }

        winning_trades = sum(
            1
            for trade
            in trades
            if trade.realized_pnl > 0
        )

        losing_trades = sum(
            1
            for trade
            in trades
            if trade.realized_pnl < 0
        )

        total_realized_pnl = sum(
            trade.realized_pnl
            for trade in trades
        )

        average_trade_pnl = (
            total_realized_pnl
            / total_trades
        )

        best_trade_pnl = max(
            trade.realized_pnl
            for trade in trades
        )

        worst_trade_pnl = min(
            trade.realized_pnl
            for trade in trades
        )

        return {
            "total_trades":
            total_trades,

            "winning_trades":
            winning_trades,

            "losing_trades":
            losing_trades,

            "win_rate":
            round(
                (
                    winning_trades
                    /
                    total_trades
                ) * 100,
                2,
            ),

            "total_realized_pnl":
            total_realized_pnl,

            "average_trade_pnl":
            average_trade_pnl,

            "best_trade_pnl":
            best_trade_pnl,

            "worst_trade_pnl":
            worst_trade_pnl,
        }