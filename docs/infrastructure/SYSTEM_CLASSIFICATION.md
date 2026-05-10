# System Classification

# 1. Runtime Systems

| Module | Classification |
|---|---|
| runtime/governed_runtime.py | CANONICAL |
| runtime/runtime_loop.py | CANONICAL |
| runtime/runtime_state.py | CANONICAL |
| runtime/runtime_enums.py | CANONICAL |
| runtime/live_tick_handler.py | CANONICAL |
| runtime/runtime_snapshot.py | CANONICAL |
| runtime/runtime_console_renderer.py | CANONICAL |
| runtime/runtime_recovery.py | SUPPORTING |
| runtime/logger.py | SUPPORTING |
| runtime/event_journal.py | SUPPORTING |
| runtime/metrics.py | SUPPORTING |
| runtime/async_runtime_loop.py | EXPERIMENTAL |
| runtime/cognitive_runtime.py | EXPERIMENTAL |
| runtime/financial_runtime.py | EXPERIMENTAL |

Validated runtime capabilities:
- runtime snapshot generation
- runtime console rendering
- active trade lifecycle visibility
- completed trade lifecycle visibility
- exposure governance
- runtime halting
- candle-close execution orchestration

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

Validated orchestration capabilities:
- governance-aware execution routing
- portfolio synchronization orchestration
- runtime risk integration
- execution decision coordination
- candle-close autonomous execution

---

# 3. Event Systems

| Module | Classification |
|---|---|
| runtime/event_bus.py | CANONICAL |
| runtime/async_event_bus.py | CANONICAL |
| market_data/market_data_router.py | CANONICAL |
| market_data/market_tick.py | CANONICAL |
| market/timeframe_aggregator.py | CANONICAL |
| events/event.py | DEPRECATED CANDIDATE |
| events/event_dispatcher.py | DEPRECATED CANDIDATE |

Validated event capabilities:
- websocket tick propagation
- candle aggregation propagation
- runtime telemetry propagation
- autonomous runtime invocation
- execution lifecycle propagation

---

# 4. Market Infrastructure

| Module | Classification |
|---|---|
| exchange/binance_websocket_client.py | CANONICAL |
| market/market_data.py | CANONICAL |
| market/timeframe_aggregator.py | CANONICAL |
| market/candle_aggregator.py | SUPPORTING |
| market/streaming_runtime.py | SUPPORTING |
| market/candle_feed_engine.py | SUPPORTING |

Validated market capabilities:
- Binance websocket ingestion
- reconnect-safe websocket lifecycle
- MarketTick normalization
- timeframe candle aggregation
- candle-close execution triggering

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
| exchange/portfolio_risk.py | CANONICAL |
| risk/risk_sync.py | SUPPORTING |
| risk/capital_governance.py | SUPPORTING |
| risk/risk_budgeting.py | EXPERIMENTAL |

Validated risk capabilities:
- exposure-based execution blocking
- runtime halting
- execution permission gating
- portfolio exposure evaluation
- governance-aware execution approval

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

Validated strategy constraints:
- strategy systems remain non-authoritative
- strategy systems cannot bypass governance
- strategy systems cannot directly execute trades

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

Validated execution capabilities:
- active trade lifecycle tracking
- completed trade journaling
- mark-to-market accounting
- unrealized pnl propagation
- holdings valuation
- portfolio valuation
- execution observability

---

# 8. Persistence Systems

| Module | Classification |
|---|---|
| persistence/runtime_store.py | PLANNED |
| persistence/metrics_store.py | PLANNED |
| persistence/event_store.py | PLANNED |
| persistence/runtime_loader.py | PLANNED |
| persistence/runtime_snapshot.py | PLANNED |

Current persistence status:
- not implemented
- runtime currently fully in-memory
- shutdown clears runtime telemetry
- shutdown clears completed trade history

Planned persistence capabilities:
- runtime snapshot persistence
- completed trade persistence
- structured execution journaling
- replay-safe event persistence

---

# 9. Runtime Status

## Validated Runtime Capabilities

- live Binance websocket ingestion
- reconnect-safe websocket lifecycle
- timeframe candle aggregation
- candle-close autonomous execution
- runtime orchestration
- portfolio synchronization
- portfolio valuation
- unrealized pnl tracking
- active trade lifecycle tracking
- completed trade journaling
- runtime snapshot generation
- runtime console rendering
- exposure governance
- runtime halting
- governance-aware execution approval
- duplicate execution prevention

## Current Runtime Limitations

- no persistence layer
- no FastAPI telemetry API
- no dashboard frontend
- no replay engine
- no stop-loss lifecycle
- no advanced exit lifecycle
- no multi-symbol orchestration
- no historical analytics

## Current Runtime Classification

runtime-stabilized
governance-controlled
observable
live-data autonomous paper trading runtime

---

# 10. Governance Freeze Policy

Until stabilization completes:

DO NOT:
- create new runtime abstractions
- create new orchestration layers
- create distributed runtimes
- create autonomous execution bypasses
- fragment observability ownership
- bypass governance authority

Allowed:
- stabilization
- observability
- lifecycle refinement
- validation
- execution integrity
- runtime simplification
- persistence infrastructure
- telemetry infrastructure
- dashboard preparation

---

# 11. Current Strategic Priority

Current priority is:

runtime stabilization
observability
execution lifecycle visibility
paper trading infrastructure completion

NOT:
- ML sophistication
- governance proliferation
- distributed execution
- aggressive feature expansion
- profitability optimization