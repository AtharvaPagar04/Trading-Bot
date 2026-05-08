from src.core.runtime import (
    RuntimeState,
)

from src.exchange.portfolio import (
    PortfolioState,
)


def synchronize_runtime_portfolio(
    runtime: RuntimeState,

    portfolio: PortfolioState,
) -> RuntimeState:

    runtime.session.current_capital = (
        portfolio.balance
        .available_capital
    )

    runtime.session.session_pnl_percent = (
        (
            portfolio.unrealized_pnl
            /
            runtime.session
            .starting_capital
        )
        * 100
    )

    if (
        runtime.session
        .session_pnl_percent
        >
        runtime.session
        .peak_pnl_percent
    ):
        runtime.session.peak_pnl_percent = (
            runtime.session
            .session_pnl_percent
        )

    return runtime