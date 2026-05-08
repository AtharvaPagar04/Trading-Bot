import json
from pathlib import Path
from datetime import datetime

from src.runtime.runtime_state import RuntimeState

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)


RUNTIME_STATE_PATH = (
    "data/runtime/runtime_state.json"
)


def load_runtime_state():

    path = Path(RUNTIME_STATE_PATH)

    if not path.exists():
        return None

    with open(path, "r") as file:

        data = json.load(file)

    return RuntimeState(
        mode=RuntimeMode(
            data["mode"]
        ),

        status=RuntimeStatus(
            data["status"]
        ),

        started_at=datetime.fromisoformat(
            data["started_at"]
        ),

        last_heartbeat=datetime.fromisoformat(
            data["last_heartbeat"]
        ),

        cooldown_until=(
            datetime.fromisoformat(
                data["cooldown_until"]
            )
            if data.get(
                "cooldown_until"
            )
            else None
        ),

        emergency_reason=(
            EmergencyReason(
                data["emergency_reason"]
            )
            if data.get(
                "emergency_reason"
            )
            else None
        ),

        session_pnl=data[
            "session_pnl"
        ],

        session_drawdown=data[
            "session_drawdown"
        ],

        active_positions=data[
            "active_positions"
        ],

        active_orders=data[
            "active_orders"
        ],

        is_trading_enabled=data[
            "is_trading_enabled"
        ],
    )