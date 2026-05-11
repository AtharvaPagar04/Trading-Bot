from src.backtest.analytics_models import (
    PerformanceReport,
)

from src.exchange.models import (
    CompletedTrade,
)


def generate_performance_report(
    completed_trades:
    list[CompletedTrade],
) -> PerformanceReport:

    total_trades = len(
        completed_trades
    )

    if total_trades == 0:

        return PerformanceReport(
            total_trades=0,

            winning_trades=0,

            losing_trades=0,

            win_rate=0.0,

            total_realized_pnl=0.0,

            average_trade_pnl=0.0,

            best_trade=0.0,

            worst_trade=0.0,
        )

    pnls = [
        trade.realized_pnl
        for trade
        in completed_trades
    ]

    winning_trades = len(
        [
            pnl
            for pnl
            in pnls
            if pnl > 0
        ]
    )

    losing_trades = len(
        [
            pnl
            for pnl
            in pnls
            if pnl < 0
        ]
    )

    win_rate = (
        winning_trades
        / total_trades
    ) * 100

    total_realized_pnl = (
        sum(pnls)
    )

    average_trade_pnl = (
        total_realized_pnl
        / total_trades
    )

    best_trade = max(
        pnls
    )

    worst_trade = min(
        pnls
    )

    return PerformanceReport(
        total_trades=
        total_trades,

        winning_trades=
        winning_trades,

        losing_trades=
        losing_trades,

        win_rate=
        win_rate,

        total_realized_pnl=
        total_realized_pnl,

        average_trade_pnl=
        average_trade_pnl,

        best_trade=
        best_trade,

        worst_trade=
        worst_trade,
    )