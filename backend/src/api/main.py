from fastapi import FastAPI, HTTPException
API_PREFIX = "/api/v1"
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
from datetime import datetime

from src.api.models.runtime_models import RuntimeResponse
from src.api.models.session_models import SessionResponse
from src.api.models.governance_models import RecoveryStatusResponse, GovernanceResponse

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
        "http://127.0.0.1:3000",
        "http://192.168.31.217:3000",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

from src.api.routes import monitoring_routes
app.include_router(monitoring_routes.router)

from src.api.websocket import runtime_stream
app.include_router(runtime_stream.router)

@app.get(f"{API_PREFIX}/health")

async def health():

    return {
        "status": "ok"
    }


@app.get(
    f"{API_PREFIX}/runtime",
    response_model=RuntimeResponse,
)
async def get_runtime():

    runtime_state = (
        runtime_controller.runtime_state
    )
    if runtime_state is None:
        return {
            "connected": False
        }
    exchange = (
    runtime_controller.exchange
    )

    
    available_capital = 0.0
    invested_capital = 0.0
    total_portfolio_value = 0.0
    active_trades = []

    if exchange is not None:

        available_capital = float(
            exchange.balance.available_capital
        )

        latest_price = (
            runtime_state.latest_price
        )

        market_data_ready = (
            latest_price is not None
            and latest_price > 0
        )

        for symbol, position in (
            exchange.positions.items()
        ):

            current_value = 0
            unrealized_pnl = None
            unrealized_pnl_percent = None

            if market_data_ready:

                current_value = (
                    position.quantity
                    * latest_price
                )

                invested_capital += (
                    current_value
                )

                unrealized_pnl = (
                    (
                        latest_price
                        -
                        position.average_price
                    )
                    *
                    position.quantity
                )

                unrealized_pnl_percent = (
                    (
                        latest_price
                        -
                        position.average_price
                    )
                    /
                    position.average_price
                ) * 100

            active_trades.append({
                "symbol":
                    symbol,

                "quantity":
                    position.quantity,

                "entry_price":
                    position.average_price,

                "current_price":
                    (
                        latest_price
                        if market_data_ready
                        else None
                    ),

                "market_data_ready":
                    market_data_ready,

                "unrealized_pnl":
                    unrealized_pnl,

                "unrealized_pnl_percent":
                    unrealized_pnl_percent,
            })
        
        total_portfolio_value = (
            available_capital
            +
            invested_capital
        )

    return {
        "connected": True,

        "status":
        runtime_state.status.value,

        "mode":
        runtime_state.mode.value,

        "is_trading_enabled":
        runtime_state.is_trading_enabled,

        "safe_mode":
        runtime_state.safe_mode,

        "latest_price":
        runtime_state.latest_price,

        "latest_candle_close":
        runtime_state.latest_candle_close,

        "total_trades":
        (
            runtime_state.total_trades
            if runtime_state.active_session_id
            else 0
        ),

        "winning_trades":
        runtime_state.winning_trades,

        "losing_trades":
        runtime_state.losing_trades,

        "websocket_connected":
        runtime_state.websocket_connected,

        "reconnect_attempts":
        runtime_state.reconnect_attempts,

        "last_heartbeat":
        runtime_state.last_heartbeat.isoformat() if runtime_state.last_heartbeat else None,

        "last_tick_received_at":
        runtime_state.last_tick_received_at.isoformat() if runtime_state.last_tick_received_at else None,

        "cooldown_until":
        runtime_state.cooldown_until.isoformat() if runtime_state.cooldown_until else None,

        "emergency_reason":
        runtime_state.emergency_reason.value if runtime_state.emergency_reason else None,

        "session_pnl":
        runtime_state.session_pnl,

        "session_drawdown":
        runtime_state.session_drawdown,

        "active_positions":
        len(
            [
                position
                for position in (
                    exchange.positions
                    .values()
                )
                if position.quantity != 0
            ]
        ),

        "active_orders":
        runtime_state.active_orders,

        "runtime_uptime_seconds":
        (
            int(
                (
                    datetime.utcnow()
                    -
                    runtime_state.started_at
                ).total_seconds()
            )
            if runtime_state.started_at
            else 0
        ),

        "started_at":
        runtime_state.started_at.isoformat() if runtime_state.started_at else None,

        "active_session_id":
        runtime_state.active_session_id,

        "current_unrealized_pnl":
        runtime_state.current_unrealized_pnl,

        "current_unrealized_pnl_percent":
        runtime_state.current_unrealized_pnl_percent,

        "last_execution_price":
        runtime_state.last_execution_price,

        "portfolio": {
        "available_capital":
            available_capital,

        "invested_capital":
            invested_capital,

        "total_portfolio_value":
            total_portfolio_value,
        },

        "active_trades":
        active_trades,
    }

