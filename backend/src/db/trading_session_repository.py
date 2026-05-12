from datetime import (
    datetime,
)

from sqlalchemy.orm import (
    Session,
)

from src.db.database import (
    SessionLocal,
)

from src.db.trading_session_model import (
    TradingSessionModel,
)

class TradingSessionRepository:

    def create_session(
        self,
        started_at: datetime,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            session = (
                TradingSessionModel(
                    started_at=
                    started_at,
                )
            )

            db.add(
                session
            )

            db.commit()

            db.refresh(
                session
            )

            return session

        finally:

            db.close()

    def end_session(
        self,
        session_id: int,

        ended_at: datetime,

        duration_seconds: int,

        total_trades: int,

        realized_pnl: float,

        portfolio_value: float,

        safe_mode_triggered: bool,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            session = (
                db.query(
                    TradingSessionModel
                )
                .filter(
                    TradingSessionModel.id
                    ==
                    session_id
                )
                .first()
            )

            if session is None:

                return None

            session.ended_at = (
                ended_at
            )

            session.duration_seconds = (
                duration_seconds
            )

            session.total_trades = (
                total_trades
            )

            session.realized_pnl = (
                realized_pnl
            )

            session.portfolio_value = (
                portfolio_value
            )

            session.safe_mode_triggered = (
                safe_mode_triggered
            )

            db.commit()

            db.refresh(
                session
            )

            return session

        finally:

            db.close()

    def get_recent_sessions(
        self,
        limit: int = 20,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            sessions = (
                db.query(
                    TradingSessionModel
                )
                .order_by(
                    TradingSessionModel.id
                    .desc()
                )
                .limit(
                    limit
                )
                .all()
            )

            return sessions

        finally:

            db.close()
    def recover_orphan_sessions(
        self,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            orphan_sessions = (
                db.query(
                    TradingSessionModel
                )
                .filter(
                    TradingSessionModel
                    .ended_at
                    == None
                )
                .all()
            )

            recovered_count = 0

            for session in orphan_sessions:

                session.ended_at = (
                    datetime.utcnow()
                )

                recovered_count += 1

            db.commit()

            return recovered_count

        finally:

            db.close()
    def get_session_analytics(
        self,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            sessions = (
                db.query(
                    TradingSessionModel
                )
                .filter(
                    TradingSessionModel
                    .ended_at
                    != None
                )
                .all()
            )

            total_sessions = (
                len(sessions)
            )

            if total_sessions == 0:

                return {
                    "total_sessions": 0,
                    "total_realized_pnl": 0.0,
                    "average_session_duration": 0,
                    "best_session_pnl": 0.0,
                    "worst_session_pnl": 0.0,
                    "profitable_sessions": 0,
                    "losing_sessions": 0,
                    "safe_mode_sessions": 0,
                    "win_rate": 0.0,
                }

            total_realized_pnl = (
                sum(
                    session.realized_pnl
                    for session in sessions
                )
            )

            average_session_duration = (
                int(
                    sum(
                        session.duration_seconds
                        for session in sessions
                    )
                    /
                    total_sessions
                )
            )

            best_session_pnl = (
                max(
                    session.realized_pnl
                    for session in sessions
                )
            )

            worst_session_pnl = (
                min(
                    session.realized_pnl
                    for session in sessions
                )
            )
            profitable_sessions = sum(
                1
                for session in sessions
                if session.realized_pnl > 0
            )

            losing_sessions = sum(
                1
                for session
                in sessions
                if session.realized_pnl < 0
            )

            safe_mode_sessions = (
                sum(
                    1
                    for session
                    in sessions
                    if session.safe_mode_triggered
                )
            )

            return {
                "total_sessions":
                total_sessions,

                "total_realized_pnl":
                total_realized_pnl,

                "average_session_duration":
                average_session_duration,

                "best_session_pnl":
                best_session_pnl,

                "worst_session_pnl":
                worst_session_pnl,

                "profitable_sessions":
                profitable_sessions,

                "losing_sessions":
                losing_sessions,

                "safe_mode_sessions":
                safe_mode_sessions,

                "win_rate":
                round(
                    (
                        profitable_sessions
                        /
                        total_sessions
                    ) * 100,
                    2,
                ),
            }

        finally:

            db.close()

    def get_session_by_id(
        self,
        session_id: int,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            session = (
                db.query(
                    TradingSessionModel
                )
                .filter(
                    TradingSessionModel.id
                    ==
                    session_id
                )
                .first()
            )

            return session

        finally:

            db.close()
    def get_active_session(self):

        db: Session = (
            SessionLocal()
        )

        try:

            return (
                db.query(
                    TradingSessionModel
                )
                .filter(
                    TradingSessionModel.ended_at == None
                )
                .order_by(
                    TradingSessionModel.id.desc()
                )
                .first()
            )

        finally:

            db.close()

    def update_live_session(
        self,
        session_id: int,
        duration_seconds: int,
        total_trades: int,
        realized_pnl: float,
        portfolio_value: float,
    ):

        db: Session = (
            SessionLocal()
        )

        try:

            session = (
                db.query(
                    TradingSessionModel
                )
                .filter(
                    TradingSessionModel.id
                    ==
                    session_id
                )
                .first()
            )

            if session is None:

                return None

            session.duration_seconds = (
                duration_seconds
            )

            session.total_trades = (
                total_trades
            )

            session.realized_pnl = (
                realized_pnl
            )

            session.portfolio_value = (
                portfolio_value
            )

            db.commit()

            db.refresh(
                session
            )

            return session

        finally:

            db.close()