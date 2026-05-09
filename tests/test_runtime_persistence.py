from src.strategy.strategy_state import (
    StrategyState,
)

from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)

from src.risk.drawdown_tracker import (
    DrawdownState,
)

from src.persistence.runtime_snapshot import (
    persist_runtime_snapshot,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

from src.core.runtime import (
    RuntimeState,
)

from src.core.state import (
    MarketState,
    RegimeState,
    VolatilityState,
)

from src.core.session import (
    TradingSession,
)

from src.risk.risk_sync import (
    RiskSyncState,
)

from src.risk.session_risk import (
    SessionRiskState,
)

from datetime import datetime


def test_runtime_snapshot_roundtrip():

    runtime = RuntimeState(
        operating_state="NORMAL",

        market_state=MarketState(
            timeframe="5m",

            adx=25,

            atr_percent=1.0,

            regime_state=
            RegimeState.SAFE,

            volatility_state=
            VolatilityState.NORMAL,

            allow_entries=True,
        ),

        session=TradingSession(
            session_id="test",

            start_time=
            datetime.utcnow(),

            starting_capital=1000,

            current_capital=1000,

            session_pnl_percent=0.0,

            peak_pnl_percent=0.0,

            entries_enabled=True,
        ),

        safe_mode=False,

        risk_state=RiskSyncState(
            risk_state=
            SessionRiskState.NORMAL,

            entries_allowed=True,

            size_multiplier=1.0,
        ),

        active_events=[],

        event_history=[],
    )

    strategy_state = (
        StrategyState()
    )

    portfolio = (
        PaperPortfolio()
    )

    drawdown_state = (
        DrawdownState(
            peak_equity=1000.0,
            current_drawdown_percent=0.0,
        )
    )

    persist_runtime_snapshot(
        runtime=runtime,

        strategy_state=
        strategy_state,

        portfolio=portfolio,

        drawdown_state=
        drawdown_state,
    )

    restored = (
        load_runtime_snapshot(
            full_snapshot=True
        )
    )

    assert (
        restored["runtime"]
        .operating_state
        ==
        "NORMAL"
    )

    assert (
        restored[
            "drawdown_state"
        ]
        .peak_equity
        ==
        1000.0
    )