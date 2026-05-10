# Event Topology

# 1. Canonical Event Authority

Canonical runtime event ownership:

runtime/
    event_bus.py
    async_event_bus.py

Responsibilities:
- deterministic propagation
- runtime coordination
- event synchronization
- runtime lifecycle propagation
- execution telemetry propagation
- governance event propagation

Architectural principle:
All runtime communication MUST use canonical runtime events.

---

# 2. Runtime Event Flow

LIVE BINANCE TRADE
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

Runtime event propagation principles:
- all market events MUST become normalized runtime events
- exchange-specific payloads MUST remain isolated
- execution decisions MUST remain governance-controlled
- runtime telemetry MUST remain centralized

---

# 3. External Event Normalization

External Binance payloads are NOT canonical runtime events.

Canonical normalization flow:

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
Runtime Consumption

Architectural principle:
Internal systems MUST remain isolated from:
- exchange-specific payload formats
- websocket payload structures
- external transport semantics

Normalization guarantees:
- deterministic runtime consumption
- exchange abstraction
- replay-safe event structures
- governance-safe propagation

---

# 4. Runtime Consumers

Canonical runtime consumers:

runtime/
core/
exchange/
risk/
strategy/

Responsibilities:
- consume normalized runtime events
- react to propagated state changes
- maintain runtime determinism
- synchronize execution lifecycle
- maintain runtime telemetry consistency

Consumers MUST NOT:
- redefine canonical event semantics
- mutate propagation topology
- bypass runtime governance
- consume raw exchange payloads

---

# 5. Observability Topology

Canonical observability modules:

runtime/
    runtime_snapshot.py
    runtime_console_renderer.py
    event_journal.py
    metrics.py
    logger.py

Observability flow:

Runtime Event
    ↓
Runtime Snapshot
    ↓
Console Rendering
    ↓
Structured Logging
    ↓
Metric Aggregation
    ↓
Persistence

Validated observability:
- live price visibility
- candle-close visibility
- active trade visibility
- completed trade visibility
- portfolio visibility
- exposure visibility
- runtime halt visibility
- unrealized pnl visibility
- portfolio valuation visibility

Current runtime observability sections:
- runtime status
- market telemetry
- portfolio telemetry
- active trades
- completed trades

Current telemetry coverage:
- latest market price
- candle-close state
- runtime operating state
- active trade lifecycle
- completed trade lifecycle
- unrealized pnl
- exposure state
- invested capital
- holdings value
- available cash
- portfolio valuation

---

# 6. Current Event Stability Status

Validated:
- websocket event ingestion
- reconnect-safe websocket lifecycle
- runtime tick routing
- candle aggregation propagation
- autonomous runtime invocation
- governance-controlled execution
- runtime snapshot propagation
- console observability propagation
- paper execution lifecycle propagation

Current limitations:
- no persistent event journal
- no replay-safe event storage
- no distributed event routing
- no telemetry streaming API
- no event replay engine

Current runtime event characteristics:
- centralized propagation
- deterministic execution flow
- governance-controlled execution lifecycle
- normalized market event routing
- runtime-driven observability

---

# 7. Immediate Event Priorities

Priority 1:
runtime persistence layer

Priority 2:
structured execution journaling

Priority 3:
FastAPI telemetry layer

Priority 4:
dashboard websocket streaming

Priority 5:
historical runtime replay

Priority 6:
multi-symbol runtime routing

Priority 7:
persistent runtime event journal

Priority 8:
structured runtime metrics streaming