from src.risk.drawdown_tracker import (
    DrawdownState,
    update_drawdown_state,
)


def test_drawdown_updates_correctly():

    state = DrawdownState(
        peak_equity=10000.0,
        current_drawdown_percent=0.0,
    )

    update_drawdown_state(
        current_equity=9000.0,
        state=state,
    )

    assert (
        state.current_drawdown_percent
        ==
        10.0
    )


def test_peak_equity_updates():

    state = DrawdownState(
        peak_equity=10000.0,
        current_drawdown_percent=0.0,
    )

    update_drawdown_state(
        current_equity=12000.0,
        state=state,
    )

    assert (
        state.peak_equity
        ==
        12000.0
    )

    assert (
        state.current_drawdown_percent
        ==
        0.0
    )