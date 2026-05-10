# Event Unification Plan

# 1. Objective

Unify all runtime infrastructure into:
- one canonical runtime authority
- one canonical event topology
- one normalized market data pipeline
- one governance-controlled execution lifecycle
- one centralized observability system

Purpose:
- eliminate propagation ambiguity
- simplify runtime governance
- improve observability
- stabilize autonomous runtime execution
- standardize execution lifecycle telemetry
- prepare replay-safe infrastructure

---

# 2. Canonical Runtime Authority

Approved runtime authority:

runtime/
    governed_runtime.py
    runtime_snapshot.py
    runtime_console_renderer.py

Approved orchestration flow:

BinanceWebSocketClient
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
Portfolio Synchronization
    ↓
Runtime Snapshot
    ↓
Console Observability

All future runtime systems MUST integrate through:
- canonical runtime governance
- canonical runtime orchestration
- canonical runtime observability

Execution authority MUST remain:
- governance-controlled
- runtime-controlled
- observable
- centralized

---

# 3. Canonical Market Data Flow

Approved market normalization flow:

BINANCE PAYLOAD
    ↓
BinanceWebSocketClient
    ↓
MarketTick
    ↓
TimeframeAggregator
    ↓
Candle
    ↓
MarketDataSnapshot
    ↓
Autonomous Runtime

Architectural principle:
Exchange-specific payloads MUST NOT leak into:
- strategy systems
- risk systems
- runtime governance
- portfolio systems
- observability systems

Normalization guarantees:
- deterministic runtime execution
- replay-safe market structures
- governance-safe execution flow
- exchange abstraction

---

# 4. Deprecated Runtime Patterns

Deprecated patterns:
- direct strategy execution
- bypassed runtime governance
- direct exchange payload usage
- duplicate execution routing
- execution without portfolio synchronization
- execution without governance evaluation
- fragmented runtime telemetry

Future runtime systems MUST remain:
- normalized
- observable
- governance-controlled
- replay-safe
- lifecycle-auditable

---

# 5. Runtime Stabilization Priorities

Priority 1:
stabilize runtime persistence

Priority 2:
stabilize execution journaling

Priority 3:
stabilize telemetry propagation

Priority 4:
implement FastAPI telemetry layer

Priority 5:
implement dashboard infrastructure

Priority 6:
implement replay-safe persistence

Priority 7:
stabilize multi-symbol orchestration

Priority 8:
stabilize structured runtime metrics

---

# 6. Runtime Lifecycle Status

Validated:
- live websocket connectivity
- reconnect-safe websocket lifecycle
- timeframe candle aggregation
- autonomous candle-close execution
- portfolio accounting
- unrealized pnl tracking
- exposure governance
- execution guardrails
- runtime synchronization
- active trade lifecycle tracking
- completed trade journaling
- runtime telemetry snapshots
- runtime observability rendering
- governance-based runtime halting
- exposure-based execution blocking

Current governance capabilities:
- exposure-based execution blocking
- runtime halt propagation
- centralized execution approval
- governance-aware execution routing

Current accounting capabilities:
- invested capital tracking
- holdings valuation
- unrealized pnl tracking
- portfolio valuation tracking
- cash utilization tracking

Current observability capabilities:
- runtime status rendering
- market telemetry rendering
- portfolio telemetry rendering
- active trade rendering
- completed trade rendering
- runtime lifecycle visibility

Current limitations:
- no persistence layer
- no dashboard frontend
- no telemetry API
- no replay engine
- no stop-loss lifecycle
- no advanced exit lifecycle
- no multi-symbol orchestration

---

# 7. Immediate Next Objectives

Next runtime objectives:

1. persistence layer
2. completed trade persistence
3. structured execution journaling
4. FastAPI telemetry layer
5. dashboard websocket streaming
6. live dashboard frontend
7. replay-safe runtime persistence
8. historical runtime analytics
9. runtime metrics API
10. structured event persistence

Immediate architectural goals:
- durable runtime state
- persistent execution lifecycle tracking
- replay-safe telemetry
- dashboard-ready runtime APIs
- centralized runtime observability

---

# 8. Production Constraints

Production runtime MUST guarantee:
- deterministic execution
- observable lifecycle transitions
- replay-safe runtime events
- governance-controlled execution
- normalized market ingestion
- centralized runtime telemetry
- auditable execution lifecycle

Runtime execution MUST remain:
- centralized
- auditable
- inspectable
- risk-governed
- governance-controlled

Production observability MUST support:
- runtime replay
- historical telemetry inspection
- execution lifecycle reconstruction
- portfolio lifecycle reconstruction
- governance event reconstruction

---

# 9. Current Architectural Goal

Current goal is:

runtime-stabilized
governance-controlled
observable
live-data
autonomous paper trading platform

Focus areas:
- runtime durability
- observability
- execution lifecycle visibility
- portfolio telemetry
- replay-safe architecture
- dashboard readiness

NOT:
- aggressive optimization
- advanced ML systems
- high-frequency execution
- distributed orchestration
- profitability optimization