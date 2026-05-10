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

---

# 2. Canonical Runtime Execution Flow

LIVE BINANCE TRADE
    ↓
exchange/binance_websocket_client.py
    ↓
MarketTick Normalization
    ↓
market_data/market_data_router.py
    ↓
runtime/live_tick_handler.py
    ↓
core/autonomous_runtime.py
    ↓
Risk Evaluation
    ↓
Execution Validation
    ↓
exchange/paper_exchange.py
    ↓
Portfolio Synchronization
    ↓
Runtime Governance
    ↓
Observability
    ↓
Persistence

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
- runtime orchestration authority

---

## Canonical Live Runtime Handler

Primary runtime execution coordinator:

runtime/live_tick_handler.py

Responsibilities:
- live tick processing
- runtime orchestration
- portfolio lifecycle coordination
- execution gating
- pnl evaluation

---

# 4. Canonical Event Authority

Canonical event transport systems:

runtime/event_bus.py
runtime/async_event_bus.py

Canonical market routing:

market_data/market_data_router.py

Architectural principle:

all external exchange payloads MUST be normalized before runtime propagation.

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
- exchange/execution_engine.py
- exchange/paper_exchange.py
- exchange/execution_simulator.py

Execution systems:
- may not bypass governance
- may not mutate runtime lifecycle
- may not authorize execution independently

---

# 7. Live Runtime Validation Status

Validated:
- websocket lifecycle
- reconnect handling
- live tick routing
- autonomous paper execution
- portfolio synchronization
- unrealized pnl tracking
- execution gating

Current limitations:
- no candle aggregation
- no stop-loss lifecycle
- no dynamic signal engine
- no multi-symbol orchestration

---

# 8. Experimental Isolation

The following systems are NOT on the production runtime path:

## Experimental Strategy Systems

- adaptive_ensemble.py
- meta_learning.py
- online_learning.py

## Experimental Governance Systems

- meta_governance.py
- evolution.py
- hierarchy.py

Experimental systems:
- may observe runtime
- may generate analytics
- may simulate decisions

Experimental systems may NOT:
- execute trades
- bypass governance
- mutate canonical runtime state

---

# 9. Production Runtime Principles

Production runtime must remain:

deterministic
recoverable
observable
risk-governed
modular
execution-safe
live-data normalized

Complexity must justify measurable operational benefit.

---

# 10. Current Strategic Objective

Current objective is:

stable live autonomous paper trading infrastructure

NOT:
- unrestricted autonomous execution
- advanced ML orchestration
- distributed governance
- high-frequency execution