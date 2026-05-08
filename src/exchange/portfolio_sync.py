from src.exchange.paper_exchange import (
    PaperExchange,
)

from src.exchange.portfolio import (
    PortfolioState,
)


def synchronize_portfolio(
    exchange: PaperExchange,

    market_prices:
    dict[str, float],
) -> PortfolioState:

    total_exposure = 0.0

    position_value = 0.0

    for (
        symbol,
        position
    ) in (
        exchange.positions.items()
    ):

        market_price = (
            market_prices.get(
                symbol,

                position.average_price,
            )
        )

        market_value = (
            position.quantity
            * market_price
        )

        position_value += (
            market_value
        )

        total_exposure += (
            market_value
        )

    cash_balance = (
        exchange.balance
        .available_capital
    )

    total_portfolio_value = (
        cash_balance
        + position_value
    )

    unrealized_pnl = (
        total_portfolio_value
        -
        exchange.balance
        .total_capital
    )

    return PortfolioState(
        balance=
        exchange.balance,

        positions=
        exchange.positions,

        cash_balance=
        cash_balance,

        position_value=
        position_value,

        total_portfolio_value=
        total_portfolio_value,

        unrealized_pnl=
        unrealized_pnl,

        total_exposure=
        total_exposure,
    )