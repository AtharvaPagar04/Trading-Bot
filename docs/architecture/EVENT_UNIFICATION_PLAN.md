# Event Unification Plan

# 1. Objective

Unify all runtime infrastructure into:
- one canonical runtime authority
- one canonical event topology
- one normalized market data pipeline

Purpose:
- eliminate propagation ambiguity
- simplify runtime governance
- improve observability
- stabilize autonomous runtime execution

---

# 2. Canonical Runtime Authority

Approved runtime authority:

runtime/
    governed_runtime.py

Approved orchestration flow:

BinanceWebSocketClient
    ↓
MarketDataRouter
    ↓
LiveTickHandler
    ↓
Autonomous Runtime
    ↓
PaperExchange

All future runtime systems MUST integrate through:
- canonical runtime governance
- canonical runtime orchestration

---

# 3. Canonical Market Data Flow

Approved market normalization flow:

BINANCE PAYLOAD
    ↓
MarketTick
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

---

# 4. Deprecated Runtime Patterns

Deprecated patterns:
- direct strategy execution
- bypassed runtime governance
- direct exchange payload usage
- duplicate execution routing

Future runtime systems MUST remain:
- normalized
- observable
- governance-controlled

---

# 5. Runtime Stabilization Priorities

Priority 1:
prevent duplicate execution

Priority 2:
stabilize portfolio synchronization

Priority 3:
stabilize execution lifecycle

Priority 4:
stabilize runtime observability

Priority 5:
implement controlled exits

---

# 6. Runtime Lifecycle Status

Validated:
- live websocket connectivity
- autonomous BUY execution
- portfolio accounting
- unrealized pnl tracking
- execution guardrails
- runtime synchronization

Current limitations:
- no advanced signal engine
- no realistic candle engine
- no dynamic strategy lifecycle
- no stop-loss engine
- no runtime telemetry persistence

---

# 7. Immediate Next Objectives

Next runtime objectives:

1. runtime log throttling
2. stop-loss integration
3. realistic take-profit lifecycle
4. cooldown after exits
5. candle aggregation engine
6. structured telemetry
7. multi-symbol orchestration

---

# 8. Production Constraints

Production runtime MUST guarantee:
- deterministic execution
- observable lifecycle transitions
- replay-safe runtime events
- governance-controlled execution
- normalized market ingestion

Runtime execution MUST remain:
- centralized
- auditable
- inspectable
- risk-governed

---

# 9. Current Architectural Goal

Current goal is:

live autonomous paper trading stabilization

NOT:
- high-frequency execution
- distributed runtimes
- advanced ML orchestration
- aggressive strategy complexity