@app.post(f"{API_PREFIX}/runtime/start")
def start_runtime():
    try:
        runtime_controller.start_runtime()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {
        "success": True,
        "runtime_running": runtime_controller.is_running(),
    }

@app.post(f"{API_PREFIX}/runtime/stop")
def stop_runtime():
    try:
        runtime_controller.stop_runtime()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {
        "success": True,
        "runtime_running": runtime_controller.is_running(),
    }

@app.post(f"{API_PREFIX}/runtime/pause")
def pause_runtime():
    try:
        runtime_controller.pause_runtime()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {
        "success": True,
        "runtime_paused": runtime_controller.is_paused(),
    }

@app.post(f"{API_PREFIX}/runtime/resume")

def resume_runtime():
    try:
        runtime_controller.resume_runtime()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {
        "success": True,
        "runtime_paused": runtime_controller.is_paused(),
    }


@app.post(f"{API_PREFIX}/runtime/emergency-stop")
def emergency_stop():
    try:
        runtime_controller.emergency_stop()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {"success": True, "status": "emergency_stop"}


@app.post(f"{API_PREFIX}/runtime/shutdown")
def shutdown_runtime():
    try:
        runtime_controller.shutdown_runtime()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {"success": True, "status": "shutdown"}


@app.get(
    f"{API_PREFIX}/runtime/recovery-status",
    response_model=RecoveryStatusResponse,
)
def get_recovery_status():
    """Returns whether recovery is currently allowed."""
    runtime_state = runtime_controller.runtime_state
    if runtime_state is None:
        return {"recovery_allowed": False, "reason": "Runtime not initialized"}

    from src.runtime.runtime_enums import RuntimeStatus
    status = runtime_state.status

    if status == RuntimeStatus.EMERGENCY_STOP:
        return {
            "recovery_allowed": True,
            "reason": "Recovery flow available after emergency stop",
            "emergency_reason": runtime_state.emergency_reason.value if runtime_state.emergency_reason else None,
            "status": status.value,
        }

    return {
        "recovery_allowed": False,
        "reason": f"Recovery not required in state: {status.value}",
        "status": status.value,
    }


@app.post(
    f"{API_PREFIX}/runtime/recover",
    response_model=GovernanceResponse,
)
def attempt_recovery():
    """Attempt recovery after emergency stop — transitions to PAUSED."""
    try:
        runtime_controller.recover_runtime()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {"success": True, "status": "paused", "message": "Recovery complete — runtime paused"}


@app.post(
    f"{API_PREFIX}/runtime/safe-mode",
    response_model=GovernanceResponse,
)
def toggle_safe_mode():
    try:
        if runtime_controller.safe_mode:
            runtime_controller.disable_safe_mode()
        else:
            runtime_controller.enable_safe_mode()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return {
        "success": True,
        "safe_mode": runtime_controller.safe_mode,
    }


@app.post(
    f"{API_PREFIX}/runtime/enable-trading",
    response_model=GovernanceResponse,
)
def enable_trading():

    try:

        runtime_controller.enable_trading()

    except RuntimeError as e:

        raise HTTPException(
            status_code=409,
            detail=str(e),
        )

    return {
        "success": True,
        "trading_enabled": True,
    }


