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
* stabilize autonomous runtime orchestration
* standardize lifecycle observability
* centralize execution telemetry

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

| Responsibility | Canonical Module |
|---|---|
| runtime lifecycle | runtime/governed_runtime.py |
| runtime execution loop | runtime/runtime_loop.py |
| async runtime loop | runtime/async_runtime_loop.py |
| runtime state | runtime/runtime_state.py |
| runtime enums | runtime/runtime_enums.py |
| live tick orchestration | runtime/live_tick_handler.py |
| runtime snapshots | runtime/runtime_snapshot.py |
| runtime rendering | runtime/runtime_console_renderer.py |

---

## Runtime Responsibilities

Canonical runtime authority controls:

* lifecycle state
* runtime transitions
* execution permissions
* safe mode state
* emergency stop state
* cooldown state
* live tick orchestration
* autonomous runtime coordination
* runtime telemetry generation
* active trade lifecycle visibility
* completed trade lifecycle visibility
* runtime observability propagation

Runtime authority may:

* pause execution
* stop execution
* disable trading
* reject runtime continuation
* initiate recovery flow
* reject live execution routing
* halt execution on exposure breach
* block new entries
* emit runtime telemetry

No downstream system may override runtime governance directly.

---

## Validated Runtime Infrastructure

| Module | Status |
|---|---|
| runtime/event_bus.py | validated |
| runtime/async_event_bus.py | validated |
| runtime/runtime_loop.py | validated |
| runtime/live_tick_handler.py | validated |
| runtime/runtime_snapshot.py | validated |
| runtime/runtime_console_renderer.py | validated |
| exchange/binance_websocket_client.py | validated |
| market_data/market_data_router.py | validated |
| market/timeframe_aggregator.py | validated |

Validated runtime capabilities:
- reconnect-safe websocket lifecycle
- candle aggregation
- candle-close execution
- active trade telemetry
- completed trade journaling
- exposure governance
- runtime halting
- portfolio telemetry rendering
- runtime snapshot generation

---

## Non-Canonical Runtime Systems

| Module | Status |
|---|---|
| core/runtime.py | consolidation candidate |
| core/autonomous_runtime.py | orchestration wrapper |
| core/strategy_runtime.py | orchestration wrapper |
| core/integrated_runtime.py | integration wrapper |
| runtime/cognitive_runtime.py | experimental |
| runtime/financial_runtime.py | analytical only |

---

# 3. Event Authority

| Responsibility | Canonical Module |
|---|---|
| synchronous propagation | runtime/event_bus.py |
| asynchronous propagation | runtime/async_event_bus.py |
| live market routing | market_data/market_data_router.py |
| candle aggregation routing | market/timeframe_aggregator.py |

---

## Event Authority Rules

Transport systems:

* propagate normalized runtime state
* MUST NOT redefine execution semantics
* MUST NOT bypass governance authority
* MUST remain replay-safe
* MUST preserve lifecycle ordering

Architectural principle:

single runtime authority
multiple transport mechanisms

---

## External Event Normalization

| Responsibility | Canonical Module |
|---|---|
| websocket ingestion | exchange/binance_websocket_client.py |
| market tick normalization | market_data/market_tick.py |
| candle aggregation | market/timeframe_aggregator.py |
| runtime routing | market_data/market_data_router.py |

External exchange payloads are NOT canonical runtime state.

Normalization flow:

BINANCE PAYLOAD
↓
MarketTick
↓
TimeframeAggregator
↓
Candle
↓
MarketDataSnapshot
↓
Runtime Consumption

Internal systems MUST remain isolated from:

* exchange-specific schemas
* websocket payload formats
* transport-specific implementations

---

# 4. Risk Authority

| Responsibility | Canonical Module |
|---|---|
| kill switch | risk/kill_switch.py |
| exposure control | risk/exposure.py |
| cooldown enforcement | risk/cooldown.py |
| session risk | risk/session_risk.py |
| position sizing | risk/dynamic_position_sizer.py |
| portfolio exposure governance | exchange/portfolio_risk.py |

---

## Risk Rules

Risk systems possess override authority over:

* strategy systems
* execution systems
* orchestration systems
* live runtime execution

No component may:

* bypass risk approval
* override kill switch state
* disable cooldown enforcement
* directly approve forbidden execution

Execution is forbidden if:

* cooldown active
* emergency stop active
* runtime governance rejected execution
* portfolio synchronization failed
* exposure threshold exceeded

Risk authority is FINAL.

Validated governance capabilities:
- exposure-based execution blocking
- runtime halting
- execution permission gating
- portfolio exposure evaluation

---

