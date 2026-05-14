from dataclasses import dataclass

from src.core.live_governance import (
    execute_live_governance_cycle,
)

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_portfolio_sync import (
    synchronize_runtime_portfolio,
)

from src.core.runtime_risk_integration import (
    integrate_portfolio_risk,
)

from src.exchange.execution_decision import (
    evaluate_execution_decision,
)

from src.exchange.models import (
    OrderSide,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

from src.exchange.portfolio_risk import (
    evaluate_portfolio_risk,
)

from src.exchange.portfolio_sync import (
    synchronize_portfolio,
)

from src.exchange.position_sizing import (
    calculate_position_size,
)

from src.market.market_data import (
    Candle,
    MarketDataSnapshot,
)

from src.market.streaming_runtime import (
    process_incoming_candle,
)
from src.runtime.runtime_isolation import (
    isolate_runtime_failure,
)
from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)
from src.runtime.event_types import (
    EXECUTION_EVENT,
)
from src.runtime.event_bus import (
    EventBus,
)


@dataclass
class AutonomousCycleResult:
    runtime: RuntimeState

    executed: bool

def execute_autonomous_cycle(
    runtime: RuntimeState,

    exchange: PaperExchange,

    snapshot: MarketDataSnapshot,

    candle: Candle,

    trade_side: str,

    event_bus: EventBus,
) -> AutonomousCycleResult:

    # Streaming update

    streaming = (
        isolate_runtime_failure(
            subsystem=
            "streaming_runtime",

            operation=lambda:
            process_incoming_candle(
                runtime=runtime,
                snapshot=snapshot,
                candle=candle,
            ),
        )
    )

    runtime = streaming.runtime

    # Portfolio state

    portfolio = (
        isolate_runtime_failure(
            subsystem=
            "portfolio_sync",

            operation=lambda:
            synchronize_portfolio(
                exchange=exchange,
                market_prices={
                    snapshot.symbol:
                    candle.close
                },
            ),
        )
    )

    # Portfolio risk

    portfolio_risk = (
        isolate_runtime_failure(
            subsystem=
            "portfolio_risk",

            operation=lambda:
            evaluate_portfolio_risk(
                portfolio
            ),
        )
    )

    # Runtime integration

    risk_integration = (
        isolate_runtime_failure(
            subsystem=
            "risk_integration",

            operation=lambda:
            integrate_portfolio_risk(
                runtime=runtime,
                portfolio_risk=
                portfolio_risk,
            ),
        )
    )


    runtime = (
        risk_integration.runtime
    )

    # Position sizing

    position_size = (
        isolate_runtime_failure(
            subsystem=
            "position_sizing",

            operation=lambda:
            calculate_position_size(
                available_capital=
                portfolio.balance
                .available_capital,

                asset_price=
                candle.close,

                runtime_state=
                runtime.operating_state,

                portfolio_risk=
                portfolio_risk,

                volatility_percent=
                runtime.market_state
                .atr_percent,
            ),
        )
    )

    # Execution decision

    decision = (
        isolate_runtime_failure(
            subsystem=
            "execution_decision",

            operation=lambda:
            evaluate_execution_decision(
                runtime_state=
                runtime.operating_state,

                entries_allowed=
                runtime.session
                .entries_enabled,

                market_entries_allowed=
                runtime.market_state
                .allow_entries,

                portfolio_entries_allowed=
                portfolio_risk
                .allow_new_entries,

                position_size=
                position_size,
            ),
        )
    )

    executed = False

    # Execute paper trade

    if decision.allowed:

        isolate_runtime_failure(
            subsystem=
            "exchange_execution",

            operation=lambda:
            exchange.execute_market_order(
                symbol=
                snapshot.symbol,

                side=(
                    OrderSide.BUY
                    if trade_side == "BUY"
                    else OrderSide.SELL
                ),

                quantity=
                decision
                .position_size
                .final_order_quantity,

                price=
                candle.close,
            ),
        )
    

        executed = True
        event_bus.publish(
            event_type=
            EXECUTION_EVENT,

            event_payload={
                "symbol":
                snapshot.symbol,

                "side":
                trade_side,

                "price":
                candle.close,

                "quantity":
                decision
                .position_size
                .final_order_quantity,
            },
        )
    

    # Sync updated portfolio

    updated_portfolio = (
        isolate_runtime_failure(
            subsystem=
            "post_trade_portfolio_sync",

            operation=lambda:
            synchronize_portfolio(
                exchange=exchange,

                market_prices={
                    snapshot.symbol:
                    candle.close
                },
            ),
        )
    )

    runtime = (
        isolate_runtime_failure(
            subsystem=
            "runtime_portfolio_sync",

            operation=lambda:
            synchronize_runtime_portfolio(
                runtime=runtime,

                portfolio=
                updated_portfolio,
            ),
        )
    )

    return AutonomousCycleResult(
        runtime=runtime,

        executed=executed,
    )