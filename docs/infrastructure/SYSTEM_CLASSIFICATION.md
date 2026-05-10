# System Classification

# 1. Runtime Systems

| Module | Classification |
|---|---|
| runtime/governed_runtime.py | CANONICAL |
| runtime/runtime_loop.py | CANONICAL |
| runtime/runtime_state.py | CANONICAL |
| runtime/runtime_enums.py | CANONICAL |
| runtime/live_tick_handler.py | CANONICAL |
| runtime/runtime_recovery.py | SUPPORTING |
| runtime/logger.py | SUPPORTING |
| runtime/event_journal.py | SUPPORTING |
| runtime/metrics.py | SUPPORTING |
| runtime/async_runtime_loop.py | EXPERIMENTAL |
| runtime/cognitive_runtime.py | EXPERIMENTAL |
| runtime/financial_runtime.py | EXPERIMENTAL |

---

# 2. Core Runtime Systems

| Module | Classification |
|---|---|
| core/runtime_state_machine.py | CANONICAL |
| core/runtime_transition_engine.py | CANONICAL |
| core/runtime_transition_rules.py | CANONICAL |
| core/runtime_integrity.py | CANONICAL |
| core/autonomous_runtime.py | SUPPORTING |
| core/integrated_runtime.py | SUPPORTING |
| core/runtime.py | DEPRECATED CANDIDATE |
| core/strategy_runtime.py | DEPRECATED CANDIDATE |

---

# 3. Event Systems

| Module | Classification |
|---|---|
| runtime/event_bus.py | CANONICAL |
| runtime/async_event_bus.py | CANONICAL |
| market_data/market_data_router.py | CANONICAL |
| market_data/market_tick.py | CANONICAL |
| events/event.py | DEPRECATED CANDIDATE |
| events/event_dispatcher.py | DEPRECATED CANDIDATE |

---

# 4. Market Infrastructure

| Module | Classification |
|---|---|
| exchange/binance_websocket_client.py | CANONICAL |
| market/market_data.py | CANONICAL |
| market/streaming_runtime.py | SUPPORTING |
| market/candle_feed_engine.py | SUPPORTING |

---

# 5. Risk Systems

| Module | Classification |
|---|---|
| risk/kill_switch.py | CANONICAL |
| risk/session_risk.py | CANONICAL |
| risk/cooldown.py | CANONICAL |
| risk/exposure.py | CANONICAL |
| risk/dynamic_position_sizer.py | CANONICAL |
| risk/grid_protection.py | CANONICAL |
| risk/risk_sync.py | SUPPORTING |
| risk/capital_governance.py | SUPPORTING |
| risk/risk_budgeting.py | EXPERIMENTAL |

---

# 6. Strategy Systems

| Module | Classification |
|---|---|
| strategy/regime.py | CANONICAL |
| strategy/spacing.py | CANONICAL |
| strategy/asymmetric_grid.py | CANONICAL |
| strategy/orchestrator.py | CANONICAL |
| strategy/performance_tracker.py | SUPPORTING |
| strategy/ensemble.py | EXPERIMENTAL |
| strategy/meta_learning.py | EXPERIMENTAL |
| strategy/adaptive_ensemble.py | EXPERIMENTAL |

---

# 7. Execution Systems

| Module | Classification |
|---|---|
| exchange/execution_engine.py | CANONICAL |
| exchange/paper_exchange.py | CANONICAL |
| exchange/execution_simulator.py | CANONICAL |
| exchange/fees.py | CANONICAL |
| exchange/slippage.py | CANONICAL |
| exchange/spread.py | CANONICAL |
| exchange/portfolio_sync.py | SUPPORTING |
| exchange/portfolio_risk.py | SUPPORTING |

---

# 8. Persistence Systems

| Module | Classification |
|---|---|
| persistence/runtime_store.py | CANONICAL |
| persistence/metrics_store.py | CANONICAL |
| persistence/event_store.py | CANONICAL |
| persistence/runtime_loader.py | SUPPORTING |
| persistence/runtime_snapshot.py | SUPPORTING |

---

# 9. Runtime Status

## Validated Runtime Capabilities

- live Binance websocket ingestion
- autonomous paper execution
- runtime orchestration
- portfolio synchronization
- live pnl tracking
- duplicate execution prevention
- websocket reconnect handling

## Current Runtime Limitations

- no candle aggregation
- no advanced signal engine
- no stop-loss lifecycle
- no multi-symbol orchestration
- no telemetry persistence

---

# 10. Governance Freeze Policy

Until stabilization completes:

DO NOT:
- create new runtime abstractions
- create new orchestration layers
- create distributed runtimes
- create autonomous execution bypasses

Allowed:
- stabilization
- observability
- lifecycle refinement
- validation
- execution integrity
- runtime simplification

---

# 11. Current Strategic Priority

Current priority is:

live autonomous paper trading stabilization

NOT:
- ML sophistication
- governance proliferation
- distributed execution
- aggressive feature expansion