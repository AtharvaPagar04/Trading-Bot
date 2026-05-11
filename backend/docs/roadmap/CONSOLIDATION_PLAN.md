````md id="n5x8v1"
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
| runtime/runtime_snapshot.py | CANONICAL | runtime telemetry snapshots |
| runtime/runtime_console_renderer.py | CANONICAL | runtime observability rendering |

---

## Stable Runtime Infrastructure

| Module | Status |
|---|---|
| exchange/binance_websocket_client.py | VALIDATED |
| market_data/market_data_router.py | VALIDATED |
| market/timeframe_aggregator.py | VALIDATED |
| exchange/paper_exchange.py | VALIDATED |
| core/autonomous_runtime.py | VALIDATED SUPPORTING |

Validated runtime capabilities:
- reconnect-safe websocket lifecycle
- candle aggregation
- candle-close execution
- runtime snapshot generation
- runtime console rendering
- active trade lifecycle visibility
- completed trade journaling
- exposure governance
- runtime halting

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
- centralize runtime observability
- preserve governance-first execution routing

---

# 2. Event System Audit

## Canonical Event System

| Module | Status |
|---|---|
| runtime/event_bus.py | CANONICAL |
| runtime/async_event_bus.py | CANONICAL |
| market_data/market_data_router.py | CANONICAL |
| market/timeframe_aggregator.py | CANONICAL |

---

## Validated Event Flow

