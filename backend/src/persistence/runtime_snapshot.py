import json

from datetime import datetime

from dataclasses import asdict

from pathlib import Path

from src.core.runtime import (
    RuntimeState,
)

from src.strategy.strategy_state import (
    StrategyState,
)

from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)

from src.risk.drawdown_tracker import (
    DrawdownState,
)


SNAPSHOT_PATH = (
    "data/runtime/runtime_snapshot.json"
)


def serialize_datetimes(
    value,
):

    if isinstance(
        value,
        dict,
    ):

        return {
            key:
            serialize_datetimes(
                item
            )
            for key, item
            in value.items()
        }

    if isinstance(
        value,
        list,
    ):

        return [
            serialize_datetimes(
                item
            )
            for item in value
        ]

    if isinstance(
        value,
        datetime,
    ):

        return (
            value.isoformat()
        )

    return value


def persist_runtime_snapshot(
    runtime: RuntimeState,

    strategy_state: (
        StrategyState
    ),

    portfolio: (
        PaperPortfolio
    ),

    drawdown_state: (
        DrawdownState
    ),
) -> None:

    path = Path(
        SNAPSHOT_PATH
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    snapshot = {

        "runtime":
        asdict(runtime),

        "strategy_state":
        asdict(
            strategy_state
        ),

        "portfolio":
        asdict(
            portfolio
        ),

        "drawdown_state":
        asdict(
            drawdown_state
        ),
    }

    snapshot = (
        serialize_datetimes(
            snapshot
        )
    )

    with open(path, "w") as file:

        json.dump(
            snapshot,
            file,
            indent=4,
        )