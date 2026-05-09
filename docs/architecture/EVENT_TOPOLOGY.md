# Event Topology

# 1. Canonical Event Authority

Canonical event definitions MUST originate from:

src/core/events.py

Responsibilities:
- authoritative RuntimeEvent definition
- event type definitions
- event normalization contracts
- runtime-safe event schemas

Architectural principle:
All runtime communication MUST use normalized internal events.

No secondary module may redefine:
- canonical runtime events
- event payload contracts
- runtime event semantics

# 2. Event Transport Layers

The system supports multiple event propagation mechanisms.

## Synchronous Transport

Canonical module:

runtime/event_bus.py

Responsibilities:
- deterministic local propagation
- synchronous runtime coordination

---

## Asynchronous Transport

Canonical module:

runtime/async_event_bus.py

Responsibilities:
- async propagation
- concurrent runtime coordination
- websocket event distribution

Architectural principle:
Transport layers propagate canonical events.
They do NOT redefine event semantics.

# 3. External Event Normalization

External exchange payloads are NOT canonical runtime events.

Canonical ingestion modules:

market/binance_ws.py

Responsibilities:
- exchange payload ingestion
- payload normalization
- RuntimeEvent conversion
- event propagation into runtime topology

Normalization pipeline:

EXTERNAL PAYLOAD
    ↓
NORMALIZATION
    ↓
RuntimeEvent
    ↓
Event Transport
    ↓
Runtime Consumers

Architectural principle:
Internal systems MUST remain isolated from
exchange-specific payload formats.

# 4. Runtime Event Consumers

Canonical runtime consumers:

core/
runtime/
risk/
exchange/
strategy/

Responsibilities:
- consume canonical runtime events
- react to propagated state changes
- emit observable runtime transitions

Consumers MUST NOT:
- redefine canonical events
- mutate transport semantics
- create competing event authorities

# 5. Observability Topology

Canonical observability modules:

runtime/
    event_journal.py
    logger.py
    metrics.py

Observability flow:

RuntimeEvent
    ↓
Journal Persistence
    ↓
Structured Logging
    ↓
Metric Aggregation

Architectural principle:
Critical runtime transitions SHOULD emit observable events.

# 5. Immediate Refactor Priority

Priority 1:
remove duplication inside core/

Priority 2:
reroute core systems to canonical event layers

Priority 3:
preserve async runtime stability

Priority 4:
avoid breaking live runtime topology

