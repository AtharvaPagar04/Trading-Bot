from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)


def update_unrealized_pnl(
    portfolio: PaperPortfolio,
    market_prices: dict[str, float],
):

    unrealized_pnl = 0.0

    for (
        symbol,
        position,
    ) in portfolio.positions.items():

        market_price = (
            market_prices.get(symbol)
        )

        if market_price is None:
            continue

        pnl = (
            (
                market_price
                -
                position.average_entry_price
            )
            *
            position.quantity
        )

        unrealized_pnl += pnl

    portfolio.unrealized_pnl = (
        unrealized_pnl
    )

def calculate_total_equity(
    portfolio: PaperPortfolio,
    market_prices: dict[str, float],
) -> float:

    position_value = 0.0

    for (
        symbol,
        position,
    ) in portfolio.positions.items():

        market_price = (
            market_prices.get(symbol)
        )

        if market_price is None:
            continue

        position_value += (
            market_price
            *
            position.quantity
        )

    return (
        portfolio.cash_balance
        +
        position_value
    )