```text
LIVE BINANCE TRADE
↓
BinanceWebSocketClient
↓
MarketTick
↓
TimeframeAggregator
↓
Candle
↓
MarketDataSnapshot
↓
LiveTickHandler
↓
Autonomous Runtime
↓
Portfolio Risk Evaluation
↓
Execution Decision
↓
PaperExchange
↓
Portfolio Synchronization
↓
Runtime Snapshot
↓
Console Observability
````

Validated event capabilities:

* websocket tick propagation
* candle aggregation propagation
* autonomous runtime invocation
* governance-aware execution routing
* runtime snapshot propagation
* observability propagation

---

## Duplicate Event Systems

| Module                     | Risk                  |
| -------------------------- | --------------------- |
| events/event.py            | duplicated semantics  |
| events/event_dispatcher.py | propagation ambiguity |

Action:

* converge toward single runtime event topology
* normalize all market ingestion through MarketTick
* preserve deterministic runtime propagation

---

# 3. Runtime Lifecycle Audit

## Stable Lifecycle Components

| Module                              |
| ----------------------------------- |
| runtime/live_tick_handler.py        |
| runtime/runtime_snapshot.py         |
| runtime/runtime_console_renderer.py |
| exchange/paper_exchange.py          |
| core/autonomous_runtime.py          |
| market_data/market_data_router.py   |
| market/timeframe_aggregator.py      |

---

## Validated Lifecycle

```text
LIVE BINANCE TRADE
↓
MarketTick
↓
TimeframeAggregator
↓
Candle
↓
Runtime Governance
↓
Portfolio Risk Evaluation
↓
Execution Validation
↓
Paper Execution
↓
Portfolio Synchronization
↓
Runtime Snapshot
↓
Console Observability
```

Validated lifecycle capabilities:

* active trade lifecycle tracking
* completed trade journaling
* unrealized pnl propagation
* portfolio valuation
* governance-aware execution approval
* exposure-based execution blocking

---

# 4. Governance Layer Audit

## Stable Governance Components

| Module                        |
| ----------------------------- |
| risk/kill_switch.py           |
| risk/session_risk.py          |
| risk/cooldown.py              |
| exchange/portfolio_risk.py    |
| core/runtime_state_machine.py |
| runtime/governed_runtime.py   |

Validated governance capabilities:

* exposure-based execution blocking
* runtime halting
* governance-aware execution routing
* execution permission gating
* portfolio exposure evaluation

---

## Governance Expansion Risk

| Module             |
| ------------------ |
| meta_governance.py |
| hierarchy.py       |
| evolution.py       |
| population.py      |

Risk:

* governance complexity exceeds runtime stabilization maturity

Action:

* isolate experimental governance systems
* prioritize runtime stabilization
* preserve centralized governance authority

---

# 5. Strategy Layer Audit

## Stable Strategy Components

| Module                      |
| --------------------------- |
| strategy/regime.py          |
| strategy/spacing.py         |
| strategy/asymmetric_grid.py |
| strategy/orchestrator.py    |

---

## Current Runtime Strategy Limitation

Current runtime behavior:

* hardcoded BUY execution
* fixed take-profit evaluation
* no dynamic signal engine
* no stop-loss lifecycle
* no advanced exits

Priority:

* stabilize lifecycle first
* stabilize persistence first
* strategy sophistication later

Architectural principle:
execution lifecycle stability > strategy sophistication

---

# 6. Persistence Layer Audit

## Canonical Persistence Roles

| Component     | Pattern           |
| ------------- | ----------------- |
| runtime_store | latest state      |
| metrics_store | append-only       |
| event_store   | immutable journal |

---

## Current Persistence Status

Current state:

* not implemented
* runtime fully in-memory
* shutdown clears telemetry
* shutdown clears trade history

Future persistence targets:

* runtime snapshot persistence
* completed trade persistence
* structured execution journaling
* replay-safe event persistence

---

## Current Risk

Potential overlap:

* runtime_snapshot
* runtime_loader
* runtime_recovery

Action:

* define explicit lifecycle recovery ownership
* separate snapshot serialization from persistence ownership
* preserve replay-safe boundaries

---

# 7. Observability Consolidation Audit

## Canonical Observability Components

| Module                              |
| ----------------------------------- |
| runtime/runtime_snapshot.py         |
| runtime/runtime_console_renderer.py |
| runtime/logger.py                   |
| runtime/event_journal.py            |
| runtime/metrics.py                  |

---

## Validated Observability

Validated:

* runtime status rendering
* market telemetry rendering
* portfolio telemetry rendering
* active trade visibility
* completed trade visibility
* unrealized pnl visibility
* exposure visibility
* governance halt visibility
* portfolio valuation visibility

Current telemetry coverage:

* latest market price
* latest candle close
* active trade lifecycle
* completed trade lifecycle
* unrealized pnl
* invested capital
* holdings value
* available cash
* portfolio valuation

Future observability targets:

* persistence-backed telemetry
* websocket dashboard streaming
* replay-safe telemetry history
* runtime analytics API

---

# 8. Immediate Freeze Policy

Frozen Areas:

* new governance abstractions
* new runtime orchestration systems
* distributed runtime systems
* ML execution autonomy
* experimental execution bypasses

Allowed Areas:

* runtime stabilization
* observability
* lifecycle refinement
* execution integrity
* recovery integrity
* persistence infrastructure
* dashboard preparation

---

# 9. Next Consolidation Objectives

Priority 1:

* stabilize runtime persistence

Priority 2:

* implement structured execution journaling

Priority 3:

* implement FastAPI telemetry layer

Priority 4:

* implement dashboard websocket streaming

Priority 5:

* reduce runtime logging spam

Priority 6:

* stabilize replay-safe persistence

Priority 7:

* isolate experimental systems

Priority 8:

* stabilize multi-symbol orchestration

---

# 10. Current Strategic Direction

The project should evolve toward:

deterministic
event-driven
risk-governed
observable
recoverable
modular
live-data autonomous paper trading infrastructure

Target characteristics:

* governance-controlled execution
* lifecycle-aware observability
* replay-safe telemetry
* centralized runtime authority
* portfolio-aware orchestration
* execution lifecycle visibility

NOT toward:

* uncontrolled abstraction growth
* premature ML complexity
* unrestricted autonomous behavior
* fragmented runtime governance
* distributed execution complexity

```
```
