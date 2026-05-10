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

Primary architectural strengths:
- modular runtime separation
- governance-first execution
- exchange abstraction
- normalized runtime state
- realistic execution modeling

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

Responsibilities:
- lifecycle control
- runtime state transitions
- emergency handling
- execution permissions
- runtime orchestration
- live market tick processing
- autonomous runtime coordination

Architectural principle:
Runtime governance MUST remain authoritative over:
- execution permissions
- emergency states
- runtime transitions

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

Responsibilities:
- capital protection
- exposure control
- drawdown management
- execution throttling
- emergency triggers

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

Execution layer MUST remain:
- downstream from runtime governance
- isolated from strategy ownership

---

# 6.1 Live Market Infrastructure

Canonical modules:

market/
    market_data_router.py

exchange/
    binance_websocket_client.py

Responsibilities:
- Binance websocket connectivity
- reconnect handling
- live trade ingestion
- MarketTick normalization
- runtime tick routing

Validated capabilities:
- live Binance websocket ingestion
- reconnect protection
- runtime tick routing
- live autonomous runtime invocation

Future objectives:
- heartbeat monitoring
- stale-feed detection
- multi-symbol streaming
- websocket backoff strategy
- candle aggregation engine

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

Operational flow:

LIVE BINANCE TRADE
    ↓
MarketTick
    ↓
MarketDataRouter
    ↓
LiveTickHandler
    ↓
Autonomous Runtime
    ↓
PaperExchange
    ↓
Portfolio Update
    ↓
Runtime Synchronization

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

---

# 9. Runtime Observability

Canonical modules:

runtime/
    logger.py
    metrics.py
    event_journal.py

Validated runtime observability:
- live execution visibility
- pnl visibility
- position visibility
- runtime lifecycle visibility

Current console telemetry:
- live BTC price
- execution status
- balance state
- position state
- unrealized pnl

Future observability goals:
- structured logging
- persistent runtime telemetry
- execution analytics
- performance dashboards

---

# 10. Paper Trading Runtime Status

Validated capabilities:
- live Binance websocket ingestion
- autonomous BUY execution
- portfolio accounting
- slippage/spread simulation
- fee simulation
- runtime governance integration
- duplicate execution prevention
- unrealized pnl monitoring
- live runtime orchestration

Current limitations:
- no advanced signal engine
- no candle aggregation
- no dynamic exits
- no stop-loss engine
- no multi-symbol orchestration

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