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


@dataclass
class AutonomousCycleResult:
    runtime: RuntimeState

    executed: bool


def execute_autonomous_cycle(
    runtime: RuntimeState,

    exchange: PaperExchange,

    snapshot: MarketDataSnapshot,

    candle: Candle,
) -> AutonomousCycleResult:

    # Streaming update

    streaming = (
        process_incoming_candle(
            runtime=runtime,

            snapshot=snapshot,

            candle=candle,
        )
    )

    runtime = streaming.runtime

    # Portfolio state

    portfolio = (
        synchronize_portfolio(
            exchange
        )
    )

    # Portfolio risk

    portfolio_risk = (
        evaluate_portfolio_risk(
            portfolio
        )
    )

    # Runtime integration

    risk_integration = (
        integrate_portfolio_risk(
            runtime=runtime,

            portfolio_risk=
            portfolio_risk,
        )
    )

    runtime = (
        risk_integration.runtime
    )

    # Position sizing

    position_size = (
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
        )
    )

    # Execution decision

    decision = (
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
        )
    )

    executed = False

    # Execute paper trade

    if decision.allowed:

        exchange.execute_market_order(
            symbol=
            snapshot.symbol,

            side=
            OrderSide.BUY,

            quantity=
            decision
            .position_size
            .final_order_quantity,

            price=
            candle.close,
        )

        executed = True

    # Sync updated portfolio

    synchronize_portfolio(
        exchange=exchange,

        market_prices={
            snapshot.symbol:
            candle.close
        },
    )

    runtime = (
        synchronize_runtime_portfolio(
            runtime=runtime,

            portfolio=
            updated_portfolio,
        )
    )

    return AutonomousCycleResult(
        runtime=runtime,

        executed=executed,
    )