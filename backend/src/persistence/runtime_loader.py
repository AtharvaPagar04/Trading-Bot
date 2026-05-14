from src.persistence.runtime_deserializer import (
    deserialize_market_state,
    deserialize_session,
    deserialize_risk_state,
    deserialize_transition_history,
    deserialize_runtime_mode,
    deserialize_runtime_status,
    deserialize_emergency_reason,
    parse_datetime,
)
from datetime import datetime
from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)
from src.core.runtime_builder import (
    build_runtime_state,
)
from src.core.runtime import (
    RuntimeState,
)
import json
SNAPSHOT_PATH = (
    "data/runtime/runtime_snapshot.json"
)
from src.events.event import (
    EventType,
    RuntimeEvent,
)
from src.strategy.strategy_state import (
    StrategyState,
)
from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)

from src.risk.drawdown_tracker import (
    DrawdownState,
)
from src.runtime.runtime_enums import (
    RuntimeStatus,
)

def load_runtime_snapshot(
    full_snapshot: bool = False,

) -> RuntimeState:

    try:

        with open(
            SNAPSHOT_PATH,
            "r",
        ) as file:

            data = json.load(
                file
            )

    except FileNotFoundError:

        print(
            "[PERSISTENCE] "
            "Runtime snapshot missing "
            "- building fresh runtime"
        )

        from src.core.runtime_builder import (
            build_runtime_state,
        )

        return build_runtime_state()

    except Exception as e:

        print(
            f"[CRITICAL] [PERSISTENCE] "
            f"Runtime snapshot load failed: {e}"
        )

        from src.core.runtime_builder import (
            build_runtime_state,
        )

        return build_runtime_state()

    market_state = (
        deserialize_market_state(
            data["runtime"]
            ["market_state"]
        )
    )

    session = (
        deserialize_session(
            data["runtime"]["session"]
        )
    )

    

    risk_state = (
        deserialize_risk_state(
            data["runtime"]["risk_state"]
        )
    )

    transition_history = (
        deserialize_transition_history(
            data["runtime"].get(
                "transition_history",
                [],
            )
        )
    )
    active_events = []
    for event in data["runtime"]["active_events"]:
        active_events.append(
            RuntimeEvent(
                event_type=
                EventType(
                    event["event_type"]
                ),

                emitted_at=
                datetime.fromisoformat(
                    event.get("emitted_at", event.get("timestamp"))
                ),

                message=
                event["message"],
            )
        )

    event_history = []

    for event in (
        data["runtime"]["event_history"]
    ):
        event_history.append(
            RuntimeEvent(
                event_type=
                EventType(
                    event["event_type"]
                ),

                emitted_at=
                datetime.fromisoformat(
                    event.get("emitted_at", event.get("timestamp"))
                ),

                message=
                event["message"],
            )
        )
    
    active_session_id = (
        data["runtime"]
        ["active_session_id"]
    )

    runtime_status = (
        deserialize_runtime_status(
            data["runtime"]["status"]
        )
    )

    session_started_at = (
        parse_datetime(
            data["runtime"]
            ["session_started_at"]
        )
    )

    total_trades = (
        data["runtime"]
        ["total_trades"]
    )

    if (
        active_session_id is None
         or
        runtime_status != RuntimeStatus.RUNNING
    ):

        session_started_at = None
        total_trades = 0

    active_events = []
    runtime = RuntimeState(

        market_state=
            market_state,

        session=
            session,

        risk_state=
            risk_state,

        safe_mode=
            data["runtime"]
            ["safe_mode"],

        active_events=
            active_events,

        event_history=
            event_history,

        transition_history=
        transition_history,

        total_trades=
            total_trades,

        winning_trades=
        data["runtime"]
        ["winning_trades"],

        losing_trades=
            data["runtime"]
            ["losing_trades"],

        latest_price=
            data["runtime"]
            ["latest_price"],

        operating_state=
            data["runtime"]
            .get(
                "operating_state"
            ),

        last_execution_price=
            data["runtime"]
            ["last_execution_price"],

        last_execution_time=
            parse_datetime(
                data["runtime"]
                ["last_execution_time"]
            ),

        latest_candle_close=
            data["runtime"]
            ["latest_candle_close"],

        latest_candle_timestamp=
            parse_datetime(
                data["runtime"]
                ["latest_candle_timestamp"]
            ),

        current_unrealized_pnl=
            data["runtime"]
            ["current_unrealized_pnl"],

        current_unrealized_pnl_percent=
            data["runtime"]
            [
                "current_unrealized_pnl_percent"
            ],

        session_started_at=
            session_started_at,

        runtime_uptime_seconds=
            data["runtime"]
            ["runtime_uptime_seconds"],

        active_session_id=
            active_session_id,

        last_tick_received_at=
            parse_datetime(
                data["runtime"]
                ["last_tick_received_at"]
            ),

        websocket_connected=
            data["runtime"]
            ["websocket_connected"],

        reconnect_attempts=
            data["runtime"]
            ["reconnect_attempts"],

        mode=
            deserialize_runtime_mode(
                data["runtime"]
                ["mode"]
            ),

        status=runtime_status,

        started_at=
            parse_datetime(
                data["runtime"]
                ["started_at"]
            ),

        last_heartbeat=
            parse_datetime(
                data["runtime"]
                ["last_heartbeat"]
            ),

        cooldown_until=
            parse_datetime(
                data["runtime"]
                ["cooldown_until"]
            ),

        emergency_reason=
            deserialize_emergency_reason(
                data["runtime"]
                ["emergency_reason"]
            ),

        session_pnl=
            data["runtime"]["session_pnl"],

        session_drawdown=
            data["runtime"]["session_drawdown"],

        active_positions=
            data["runtime"]
            ["active_positions"],

        active_orders=
            data["runtime"]
            ["active_orders"],

        is_trading_enabled=
            data["runtime"]
            ["is_trading_enabled"],
    )
    runtime_log(
        level=LogLevel.WARNING,
        category=LogCategory.PERSISTENCE,
        message=(
            f"Recovered session state | "
            f"active_session_id={runtime.active_session_id} | "
            f"session_started_at={runtime.session_started_at}"
        ),
    )

    strategy_state = (
        StrategyState(
            **data[
                "strategy_state"
            ]
        )
    )


    portfolio = (
        PaperPortfolio(
            **data[
                "portfolio"
            ]
        )
    )

    drawdown_state = (
        DrawdownState(
            **data[
                "drawdown_state"
            ]
        )
    )

    if full_snapshot:

        return {

            "runtime":
                runtime,

            "strategy_state":
                strategy_state,

            "portfolio":
                portfolio,

            "drawdown_state":
                drawdown_state,
        }

    return runtime
def safe_load_runtime_snapshot():

    runtime = (
        load_runtime_snapshot()
    )

    if runtime is not None:

        return runtime

    runtime_log(
        level=LogLevel.WARNING,

        category=LogCategory.PERSISTENCE,

        message=(
            "Falling back to clean "
            "runtime initialization"
        ),
    )

    return build_runtime_state(
        capital=1000,

        timeframe="5m",

        adx_value=20,

        atr_percent=1.0,
    )