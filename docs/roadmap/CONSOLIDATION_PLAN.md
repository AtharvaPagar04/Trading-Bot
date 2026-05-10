# Consolidation Plan

# 1. Runtime Layer Audit

## Canonical Runtime Modules

| Module | Status | Responsibility |
|---|---|---|
| runtime/governed_runtime.py | CANONICAL | runtime lifecycle |
| runtime/runtime_loop.py | CANONICAL | execution loop |
| runtime/runtime_state.py | CANONICAL | runtime state |
| runtime/runtime_enums.py | CANONICAL | runtime enums |
| runtime/live_tick_handler.py | CANONICAL | live runtime orchestration |

---

## Stable Runtime Infrastructure

| Module | Status |
|---|---|
| exchange/binance_websocket_client.py | VALIDATED |
| market_data/market_data_router.py | VALIDATED |
| exchange/paper_exchange.py | VALIDATED |
| core/autonomous_runtime.py | VALIDATED SUPPORTING |

---

## Runtime Candidates For Consolidation

| Module | Current Risk |
|---|---|
| core/runtime.py | ownership overlap |
| core/strategy_runtime.py | orchestration duplication |
| core/integrated_runtime.py | integration ambiguity |
| runtime/financial_runtime.py | undefined scope |
| runtime/cognitive_runtime.py | experimental creep |

Action:
- freeze expansion
- preserve validated runtime path
- consolidate overlapping orchestration later

---

# 2. Event System Audit

## Canonical Event System

| Module | Status |
|---|---|
| runtime/event_bus.py | CANONICAL |
| runtime/async_event_bus.py | CANONICAL |
| market_data/market_data_router.py | CANONICAL |

---

## Duplicate Event Systems

| Module | Risk |
|---|---|
| events/event.py | duplicated semantics |
| events/event_dispatcher.py | propagation ambiguity |

Action:
- converge toward single runtime event topology
- normalize all market ingestion through MarketTick

---

# 3. Runtime Lifecycle Audit

## Stable Lifecycle Components

| Module |
|---|
| runtime/live_tick_handler.py |
| exchange/paper_exchange.py |
| core/autonomous_runtime.py |
| market_data/market_data_router.py |

Validated lifecycle:

LIVE TICK
↓
Runtime Governance
↓
Execution Validation
↓
Paper Execution
↓
Portfolio Synchronization
↓
PnL Monitoring

---

# 4. Governance Layer Audit

## Stable Governance Components

| Module |
|---|
| risk/kill_switch.py |
| risk/session_risk.py |
| risk/cooldown.py |
| core/runtime_state_machine.py |
| runtime/governed_runtime.py |

---

## Governance Expansion Risk

| Module |
|---|
| meta_governance.py |
| hierarchy.py |
| evolution.py |
| population.py |

Risk:
- governance complexity exceeds runtime stabilization maturity

Action:
- isolate experimental governance systems
- prioritize runtime stabilization

---

# 5. Strategy Layer Audit

## Stable Strategy Components

| Module |
|---|
| strategy/regime.py |
| strategy/spacing.py |
| strategy/asymmetric_grid.py |
| strategy/orchestrator.py |

---

## Current Runtime Strategy Limitation

Current runtime behavior:
- hardcoded BUY execution
- fixed take-profit evaluation
- no dynamic signal engine

Priority:
- stabilize lifecycle first
- strategy sophistication later

---

# 6. Persistence Layer Audit

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
- define explicit lifecycle recovery ownership

---

# 7. Immediate Freeze Policy

Frozen Areas:
- new governance abstractions
- new runtime orchestration systems
- distributed runtime systems
- ML execution autonomy

Allowed Areas:
- runtime stabilization
- observability
- lifecycle refinement
- execution integrity
- recovery integrity

---

# 8. Next Consolidation Objectives

Priority 1:
- stabilize live runtime lifecycle

Priority 2:
- implement candle aggregation

Priority 3:
- add stop-loss lifecycle

Priority 4:
- reduce runtime logging spam

Priority 5:
- improve execution observability

Priority 6:
- isolate experimental systems

---

# 9. Current Strategic Direction

The project should evolve toward:

deterministic
event-driven
risk-governed
observable
recoverable
modular
live autonomous paper trading infrastructure

NOT toward:
- uncontrolled abstraction growth
- premature ML complexity
- unrestricted autonomous behavior