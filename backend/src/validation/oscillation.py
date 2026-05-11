import pandas as pd


def measure_oscillation_frequency(
    df: pd.DataFrame,
    threshold_pct: float,
) -> dict:
    close_prices = df["close"]

    pct_moves = (
        close_prices.pct_change().abs() * 100
    )

    oscillation_count = (
        pct_moves >= threshold_pct
    ).sum()

    total_candles = len(df)

    oscillation_ratio = (
        oscillation_count / total_candles
    )

    return {
        "threshold_pct": threshold_pct,
        "oscillation_count": int(oscillation_count),
        "total_candles": total_candles,
        "oscillation_ratio": float(
            round(oscillation_ratio, 4)
        ),
    }