from src.core.runtime import (
    RuntimeState,
)

from src.core.state_builder import (
    build_market_state,
)

from src.core.session_builder import (
    create_trading_session,
)

from src.risk.risk_sync import (
    synchronize_risk_state,
)
from datetime import (
    datetime,
)
from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
)
def build_runtime_state(
    capital: float,
    timeframe: str,
    adx_value: float,
    atr_percent: float,
) -> RuntimeState:
    market_state = build_market_state(
        timeframe=timeframe,
        adx_value=adx_value,
        atr_percent=atr_percent,
    )

    session = create_trading_session(
        starting_capital=capital
    )

    risk_state = (
        synchronize_risk_state(
            session
        )
    )

    return RuntimeState(
        operating_state="NORMAL",
        market_state=market_state,

        session=session,
        safe_mode=False,
        risk_state=risk_state,

        active_events=[],
        event_history=[],
        session_started_at=
        datetime.utcnow(),
        runtime_uptime_seconds=0,
        last_tick_received_at=None,
        websocket_connected=False,
        reconnect_attempts=0,
        mode=RuntimeMode.DRY_RUN,

        status=RuntimeStatus.STARTING,

        started_at=datetime.utcnow(),

        last_heartbeat=datetime.utcnow(),

        is_trading_enabled=True,
    )