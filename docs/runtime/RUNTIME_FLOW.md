````md id="h3k9v2"
# Runtime Execution Flow

# 1. Objective

This document defines the canonical operational flow of the trading system.

Purpose:
- eliminate execution ambiguity
- prevent runtime fragmentation
- enforce risk-first execution
- centralize governance authority
- stabilize live runtime orchestration
- standardize lifecycle observability
- preserve replay-safe execution topology

This flow is authoritative.

All future runtime systems must conform to this topology.

---

# 2. Canonical Runtime Flow

```text
LIVE MARKET DATA
    ↓
MARKET NORMALIZATION
    ↓
CANDLE AGGREGATION
    ↓
RUNTIME ROUTING
    ↓
AUTONOMOUS RUNTIME
    ↓
PORTFOLIO RISK EVALUATION
    ↓
POSITION SIZING
    ↓
EXECUTION APPROVAL
    ↓
PAPER EXECUTION
    ↓
PORTFOLIO UPDATE
    ↓
RUNTIME SNAPSHOT
    ↓
RUNTIME GOVERNANCE
    ↓
OBSERVABILITY
    ↓
PERSISTENCE
````

Validated runtime capabilities:

* reconnect-safe websocket lifecycle
* candle aggregation
* candle-close execution
* governance-aware execution routing
* active trade lifecycle tracking
* completed trade journaling
* runtime snapshot generation
* portfolio valuation propagation

---

# 2.1 Validated Live Runtime Execution Path

Validated execution topology:

```text
BINANCE WEBSOCKET
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
MarketDataRouter
    ↓
LiveTickHandler
    ↓
Autonomous Runtime
    ↓
Portfolio Risk Synchronization
    ↓
Position Sizing
    ↓
Execution Validation
    ↓
Paper Execution
    ↓
Portfolio Synchronization
    ↓
PnL Evaluation
    ↓
Runtime Snapshot
    ↓
Console Observability
```

Validated components:

* live websocket ingestion
* reconnect handling
* websocket shutdown lifecycle
* timeframe candle aggregation
* candle-close autonomous execution
* autonomous execution
* paper trading lifecycle
* portfolio synchronization
* unrealized pnl tracking
* invested capital tracking
* holdings valuation
* portfolio valuation
* active trade lifecycle tracking
* completed trade journaling
* runtime snapshot generation
* runtime observability

---

# 3. Runtime Authority Hierarchy

## Highest Authority

Risk systems possess override authority over:

* strategy systems
* execution systems
* orchestration systems

Risk authority may:

* reject trades
* trigger cooldowns
* trigger emergency stops
* disable execution globally
* halt runtime execution
* block new entries

Validated governance capabilities:

* exposure-based execution blocking
* execution permission gating
* centralized execution approval

Architectural principle:

risk authority is FINAL.

---

## Runtime Governance Authority

Governed runtime controls:

* lifecycle state
* execution permissions
* cooldown state
* emergency state
* recovery state
* live runtime coordination
* runtime observability propagation

Runtime governance may:

* pause runtime
* stop runtime
* disable trading
* enter safe mode
* halt execution
* suppress execution routing

Validated governance capabilities:

* governance-aware execution routing
* runtime halting
* exposure-aware execution suppression

---

## Strategy Authority

Strategy systems may:

* generate recommendations
* generate execution proposals
* provide regime classifications

Strategy systems may NOT:

* execute orders directly
* bypass risk
* mutate runtime state
* override governance

Current runtime strategy limitations:

* hardcoded BUY execution
* fixed take-profit evaluation
* no advanced signal engine

Architectural principle:

lifecycle stability > strategy sophistication

---

## Execution Authority

Execution systems may:

* simulate fills
* route approved orders
* apply spread/slippage models
* update portfolio state
* emit lifecycle telemetry

Execution systems may NOT:

* override governance state
* bypass risk approval
* authorize execution independently

Validated execution capabilities:

* active trade lifecycle tracking
* completed trade journaling
* unrealized pnl propagation
* mark-to-market accounting
* portfolio valuation propagation

---

# 4. Canonical Event Flow

```text
LIVE_MARKET_TICK
    ↓
MARKET_NORMALIZED
    ↓
CANDLE_UPDATED
    ↓
CANDLE_CLOSED
    ↓
