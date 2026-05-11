from src.exchange.execution_engine import (
    ExecutionEngine,
)

from src.runtime.handlers.risk_handler import (
    evaluate_runtime_risk,
)

from src.strategy.models import (
    TradeSignal,
)

engine = (
    ExecutionEngine()
)


async def handle_execution_signal(
    signal_decision,
):

    risk_status = (
        await evaluate_runtime_risk()
    )

    if (
        not
        risk_status.trading_allowed
    ):

        print(
            "EXECUTION BLOCKED"
        )

        print(
            risk_status
        )

        return

    signal = (
        signal_decision.signal
    )

    if signal == TradeSignal.HOLD:

        return

    side = "BUY"

    if signal == TradeSignal.SELL:

        side = "SELL"

    position = (
        engine.open_position(
            symbol="BTCUSDT",

            side=side,

            quantity=0.001,

            entry_price=100000,
        )
    )

    print(
        "POSITION OPENED"
    )

    print(position)