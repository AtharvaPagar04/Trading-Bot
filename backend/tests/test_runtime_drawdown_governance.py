from src.core.runtime_builder import (
    build_runtime_state,
)
from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
)

from src.runtime.event_bus import (
    EventBus,
)

from src.risk.drawdown_tracker import (
    DrawdownState,
)

from src.risk.runtime_drawdown_governance import (
    apply_drawdown_governance,
)


def test_drawdown_triggers_cooldown():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.start()

    state = DrawdownState(
        peak_equity=10000.0,
        current_drawdown_percent=5.0,
    )

    apply_drawdown_governance(
        runtime=runtime,
        drawdown_state=state,
    )

    assert (
        runtime.state.status
        ==
        RuntimeStatus.COOLDOWN
    )


def test_drawdown_triggers_pause():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.start()

    state = DrawdownState(
        peak_equity=10000.0,
        current_drawdown_percent=10.0,
    )

    apply_drawdown_governance(
        runtime=runtime,
        drawdown_state=state,
    )

    assert (
        runtime.state.status
        ==
        RuntimeStatus.PAUSED
    )


def test_drawdown_triggers_emergency_stop():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.start()

    state = DrawdownState(
        peak_equity=10000.0,
        current_drawdown_percent=20.0,
    )

    apply_drawdown_governance(
        runtime=runtime,
        drawdown_state=state,
    )

    assert (
        runtime.state.status
        ==
        RuntimeStatus.EMERGENCY_STOP
    )