MARKET_STATE_UPDATE
    ↓
RUNTIME_EVALUATION
    ↓
RISK_CHECK
    ↓
POSITION_SIZED
    ↓
EXECUTION_APPROVED
    ↓
ORDER_EXECUTED
    ↓
POSITION_UPDATED
    ↓
PNL_UPDATED
    ↓
RUNTIME_SNAPSHOT_UPDATED
    ↓
RUNTIME_UPDATED
```

Validated event capabilities:

* websocket tick propagation
* candle aggregation propagation
* runtime telemetry propagation
* lifecycle observability propagation
* governance-aware execution propagation

---

# 5. Runtime Loop Ownership

Canonical runtime loop:

```text id="d4f2wa"
runtime/runtime_loop.py
```

Responsibilities:

* polling
* event propagation
* orchestration coordination
* heartbeat management
* runtime lifecycle coordination

Validated runtime loop capabilities:

* reconnect-safe orchestration
* runtime propagation coordination
* lifecycle-safe execution routing

---

# 5.1 Live Runtime Ownership

Canonical live runtime coordinator:

```text id="p6m71s"
runtime/live_tick_handler.py
```

Responsibilities:

* live tick processing
* autonomous runtime invocation
* execution gating
* pnl monitoring
* candle-close orchestration
* position lifecycle management
* runtime telemetry propagation

Validated live runtime capabilities:

* candle-close execution
* active trade lifecycle visibility
* unrealized pnl propagation
* portfolio valuation propagation
* runtime snapshot propagation

---

# 5.2 Runtime Observability Ownership

Canonical runtime observability systems:

```text id="i5eqv2"
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

Validated telemetry visibility:

* latest market price
* latest candle close
* unrealized pnl
* invested capital
* holdings value
* available cash
* total portfolio value
* active trade lifecycle
* completed trade lifecycle
* runtime operating state

---

# 6. Persistence Flow

## Runtime State

Stored after:

* lifecycle changes
* cooldown transitions
* emergency transitions
* governance transitions

Pattern:

* overwrite latest authoritative state

---

## Metrics

Stored after:

* execution events
* pnl transitions
* runtime cycles
* portfolio valuation updates

Pattern:

* append-only

---

## Event Journal

Stored after:

* critical runtime events
* execution transitions
* emergency triggers
* lifecycle transitions

Pattern:

* immutable append-only

---

## Current Persistence Status

Current state:

* not implemented
* runtime fully in-memory
* shutdown clears telemetry
* shutdown clears trade history

Planned persistence targets:

* runtime snapshot persistence
* completed trade persistence
* structured execution journaling
* replay-safe event persistence

---

# 7. Execution Safety Rules

No execution allowed if:

* emergency stop active
* cooldown active
* runtime paused
* risk gate rejected
* portfolio reconciliation failed
* exposure threshold exceeded
* governance halted execution

Execution approval requires:

* runtime approval
* risk approval
* execution integrity validation
* portfolio synchronization integrity

Architectural principle:

execution authority MUST remain downstream from:

* governance
* risk systems
* execution validation

---

# 8. Runtime Lifecycle Status

Validated:

* live market ingestion
* reconnect-safe websocket lifecycle
* timeframe candle aggregation
* candle-close autonomous execution
* autonomous BUY execution
* portfolio synchronization
* unrealized pnl evaluation
* invested capital tracking
* holdings valuation
* portfolio valuation
* duplicate execution prevention
* active trade lifecycle tracking
* completed trade journaling
* runtime snapshot generation
* runtime console rendering
* governance-aware execution routing

Current limitations:

* no persistence layer
* no FastAPI telemetry API
* no dashboard frontend
* no replay engine
* no advanced signal engine
* no stop-loss lifecycle
* no multi-symbol execution

---

# 9. Immediate Runtime Priorities

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

---

# 10. Current Strategic Goal

Target runtime properties:

deterministic
recoverable
risk-governed
event-driven
observable
modular
execution-safe
live-data autonomous paper trading
governance-controlled
lifecycle-observable
replay-safe prepared

Current focus:

* runtime stabilization
* observability
* lifecycle integrity
* persistence preparation
* dashboard readiness

NOT:

* unrestricted autonomous execution
* advanced ML orchestration
* distributed governance
* profitability optimization

```
```
