from src.backtest.walkforward import (
    generate_walkforward_windows,
)

windows = (
    generate_walkforward_windows(
        total_size=100,

        train_size=60,

        test_size=20,
    )
)

for window in windows:

    print(window)