# 5. Strategy Authority

| Responsibility | Canonical Module |
|---|---|
| regime classification | strategy/regime.py |
| grid spacing | strategy/spacing.py |
| grid structure | strategy/asymmetric_grid.py |
| orchestration | strategy/orchestrator.py |

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
* bypass execution validation

---

# 6. Execution Authority

| Responsibility | Canonical Module |
|---|---|
| execution routing | exchange/execution_engine.py |
| paper trading | exchange/paper_exchange.py |
| execution simulation | exchange/execution_simulator.py |
| websocket execution ingestion | exchange/binance_websocket_client.py |
| portfolio synchronization | exchange/portfolio_sync.py |
| trade lifecycle tracking | runtime/runtime_snapshot.py |

---

## Execution Rules

Execution systems:

* require prior runtime approval
* require prior risk approval
* require execution validation
* must emit observable runtime transitions
* must synchronize portfolio state
* must emit lifecycle telemetry

Execution systems may NOT:

* override governance state
* bypass risk systems
* mutate runtime lifecycle
* directly authorize execution

Execution approval chain:

LIVE MARKET DATA
↓
RUNTIME GOVERNANCE
↓
RISK VALIDATION
↓
EXECUTION VALIDATION
↓
PAPER EXCHANGE EXECUTION
↓
PORTFOLIO SYNCHRONIZATION
↓
RUNTIME SNAPSHOT
↓
OBSERVABILITY

Validated execution capabilities:
- active trade lifecycle tracking
- completed trade journaling
- mark-to-market accounting
- unrealized pnl tracking
- holdings valuation
- exposure tracking

---

# 7. Persistence Authority

| Responsibility | Canonical Module |
|---|---|
| runtime persistence | persistence/runtime_store.py |
| metrics persistence | persistence/metrics_store.py |
| event persistence | persistence/event_store.py |
| runtime journaling | runtime/event_journal.py |

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

Current persistence status:
- not yet implemented
- runtime currently fully in-memory

Future persistence objectives:
- runtime snapshot persistence
- completed trade persistence
- structured telemetry persistence
- replay-safe execution journaling

---

# 8. Observability Authority

| Responsibility | Canonical Module |
|---|---|
| runtime logging | runtime/logger.py |
| event journaling | runtime/event_journal.py |
| runtime metrics | runtime/metrics.py |
| runtime snapshots | runtime/runtime_snapshot.py |
| console rendering | runtime/runtime_console_renderer.py |

---

## Observability Rules

Critical runtime transitions SHOULD emit observable events.

Observable categories:

* runtime transitions
* live execution
* portfolio synchronization
* unrealized pnl
* execution failures
* emergency conditions
* websocket connectivity
* active trade lifecycle
* completed trade lifecycle
* exposure state
* portfolio valuation

Architectural principle:

critical runtime behavior MUST remain auditable

Validated observability capabilities:
- runtime status rendering
- market telemetry rendering
- portfolio telemetry rendering
- active trade rendering
- completed trade rendering
- governance halt visibility
- exposure visibility

---

# 9. Governance Authority

| Responsibility | Canonical Module |
|---|---|
| governed runtime | runtime/governed_runtime.py |
| runtime transitions | core/runtime_transition_engine.py |
| transition rules | core/runtime_transition_rules.py |
| runtime state machine | core/runtime_state_machine.py |

---

## Governance Rules

Governance systems possess authority over:

* runtime lifecycle
* execution permissions
* emergency stop state
* recovery state
* cooldown coordination
* live runtime orchestration
* exposure halting
* execution gating

Governance systems may:

* halt execution
* disable trading
* enter recovery mode
* trigger safe mode
* reject execution
* block new entries

Governance systems may NOT:

* bypass persistence integrity
* override immutable journal history
* bypass risk authority

Validated governance capabilities:
- runtime halting
- exposure-based blocking
- governance-aware execution routing
- centralized execution approval

---

# 10. Repository Boundary Authority

| Repository Area | Responsibility |
|---|---|
| src/ | implementation |
| tests/ | deterministic validation |
| scripts/ | runtime demos and experimentation |
| docs/ | architectural authority |

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

* stabilize runtime persistence

Priority 2:

* centralize execution telemetry

Priority 3:

* implement FastAPI telemetry layer

Priority 4:

* implement dashboard infrastructure

Priority 5:

* stabilize replay-safe persistence

Priority 6:

* isolate experimental ML systems

Priority 7:

* improve runtime observability consistency

Priority 8:

* stabilize multi-symbol orchestration

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
live-data driven
autonomous
operationally auditable
runtime-stabilized
lifecycle-observable
replay-safe