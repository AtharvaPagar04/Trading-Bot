# Runtime Execution Flow

# 1. Objective

This document defines the canonical operational flow of the trading system.

Purpose:
- eliminate execution ambiguity
- prevent runtime fragmentation
- enforce risk-first execution
- centralize governance authority
- stabilize live runtime orchestration

This flow is authoritative.

All future runtime systems must conform to this topology.

---

# 2. Canonical Runtime Flow

LIVE MARKET DATA
    ↓
MARKET NORMALIZATION
    ↓
RUNTIME ROUTING
    ↓
AUTONOMOUS RUNTIME
    ↓
RISK EVALUATION
    ↓
EXECUTION APPROVAL
    ↓
PAPER EXECUTION
    ↓
PORTFOLIO UPDATE
    ↓
RUNTIME GOVERNANCE
    ↓
OBSERVABILITY
    ↓
PERSISTENCE

---

# 2.1 Validated Live Runtime Execution Path

Validated execution topology:

BINANCE WEBSOCKET
    ↓
BinanceWebSocketClient
    ↓
MarketTick
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
Runtime Observability

Validated components:
- live websocket ingestion
- reconnect handling
- autonomous execution
- paper trading lifecycle
- portfolio synchronization
- unrealized pnl tracking
- runtime observability

---

# 3. Runtime Authority Hierarchy

## Highest Authority

Risk systems possess override authority over:
- strategy systems
- execution systems
- orchestration systems

Risk authority may:
- reject trades
- trigger cooldowns
- trigger emergency stops
- disable execution globally

---

## Runtime Governance Authority

Governed runtime controls:
- lifecycle state
- execution permissions
- cooldown state
- emergency state
- recovery state
- live runtime coordination

Runtime governance may:
- pause runtime
- stop runtime
- disable trading
- enter safe mode

---

## Strategy Authority

Strategy systems may:
- generate recommendations
- generate execution proposals
- provide regime classifications

Strategy systems may NOT:
- execute orders directly
- bypass risk
- mutate runtime state

---

## Execution Authority

Execution systems may:
- simulate fills
- route approved orders
- apply spread/slippage models
- update portfolio state

Execution systems may NOT:
- override governance state
- bypass risk approval

---

# 4. Canonical Event Flow

LIVE_MARKET_TICK
    ↓
MARKET_STATE_UPDATE
    ↓
RUNTIME_EVALUATION
    ↓
RISK_CHECK
    ↓
EXECUTION_APPROVED
    ↓
ORDER_EXECUTED
    ↓
POSITION_UPDATED
    ↓
PNL_UPDATED
    ↓
RUNTIME_UPDATED

---

# 5. Runtime Loop Ownership

Canonical runtime loop:

runtime/runtime_loop.py

Responsibilities:
- polling
- event propagation
- orchestration coordination
- heartbeat management

---

# 5.1 Live Runtime Ownership

Canonical live runtime coordinator:

runtime/live_tick_handler.py

Responsibilities:
- live tick processing
- autonomous runtime invocation
- execution gating
- pnl monitoring
- position lifecycle management

---

# 6. Persistence Flow

## Runtime State

Stored after:
- lifecycle changes
- cooldown transitions
- emergency transitions

Pattern:
- overwrite latest authoritative state

---

## Metrics

Stored after:
- execution events
- pnl transitions
- runtime cycles

Pattern:
- append-only

---

## Event Journal

Stored after:
- critical runtime events
- execution transitions
- emergency triggers

Pattern:
- immutable append-only

---

# 7. Execution Safety Rules

No execution allowed if:
- emergency stop active
- cooldown active
- runtime paused
- risk gate rejected
- portfolio reconciliation failed

Execution approval requires:
- runtime approval
- risk approval
- execution integrity validation

---

# 8. Runtime Lifecycle Status

Validated:
- live market ingestion
- autonomous BUY execution
- portfolio persistence
- unrealized pnl evaluation
- duplicate execution prevention

Current limitations:
- no advanced signal engine
- no candle aggregation
- no stop-loss lifecycle
- no multi-symbol execution

---

# 9. Current Strategic Goal

Target runtime properties:

deterministic
recoverable
risk-governed
event-driven
observable
modular
execution-safe
live-data autonomous paper trading