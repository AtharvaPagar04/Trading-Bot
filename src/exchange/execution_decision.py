from dataclasses import dataclass

from src.exchange.position_sizing import (
    PositionSizingResult,
)


@dataclass
class ExecutionDecision:
    allowed: bool

    reason: str

    position_size: PositionSizingResult | None


def evaluate_execution_decision(
    runtime_state: str,

    entries_allowed: bool,

    market_entries_allowed: bool,

    portfolio_entries_allowed: bool,

    position_size: PositionSizingResult,
) -> ExecutionDecision:

    if runtime_state == "HALTED":

        return ExecutionDecision(
            allowed=False,

            reason=
            "Runtime halted",

            position_size=None,
        )

    if not entries_allowed:

        return ExecutionDecision(
            allowed=False,

            reason=
            "Runtime entries disabled",

            position_size=None,
        )

    if not market_entries_allowed:

        return ExecutionDecision(
            allowed=False,

            reason=
            "Market regime blocked entries",

            position_size=None,
        )

    if (
        not
        portfolio_entries_allowed
    ):

        return ExecutionDecision(
            allowed=False,

            reason=
            "Portfolio risk blocked entries",

            position_size=None,
        )

    if (
        position_size
        .final_order_quantity
        <= 0
    ):

        return ExecutionDecision(
            allowed=False,

            reason=
            "Position size resolved to zero",

            position_size=None,
        )

    return ExecutionDecision(
        allowed=True,

        reason=
        "Execution approved",

        position_size=
        position_size,
    )