from fastapi import FastAPI

from src.runtime.runtime_registry import (
    runtime_snapshot,
)
from fastapi.middleware.cors import (
    CORSMiddleware,
)
from src.runtime.runtime_controller import (
    RuntimeController,
)

from src.db.trading_session_repository import (
    TradingSessionRepository,
)
from src.db.repository import (
    CompletedTradeRepository,
)


app = FastAPI()

runtime_controller = (
    RuntimeController()
)
session_repository = (
    TradingSessionRepository()
)
trade_repository = (
    CompletedTradeRepository()
)
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

@app.get("/health")
async def health():

    return {
        "status": "ok"
    }


@app.get("/runtime")
async def get_runtime():

    return runtime_snapshot


@app.post(
    "/runtime/start"
)
def start_runtime():

    runtime_controller.start_runtime()
    
    


    return {
        "success": True,

        "runtime_running":
        runtime_controller
        .is_running,
    }

@app.post(
    "/runtime/stop"
)
def stop_runtime():

    runtime_controller.stop_runtime()

    return {
        "success": True,

        "runtime_running":
        runtime_controller
        .is_running,
    }

@app.post(
    "/runtime/pause"
)
def pause_runtime():

    runtime_controller.pause_runtime()

    return {
        "success": True,

        "runtime_paused":
        runtime_controller
        .is_paused,
    }

@app.post(
    "/runtime/resume"
)
def resume_runtime():

    runtime_controller.resume_runtime()

    return {
        "success": True,

        "runtime_paused":
        runtime_controller
        .is_paused,
    }

@app.post(
    "/runtime/safe-mode"
)
def toggle_safe_mode():

    if runtime_controller.safe_mode:

        runtime_controller.disable_safe_mode()

    else:

        runtime_controller.enable_safe_mode()

    return {
        "success": True,

        "safe_mode":
        runtime_controller
        .safe_mode,
    }
@app.get(
    "/sessions"
)
def get_sessions():

    sessions = (
        session_repository
        .get_recent_sessions()
    )

    return [
        {
            "id":
            session.id,

            "started_at":
            session.started_at,

            "ended_at":
            session.ended_at,

            "duration_seconds":
            session.duration_seconds,

            "total_trades":
            session.total_trades,

            "realized_pnl":
            session.realized_pnl,

            "portfolio_value":
            session.portfolio_value,

            "safe_mode_triggered":
            session.safe_mode_triggered,
        }
        for session
        in sessions
    ]

@app.get(
    "/sessions/analytics"
)
def get_session_analytics():

    analytics = (
        session_repository
        .get_session_analytics()
    )

    return analytics

@app.get(
    "/trades/analytics"
)
def get_trade_analytics():

    analytics = (
        trade_repository
        .get_trade_analytics()
    )

    return analytics


@app.get(
    "/sessions/{session_id}/trades"
)
def get_session_trades(
    session_id: int,
):

    trades = (
        trade_repository
        .get_trades_by_session(
            session_id
        )
    )

    return [
        {
            "id":
            trade.id,

            "symbol":
            trade.symbol,

            "quantity":
            trade.quantity,

            "entry_price":
            trade.entry_price,

            "exit_price":
            trade.exit_price,

            "realized_pnl":
            trade.realized_pnl,

            "fees_paid":
            trade.fees_paid,

            "opened_at":
            trade.opened_at,

            "closed_at":
            trade.closed_at,

            "session_id":
            trade.session_id,
        }
        for trade
        in trades
    ]
@app.get(
    "/sessions/{session_id}"
)
def get_session(
    session_id: int,
):

    session = (
        session_repository
        .get_session_by_id(
            session_id
        )
    )

    if session is None:

        return {
            "error":
            "Session not found"
        }

    return {
        "id":
        session.id,

        "started_at":
        session.started_at,

        "ended_at":
        session.ended_at,

        "duration_seconds":
        session.duration_seconds,

        "total_trades":
        session.total_trades,

        "realized_pnl":
        session.realized_pnl,

        "portfolio_value":
        session.portfolio_value,

        "safe_mode_triggered":
        session.safe_mode_triggered,
    }

@app.get(
    "/sessions/{session_id}/analytics"
)
def get_session_trade_analytics(
    session_id: int,
):

    analytics = (
        trade_repository
        .get_session_trade_analytics(
            session_id
        )
    )

    return analytics

@app.get(
    "/analytics"
)
def get_analytics():

    return (
        session_repository
        .get_session_analytics()
    )

@app.get(
    "/active-session"
)
def get_active_session():

    session = (
        session_repository
        .get_active_session()
    )


    if session is None:

        return {
            "active": False
        }

    return {
        "active": True,

        "session": {
            "id": session.id,

            "started_at":
            session.started_at,

            "ended_at":
            session.ended_at,

            "duration_seconds":
            session.duration_seconds,

            "total_trades":
            session.total_trades,

            "realized_pnl":
            session.realized_pnl,

            "portfolio_value":
            session.portfolio_value,

            "safe_mode_triggered":
            session.safe_mode_triggered,
        }
    }