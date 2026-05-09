# Consolidation Plan

# 1. Runtime Layer Audit

## Canonical Runtime Modules

| Module | Status | Responsibility |
|---|---|---|
| runtime/governed_runtime.py | CANONICAL | runtime lifecycle |
| runtime/runtime_loop.py | CANONICAL | execution loop |
| runtime/runtime_state.py | CANONICAL | runtime state |
| runtime/runtime_enums.py | CANONICAL | runtime enums |

---

## Runtime Candidates For Consolidation

| Module | Current Risk |
|---|---|
| core/runtime.py | ownership overlap |
| core/autonomous_runtime.py | unclear authority |
| core/strategy_runtime.py | runtime fragmentation |
| core/integrated_runtime.py | integration ambiguity |
| runtime/financial_runtime.py | undefined scope |
| runtime/cognitive_runtime.py | experimental creep |

Action:
- freeze expansion
- evaluate ownership
- merge or isolate later

---

# 2. Event System Audit

## Canonical Event System

| Module | Status |
|---|---|
| core/events.py | CANONICAL |
| core/event_bus.py | CANONICAL |

---

## Duplicate Event Systems

| Module | Risk |
|---|---|
| events/event.py | duplicated semantics |
| events/event_dispatcher.py | propagation ambiguity |
| runtime/event_bus.py | topology fragmentation |
| runtime/async_event_bus.py | split infrastructure |

Action:
- converge toward single event authority
- async handled as implementation detail

---

# 3. Governance Layer Audit

## Stable Governance Components

| Module |
|---|
| risk/kill_switch.py |
| risk/session_risk.py |
| risk/cooldown.py |
| core/runtime_state_machine.py |

---

## Governance Expansion Risk

| Module |
|---|
| meta_governance.py |
| hierarchy.py |
| evolution.py |
| population.py |
| runtime_auto_escalation.py |

Risk:
- governance complexity exceeds validation maturity

Action:
- isolate experimental governance systems

---

# 4. Strategy Layer Audit

## Stable Strategy Components

| Module |
|---|
| strategy/regime.py |
| strategy/spacing.py |
| strategy/asymmetric_grid.py |
| strategy/orchestrator.py |

---

## Experimental Strategy Systems

| Module |
|---|
| meta_learning.py |
| online_learning.py |
| adaptive_ensemble.py |
| ensemble_selection.py |
| autonomous_decay.py |

Action:
- isolate from production runtime path

---

# 5. Persistence Layer Audit

## Canonical Persistence Roles

| Component | Pattern |
|---|---|
| runtime_store | latest state |
| metrics_store | append-only |
| event_store | immutable journal |

---

## Current Risk

Potential overlap:
- runtime_snapshot
- runtime_loader
- runtime_recovery

Action:
- define explicit ownership boundaries

---

# 6. Immediate Freeze Policy

Frozen Areas:
- new runtime systems
- new governance abstractions
- new ML orchestration
- new evolutionary systems

Allowed Areas:
- consolidation
- validation
- testing
- observability
- execution integrity
- recovery integrity

---

# 7. Next Consolidation Objectives

Priority 1:
- remove duplicate event buses

Priority 2:
- define single runtime authority

Priority 3:
- define runtime bootstrap sequence

Priority 4:
- define execution approval hierarchy

Priority 5:
- isolate experimental systems

---

# 8. Current Strategic Direction

The project should evolve toward:

deterministic
event-driven
risk-governed
recoverable
observable
modular
validated trading infrastructure

NOT toward:
- uncontrolled abstraction growth
- premature autonomous complexity
- unvalidated adaptive behavior