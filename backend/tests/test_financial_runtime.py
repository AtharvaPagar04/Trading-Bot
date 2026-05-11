from src.runtime.financial_runtime import (
    FinancialRuntime,
)

runtime = (
    FinancialRuntime()
)

runtime.execute_trade(
    symbol="BTCUSDT",

    market_price=100000,

    quantity=0.1,
)

runtime.update_market(
    symbol="BTCUSDT",

    market_price=105000,
)

runtime.portfolio_status()