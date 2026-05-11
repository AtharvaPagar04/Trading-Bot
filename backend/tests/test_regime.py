from src.strategy.regime import (
    classify_regime,
    allow_new_entries,
)

adx_values = [
    18,
    27,
    35,
]

for value in adx_values:
    regime = classify_regime(value)

    allowed = allow_new_entries(regime)

    print(
        f"ADX: {value} | "
        f"Regime: {regime} | "
        f"Allow Entries: {allowed}"
    )