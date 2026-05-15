

# Purpose

This document defines the canonical ownership model of the repository.

Goals:

- eliminate architectural ambiguity
- prevent duplicate subsystem creation
- define authoritative runtime paths
- classify legacy and experimental systems
- enforce future consolidation discipline

This document is the primary architectural stabilization reference.

---

# Architectural Principles

## 1. Same Name ≠ Duplication

Many similarly named modules exist intentionally across layers.

Examples:

- runtime/runtime_snapshot.py
- persistence/runtime_snapshot.py

These are different responsibilities, not duplicates.

---

## 2. Runtime Layering Model

The repository follows layered runtime architecture:

```text
core/
    foundational contracts + primitives

runtime/
    live operational orchestration

strategy/
    strategy intelligence + orchestration

exchange/
    execution implementation

execution/
    execution abstractions/contracts

persistence/
    durable state management
````

---

## 3. Cleanup Rules

Code may only be removed if:

* no runtime imports exist
* no persistence dependency exists
* no serialization dependency exists
* runtime boot passes
* validation tests pass

Mandatory process:

```text
audit
→ classify
→ migrate
→ validate
→ remove
→ validate again
```

---

# DOMAIN AUTHORITY MATRIX

| Domain                       | Canonical                       | Supporting                         | Legacy                                | Experimental          |
| ---------------------------- | ------------------------------- | ---------------------------------- | ------------------------------------- | --------------------- |
| Runtime lifecycle            | runtime/*                       | core/runtime_transition_engine.py  | -                                     | cognitive_runtime.py  |
| Runtime contracts            | core/runtime.py                 | core/runtime_state_machine.py      | -                                     | integrated_runtime.py |
| Runtime governance           | runtime/governed_runtime.py     | runtime/runtime_controller.py      | -                                     | financial_runtime.py  |
| Event transport              | runtime/event_bus.py            | core/event_bus.py                  | events/runtime_event_bus.py (removed) | async_event_bus.py    |
| Event models                 | events/runtime_events.py        | core/events.py                     | -                                     | -                     |
| Market ingestion             | market_data/*                   | market/*                           | -                                     | -                     |
| Execution implementation     | exchange/*                      | paper_execution/*                  | -                                     | -                     |
| Execution abstractions       | execution/*                     | -                                  | -                                     | -                     |
| Strategy orchestration       | strategy/*                      | core/autonomous_runtime.py         | strategies/* (removed)                | -                     |
| Runtime persistence          | persistence/*                   | db/*                               | -                                     | -                     |
| Runtime operational snapshot | runtime/runtime_snapshot.py     | runtime/runtime_registry.py        | -                                     | -                     |
| Runtime durable snapshot     | persistence/runtime_snapshot.py | persistence/runtime_loader.py      | -                                     | -                     |
| Runtime logging              | logging/runtime_logger.py       | runtime/logging/runtime_loggers.py | runtime/logger.py (removed)           | logging/logger.py     |
| Monitoring                   | monitoring/*                    | runtime/runtime_monitor.py         | -                                     | -                     |

---

# Canonical Runtime Path

```text
exchange/binance_websocket_client.py
    ↓
market_data/market_data_router.py
    ↓
runtime/live_tick_handler.py
    ↓
core/autonomous_runtime.py
    ↓
exchange/paper_exchange.py
    ↓
portfolio synchronization
    ↓
runtime observability
```

---

# Canonical Event Topology

```text
core/event_bus.py
    ↓
runtime/event_bus.py
    ↓
governed_runtime.py
    ↓
live_tick_handler.py
    ↓
autonomous_runtime.py
```

---

# Runtime Snapshot Topology

## Operational Snapshot

```text
runtime/runtime_snapshot.py
```

Responsibilities:

* live telemetry
* runtime dashboard state
* active trade projection
* unrealized pnl calculations
* frontend operational state

---

## Durable Snapshot

```text
persistence/runtime_snapshot.py
```

Responsibilities:

* atomic snapshot persistence
* recovery state durability
* runtime restoration
* corruption-safe persistence

---

# Removed During Stabilization

| Removed Module                  | Reason                           |
| ------------------------------- | -------------------------------- |
| src/strategies/                 | abandoned legacy strategy layer  |
| src/events/runtime_event_bus.py | deprecated compatibility wrapper |
| src/runtime/runtime_events.py   | deprecated transition wrapper    |
| src/utils/logger.py             | dead unused abstraction          |
| src/runtime/logger.py           | abandoned runtime logger         |

---

# Experimental Systems

These systems are NOT authoritative runtime paths.

| Module                       | Status                       |
| ---------------------------- | ---------------------------- |
| core/integrated_runtime.py   | experimental                 |
| runtime/cognitive_runtime.py | experimental                 |
| runtime/financial_runtime.py | experimental                 |
| logging/logger.py            | structured logging prototype |

---

# Dependency Direction Rules

Allowed:

```text
runtime → core
runtime → persistence
runtime → exchange
strategy → core
exchange → core
exchange → persistence
```

Avoid:

```text
core → runtime
core → frontend
persistence → runtime orchestration
exchange → runtime governance
```

---

# Future Stabilization Priorities

## High Priority

* dependency boundary enforcement
* runtime interface normalization
* structured observability standardization
* runtime metrics consolidation

---

## Medium Priority

* experimental runtime isolation
* strategy orchestration cleanup
* monitoring standardization

---

## Low Priority

* structured logging migration
* async runtime convergence
* telemetry optimization

---

# Engineering Rule

No subsystem may introduce:

* parallel runtime authority
* duplicate orchestration layer
* duplicate persistence engine
* duplicate event transport
* duplicate logger system

without explicit authority matrix update.

````
