# Grid Trading Bot V3 — API Contract Documentation

## Overview

This document defines the authoritative API contract for the Grid Trading Bot V3 backend.

The API layer is designed around strict operational semantics:

* Runtime lifecycle
* Trading session lifecycle
* Governance control
* Recovery workflows
* Derived telemetry consistency
* Operational safety

This document acts as the single source of truth for:

* Frontend integration
* Backend API semantics
* Monitoring systems
* Testing infrastructure
* Future websocket migration

---

# Base URL

```text
http://localhost:8000/api/v1
```

---

# Runtime Lifecycle Model

## Runtime States

| State          | Description                                     |
| -------------- | ----------------------------------------------- |
| STARTING       | Runtime boot sequence in progress               |
| RUNNING        | Runtime operational and processing market data  |
| PAUSED         | Runtime paused intentionally                    |
| SAFE_MODE      | Runtime restricted due to governance/risk event |
| EMERGENCY_STOP | Runtime halted due to critical failure          |
| SHUTDOWN       | Runtime terminated                              |

---

# Runtime Lifecycle Semantics

## Important Architectural Rule

```text
Runtime lifecycle != Trading session lifecycle
```

The runtime may be operational without an active trading session.

Examples:

| Runtime        | Session  |
| -------------- | -------- |
| RUNNING        | inactive |
| RUNNING        | active   |
| PAUSED         | inactive |
| EMERGENCY_STOP | blocked  |

---

# Governance Model

## Governance Authority

Governance controls whether trading activity is permitted.

Primary governance field:

```json
{
  "is_trading_enabled": true
}
```

---

# Governance Endpoints

| Endpoint                      | Purpose                      |
| ----------------------------- | ---------------------------- |
| POST /runtime/enable-trading  | Enable trading permissions   |
| POST /runtime/disable-trading | Disable trading permissions  |
| POST /runtime/emergency-stop  | Trigger emergency stop       |
| POST /runtime/recover         | Recover from emergency state |

---

# Governance Rules

## Trading Disabled

When:

```json
{
  "is_trading_enabled": false
}
```

The system:

* blocks session creation
* blocks trading execution
* preserves runtime operation

Example error:

```json
{
  "detail": "Cannot start session: trading is disabled by governance"
}
```

---

# Session Lifecycle Model

## Session Definition

A trading session represents an active trading lifecycle.

Runtime operation does NOT imply an active session.

---

# Session Lifecycle Invariants

## Inactive Session Invariant

When no active session exists:

```json
{
  "session_active": false,
  "active_session_id": null,
  "session_started_at": null,
  "total_trades": 0
}
```

These are mandatory lifecycle invariants.

---

# Runtime API

# GET /api/v1/runtime

## Description

Returns authoritative runtime operational telemetry.

## Response Example

```json
{
  "connected": true,
  "status": "running",
  "mode": "dry_run",
  "is_trading_enabled": true,
  "safe_mode": false,
  "latest_price": 0.0,
  "latest_candle_close": 0.0,
  "total_trades": 0,
  "winning_trades": 0,
  "losing_trades": 0,
  "websocket_connected": true,
  "reconnect_attempts": 0,
  "last_heartbeat": "2026-05-14T03:57:44.250452",
  "last_tick_received_at": null,
  "cooldown_until": null,
  "emergency_reason": null,
  "session_pnl": 0.0,
  "session_drawdown": 0.0,
  "active_positions": 1,
  "active_orders": 0,
  "runtime_uptime_seconds": 17,
  "started_at": "2026-05-14T03:57:44.246244",
  "active_session_id": null,
  "current_unrealized_pnl": 0.0,
  "current_unrealized_pnl_percent": 0.0,
  "last_execution_price": 0.0,
  "portfolio": {
    "available_capital": 995.99,
    "invested_capital": 0.0,
    "total_portfolio_value": 995.99
  },
  "active_trades": []
}
```

---

# Runtime Field Semantics

| Field                  | Type             | Authority     | Description                        |
| ---------------------- | ---------------- | ------------- | ---------------------------------- |
| status                 | string           | authoritative | Runtime lifecycle state            |
| is_trading_enabled     | authoritative    | governance    | Trading permission state           |
| runtime_uptime_seconds | derived          | derived       | Calculated from started_at         |
| active_positions       | derived          | derived       | Calculated from exchange positions |
| total_trades           | lifecycle-scoped | session       | Session trade count                |
| active_session_id      | authoritative    | session       | Active session identifier          |
| websocket_connected    | authoritative    | transport     | Websocket connectivity state       |
| reconnect_attempts     | authoritative    | transport     | Current reconnect counter          |
| emergency_reason       | authoritative    | governance    | Emergency stop reason              |

