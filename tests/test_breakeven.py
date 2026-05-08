from src.validation.breakeven import (
    calculate_minimum_grid_spacing,
)

minimum_spacing = (
    calculate_minimum_grid_spacing(
        maker_fee_pct=0.10,
        taker_fee_pct=0.10,
        spread_pct=0.05,
        slippage_pct=0.05,
    )
)

print(
    f"Minimum profitable grid spacing: "
    f"{minimum_spacing}%"
)
