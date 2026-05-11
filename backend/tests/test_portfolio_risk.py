from src.exchange.models import (
    OrderSide,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

from src.exchange.portfolio_risk import (
    evaluate_portfolio_risk,
)

from src.exchange.portfolio_sync import (
    synchronize_portfolio,
)

exchange = PaperExchange(
    starting_capital=2000
)

exchange.execute_market_order(
    symbol="SOL/USDT",

    side=OrderSide.BUY,

    quantity=10,

    price=100,
)

portfolio = (
    synchronize_portfolio(
        exchange=exchange,

        market_prices={
            "SOL/USDT": 100
        },
    )
)

risk = (
    evaluate_portfolio_risk(
        portfolio
    )
)

print(risk)