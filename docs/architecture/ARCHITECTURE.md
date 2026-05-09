# Grid Trading Bot v3 — Canonical Architecture

# 1. Current System State

The system has evolved from:
- simple grid execution
into:
- event-driven adaptive trading infrastructure

The architecture currently contains:
- runtime governance
- event systems
- recovery systems
- risk orchestration
- strategy orchestration
- execution simulation
- analytics
- portfolio intelligence
- adaptive ensemble systems

Primary architectural risk:
- overlapping ownership boundaries
- duplicated runtime abstractions
- fragmented event infrastructure
- governance layer explosion

This document defines:
- canonical ownership
- authoritative modules
- deprecation targets
- future consolidation direction

---

# 2. Canonical Runtime Ownership

## Authoritative Runtime Layer

Canonical runtime modules:

runtime/
    governed_runtime.py
    runtime_loop.py
    runtime_state.py
    runtime_enums.py

Responsibilities:
- lifecycle control
- runtime state transitions
- cooldown state
- emergency state
- execution permissions
- runtime orchestration

Non-canonical runtime modules in core/ are candidates for consolidation.

---

# 3. Canonical Event System

## Authoritative Event Layer

Canonical modules:

core/
    events.py
    event_bus.py

Responsibilities:
- event definitions
- event propagation
- event subscription
- runtime communication

Deprecated direction:
- src/events/
- duplicate runtime event buses

Future objective:
- single centralized event topology

---
# 3.1 Async Runtime Infrastructure

Canonical async runtime modules:

runtime/
    async_event_bus.py
    async_runtime_loop.py

Responsibilities:
- async event propagation
- concurrent runtime orchestration
- streaming event coordination
- async lifecycle management

Validated capabilities:
- async event publishing
- graceful runtime shutdown
- async handler execution
- runtime loop lifecycle integrity

Current limitations:
- no backpressure management
- no task fanout control
- limited cancellation coordination
- minimal timeout protection

Future objective:
- resilient concurrent event infrastructure
# 4. Canonical Risk Ownership

Canonical modules:

risk/
    kill_switch.py
    exposure.py
    session_risk.py
    cooldown.py
    dynamic_position_sizer.py

Responsibilities:
- capital protection
- exposure control
- drawdown management
- cooldown enforcement
- emergency triggers

Risk layer MUST remain independent from:
- strategy layer
- execution layer

---

# 5. Canonical Strategy Ownership

Canonical modules:

strategy/
    regime.py
    spacing.py
    asymmetric_grid.py
    orchestrator.py

Responsibilities:
- signal generation
- regime adaptation
- grid construction
- execution recommendations

Strategy layer MUST NOT:
- place orders directly
- bypass risk systems
- mutate runtime state

---

# 6. Canonical Execution Ownership

Canonical modules:

exchange/
    execution_engine.py
    execution_simulator.py
    paper_exchange.py

Responsibilities:
- simulated fills
- fee modeling
- slippage handling
- execution routing

Execution layer MUST remain:
- stateless where possible
- downstream from risk approval

---
# 6.1 Streaming Market Infrastructure

Canonical modules:

market/
    binance_ws.py

Responsibilities:
- websocket market ingestion
- market tick normalization
- exchange event transformation
- runtime event publication

Current resilience capabilities:
- reconnect loop
- exception containment
- runtime-controlled shutdown

Architectural principle:
External exchange payloads MUST be normalized into
internal RuntimeEvent structures before propagation.

Future objectives:
- heartbeat monitoring
- stale-feed detection
- reconnect backoff strategies
- multi-symbol stream orchestration


# 7. Persistence Architecture

Persistence categories:

## Runtime State
Purpose:
- restart recovery
- cooldown persistence
- emergency persistence

Pattern:
- overwrite latest authoritative state

## Metrics
Purpose:
- analytics
- telemetry
- monitoring

Pattern:
- append-only

## Event Journal
Purpose:
- replay
- auditability
- debugging

Pattern:
- immutable append-only

---
# 7.1 Observability Infrastructure

Canonical modules:

runtime/
    event_journal.py
    metrics.py
    logger.py

Responsibilities:
- runtime telemetry
- event persistence
- operational diagnostics
- execution auditing

Validated capabilities:
- persistent event journaling
- runtime metric aggregation
- structured runtime logging

Architectural principle:
All critical runtime transitions SHOULD emit observable events.

# 8. Immediate Consolidation Priorities

Priority 1:
- eliminate duplicate event systems

Priority 2:
- consolidate runtime ownership

Priority 3:
- define governance authority hierarchy

Priority 4:
- isolate experimental ML systems

Priority 5:
- reduce architectural overlap

---

# 9. Development Freeze Rules

Until consolidation stabilizes:

DO NOT ADD:
- new governance layers
- new runtime abstractions
- new orchestration systems
- additional meta-learning systems
- distributed runtime systems

Focus:
- validation
- consolidation
- deterministic behavior
- observability
- runtime integrity

---

# 9. Validation Architecture

Repository validation structure:

tests/
    deterministic runtime validation

scripts/
    manual runtime demos
    experimentation
    operational simulations

Validation status:
- governance runtime validated
- async runtime validated
- websocket lifecycle validated
- execution orchestration validated
- runtime metrics validated
- event journaling validated

Architectural principle:
Deterministic validation MUST remain separated from
manual runtime experimentation.

# 10. Current Architectural Goal

Target state:

event-driven
risk-governed
recoverable
observable
modular
validated
event-driven
risk-governed
observable
recoverable
adaptive trading infrastructure