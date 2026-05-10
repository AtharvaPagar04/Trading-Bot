# Grid Trading Bot v3 — Canonical Architecture

# 1. Current System State

The system has evolved from:
- simple grid execution

into:
- event-driven autonomous paper trading infrastructure

The architecture currently contains:
- runtime governance
- event systems
- recovery systems
- risk orchestration
- strategy orchestration
- execution simulation
- portfolio intelligence
- live websocket ingestion
- autonomous runtime execution
- paper trading lifecycle management
- runtime observability
- runtime telemetry snapshots
- active trade lifecycle tracking
- completed trade journal infrastructure
- exposure governance
- candle aggregation runtime
- console observability renderer
- portfolio mark-to-market accounting

Primary architectural strengths:
- modular runtime separation
- governance-first execution
- exchange abstraction
- normalized runtime state
- realistic execution modeling
- runtime observability
- lifecycle visibility
- portfolio telemetry transparency

Primary architectural risks:
- overlapping ownership boundaries
- duplicated runtime abstractions
- fragmented event infrastructure
- governance layer explosion
- runtime orchestration drift

This document defines:
- canonical ownership
- authoritative modules
- runtime topology
- operational architecture
- consolidation direction

---

# 2. Canonical Runtime Ownership

## Authoritative Runtime Layer

Canonical runtime modules:

runtime/
    governed_runtime.py
    runtime_loop.py
    runtime_state.py
    runtime_enums.py
    live_tick_handler.py
    runtime_snapshot.py
    runtime_console_renderer.py

Responsibilities:
- lifecycle control
- runtime state transitions
- emergency handling
- execution permissions
- runtime orchestration
- live market tick processing
- autonomous runtime coordination
- runtime telemetry generation
- execution lifecycle visibility
- console observability rendering

Architectural principle:
Runtime governance MUST remain authoritative over:
- execution permissions
- emergency states
- runtime transitions
- governance enforcement
- runtime telemetry propagation

---

# 3. Canonical Event System

## Authoritative Event Layer

Canonical modules:

runtime/
    event_bus.py
    async_event_bus.py

Responsibilities:
- runtime communication
- event propagation
- async event coordination
- runtime synchronization

Future objective:
- centralized deterministic event topology

---

# 4. Canonical Risk Ownership

Canonical modules:

risk/
    kill_switch.py
    exposure.py
    cooldown.py
    dynamic_position_sizer.py

exchange/
    portfolio_risk.py

Responsibilities:
- capital protection
- exposure control
- drawdown management
- execution throttling
- emergency triggers
- exposure governance
- execution blocking

Risk layer MUST remain independent from:
- strategy layer
- execution layer

---

# 5. Canonical Strategy Ownership

Canonical modules:

strategy/
    regime.py
    orchestrator.py

Responsibilities:
- signal generation
- market regime interpretation
- execution recommendations

Strategy layer MUST NOT:
- place orders directly
- bypass runtime governance
- mutate portfolio state

---

# 6. Canonical Execution Ownership

Canonical modules:

exchange/
    execution_engine.py
    paper_exchange.py
    binance_websocket_client.py

Responsibilities:
- simulated fills
- fee modeling
- spread modeling
- slippage modeling
- websocket ingestion
- exchange normalization
- paper execution lifecycle
- active trade lifecycle tracking
- completed trade journaling
- realized pnl calculation
- unrealized pnl propagation
- exposure-aware execution governance

Execution layer MUST remain:
- downstream from runtime governance
- isolated from strategy ownership

---

# 6.1 Live Market Infrastructure

Canonical modules:

market/
    market_data_router.py
    timeframe_aggregator.py

exchange/
    binance_websocket_client.py

Responsibilities:
- Binance websocket connectivity
- reconnect handling
- live trade ingestion
- MarketTick normalization
- runtime tick routing
- timeframe candle aggregation
- candle-close runtime propagation

Validated capabilities:
- live Binance websocket ingestion
- reconnect protection
- runtime tick routing
- live autonomous runtime invocation
- timeframe candle aggregation
- candle-close autonomous execution
- runtime candle orchestration