---

# Session API

# GET /api/v1/session/status

## Description

Returns current trading session lifecycle state.

## Response Example (Inactive)

```json
{
  "session_active": false,
  "active_session_id": null,
  "session_started_at": null,
  "session_duration_seconds": 0,
  "session_pnl": 0.0,
  "total_trades": 0,
  "status": "inactive"
}
```

## Response Example (Active)

```json
{
  "session_active": true,
  "active_session_id": 5,
  "session_started_at": "2026-05-14T03:58:08.283473",
  "session_duration_seconds": 7,
  "session_pnl": 0.0,
  "total_trades": 5,
  "status": "active"
}
```

---

# Session Endpoints

| Endpoint            | Description               |
| ------------------- | ------------------------- |
| POST /session/start | Start trading session     |
| POST /session/stop  | Stop trading session      |
| GET /session/status | Get current session state |

---

# Session Start Requirements

A session may only start when:

* runtime status is RUNNING
* trading is enabled
* runtime not in emergency stop
* no active session exists
* safe mode inactive

---

# Recovery Workflow

# GET /api/v1/runtime/recovery-status

## Description

Returns whether runtime recovery is currently permitted.

## Example Response

```json
{
  "recovery_allowed": true,
  "reason": "Recovery flow available after emergency stop",
  "emergency_reason": "heartbeat_failure",
  "status": "emergency_stop"
}
```

---

# POST /api/v1/runtime/recover

## Description

Recovers runtime from emergency stop.

Recovery transitions runtime into:

```text
PAUSED
```

Trading remains disabled until governance explicitly re-enables trading.

## Example Response

```json
{
  "success": true,
  "status": "paused",
  "message": "Recovery complete — runtime paused"
}
```

---

# Runtime Control Endpoints

| Endpoint                     | Description            |
| ---------------------------- | ---------------------- |
| POST /runtime/start          | Start runtime          |
| POST /runtime/stop           | Stop runtime           |
| POST /runtime/pause          | Pause runtime          |
| POST /runtime/resume         | Resume runtime         |
| POST /runtime/shutdown       | Shutdown runtime       |
| POST /runtime/emergency-stop | Trigger emergency stop |
| POST /runtime/recover        | Recover runtime        |

---

# Derived vs Authoritative Fields

## Derived Fields

These values are calculated dynamically.

| Field                    | Source                                 |
| ------------------------ | -------------------------------------- |
| runtime_uptime_seconds   | datetime.utcnow() - started_at         |
| active_positions         | exchange.positions                     |
| invested_capital         | calculated from active positions       |
| total_portfolio_value    | available + invested capital           |
| session_duration_seconds | datetime.utcnow() - session_started_at |

Derived fields should NEVER be persisted as authoritative state.

---

## Authoritative Fields

These values represent operational truth.

| Field               | Domain            |
| ------------------- | ----------------- |
| status              | runtime lifecycle |
| active_session_id   | session lifecycle |
| session_started_at  | session lifecycle |
| is_trading_enabled  | governance        |
| emergency_reason    | governance        |
| websocket_connected | transport         |

---

# Failure Semantics

## HTTP 409 Conflict

Used for invalid operational transitions.

Examples:

```json
{
  "detail": "Cannot start session: runtime is emergency_stop"
}
```

```json
{
  "detail": "Cannot start session: trading is disabled by governance"
}
```

```json
{
  "detail": "No active session to stop"
}
```

---

# Frontend Polling Recommendations

| Endpoint               | Recommended Poll Interval |
| ---------------------- | ------------------------- |
| GET /runtime           | 2-5 seconds               |
| GET /session/status    | 2-5 seconds               |
| GET /analytics/summary | 15-30 seconds             |
| GET /sessions          | On-demand                 |

---

# Operational Design Principles

## Key Architectural Principles

### Runtime != Session

Infrastructure lifecycle is separated from trading lifecycle.

---

### Governance != Runtime

Trading permissions are governed independently from runtime operation.

---

### Derived != Authoritative State

Derived telemetry should not be persisted.

---

### Recovery != Trading Approval

Recovering runtime operation does not automatically re-enable trading.

---

# Future Improvements

## Planned Enhancements

* Pydantic response models
* Websocket event streaming
* Typed API schemas
* OpenAPI lifecycle annotations
* Event authority unification
* Real-time frontend synchronization
* Operational observability dashboards

---

# Current Backend Validation Status

## Test Suite

```text
89 passed
2 skipped
0 failures
```

## Validated Domains

* Runtime lifecycle
* Session lifecycle
* Governance controls
* Recovery flows
* Persistence fallback
* API telemetry consistency
* Runtime resilience
* Emergency stop handling

---

# End of Document
