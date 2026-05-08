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
) -> RuntimeState:

    with open(SNAPSHOT_PATH, "r") as file:
        data = json.load(file)

    market_state = MarketState(
        timeframe=
        data["market_state"]
        ["timeframe"],

        adx=
        data["market_state"]
        ["adx"],

        atr_percent=
        data["market_state"]
        ["atr_percent"],

        regime_state=
        RegimeState(
            data["market_state"]
            ["regime_state"]
        ),

        volatility_state=
        VolatilityState(
            data["market_state"]
            ["volatility_state"]
        ),

        allow_entries=
        data["market_state"]
        ["allow_entries"],
    )

    session = TradingSession(
        session_id=
        data["session"]
        ["session_id"],

        start_time=
        datetime.fromisoformat(
            data["session"]
            ["start_time"]
        ),

        starting_capital=
        data["session"]
        ["starting_capital"],

        current_capital=
        data["session"]
        ["current_capital"],

        session_pnl_percent=
        data["session"]
        ["session_pnl_percent"],

        peak_pnl_percent=
        data["session"]
        ["peak_pnl_percent"],

        entries_enabled=
        data["session"]
        ["entries_enabled"],
    )

    risk_state = RiskSyncState(
        risk_state=
        SessionRiskState(
            data["risk_state"]
            ["risk_state"]
        ),

        entries_allowed=
        data["risk_state"]
        ["entries_allowed"],

        size_multiplier=
        data["risk_state"]
        ["size_multiplier"],
    )

    active_events = []

    for event in data["active_events"]:
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
        data["event_history"]
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

    return RuntimeState(
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