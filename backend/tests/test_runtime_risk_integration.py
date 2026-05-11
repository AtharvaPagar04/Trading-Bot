from src.core.runtime_risk_integration import (
    integrate_portfolio_risk,
)

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

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

print("INITIAL")
print(runtime.operating_state)

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

portfolio_risk = (
    evaluate_portfolio_risk(
        portfolio
    )
)

result = (
    integrate_portfolio_risk(
        runtime=runtime,

        portfolio_risk=
        portfolio_risk,
    )
)

print("\nPORTFOLIO RISK")
print(portfolio_risk)

print("\nUPDATED RUNTIME")
print(
    result.runtime
    .operating_state
)

print("\nEXECUTION")
print(
    result.execution_allowed
)

print("\nEVENTS")
for event in (
    result.runtime
    .active_events
):
    print(event)