Future objectives:
- heartbeat monitoring
- stale-feed detection
- multi-symbol streaming
- websocket backoff strategy

---

# 7. Autonomous Runtime Architecture

Canonical modules:

core/
    autonomous_runtime.py
    streaming_runtime.py

Responsibilities:
- runtime orchestration
- portfolio synchronization
- portfolio risk integration
- execution evaluation
- autonomous execution lifecycle
- active trade telemetry generation
- runtime snapshot generation
- portfolio telemetry synchronization
- governance-aware execution routing

Operational flow:

LIVE BINANCE TRADE
    ↓
MarketTick
    ↓
TimeframeAggregator
    ↓
Candle
    ↓
MarketDataSnapshot
    ↓
MarketDataRouter
    ↓
LiveTickHandler
    ↓
Autonomous Runtime
    ↓
Portfolio Risk Evaluation
    ↓
Execution Decision
    ↓
PaperExchange
    ↓
Portfolio Update
    ↓
Runtime Synchronization
    ↓
Runtime Snapshot
    ↓
Console Renderer

Architectural principle:
Execution authority MUST remain downstream from:
- runtime governance
- portfolio risk evaluation
- execution validation

---

# 8. Persistence Architecture

Persistence categories:

## Runtime State
Purpose:
- restart recovery
- emergency persistence
- lifecycle continuity

## Event Journal
Purpose:
- replay
- auditability
- debugging

## Runtime Metrics
Purpose:
- observability
- telemetry
- runtime diagnostics

Current persistence status:
- not yet implemented
- runtime currently fully in-memory
- shutdown clears telemetry and trade history

Next persistence objectives:
- runtime snapshot persistence
- completed trade persistence
- structured execution journaling
- replay-safe event persistence

---

# 9. Runtime Observability

Canonical modules:

runtime/
    runtime_snapshot.py
    runtime_console_renderer.py
    logger.py
    metrics.py
    event_journal.py

Validated runtime observability:
- live BTC price telemetry
- candle-close telemetry
- runtime lifecycle visibility
- execution visibility
- active trade visibility
- completed trade journal visibility
- portfolio accounting visibility
- unrealized pnl visibility
- exposure visibility
- governance halt visibility

Current runtime console sections:
- runtime status
- market telemetry
- portfolio telemetry
- active trades
- completed trade journal

Current runtime telemetry:
- latest market price
- candle close state
- runtime operating state
- exposure state
- unrealized pnl
- portfolio value
- invested capital
- holdings value
- available cash
- trade count
- active trade lifecycle
- completed trade lifecycle

Future observability goals:
- structured telemetry persistence
- websocket dashboard streaming
- historical runtime replay
- execution analytics
- equity curve rendering
- runtime metrics API

---

# 10. Paper Trading Runtime Status

Validated capabilities:
- live Binance websocket ingestion
- reconnect-safe websocket lifecycle
- autonomous candle-close execution
- runtime governance integration
- exposure-based execution blocking
- portfolio synchronization
- mark-to-market accounting
- slippage simulation
- spread simulation
- fee simulation
- active trade lifecycle tracking
- completed trade journaling
- runtime telemetry snapshots
- runtime console observability
- unrealized pnl propagation
- halted runtime state handling
- execution lifecycle visibility

Current governance capabilities:
- exposure-based runtime halting
- runtime execution blocking
- governance-controlled execution approval

Current accounting capabilities:
- invested capital tracking
- holdings valuation
- unrealized pnl tracking
- total portfolio valuation
- cash utilization tracking

Current limitations:
- no persistence layer
- no FastAPI telemetry layer
- no dashboard frontend
- no replay engine
- no stop-loss lifecycle
- no advanced exits
- no multi-symbol orchestration
- no historical analytics

Current architectural status:
runtime-stabilized
governance-controlled
observable
live-data autonomous paper trading platform

---

# 11. Current Architectural Goal

Target state:

event-driven
governed
observable
recoverable
modular
live-data
paper-trading infrastructure