from src.core.runtime_portfolio_sync import (
    synchronize_runtime_portfolio,
)

from src.exchange.models import (
    OrderSide,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

from src.exchange.portfolio_sync import (
    synchronize_portfolio,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

exchange = PaperExchange(
    starting_capital=2000
)

exchange.execute_market_order(
    symbol="SOL/USDT",

    side=OrderSide.BUY,

    quantity=2,

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

runtime = (
    synchronize_runtime_portfolio(
        runtime=runtime,

        portfolio=portfolio,
    )
)

print("PORTFOLIO")
print(portfolio)

print("\nRUNTIME SESSION")
print(runtime.session)