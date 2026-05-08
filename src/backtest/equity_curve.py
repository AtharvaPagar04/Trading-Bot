from src.backtest.equity_models import (
    EquityCurveReport,
)


def generate_equity_curve_report(
    equity_values: list[float],
) -> EquityCurveReport:

    if len(equity_values) == 0:

        return EquityCurveReport(
            equity_curve=[],

            peak_equity=0.0,

            max_drawdown_percent=0.0,

            final_equity=0.0,
        )

    peak_equity = (
        equity_values[0]
    )

    max_drawdown_percent = 0.0

    for equity in equity_values:

        if equity > peak_equity:

            peak_equity = equity

        drawdown_percent = (
            (
                peak_equity
                - equity
            )
            / peak_equity
        ) * 100

        if (
            drawdown_percent
            >
            max_drawdown_percent
        ):

            max_drawdown_percent = (
                drawdown_percent
            )

    return EquityCurveReport(
        equity_curve=
        equity_values,

        peak_equity=
        peak_equity,

        max_drawdown_percent=
        max_drawdown_percent,

        final_equity=
        equity_values[-1],
    )