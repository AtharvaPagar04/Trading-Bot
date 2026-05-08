import numpy as np
import pandas as pd


def calculate_adx(
    df: pd.DataFrame,
    period: int = 14,
) -> pd.Series:
    high = df["high"]
    low = df["low"]
    close = df["close"]

    plus_dm = high.diff()
    minus_dm = low.diff() * -1

    plus_dm = np.where(
        (plus_dm > minus_dm) & (plus_dm > 0),
        plus_dm,
        0,
    )

    minus_dm = np.where(
        (minus_dm > plus_dm) & (minus_dm > 0),
        minus_dm,
        0,
    )

    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()

    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    atr = tr.rolling(period).mean()

    plus_di = 100 * (
        pd.Series(plus_dm).rolling(period).mean() / atr
    )

    minus_di = 100 * (
        pd.Series(minus_dm).rolling(period).mean() / atr
    )

    dx = (
        (plus_di - minus_di).abs()
        / (plus_di + minus_di)
    ) * 100

    adx = dx.rolling(period).mean()

    return adx