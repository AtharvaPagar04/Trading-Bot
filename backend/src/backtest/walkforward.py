from src.backtest.walkforward_models import (
    WalkForwardWindow,
)


def generate_walkforward_windows(
    total_size: int,

    train_size: int,

    test_size: int,
) -> list[WalkForwardWindow]:

    windows = []

    start = 0

    while (
        start
        +
        train_size
        +
        test_size
        <= total_size
    ):

        train_start = start

        train_end = (
            start
            +
            train_size
        )

        test_start = train_end

        test_end = (
            test_start
            +
            test_size
        )

        windows.append(
            WalkForwardWindow(
                train_start=
                train_start,

                train_end=
                train_end,

                test_start=
                test_start,

                test_end=
                test_end,
            )
        )

        start += test_size

    return windows