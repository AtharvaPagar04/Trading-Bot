
import json
from datetime import datetime

from src.core.runtime import (
    RuntimeState,
)

from src.core.session import (
    TradingSession,
)
from src.risk.session_risk import (
    SessionRiskState,
)

from src.core.state import (
    MarketState,
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
from src.risk.risk_sync import (
    RiskSyncState,
)

from src.core.state import (
    RegimeState,
    VolatilityState,
)


SNAPSHOT_PATH = (
    "data/runtime/runtime_snapshot.json"
)


def load_runtime_snapshot(
    full_snapshot: bool = False,

) -> RuntimeState:

    with open(SNAPSHOT_PATH, "r") as file:
        data = json.load(file)

    market_state = MarketState(
        timeframe=
        data["runtime"]["market_state"]
        ["timeframe"],

        adx=
        data["runtime"]["market_state"]
        ["adx"],

        atr_percent=
        data["runtime"]["market_state"]
        ["atr_percent"],

        regime_state=
        RegimeState(
            data["runtime"]["market_state"]
            ["regime_state"]
        ),

        volatility_state=
        VolatilityState(
            data["runtime"]["market_state"]
            ["volatility_state"]
        ),

        allow_entries=
        data["runtime"]["market_state"]
        ["allow_entries"],
    )

    session = TradingSession(
        session_id=
        data["runtime"]["session"]
        ["session_id"],

        start_time=
        datetime.fromisoformat(
            data["runtime"]["session"]
            ["start_time"]
        ),

        starting_capital=
        data["runtime"]["session"]
        ["starting_capital"],

        current_capital=
        data["runtime"]["session"]
        ["current_capital"],

        session_pnl_percent=
        data["runtime"]["session"]
        ["session_pnl_percent"],

        peak_pnl_percent=
        data["runtime"]["session"]
        ["peak_pnl_percent"],

        entries_enabled=
        data["runtime"]["session"]
        ["entries_enabled"],
    )

    risk_state = RiskSyncState(
        risk_state=
        SessionRiskState(
            data["runtime"]["risk_state"]
            ["risk_state"]
        ),

        entries_allowed=
        data["runtime"]["risk_state"]
        ["entries_allowed"],

        size_multiplier=
        data["runtime"]["risk_state"]
        ["size_multiplier"],
    )

    active_events = []

    for event in data["runtime"]["active_events"]:
        active_events.append(
            RuntimeEvent(
                event_type=
                EventType(
                    event["event_type"]
                ),

                timestamp=
                datetime.fromisoformat(
                    event["timestamp"]
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

                timestamp=
                datetime.fromisoformat(
                    event["timestamp"]
                ),

                message=
                event["message"],
            )
        )

    runtime = RuntimeState(
        operating_state="NORMAL",

        market_state=
        market_state,

        session=session,

        safe_mode=False,

        risk_state=
            risk_state,

        active_events=
            active_events,

        event_history=
            event_history,
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