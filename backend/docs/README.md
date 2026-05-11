# Grid Trading Bot V3

> **Validated · Observable · Governance-Controlled**
> Autonomous paper trading infrastructure built for runtime integrity, not speculation.

---

## What This Is

Grid Trading Bot V3 is an **event-driven autonomous paper trading runtime** built on live Binance WebSocket data. It is designed for correctness, observability, and architectural rigor — not for profitability optimization or high-frequency execution.

The runtime is currently classified as:

```
validated · observable · governance-controlled · autonomous paper trading infrastructure
```

---

## Core Design Philosophy

Execution authority is **always** downstream from:

1. **Governance** — exposure limits, runtime halting, permission gating
2. **Portfolio Risk** — mark-to-market valuation, invested capital evaluation
3. **Execution Validation** — approval-gated order routing

The system does not chase performance. It enforces discipline.

---

## Runtime Execution Flow

```
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
  MarketDataRouter
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
```

---

## Operational Capabilities

### Market Infrastructure
- Live Binance WebSocket connectivity with reconnect-safe lifecycle
- Real-time `MarketTick` ingestion and normalization
- Timeframe candle aggregation
- Candle-close autonomous execution orchestration

### Trading Infrastructure
- Paper exchange execution with spread, slippage, and fee simulation
- Portfolio synchronization and mark-to-market accounting
- Unrealized PnL tracking and holdings valuation
- Active trade lifecycle tracking
- Completed trade journaling

### Governance Infrastructure
- Exposure-based execution blocking and runtime halting
- Execution permission gating upstream from all order flow
- Governance-aware execution routing and approval

### Observability Infrastructure
- Runtime snapshot generation
- Console rendering with structured telemetry sections
- Full execution lifecycle visibility

---

## Runtime Console

The live console renders the following sections in real time:

| Section | Telemetry |
|---|---|
| **Runtime Status** | Operating state, governance state, exposure state |
| **Market Telemetry** | Latest tick price, latest candle close |
| **Portfolio Telemetry** | Available cash, invested capital, holdings value, total portfolio value |
| **Active Trades** | Symbol, quantity, entry price, current price, unrealized PnL, unrealized PnL %, live valuation, execution status |
| **Completed Trades** | Symbol, quantity, entry price, exit price, realized PnL, fees paid, opened/closed timestamps |

---

## Repository Structure

```
src/          # Runtime implementation
tests/        # Deterministic validation
scripts/      # Runtime demos and experimentation
docs/         # Architecture and operational documentation
```

### Documentation Map

**Architecture**

| Document | Purpose |
|---|---|
| `architecture/ARCHITECTURE.md` | Canonical runtime architecture |
| `architecture/EVENT_TOPOLOGY.md` | Runtime event propagation topology |
| `architecture/EVENT_UNIFICATION_PLAN.md` | Event consolidation and stabilization |

**Governance**

| Document | Purpose |
|---|---|
| `governance/AUTHORITY_MATRIX.md` | Canonical ownership and authority mapping |

**Infrastructure**

| Document | Purpose |
|---|---|
| `infrastructure/SYSTEM_CLASSIFICATION.md` | System classification and stabilization status |

---

## Validated Capabilities

- [x] WebSocket ingestion and reconnect-safe lifecycle
- [x] Candle aggregation and candle-close execution
- [x] Autonomous runtime orchestration
- [x] Portfolio synchronization and mark-to-market accounting
- [x] Runtime halting and governance-aware execution routing
- [x] Active and completed trade lifecycle visibility
- [x] Runtime snapshot propagation
- [x] Console observability rendering

---

## Current Limitations

The following are **not yet implemented**:

- [ ] Persistence layer
- [ ] FastAPI telemetry API
- [ ] Dashboard frontend
- [ ] Replay engine
- [ ] Stop-loss and advanced exit lifecycle
- [ ] Multi-symbol orchestration
- [ ] Historical analytics

---

## Roadmap

| Priority | Milestone |
|---|---|
| 1 | Runtime persistence layer |
| 2 | Structured execution journaling |
| 3 | FastAPI telemetry layer |
| 4 | Dashboard WebSocket streaming |
| 5 | Historical runtime replay |
| 6 | Multi-symbol orchestration |

---

## Out of Scope

This project is explicitly **not** focused on:

- Profitability optimization
- ML-based strategy sophistication
- High-frequency execution
- Distributed orchestration

---

## Architectural Principles

- **Centralized governance** — all execution routes through a single authority
- **Normalized market ingestion** — consistent tick and candle representation
- **Observable execution lifecycle** — every state transition is visible
- **Deterministic orchestration** — no hidden side effects
- **Replay-safe architectural preparation** — designed for future audit and replay
- **Portfolio-aware execution** — risk is evaluated before every order
- **Lifecycle-driven observability** — observability is structural, not bolted on