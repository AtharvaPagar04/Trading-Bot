from src.backtest.equity_curve import (
    generate_equity_curve_report,
)

from src.backtest.models import (
    BacktestResult,
)

from src.core.strategy_runtime import (
    execute_strategy_cycle,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

from src.exchange.portfolio_sync import (
    synchronize_portfolio,
)

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)
from src.strategy.diagnostics import (
    update_strategy_diagnostics,
)

from src.strategy.diagnostics_models import (
    StrategyDiagnostics,
)

def run_backtest(
    snapshot: MarketDataSnapshot,
) -> BacktestResult:

    runtime = (
        load_runtime_snapshot()
    )

    runtime.operating_state = (
        "NORMAL"
    )

    exchange = PaperExchange(
        starting_capital=2000
    )

    executed_trades = 0

    wins = 0
    
    diagnostics = (
        StrategyDiagnostics(
            buy_signals=0,

            sell_signals=0,

            hold_signals=0,

            executed_trades=0,

            suppressed_signals=0,
        )
    )

    equity_curve = []

    candles = snapshot.candles

    for candle in candles[10:]:

        result = (
            execute_strategy_cycle(
                runtime=runtime,

                exchange=exchange,

                snapshot=snapshot,

                candle=candle,
            )
        )
        diagnostics = (
            update_strategy_diagnostics(
                diagnostics=
                diagnostics,

                signal=
                result.signal,

                executed=
                result.executed,
            )
        )

        portfolio = (
            synchronize_portfolio(
                exchange=exchange,

                market_prices={
                    snapshot.symbol:
                    candle.close
                },
            )
        )

        equity_curve.append(
            portfolio
            .total_portfolio_value
        )

        completed_trade_count = len(
            exchange.completed_trades
        )

        if (
            completed_trade_count
            >
            executed_trades
        ):

            latest_trade = (
                exchange
                .completed_trades[-1]
            )

            executed_trades += 1

            if (
                latest_trade
                .realized_pnl
                > 0
            ):

                wins += 1

    equity_report = (
        generate_equity_curve_report(
            equity_curve
        )
    )

    final_capital = (
        equity_report
        .final_equity
    )

    pnl_percent = (
        (
            final_capital
            - 2000
        )
        / 2000
    ) * 100

    win_rate = 0.0

    if executed_trades > 0:

        win_rate = (
            wins
            / executed_trades
        ) * 100

    return BacktestResult(
        total_trades=
        executed_trades,

        final_capital=
        final_capital,

        pnl_percent=
        pnl_percent,

        win_rate=
        win_rate,

        diagnostics=
        diagnostics,

        equity_curve=
        equity_curve,

        max_drawdown_percent=
        equity_report
        .max_drawdown_percent,
    )