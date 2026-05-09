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

MARKET DATA
    ↓
market/market_state_pipeline.py
    ↓
core/events.py
    ↓
core/event_bus.py
    ↓
strategy/orchestrator.py
    ↓
risk/session_risk.py
risk/exposure.py
risk/cooldown.py
risk/kill_switch.py
    ↓
exchange/execution_engine.py
    ↓
exchange/paper_exchange.py
    ↓
portfolio/accounting_engine.py
    ↓
runtime/governed_runtime.py
    ↓
persistence/runtime_store.py
persistence/event_store.py
persistence/metrics_store.py

---

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

Approved event system:

core/events.py
core/event_bus.py

No secondary event propagation systems may bypass canonical event authority.

---

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

## Experimental Runtime
- cognitive_runtime.py
- financial_runtime.py
- async_runtime_loop.py

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

# 10. Current Strategic Objective

Current objective is:

stable validated execution infrastructure

NOT:
- autonomous intelligence
- self-modifying governance
- evolutionary execution
- unrestricted adaptive complexity