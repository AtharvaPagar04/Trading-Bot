from pydantic import BaseModel
from typing import Optional


class PortfolioResponse(
    BaseModel,
):
    available_capital: float
    invested_capital: float
    total_portfolio_value: float


class ActiveTradeResponse(
    BaseModel,
):
    symbol: str
    quantity: float
    entry_price: float

    current_price: Optional[float]

    market_data_ready: bool

    unrealized_pnl: Optional[float]

    unrealized_pnl_percent: Optional[float]


class RuntimeResponse(
    BaseModel,
):
    connected: bool

    status: str

    mode: str

    is_trading_enabled: bool

    safe_mode: bool

    latest_price: float

    latest_candle_close: float

    total_trades: int

    winning_trades: int

    losing_trades: int

    websocket_connected: bool

    reconnect_attempts: int

    last_heartbeat: Optional[str]

    last_tick_received_at: Optional[str]

    cooldown_until: Optional[str]

    emergency_reason: Optional[str]

    session_pnl: float

    session_drawdown: float

    active_positions: int

    active_orders: int

    runtime_uptime_seconds: int

    started_at: Optional[str]

    active_session_id: Optional[int]

    current_unrealized_pnl: float

    current_unrealized_pnl_percent: float

    last_execution_price: float

    portfolio: PortfolioResponse

    active_trades: list[
        ActiveTradeResponse
    ]
