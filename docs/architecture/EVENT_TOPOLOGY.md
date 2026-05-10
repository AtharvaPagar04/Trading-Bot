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
MarketDataRouter
    ↓
LiveTickHandler
    ↓
Autonomous Runtime
    ↓
PaperExchange
    ↓
Portfolio Synchronization
    ↓
Runtime Governance
    ↓
Observability

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
MarketDataSnapshot
    ↓
Runtime Consumption

Architectural principle:
Internal systems MUST remain isolated from
exchange-specific payload formats.

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

Consumers MUST NOT:
- redefine canonical event semantics
- mutate propagation topology

---

# 5. Observability Topology

Canonical observability modules:

runtime/
    event_journal.py
    metrics.py
    logger.py

Observability flow:

Runtime Event
    ↓
Structured Logging
    ↓
Metric Aggregation
    ↓
Persistence

Validated observability:
- live price visibility
- position visibility
- balance visibility
- pnl visibility

---

# 6. Current Event Stability Status

Validated:
- websocket event ingestion
- runtime event routing
- autonomous runtime invocation
- paper execution propagation

Current limitations:
- no event replay
- no event persistence guarantees
- no event throttling
- no distributed event topology

---

# 7. Immediate Event Priorities

Priority 1:
stabilize live runtime propagation

Priority 2:
reduce console spam

Priority 3:
add structured runtime logging

Priority 4:
implement candle aggregation topology

Priority 5:
prepare multi-symbol event routing