from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    EmergencyReason,
)

from src.risk.drawdown_tracker import (
    DrawdownState,
)


def apply_drawdown_governance(
    runtime: GovernedRuntime,
    drawdown_state: DrawdownState,
):

    drawdown = (
        drawdown_state
        .current_drawdown_percent
    )

    if drawdown >= 20.0:

        runtime.emergency_stop(
            EmergencyReason
            .MAX_DRAWDOWN
        )

        return

    if drawdown >= 10.0:

        runtime.pause()

        return

    if drawdown >= 5.0:

        runtime.activate_cooldown(
            seconds=300
        )