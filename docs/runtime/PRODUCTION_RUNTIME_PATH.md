````md id="w8m2q4"
# Production Runtime Path

# 1. Objective

This document defines the ONLY approved runtime execution path for:

- dry-run execution
- paper trading
- future live execution

Any module outside this path is considered:
- supporting
- analytical
- experimental

Experimental systems may NOT bypass this runtime path.

The production runtime path MUST remain:
- governance-controlled
- lifecycle-observable
- replay-safe prepared
- portfolio-aware
- execution-safe

---

# 2. Canonical Runtime Execution Flow

```text
LIVE BINANCE TRADE
    ↓
exchange/binance_websocket_client.py
    ↓
MarketTick Normalization
    ↓
market/timeframe_aggregator.py
    ↓
Candle
    ↓
MarketDataSnapshot
    ↓
market_data/market_data_router.py
    ↓
runtime/live_tick_handler.py
    ↓
core/autonomous_runtime.py
    ↓
Portfolio Risk Evaluation
    ↓
Execution Validation
    ↓
exchange/paper_exchange.py
    ↓
Portfolio Synchronization
    ↓
Runtime Snapshot
    ↓
Runtime Governance
    ↓
Console Observability
    ↓
Persistence
````

Validated runtime execution capabilities:

* reconnect-safe websocket lifecycle
* candle aggregation
* candle-close execution
* governance-aware execution routing
* active trade lifecycle tracking
* completed trade journaling
* runtime snapshot generation
* portfolio valuation propagation

---

# 3. Runtime Ownership

## Canonical Runtime Authority

Primary authority:

```text
runtime/governed_runtime.py
```

Responsibilities:

* lifecycle control
* emergency state
* cooldown state
* execution permission state
* runtime orchestration authority
* runtime halting
* governance-aware execution gating

Validated governance capabilities:

* exposure-based execution blocking
* centralized execution approval
* runtime halt propagation
* execution suppression

---

## Canonical Live Runtime Handler

Primary runtime execution coordinator:

```text
runtime/live_tick_handler.py
```

Responsibilities:

* live tick processing
* runtime orchestration
* portfolio lifecycle coordination
* execution gating
* pnl evaluation
* candle-close orchestration
* active trade lifecycle propagation
* runtime telemetry propagation

Validated runtime capabilities:

* candle-close autonomous execution
* unrealized pnl propagation
* portfolio telemetry propagation
* active trade lifecycle visibility
* completed trade lifecycle visibility

---

## Canonical Runtime Observability

Primary runtime observability systems:

```text
runtime/runtime_snapshot.py
runtime/runtime_console_renderer.py
```

Responsibilities:

* runtime snapshot generation
* portfolio telemetry generation
* active trade telemetry
* completed trade telemetry
* runtime console rendering
* lifecycle observability propagation

Current telemetry visibility:

* latest market price
* latest candle close
* runtime operating state
* unrealized pnl
* invested capital
* holdings valuation
* portfolio valuation
* active trade lifecycle
* completed trade lifecycle
* exposure state

---

# 4. Canonical Event Authority

Canonical event transport systems:

```text
runtime/event_bus.py
runtime/async_event_bus.py
```

Canonical market routing:

```text
market_data/market_data_router.py
market/timeframe_aggregator.py
```

Architectural principle:

all external exchange payloads MUST be normalized before runtime propagation.

Validated event capabilities:

* websocket tick propagation
* candle aggregation propagation
* runtime telemetry propagation
* governance-aware execution propagation
* execution lifecycle propagation

Normalization flow:

```text
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
```

---

# 5. Canonical Risk Authority

Risk systems possess final override authority.

Approved risk systems:

* session_risk.py
* exposure.py
* cooldown.py
* kill_switch.py
* exchange/portfolio_risk.py

Execution is forbidden if:

* cooldown active
* emergency stop active
* runtime paused
* reconciliation failed
* portfolio exposure exceeded
* governance halted execution

Validated governance capabilities:

* exposure-based execution blocking
* runtime execution gating
* centralized execution approval
* governance-aware routing

Architectural principle:

risk authority is FINAL.

---

# 6. Canonical Execution Authority

Approved execution systems:

* exchange/execution_engine.py
* exchange/paper_exchange.py
* exchange/execution_simulator.py

Execution systems:

* may not bypass governance
* may not mutate runtime lifecycle
* may not authorize execution independently

Validated execution capabilities:

* paper execution lifecycle
* mark-to-market accounting
* unrealized pnl propagation
* active trade lifecycle tracking
* completed trade journaling
* portfolio valuation propagation

Execution flow:

```text
Runtime Governance
↓
Portfolio Risk Evaluation
↓
Execution Validation
↓
PaperExchange
↓
Portfolio Synchronization
↓
Runtime Snapshot
↓
Console Observability
```

---

# 7. Live Runtime Validation Status

Validated:

* websocket lifecycle
* reconnect handling
* websocket shutdown lifecycle
* live tick routing
* timeframe candle aggregation
* candle-close execution
* autonomous paper execution
* portfolio synchronization
* unrealized pnl tracking
* invested capital tracking
* holdings valuation
* portfolio valuation
* active trade lifecycle tracking
* completed trade journaling
* runtime snapshot generation
* runtime console rendering
* exposure governance
* runtime halting
* execution gating

Current limitations:

* no persistence layer
* no FastAPI telemetry API
* no dashboard frontend
* no replay engine
* no stop-loss lifecycle
* no dynamic signal engine
* no multi-symbol orchestration

---

# 8. Persistence Path

Current persistence status:

* not implemented
* runtime fully in-memory
* shutdown clears telemetry
* shutdown clears trade history

Planned persistence targets:

* runtime snapshot persistence
* completed trade persistence
* structured execution journaling
* replay-safe event persistence

Future persistence flow:

```text
Runtime Snapshot
↓
Persistence Layer
↓
Historical Runtime Store
↓
Replay Engine
↓
Analytics Layer
```

---

# 9. Experimental Isolation

The following systems are NOT on the production runtime path:

## Experimental Strategy Systems

* adaptive_ensemble.py
* meta_learning.py
* online_learning.py

## Experimental Governance Systems

* meta_governance.py
* evolution.py
* hierarchy.py

Experimental systems:

* may observe runtime
* may generate analytics
* may simulate decisions

Experimental systems may NOT:

* execute trades
* bypass governance
* mutate canonical runtime state
* bypass risk systems

Architectural principle:

experimental systems MUST remain downstream from:

* governance
* execution validation
* runtime authority

---

# 10. Production Runtime Principles

Production runtime must remain:

deterministic
recoverable
observable
risk-governed
modular
execution-safe
live-data normalized
governance-controlled
lifecycle-observable
replay-safe prepared

Core architectural principles:

* centralized runtime governance
* normalized market ingestion
* governance-aware execution
* observable lifecycle propagation
* portfolio-aware orchestration
* execution-safe runtime flow

Complexity must justify measurable operational benefit.

---

# 11. Immediate Runtime Priorities

Priority 1:
runtime persistence layer

Priority 2:
structured execution journaling

Priority 3:
FastAPI telemetry layer

Priority 4:
dashboard websocket streaming

Priority 5:
historical runtime replay

Priority 6:
multi-symbol orchestration

Priority 7:
dashboard observability stabilization

---

# 12. Current Strategic Objective

Current objective is:

stable
observable
governance-controlled
live autonomous paper trading infrastructure

Current focus:

* runtime stabilization
* lifecycle observability
* persistence preparation
* dashboard readiness
* execution lifecycle integrity

NOT:

* unrestricted autonomous execution
* advanced ML orchestration
* distributed governance
* high-frequency execution
* profitability optimization

```
```
