# Event Unification Plan

# 1. Objective

Unify all event infrastructure into:
- one canonical event definition layer
- one canonical propagation layer
- one runtime topology

Purpose:
- eliminate event ambiguity
- simplify runtime governance
- improve observability
- improve replayability
- reduce propagation fragmentation

---

# 2. Canonical Event Authority

Approved event definition module:

core/events.py

Approved event propagation module:

core/event_bus.py

All future runtime systems must use canonical event authority.

---

# 3. Deprecated Event Systems

## Event Definitions

Deprecated candidate:
- events/event.py

Reason:
- duplicates event semantics
- creates ownership ambiguity

---

## Event Propagation

Deprecated candidates:
- runtime/event_bus.py
- events/event_dispatcher.py

Reason:
- fragmented propagation topology
- unclear runtime authority

---

# 4. Async Event Handling

Current:
- runtime/async_event_bus.py

Status:
- EXPERIMENTAL

Rule:
- async execution must remain implementation detail
- async layer may not redefine event semantics

Future direction:
- async wrapper around canonical event bus

NOT:
- independent propagation system

---

# 5. Canonical Event Flow

MARKET_TICK
    ↓
EVENT BUS
    ↓
STRATEGY
    ↓
RISK
    ↓
EXECUTION
    ↓
PORTFOLIO
    ↓
RUNTIME GOVERNANCE
    ↓
PERSISTENCE
    ↓
METRICS

---

# 6. Migration Strategy

Phase 1:
- freeze duplicate event systems

Phase 2:
- identify imports using deprecated systems

Phase 3:
- reroute imports toward canonical systems

Phase 4:
- isolate async wrappers

Phase 5:
- deprecate fragmented event infrastructure

---

# 7. Event Design Rules

Event definitions must remain:
- deterministic
- immutable where possible
- serialization-safe
- replay-safe

Events may contain:
- payload
- timestamp
- metadata
- source identifiers

Events may NOT:
- mutate runtime directly
- contain execution authority

---

# 8. Runtime Event Authority

Runtime governance events must flow through:
- canonical event bus
- canonical runtime authority

No secondary runtime loop may bypass canonical propagation topology.

---

# 9. Production Event Constraints

Production runtime must guarantee:
- deterministic propagation
- observable propagation
- replayable propagation
- auditable propagation

Event propagation must remain:
- centralized
- inspectable
- testable

---

# 10. Current Priority

Current goal is:

event topology stabilization

NOT:
- async sophistication
- distributed event systems
- autonomous propagation layers