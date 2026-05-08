from src.portfolio.accounting_engine import (
    PortfolioAccountingEngine,
)

engine = (
    PortfolioAccountingEngine(
        initial_cash=10000
    )
)

engine.open_position(
    symbol="BTCUSDT",

    quantity=0.1,

    entry_price=100000,
)

engine.update_market_price(
    symbol="BTCUSDT",

    market_price=105000,
)

snapshot = (
    engine.portfolio_snapshot()
)

print()

print(
    "PORTFOLIO SNAPSHOT"
)

print(snapshot)

engine.close_position(
    "BTCUSDT"
)

print()

print(
    "FINAL SNAPSHOT"
)

print(
    engine.portfolio_snapshot()
)