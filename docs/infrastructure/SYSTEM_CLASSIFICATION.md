# System Classification

# 1. Runtime Systems

| Module | Classification |
|---|---|
| runtime/governed_runtime.py | CANONICAL |
| runtime/runtime_loop.py | CANONICAL |
| runtime/runtime_state.py | CANONICAL |
| runtime/runtime_enums.py | CANONICAL |
| runtime/runtime_recovery.py | SUPPORTING |
| runtime/logger.py | SUPPORTING |
| runtime/event_journal.py | SUPPORTING |
| runtime/instrumentation.py | SUPPORTING |
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
| core/recovery_policy.py | SUPPORTING |
| core/recovery_workflow.py | SUPPORTING |
| core/recovery_coordinator.py | SUPPORTING |
| core/runtime_governance_loop.py | SUPPORTING |
| core/runtime_tick_engine.py | SUPPORTING |
| core/runtime_tick_actions.py | SUPPORTING |
| core/runtime.py | DEPRECATED CANDIDATE |
| core/autonomous_runtime.py | EXPERIMENTAL |
| core/strategy_runtime.py | DEPRECATED CANDIDATE |
| core/integrated_runtime.py | SUPPORTING |

---

# 3. Event Systems

| Module | Classification |
|---|---|
| core/events.py | CANONICAL |
| core/event_bus.py | CANONICAL |
| runtime/event_bus.py | DEPRECATED CANDIDATE |
| runtime/async_event_bus.py | EXPERIMENTAL |
| events/event.py | DEPRECATED CANDIDATE |
| events/event_dispatcher.py | DEPRECATED CANDIDATE |
| events/event_factory.py | SUPPORTING |

---

# 4. Risk Systems

| Module | Classification |
|---|---|
| risk/kill_switch.py | CANONICAL |
| risk/session_risk.py | CANONICAL |
| risk/cooldown.py | CANONICAL |
| risk/exposure.py | CANONICAL |
| risk/dynamic_position_sizer.py | CANONICAL |
| risk/grid_protection.py | CANONICAL |
| risk/recovery.py | SUPPORTING |
| risk/risk_sync.py | SUPPORTING |
| risk/capital_governance.py | SUPPORTING |
| risk/risk_budgeting.py | EXPERIMENTAL |

---

# 5. Strategy Systems

| Module | Classification |
|---|---|
| strategy/regime.py | CANONICAL |
| strategy/spacing.py | CANONICAL |
| strategy/asymmetric_grid.py | CANONICAL |
| strategy/grid_anchor.py | CANONICAL |
| strategy/orchestrator.py | CANONICAL |
| strategy/performance_tracker.py | SUPPORTING |
| strategy/strategy_registry.py | SUPPORTING |
| strategy/ensemble.py | EXPERIMENTAL |
| strategy/meta_learning.py | EXPERIMENTAL |
| strategy/adaptive_ensemble.py | EXPERIMENTAL |
| strategy/online_learning.py | EXPERIMENTAL |
| strategy/regime_router.py | EXPERIMENTAL |
| strategy/adaptive_orchestrator.py | EXPERIMENTAL |

---

# 6. Execution Systems

| Module | Classification |
|---|---|
| exchange/execution_engine.py | CANONICAL |
| exchange/paper_exchange.py | CANONICAL |
| exchange/execution_simulator.py | CANONICAL |
| exchange/fees.py | CANONICAL |
| exchange/slippage.py | CANONICAL |
| exchange/spread.py | CANONICAL |
| exchange/portfolio.py | SUPPORTING |
| exchange/portfolio_sync.py | SUPPORTING |
| exchange/portfolio_risk.py | SUPPORTING |

---

# 7. Persistence Systems

| Module | Classification |
|---|---|
| persistence/runtime_store.py | CANONICAL |
| persistence/metrics_store.py | CANONICAL |
| persistence/event_store.py | CANONICAL |
| persistence/runtime_loader.py | SUPPORTING |
| persistence/runtime_snapshot.py | SUPPORTING |

---

# 8. Analytics Systems

| Module | Classification |
|---|---|
| analytics/performance.py | SUPPORTING |
| analytics/montecarlo.py | EXPERIMENTAL |
| analytics/risk_of_ruin.py | SUPPORTING |

---

# 9. Governance Freeze Policy

Until consolidation stabilizes:

DO NOT:
- create new runtime abstractions
- create new event systems
- create new orchestration layers
- create new governance frameworks

Allowed:
- consolidation
- simplification
- validation
- observability
- deterministic recovery
- execution integrity

---

# 10. Current Strategic Priority

Current priority is:

architecture stabilization

NOT:
- feature expansion
- autonomous complexity
- ML sophistication
- governance proliferation