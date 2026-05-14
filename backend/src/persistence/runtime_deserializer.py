from datetime import datetime

from src.core.state import (
    MarketState,
)

from src.core.session import (
    TradingSession,
)

from src.risk.risk_sync import (
    RiskSyncState,
)

from src.risk.session_risk import (
    SessionRiskState,
)

from src.strategy.regime import (
    RegimeState,
)

from src.strategy.volatility import (
    VolatilityState,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)

from src.runtime.runtime_transition_models import (
    RuntimeTransitionRecord,
)


def parse_datetime(
    value,
):

    if value is None:

        return None

    return datetime.fromisoformat(
        value
    )


def deserialize_market_state(
    data,
) -> MarketState:

    return MarketState(
        timeframe=
        data["timeframe"],

        adx=
        data["adx"],

        atr_percent=
        data["atr_percent"],

        regime_state=
        RegimeState(
            data["regime_state"]
        ),

        volatility_state=
        VolatilityState(
            data["volatility_state"]
        ),

        allow_entries=
        data["allow_entries"],
    )


def deserialize_session(
    data,
) -> TradingSession:

    return TradingSession(
        session_id=
        data["session_id"],

        start_time=
        parse_datetime(
            data["start_time"]
        ),

        starting_capital=
        data["starting_capital"],

        current_capital=
        data["current_capital"],

        session_pnl_percent=
        data["session_pnl_percent"],

        peak_pnl_percent=
        data["peak_pnl_percent"],

        entries_enabled=
        data["entries_enabled"],
    )


def deserialize_risk_state(
    data,
) -> RiskSyncState:

    return RiskSyncState(
        risk_state=
        SessionRiskState(
            data["risk_state"]
        ),

        entries_allowed=
        data["entries_allowed"],

        size_multiplier=
        data["size_multiplier"],
    )


def deserialize_transition_history(
    data,
):

    records = []

    for item in data:

        records.append(
            RuntimeTransitionRecord(
                previous_state=
                RuntimeStatus(
                    item[
                        "previous_state"
                    ]
                ),

                next_state=
                RuntimeStatus(
                    item[
                        "next_state"
                    ]
                ),

                reason=
                item["reason"],

                timestamp=
                parse_datetime(
                    item[
                        "timestamp"
                    ]
                ),
            )
        )

    return records


def deserialize_runtime_mode(
    value,
):

    return RuntimeMode(
        value
    )


def deserialize_runtime_status(
    value,
):

    return RuntimeStatus(
        value
    )


def deserialize_emergency_reason(
    value,
):

    if value is None:

        return None

    return EmergencyReason(
        value
    )