from dataclasses import dataclass


@dataclass
class DrawdownState:

    peak_equity: float

    current_drawdown_percent: float


def update_drawdown_state(
    current_equity: float,
    state: DrawdownState,
):

    if current_equity > state.peak_equity:

        state.peak_equity = (
            current_equity
        )

    drawdown = (
        (
            state.peak_equity
            -
            current_equity
        )
        /
        state.peak_equity
    ) * 100

    state.current_drawdown_percent = (
        drawdown
    )