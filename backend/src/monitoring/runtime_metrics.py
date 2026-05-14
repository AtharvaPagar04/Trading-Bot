from dataclasses import dataclass
from datetime import datetime


@dataclass
class RuntimeMetrics:

    collected_at: datetime

    runtime_status: str

    trading_enabled: bool

    websocket_connected: bool

    reconnect_attempts: int

    active_session: bool

    active_positions: int

    active_orders: int

    portfolio_value: float

    unrealized_pnl: float

    realized_pnl: float

    total_trades: int

    runtime_uptime_seconds: int


def build_runtime_metrics(
    runtime_state,
    exchange,
) -> RuntimeMetrics:

    if runtime_state is None:
        return RuntimeMetrics(
            collected_at=datetime.utcnow(),
            runtime_status="uninitialized",
            trading_enabled=False,
            websocket_connected=False,
            reconnect_attempts=0,
            active_session=False,
            active_positions=0,
            active_orders=0,
            portfolio_value=0.0,
            unrealized_pnl=0.0,
            realized_pnl=0.0,
            total_trades=0,
            runtime_uptime_seconds=0,
        )

    portfolio_value = 0.0
    active_positions = 0
    if exchange is not None:
        portfolio_value = float(exchange.balance.available_capital)
        if runtime_state.latest_price is not None:
            for position in exchange.positions.values():
                if position.quantity != 0:
                    active_positions += 1
                    portfolio_value += position.quantity * runtime_state.latest_price

    uptime = 0
    if runtime_state.started_at is not None:
        uptime = int((datetime.utcnow() - runtime_state.started_at).total_seconds())

    return RuntimeMetrics(
        collected_at=datetime.utcnow(),
        runtime_status=runtime_state.status.value,
        trading_enabled=runtime_state.is_trading_enabled,
        websocket_connected=runtime_state.websocket_connected,
        reconnect_attempts=runtime_state.reconnect_attempts,
        active_session=runtime_state.active_session_id is not None,
        active_positions=active_positions,
        active_orders=runtime_state.active_orders,
        portfolio_value=portfolio_value,
        unrealized_pnl=runtime_state.current_unrealized_pnl,
        realized_pnl=runtime_state.session_pnl,
        total_trades=runtime_state.total_trades if runtime_state.active_session_id else 0,
        runtime_uptime_seconds=uptime,
    )