@app.post(
    f"{API_PREFIX}/runtime/disable-trading",
    response_model=GovernanceResponse,
)
def disable_trading():

    try:

        runtime_controller.disable_trading()

    except RuntimeError as e:

        raise HTTPException(
            status_code=409,
            detail=str(e),
        )

    return {
        "success": True,
        "trading_enabled": False,
    }


@app.post(f"{API_PREFIX}/session/start")
def start_session():
    """Start a trading session. Governed by runtime state."""
    try:
        result = runtime_controller.start_session()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return {"success": True, **result}


@app.post(f"{API_PREFIX}/session/stop")
def stop_session():
    """Stop the active trading session without changing runtime state."""
    try:
        result = runtime_controller.stop_session()
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return {"success": True, **result}



@app.get(
    f"{API_PREFIX}/sessions/active",
    response_model=SessionResponse,
)
def active_session():
    return session_status()


@app.get(f"{API_PREFIX}/sessions")
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
    f"{API_PREFIX}/sessions/analytics"
)
def get_session_analytics():

    analytics = (
        session_repository
        .get_session_analytics()
    )

    return analytics


@app.get(
    f"{API_PREFIX}/sessions/{{session_id}}"
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
    f"{API_PREFIX}/sessions/{{session_id}}/trades"
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
    f"{API_PREFIX}/sessions/{{session_id}}/analytics"
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
    f"{API_PREFIX}/trades/analytics"
)
def get_trade_analytics():

    analytics = (
        trade_repository
        .get_trade_analytics()
    )

    return analytics
@app.get(
    f"{API_PREFIX}/analytics/summary"
)
def get_analytics():

    analytics = (
        session_repository
        .get_session_analytics()
    )

    total_sessions = (
        analytics.get(
            "total_sessions",
            0,
        ) or 0
    )

    total_trades = (
        analytics.get(
            "total_trades",
            0,
        ) or 0
    )

    total_pnl = float(
        analytics.get(
            "total_pnl",
            0.0,
        ) or 0.0
    )

    winning_trades = (
        analytics.get(
            "winning_trades",
            0,
        ) or 0
    )

    best_trade = float(
        analytics.get(
            "best_trade",
            0.0,
        ) or 0.0
    )

    worst_trade = float(
        analytics.get(
            "worst_trade",
            0.0,
        ) or 0.0
    )

    avg_pnl_per_trade = (
        total_pnl / total_trades
        if total_trades > 0
        else 0.0
    )

    overall_win_rate = (
        (
            winning_trades
            /
            total_trades
        ) * 100
        if total_trades > 0
        else 0.0
    )
    
    return {
        "total_sessions":
            total_sessions,

        "total_trades":
            total_trades,

        "overall_win_rate":
            overall_win_rate,

        "total_pnl":
            total_pnl,

        "avg_pnl_per_trade":
            avg_pnl_per_trade,

        "best_trade":
            best_trade,

        "worst_trade":
            worst_trade,
    }

@app.get(
    "/api/v1/session/status",
    response_model=SessionResponse,
)
def session_status():

    runtime_state = (
        runtime_controller
        .runtime_state
    )

    if runtime_state is None:

        return {
            "session_active": False,
            "active_session_id": None,
            "session_started_at": None,
            "session_duration_seconds": 0,
            "session_pnl": 0.0,
            "total_trades": 0,
            "status": "uninitialized",
        }

    active = (
        runtime_state
        .active_session_id
        is not None
    )

    duration_seconds = 0

    session_started_at = None

    if active:

        session_started_at = (
            runtime_state
            .session_started_at
        )

        if (
            session_started_at
            is not None
        ):

            duration_seconds = int(
                (
                    datetime.utcnow()
                    -
                    session_started_at
                ).total_seconds()
            )

    total_trades = (
        runtime_state.total_trades
        if active
        else 0
    )

    return {
        "session_active":
        active,

        "active_session_id":
        runtime_state
        .active_session_id,

        "session_started_at":
        session_started_at,

        "session_duration_seconds":
        duration_seconds,

        "session_pnl":
        runtime_state
        .session_pnl,

        "total_trades":
        total_trades,

        "status":
        (
            "active"
            if active
            else "inactive"
        ),
    }