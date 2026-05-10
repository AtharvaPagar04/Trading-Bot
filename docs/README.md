# Grid Trading Bot V3 Documentation

## Overview

This repository contains a modular event-driven autonomous trading infrastructure focused on:

- runtime governance
- live Binance websocket ingestion
- autonomous paper execution
- execution orchestration
- portfolio synchronization
- risk-aware execution
- observability and validation
- runtime lifecycle management

---

# Current Runtime Status

## Operational Capabilities

The system now supports:

- live Binance websocket connectivity
- real-time market tick ingestion
- autonomous runtime orchestration
- paper trading execution
- portfolio accounting
- unrealized pnl monitoring
- execution guardrails
- runtime governance integration
- websocket reconnect handling

---

# Runtime Execution Flow

LIVE BINANCE TRADE
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
PaperExchange
↓
Portfolio Synchronization
↓
Runtime Observability

---

# Documentation Structure

## Architecture

| Document | Purpose |
|---|---|
| architecture/ARCHITECTURE.md | Core system architecture |
| architecture/EVENT_TOPOLOGY.md | Runtime event propagation topology |
| architecture/EVENT_UNIFICATION_PLAN.md | Event model consolidation plan |

---

## Governance

| Document | Purpose |
|---|---|
| governance/AUTHORITY_MATRIX.md | Runtime authority and ownership mapping |

---

## Infrastructure

| Document | Purpose |
|---|---|
| infrastructure/SYSTEM_CLASSIFICATION.md | System component classification |

---

# Validated Infrastructure

## Runtime Infrastructure

- governed runtime lifecycle
- runtime orchestration
- async runtime propagation
- websocket lifecycle handling
- runtime observability

## Trading Infrastructure

- paper exchange execution
- spread simulation
- slippage simulation
- fee modeling
- position synchronization
- pnl tracking

## Validation Infrastructure

- deterministic runtime validation
- websocket validation
- execution lifecycle validation
- strategy runtime validation
- runtime persistence validation

Current validation count:

95+ passing tests

---

# Repository Structure

```text
src/        -> implementation
tests/      -> deterministic validation
scripts/    -> runtime demos and experiments
docs/       -> architecture and operational documentation