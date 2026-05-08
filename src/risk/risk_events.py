from typing import List

from src.events.event import (
    EventType,
    RuntimeEvent,
)

from src.events.event_factory import (
    create_event,
)

from src.risk.risk_sync import (
    RiskSyncState,
)

from src.risk.session_risk import (
    SessionRiskState,
)


def generate_risk_events(
    previous_state,
    current_state: RiskSyncState,
) -> List[RuntimeEvent]:
    events = []

    if (
        previous_state
        ==
        current_state.risk_state
    ):
        return events

    if current_state.risk_state in [
        SessionRiskState.DISABLE_ENTRIES,
        SessionRiskState.STOP_SESSION,
    ]:
        events.append(
            create_event(
                EventType.COOLDOWN_STARTED,
                (
                    "Cooldown triggered "
                    "due to session risk"
                ),
            )
        )

    if (
        current_state.risk_state
        ==
        SessionRiskState
        .EMERGENCY_LIQUIDATION
    ):
        events.append(
            create_event(
                EventType
                .EMERGENCY_LIQUIDATION,
                (
                    "Emergency liquidation "
                    "triggered"
                ),
            )
        )

    if (
        current_state.risk_state
        !=
        SessionRiskState.NORMAL
    ):
        events.append(
            create_event(
                EventType.RISK_ESCALATED,
                (
                    f"Risk escalated to "
                    f"{current_state.risk_state}"
                ),
            )
        )

    return events