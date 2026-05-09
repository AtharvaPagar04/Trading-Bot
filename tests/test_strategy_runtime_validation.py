from datetime import datetime

from src.core.runtime import (
    RuntimeState,
)
from src.strategy.regime import (
    RegimeState,
)

from src.strategy.volatility import (
    VolatilityState,
)
from src.core.strategy_runtime import (
    execute_strategy_cycle,
)

from src.core.session import (
    TradingSession,
)

from src.core.state import (
    MarketState,
)

from src.events.event import (
    RuntimeEvent,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

from src.market.market_data import (
    Candle,
    MarketDataSnapshot,
)

from src.risk.risk_sync import (
    RiskSyncState,
)

from src.strategy.models import (
    TradeSignal,
)
from src.risk.session_risk import (
    SessionRiskState,
)
from src.exchange.models import (
    Position,
)
from src.strategy.strategy_state import (
    StrategyState,
)
def create_runtime() -> RuntimeState:

    return RuntimeState(
        market_state=MarketState(
            timeframe="5m",

            adx=20,

            atr_percent=1.0,

            regime_state=
            RegimeState.SAFE,

            volatility_state=
            VolatilityState.NORMAL,

            allow_entries=True,
        ),

        session=TradingSession(
            session_id="test-session",

            start_time=
            datetime.utcnow(),

            starting_capital=2000,

            current_capital=2000,

            session_pnl_percent=0,

            peak_pnl_percent=0,

            entries_enabled=True,
        ),

        risk_state=RiskSyncState(
            risk_state=
            SessionRiskState.NORMAL,
            entries_allowed=True,
            size_multiplier=1.0,
        ),

        safe_mode=False,

        operating_state="NORMAL",

        active_events=[],

        event_history=[],
    )


def create_snapshot() -> MarketDataSnapshot:

    candles = []

    base_price = 100

    for i in range(20):

        candles.append(
            Candle(
                timestamp=
                datetime.utcnow(),

                open=base_price,

                high=base_price + 1,

                low=base_price - 1,

                close=base_price,

                volume=1000,
            )
        )

    candles[-1].close = 95

    return MarketDataSnapshot(
        symbol="BTC/USDT",
        timeframe="5m",
        candles=candles,
    )


def create_candle() -> Candle:

    return Candle(
        timestamp=datetime.utcnow(),
        open=95,
        high=96,
        low=94,
        close=95,
        volume=1000,
    )


def test_buy_signal_executes():

    runtime = create_runtime()

    exchange = PaperExchange(
        starting_capital=2000
    )

    snapshot = create_snapshot()

    candle = create_candle()

    result = execute_strategy_cycle(
        runtime=runtime,
        exchange=exchange,
        snapshot=snapshot,
        candle=candle,
        state=StrategyState(),
    )

    assert (
        result.signal
        ==
        TradeSignal.BUY
    )

    assert result.executed is True

    assert (
        len(exchange.positions)
        ==
        1
    )


def test_buy_blocked_when_position_exists():

    runtime = create_runtime()

    exchange = PaperExchange(
        starting_capital=2000
    )

    exchange.positions["BTC/USDT"] = (
        Position(
            symbol="BTC/USDT",
            quantity=1,
            average_price=100,
        )
    )

    snapshot = create_snapshot()

    candle = create_candle()

    result = execute_strategy_cycle(
        runtime=runtime,
        exchange=exchange,
        snapshot=snapshot,
        candle=candle,
        state=StrategyState(),
    )

    assert (
        result.signal
        ==
        TradeSignal.BUY
    )

    assert result.executed is False
def test_sell_signal_executes():

    runtime = create_runtime()

    exchange = PaperExchange(
        starting_capital=2000
    )

    from src.exchange.models import (
        Position,
    )

    exchange.positions["BTC/USDT"] = (
        Position(
            symbol="BTC/USDT",

            quantity=1,

            average_price=120,
        )
    )

    snapshot = create_snapshot()

    snapshot.candles[-1].close = 105

    candle = Candle(
        timestamp=datetime.utcnow(),
        open=105,
        high=106,
        low=104,
        close=105,
        volume=1000,
    )

    result = execute_strategy_cycle(
        runtime=runtime,
        exchange=exchange,
        snapshot=snapshot,
        candle=candle,
        state=StrategyState(),
    )

    assert (
        result.signal
        ==
        TradeSignal.SELL
    )

    assert result.executed is True

    assert (
        len(exchange.completed_trades)
        ==
        1
    )

def test_hold_signal_skips_execution():

    runtime = create_runtime()

    exchange = PaperExchange(
        starting_capital=2000
    )

    candles = []

    for _ in range(20):

        candles.append(
            Candle(
                timestamp=
                datetime.utcnow(),

                open=100,
                high=101,
                low=99,
                close=100,
                volume=1000,
            )
        )

    snapshot = MarketDataSnapshot(
        symbol="BTC/USDT",
        timeframe="5m",
        candles=candles,
    )

    candle = Candle(
        timestamp=datetime.utcnow(),
        open=100,
        high=101,
        low=99,
        close=100,
        volume=1000,
    )

    result = execute_strategy_cycle(
        runtime=runtime,
        exchange=exchange,
        snapshot=snapshot,
        candle=candle,
        state=StrategyState(),
    )

    assert (
        result.signal
        ==
        TradeSignal.HOLD
    )

    assert result.executed is False

    assert (
        len(exchange.positions)
        ==
        0
    )

    assert (
        len(exchange.completed_trades)
        ==
        0
    )