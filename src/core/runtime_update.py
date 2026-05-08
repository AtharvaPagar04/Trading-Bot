from src.core.runtime import (
    RuntimeState,
)

from src.core.session_update import (
    update_session_after_trade,
)

from src.risk.risk_events import (
    generate_risk_events,
)

from src.risk.risk_sync import (
    synchronize_risk_state,
)


def process_runtime_trade(
    runtime: RuntimeState,
    realized_pnl: float,
) -> RuntimeState:
    previous_risk_state = (
        runtime.risk_state.risk_state
    )

    runtime.session = (
        update_session_after_trade(
            session=runtime.session,
            realized_pnl=realized_pnl,
        )
    )

    runtime.risk_state = (
        synchronize_risk_state(
            runtime.session
        )
    )

    new_events = generate_risk_events(
        previous_state=
        previous_risk_state,

        current_state=
        runtime.risk_state,
    )

    runtime.active_events.extend(
        new_events
    )

    return runtime