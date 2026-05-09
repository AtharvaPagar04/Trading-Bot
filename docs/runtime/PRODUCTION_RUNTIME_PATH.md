# Production Runtime Path

# 1. Objective

This document defines the ONLY approved execution path for:
- dry-run execution
- paper trading
- future live trading

Any module outside this path is considered:
- supporting
- analytical
- experimental

Experimental systems may NOT bypass this runtime path.

---
# 2. Canonical Production Runtime Flow

WEBSOCKET MARKET INGESTION
    ↓
market/binance_ws.py
    ↓
EVENT NORMALIZATION
    ↓
core/events.py
    ↓
EVENT TRANSPORT
    ↓
runtime/event_bus.py
runtime/async_event_bus.py
    ↓
MARKET STATE PIPELINE
    ↓
strategy/orchestrator.py
    ↓
RISK SYNCHRONIZATION
    ↓
risk/session_risk.py
risk/exposure.py
risk/cooldown.py
risk/kill_switch.py
    ↓
EXECUTION VALIDATION
    ↓
exchange/execution_engine.py
exchange/paper_exchange.py
    ↓
PORTFOLIO SYNCHRONIZATION
    ↓
runtime/governed_runtime.py
    ↓
OBSERVABILITY
    ↓
runtime/event_journal.py
runtime/logger.py
runtime/metrics.py
    ↓
PERSISTENCE
# 3. Runtime Ownership

## Canonical Runtime Authority

Primary authority:

runtime/governed_runtime.py

Responsibilities:
- lifecycle control
- emergency state
- cooldown state
- execution permission state

---

## Canonical Runtime Loop

Primary runtime loop:

runtime/runtime_loop.py

Responsibilities:
- orchestration coordination
- event propagation
- heartbeat management
- runtime tick execution

---
# 4. Canonical Event Authority

Canonical event definitions:

core/events.py

Canonical event transport systems:

runtime/event_bus.py
runtime/async_event_bus.py

Architectural principle:
Transport systems propagate canonical runtime events.
They MUST NOT redefine event semantics.


# 5. Canonical Risk Authority

Risk systems possess final override authority.

Approved risk systems:
- session_risk.py
- exposure.py
- cooldown.py
- kill_switch.py

Execution is forbidden if:
- cooldown active
- emergency stop active
- runtime paused
- reconciliation failed

---

# 6. Canonical Execution Authority

Approved execution systems:
- execution_engine.py
- paper_exchange.py
- execution_simulator.py

Execution systems:
- may not bypass risk approval
- may not mutate runtime governance directly

---

# 7. Experimental Isolation

The following systems are NOT on the production runtime path:

## Validated But Non-Production-Hardened Runtime

Validated infrastructure:
- async_runtime_loop.py
- async_event_bus.py
- binance_ws.py

Validated capabilities:
- async propagation
- websocket lifecycle management
- reconnect containment
- runtime-controlled shutdown

NOT yet production-hardened:
- stale-feed detection
- heartbeat monitoring
- reconnect backoff strategy
- backpressure handling
- task supervision

## Experimental Strategy
- adaptive_ensemble.py
- meta_learning.py
- online_learning.py
- autonomous_decay.py

## Experimental Governance
- meta_governance.py
- evolution.py
- hierarchy.py
- population.py

Experimental systems:
- may observe runtime
- may generate analytics
- may simulate decisions

Experimental systems may NOT:
- directly execute trades
- override governance
- mutate canonical runtime state

---

# 8. Production Runtime Principles

Production runtime must remain:

deterministic
recoverable
observable
risk-governed
modular
execution-safe

Complexity must justify measurable operational benefit.

---

# 9. Runtime Expansion Rules

Before adding ANY new runtime/governance system:

Required:
1. explicit ownership definition
2. event flow definition
3. runtime authority review
4. recovery impact analysis
5. observability plan
6. statistical validation objective

No runtime expansion allowed without:
- consolidation review
- operational justification

---
# 9. Observability Requirements

Production runtime MUST emit observable events for:
- runtime state transitions
- governance overrides
- execution approvals
- execution failures
- portfolio synchronization
- emergency conditions

Canonical observability systems:

runtime/
    event_journal.py
    logger.py
    metrics.py

Architectural principle:
Critical runtime behavior MUST remain auditable.

# 10. Production Safety Constraints

NO execution path may bypass:
- runtime governance
- risk synchronization
- execution validation
- portfolio reconciliation

Execution approval REQUIRES:
- runtime approval
- risk approval
- governance approval
- execution integrity validation

Any bypass of canonical runtime authority is considered a production violation.

# 10. Current Strategic Objective

Current objective is:

stable validated execution infrastructure

NOT:
- autonomous intelligence
- self-modifying governance
- evolutionary execution
- unrestricted adaptive complexity

