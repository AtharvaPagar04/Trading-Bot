from src.backtest.equity_curve import (
    generate_equity_curve_report,
)

equity_values = [
    2000,
    2050,
    2100,
    1950,
    1980,
    2200,
    2150,
]

report = (
    generate_equity_curve_report(
        equity_values
    )
)

print(report)