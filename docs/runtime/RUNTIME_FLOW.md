# Runtime Execution Flow

# 1. Objective

This document defines the canonical operational flow of the trading system.

Purpose:
- eliminate execution ambiguity
- prevent runtime fragmentation
- enforce risk-first execution
- centralize governance authority

This flow is authoritative.

All future runtime systems must conform to this topology.

---

# 2. Canonical Runtime Flow

MARKET DATA
    ↓
MARKET STATE PIPELINE
    ↓
EVENT GENERATION
    ↓
STRATEGY EVALUATION
    ↓
RISK EVALUATION
    ↓
EXECUTION APPROVAL
    ↓
EXECUTION ENGINE
    ↓
PORTFOLIO UPDATE
    ↓
RUNTIME GOVERNANCE
    ↓
PERSISTENCE + LOGGING
    ↓
METRICS + ANALYTICS

---
# 2.1 Validated Runtime Execution Path

Validated execution topology:

WEBSOCKET INGESTION
    ↓
MARKET EVENT NORMALIZATION
    ↓
ASYNC EVENT PROPAGATION
    ↓
RUNTIME GOVERNANCE
    ↓
MARKET STATE UPDATE
    ↓
STRATEGY EVALUATION
    ↓
PORTFOLIO RISK SYNCHRONIZATION
    ↓
POSITION SIZING
    ↓
EXECUTION VALIDATION
    ↓
PAPER EXECUTION
    ↓
PORTFOLIO SYNCHRONIZATION
    ↓
EVENT JOURNALING
    ↓
RUNTIME METRICS

Validated components:
- async event propagation
- websocket lifecycle management
- runtime governance transitions
- strategy execution flow
- portfolio synchronization
- event journaling
- runtime telemetry

# 3. Runtime Authority Hierarchy

## Highest Authority

Risk systems possess override authority over:
- strategy systems
- execution systems
- orchestration systems

Risk authority may:
- reject trades
- trigger cooldowns
- trigger emergency stops
- disable execution globally

---

## Runtime Governance Authority

Governed runtime controls:
- lifecycle state
- execution permissions
- cooldown state
- emergency state
- recovery state

Runtime governance may:
- pause runtime
- stop runtime
- disable trading
- enter safe mode

---

## Strategy Authority

Strategy systems may:
- generate recommendations
- generate execution proposals
- provide regime classifications

Strategy systems may NOT:
- execute orders directly
- bypass risk
- mutate runtime state

---

## Execution Authority

Execution systems may:
- simulate fills
- route approved orders
- apply fee/slippage models

Execution systems may NOT:
- override risk decisions
- override governance state

---

# 4. Canonical Event Flow

MARKET_TICK
    ↓
STRATEGY_SIGNAL
    ↓
RISK_CHECK
    ↓
EXECUTION_APPROVED
    ↓
ORDER_EXECUTED
    ↓
POSITION_UPDATED
    ↓
RUNTIME_UPDATED
    ↓
METRICS_RECORDED

---

# 5. Runtime Loop Ownership

Canonical runtime loop:

runtime/runtime_loop.py

Responsibilities:
- polling
- event propagation
- orchestration coordination
- heartbeat management

No secondary runtime loops should bypass canonical runtime flow.

---
# 5.1 Async Runtime Ownership

Canonical async runtime modules:

runtime/
    async_runtime_loop.py
    async_event_bus.py

Responsibilities:
- concurrent event propagation
- async runtime coordination
- streaming event distribution
- async lifecycle management

Validated capabilities:
- async handler execution
- graceful runtime shutdown
- event propagation integrity
- coordinated runtime stopping

Current limitations:
- no event backpressure management
- limited timeout enforcement
- minimal task supervision

# 6. Persistence Flow

## Runtime State

Stored after:
- lifecycle changes
- cooldown transitions
- emergency transitions

Pattern:
- overwrite latest authoritative state

---

## Metrics

Stored after:
- completed cycles
- completed sessions
- execution events

Pattern:
- append-only

---

## Event Journal

Stored after:
- all critical events
- emergency triggers
- runtime transitions

Pattern:
- immutable append-only

---
# 6.1 Observability Flow

Canonical observability modules:

runtime/
    event_journal.py
    logger.py
    metrics.py

Observability pipeline:

RUNTIME EVENT
    ↓
EVENT JOURNAL
    ↓
STRUCTURED LOGGING
    ↓
METRIC AGGREGATION

Validated capabilities:
- persistent event journaling
- runtime metric tracking
- structured event logging

Architectural principle:
Critical runtime transitions SHOULD emit observable events.

# 7. Recovery Flow

BOOT
    ↓
LOAD RUNTIME STATE
    ↓
VALIDATE RECOVERY POLICY
    ↓
RECONCILE POSITIONS
    ↓
RESTORE GOVERNANCE STATE
    ↓
RESUME RUNTIME

Recovery must:
- validate cooldown state
- validate emergency state
- validate portfolio consistency

---
# 7.1 Websocket Recovery Behavior

Canonical streaming module:

market/
    binance_ws.py

Current resilience capabilities:
- reconnect loop
- exception containment
- runtime-controlled shutdown

Current limitations:
- no stale-feed detection
- no heartbeat verification
- limited reconnect backoff strategy

Architectural principle:
Exchange payloads MUST be normalized into
internal RuntimeEvent structures before propagation.

# 8. Execution Safety Rules

No execution allowed if:
- emergency stop active
- cooldown active
- runtime paused
- risk gate rejected
- portfolio reconciliation failed

Execution approval requires:
- runtime approval
- risk approval
- execution integrity validation

---
# 9. Validation Architecture

Repository validation structure:

tests/
    deterministic runtime validation

scripts/
    manual runtime demos
    experimentation
    operational simulations

Validated systems:
- governance runtime
- async runtime
- websocket lifecycle
- event propagation
- runtime metrics
- strategy execution flow

Architectural principle:
Deterministic validation MUST remain isolated from
manual runtime experimentation.

# 9. Experimental System Isolation

The following systems are considered experimental:
- cognitive runtime
- evolution systems
- population systems
- meta governance
- online learning
- autonomous orchestration

Experimental systems must NOT:
- possess execution authority
- override risk systems
- mutate canonical runtime state directly

---

# 10. Canonical System Goal

Target system properties:

deterministic
recoverable
risk-governed
event-driven
observable
modular
execution-safe
statistically validated