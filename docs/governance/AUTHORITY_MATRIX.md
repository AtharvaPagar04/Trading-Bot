# Authority Matrix

# 1. Objective

This document defines authoritative ownership across the system.

Purpose:

* eliminate ownership ambiguity
* prevent runtime fragmentation
* prevent duplicated authority
* simplify consolidation
* preserve execution safety
* centralize operational control

Each domain must have:

* one canonical authority
* clearly bounded responsibilities
* explicit mutation permissions
* observable state transitions

Architectural principle:

authority != participation

Many systems may observe runtime state.

Very few systems may mutate canonical runtime state.

---

# 2. Runtime Authority

| Responsibility         | Canonical Module              |
| ---------------------- | ----------------------------- |
| runtime lifecycle      | runtime/governed_runtime.py   |
| runtime execution loop | runtime/runtime_loop.py       |
| async runtime loop     | runtime/async_runtime_loop.py |
| runtime state          | runtime/runtime_state.py      |
| runtime enums          | runtime/runtime_enums.py      |

---

## Runtime Responsibilities

Canonical runtime authority controls:

* lifecycle state
* runtime transitions
* execution permissions
* safe mode state
* emergency stop state
* cooldown state
* runtime coordination

Runtime authority may:

* pause execution
* stop execution
* disable trading
* reject runtime continuation
* initiate recovery flow

No downstream system may override runtime governance directly.

---

## Validated Runtime Infrastructure

| Module                        | Status    |
| ----------------------------- | --------- |
| runtime/event_bus.py          | validated |
| runtime/async_event_bus.py    | validated |
| runtime/runtime_loop.py       | validated |
| runtime/async_runtime_loop.py | validated |
| market/binance_ws.py          | validated |

---

## Non-Canonical Runtime Systems

| Module                       | Status                  |
| ---------------------------- | ----------------------- |
| core/runtime.py              | consolidation candidate |
| core/autonomous_runtime.py   | orchestration wrapper   |
| core/strategy_runtime.py     | orchestration wrapper   |
| core/integrated_runtime.py   | integration wrapper     |
| runtime/cognitive_runtime.py | experimental            |
| runtime/financial_runtime.py | analytical only         |

---

# 3. Event Authority

| Responsibility              | Canonical Module           |
| --------------------------- | -------------------------- |
| canonical event definitions | core/events.py             |
| synchronous propagation     | runtime/event_bus.py       |
| asynchronous propagation    | runtime/async_event_bus.py |

---

## Event Authority Rules

Canonical runtime events MUST originate from:

* core/events.py

Transport systems:

* propagate canonical events
* MUST NOT redefine event semantics
* MUST NOT create competing event authorities

Architectural principle:

single event authority
multiple transport mechanisms

---

## External Event Normalization

| Responsibility                 | Canonical Module     |
| ------------------------------ | -------------------- |
| websocket ingestion            | market/binance_ws.py |
| exchange payload normalization | core/events.py       |

External exchange payloads are NOT canonical runtime events.

Normalization flow:

EXTERNAL PAYLOAD
↓
NORMALIZATION
↓
RuntimeEvent
↓
Transport Layer
↓
Runtime Consumers

Internal systems MUST remain isolated from:

* exchange-specific schemas
* websocket payload formats
* transport-specific implementations

---

# 4. Risk Authority

| Responsibility       | Canonical Module               |
| -------------------- | ------------------------------ |
| kill switch          | risk/kill_switch.py            |
| exposure control     | risk/exposure.py               |
| cooldown enforcement | risk/cooldown.py               |
| session risk         | risk/session_risk.py           |
| position sizing      | risk/dynamic_position_sizer.py |

---

## Risk Rules

Risk systems possess override authority over:

* strategy systems
* execution systems
* orchestration systems

No component may:

* bypass risk approval
* override kill switch state
* disable cooldown enforcement
* directly approve forbidden execution

Execution is forbidden if:

* cooldown active
* emergency stop active
* portfolio reconciliation failed
* runtime governance rejected execution

Risk authority is FINAL.

---

# 5. Strategy Authority

| Responsibility            | Canonical Module            |
| ------------------------- | --------------------------- |
| regime classification     | strategy/regime.py          |
| volatility classification | strategy/volatility.py      |
| grid spacing              | strategy/spacing.py         |
| grid structure            | strategy/asymmetric_grid.py |
| orchestration             | strategy/orchestrator.py    |
| mean reversion strategy   | strategy/mean_reversion.py  |

---

## Strategy Rules

Strategy systems may:

* generate signals
* classify market state
* recommend execution
* generate portfolio suggestions

Strategy systems may NOT:

* execute trades directly
* bypass runtime governance
* override risk systems
* mutate canonical runtime state

---

## Experimental Strategy Systems

