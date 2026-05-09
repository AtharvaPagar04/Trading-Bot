# Authority Matrix

# 1. Objective

This document defines authoritative ownership across the system.

Purpose:
- eliminate ownership ambiguity
- prevent runtime fragmentation
- prevent duplicated authority
- simplify consolidation

Each domain must have:
- one canonical authority
- clearly bounded responsibilities

---

# 2. Runtime Authority

| Responsibility | Canonical Module |
|---|---|
| runtime lifecycle | runtime/governed_runtime.py |
| runtime execution loop | runtime/runtime_loop.py |
| runtime state | runtime/runtime_state.py |
| runtime enums | runtime/runtime_enums.py |

---

## Non-Canonical Runtime Systems

| Module | Status |
|---|---|
| core/runtime.py | consolidation candidate |
| core/autonomous_runtime.py | experimental |
| core/strategy_runtime.py | consolidation candidate |
| core/integrated_runtime.py | integration wrapper only |
| runtime/cognitive_runtime.py | experimental |
| runtime/financial_runtime.py | analytical only |

---

# 3. Event Authority

| Responsibility | Canonical Module |
|---|---|
| event definitions | core/events.py |
| event propagation | core/event_bus.py |

---

## Non-Canonical Event Systems

| Module | Status |
|---|---|
| events/event.py | deprecated candidate |
| events/event_dispatcher.py | deprecated candidate |
| runtime/event_bus.py | consolidation candidate |
| runtime/async_event_bus.py | implementation detail only |

---

# 4. Risk Authority

| Responsibility | Canonical Module |
|---|---|
| kill switch | risk/kill_switch.py |
| exposure control | risk/exposure.py |
| cooldown enforcement | risk/cooldown.py |
| session risk | risk/session_risk.py |
| position sizing | risk/dynamic_position_sizer.py |

---

## Risk Rules

Risk systems possess override authority over:
- strategy systems
- execution systems
- orchestration systems

No component may bypass risk approval.

---

# 5. Strategy Authority

| Responsibility | Canonical Module |
|---|---|
| regime classification | strategy/regime.py |
| grid spacing | strategy/spacing.py |
| grid structure | strategy/asymmetric_grid.py |
| orchestration | strategy/orchestrator.py |

---

## Experimental Strategy Systems

| Module | Status |
|---|---|
| adaptive_ensemble.py | experimental |
| meta_learning.py | experimental |
| online_learning.py | experimental |
| autonomous_decay.py | experimental |
| regime_router.py | experimental |

---

# 6. Execution Authority

| Responsibility | Canonical Module |
|---|---|
| execution routing | exchange/execution_engine.py |
| paper trading | exchange/paper_exchange.py |
| execution simulation | exchange/execution_simulator.py |

---

## Execution Rules

Execution systems:
- require prior risk approval
- cannot mutate runtime governance
- cannot override cooldown state

---

# 7. Persistence Authority

| Responsibility | Canonical Module |
|---|---|
| runtime persistence | persistence/runtime_store.py |
| metrics persistence | persistence/metrics_store.py |
| event persistence | persistence/event_store.py |

---

## Persistence Rules

Runtime state:
- overwrite latest authoritative state

Metrics:
- append-only

Events:
- immutable append-only

---

# 8. Governance Authority

| Responsibility | Canonical Module |
|---|---|
| runtime transitions | core/runtime_transition_engine.py |
| transition rules | core/runtime_transition_rules.py |
| runtime state machine | core/runtime_state_machine.py |

---

## Experimental Governance Systems

| Module | Status |
|---|---|
| meta_governance.py | experimental |
| hierarchy.py | experimental |
| evolution.py | experimental |
| population.py | experimental |

---

# 9. Experimental Isolation Policy

Experimental systems:
- may observe runtime
- may generate analytics
- may generate recommendations

Experimental systems may NOT:
- directly execute trades
- bypass risk systems
- mutate canonical runtime state
- override governance state

---

# 10. Immediate Consolidation Targets

Priority 1:
- unify event infrastructure

Priority 2:
- eliminate duplicate runtime abstractions

Priority 3:
- simplify governance ownership

Priority 4:
- isolate experimental ML systems

Priority 5:
- reduce orchestration overlap

---

# 11. Long-Term Architectural Goal

Target architecture:

deterministic
event-driven
risk-governed
recoverable
observable
modular
execution-safe
validation-first