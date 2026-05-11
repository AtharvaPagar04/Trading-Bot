from src.backtest.engine import (
    run_backtest,
)

from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

result = (
    run_backtest(
        snapshot
    )
)

print("TRADES")
print(result.total_trades)

print("\nFINAL CAPITAL")
print(result.final_capital)

print("\nPNL %")
print(result.pnl_percent)

print("\nMAX DRAWDOWN")
print(
    result
    .max_drawdown_percent
)
print("\nDIAGNOSTICS")
print(result.diagnostics)

print("\nEQUITY CURVE SIZE")
print(
    len(
        result
        .equity_curve
    )
)