| Module               | Status       |
| -------------------- | ------------ |
| adaptive_ensemble.py | experimental |
| meta_learning.py     | experimental |
| online_learning.py   | experimental |
| autonomous_decay.py  | experimental |
| regime_router.py     | experimental |

Experimental strategy systems:

* may observe runtime
* may simulate decisions
* may generate recommendations

Experimental systems may NOT:

* directly execute trades
* mutate governance state
* bypass canonical execution flow

---

# 6. Execution Authority

| Responsibility            | Canonical Module                |
| ------------------------- | ------------------------------- |
| execution routing         | exchange/execution_engine.py    |
| paper trading             | exchange/paper_exchange.py      |
| execution simulation      | exchange/execution_simulator.py |
| portfolio synchronization | exchange/portfolio_sync.py      |

---

## Execution Rules

Execution systems:

* require prior runtime approval
* require prior risk approval
* require execution validation
* must emit observable events

Execution systems may NOT:

* override governance state
* bypass risk systems
* mutate runtime lifecycle
* directly authorize execution

Execution approval chain:

RUNTIME GOVERNANCE
↓
RISK VALIDATION
↓
EXECUTION VALIDATION
↓
EXECUTION ENGINE

---

# 7. Persistence Authority

| Responsibility      | Canonical Module             |
| ------------------- | ---------------------------- |
| runtime persistence | persistence/runtime_store.py |
| metrics persistence | persistence/metrics_store.py |
| event persistence   | persistence/event_store.py   |
| runtime journaling  | runtime/event_journal.py     |

---

## Persistence Rules

Runtime state:

* overwrite latest authoritative state

Metrics:

* append-only

Events:

* immutable append-only

Journal entries:

* immutable operational history

Persistence systems MUST NOT:

* mutate runtime decisions
* override governance state
* replay unauthorized execution

---

# 8. Observability Authority

| Responsibility   | Canonical Module         |
| ---------------- | ------------------------ |
| runtime logging  | runtime/logger.py        |
| event journaling | runtime/event_journal.py |
| runtime metrics  | runtime/metrics.py       |

---

## Observability Rules

Critical runtime transitions SHOULD emit observable events.

Observable categories:

* runtime transitions
* governance overrides
* execution approvals
* execution failures
* portfolio synchronization
* emergency conditions

Architectural principle:

critical runtime behavior MUST remain auditable

---

# 9. Governance Authority

| Responsibility        | Canonical Module                  |
| --------------------- | --------------------------------- |
| governed runtime      | runtime/governed_runtime.py       |
| runtime transitions   | core/runtime_transition_engine.py |
| transition rules      | core/runtime_transition_rules.py  |
| runtime state machine | core/runtime_state_machine.py     |

---

## Governance Rules

Governance systems possess authority over:

* runtime lifecycle
* execution permissions
* emergency stop state
* recovery state
* cooldown coordination

Governance systems may:

* halt execution
* disable trading
* enter recovery mode
* trigger safe mode

Governance systems may NOT:

* bypass persistence integrity
* override immutable journal history
* bypass risk authority

---

## Experimental Governance Systems

| Module             | Status       |
| ------------------ | ------------ |
| meta_governance.py | experimental |
| hierarchy.py       | experimental |
| evolution.py       | experimental |
| population.py      | experimental |

Experimental governance systems:

* may simulate governance policies
* may produce analytics
* may recommend runtime adjustments

Experimental governance systems may NOT:

* directly mutate runtime governance
* bypass canonical runtime authority
* authorize execution independently

---

# 10. Repository Boundary Authority

| Repository Area | Responsibility                    |
| --------------- | --------------------------------- |
| src/            | implementation                    |
| tests/          | deterministic validation          |
| scripts/        | runtime demos and experimentation |
| docs/           | architectural authority           |

---

## Repository Rules

tests/

* deterministic validation only

scripts/

* manual execution
* runtime demos
* experimentation
* operational simulations

Demo scripts MUST NOT:

* pollute pytest collection
* redefine runtime contracts
* replace deterministic validation

---

# 11. Experimental Isolation Policy

Experimental systems:

* may observe runtime
* may generate analytics
* may simulate execution
* may recommend decisions

Experimental systems may NOT:

* directly execute trades
* bypass governance
* bypass risk systems
* mutate canonical runtime state
* redefine runtime authority

Experimental infrastructure MUST remain downstream from:

* governance authority
* runtime authority
* risk authority

---

# 12. Immediate Consolidation Targets

Priority 1:

* consolidate runtime ownership

Priority 2:

* centralize event contracts

Priority 3:

* simplify governance topology

Priority 4:

* isolate experimental ML systems

Priority 5:

* reduce orchestration overlap

Priority 6:

* improve runtime observability consistency

---

# 13. Long-Term Architectural Goal

Target architecture:

validated
event-driven
risk-governed
recoverable
observable
modular
execution-safe
deterministic
authority-centralized
operationally auditable
