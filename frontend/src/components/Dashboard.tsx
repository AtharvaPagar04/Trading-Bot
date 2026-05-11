"use client";

import { MetricCard } from "./MetricCard";
import { TradesTable } from "./TradesTable";
import type { ActiveTrade, CompletedTrade } from "@/types";
import { useEffect, useState, useRef } from "react";
import { fetchRuntime } from "../../services/api";

// ── helpers ──────────────────────────────────────────────────────────────────

function usd(n: number) {
  return n.toLocaleString("en-US", { style: "currency", currency: "USD" });
}

function pct(n: number) {
  return `${n >= 0 ? "+" : ""}${n.toFixed(2)}%`;
}

function pnlColor(n: number): "green" | "red" | "default" {
  return n > 0 ? "green" : n < 0 ? "red" : "default";
}

// ── section label ─────────────────────────────────────────────────────────────

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section style={{ marginBottom: 32 }}>
      <div style={{
        fontSize: 10,
        textTransform: "uppercase",
        letterSpacing: "0.1em",
        color: "#334155",
        borderBottom: "1px solid #1e293b",
        paddingBottom: 6,
        marginBottom: 12,
      }}>
        {title}
      </div>
      {children}
    </section>
  );
}

// ── status dot ───────────────────────────────────────────────────────────────

function StateDot({ state }: { state: string }) {
  const color =
    state === "RUNNING" ? "#22c55e"
      : state === "PAUSED" ? "#f59e0b"
        : state === "HALTED" || state === "ERROR" ? "#ef4444"
          : "#64748b";
  return (
    <span style={{
      display: "inline-block",
      width: 7,
      height: 7,
      borderRadius: "50%",
      background: color,
      marginRight: 5,
      verticalAlign: "middle",
    }} />
  );
}

// ── Dashboard ─────────────────────────────────────────────────────────────────

interface BackendData {
  runtime?: { operating_state?: string; safe_mode?: boolean };
  telemetry?: { latest_price?: number; total_trades?: number; current_unrealized_pnl?: number; current_unrealized_pnl_percent?: number };
  portfolio?: { total_capital?: number; total_portfolio_value?: number; available_capital?: number; invested_capital?: number; total_unrealized_pnl?: number };
  active_trades?: Array<{ symbol?: string; quantity?: number; entry_price?: number; current_price?: number; unrealized_pnl?: number; unrealized_pnl_percent?: number }>;
  trade_journal?: Array<{ id?: string; symbol?: string; quantity?: number; entry_price?: number; exit_price?: number; realized_pnl?: number; pnl?: number; fees?: number; opened_at?: string; closed_at?: string }>;
}

type ConnectionStatus = 'CONNECTED' | 'DISCONNECTED' | 'RECONNECTING';

export function Dashboard() {
  const [data, setData] = useState<BackendData>({
    runtime: {},
    telemetry: {},
    portfolio: {},
    active_trades: [],
    trade_journal: [],
  });
  const [isInitialLoad, setIsInitialLoad] = useState(true);
  const [connStatus, setConnStatus] = useState<ConnectionStatus>('RECONNECTING');
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);
  const abortControllerRef = useRef<AbortController | null>(null);

  useEffect(() => {
    let mounted = true;

    async function poll() {
      if (!mounted) return;

      try {
        const controller = new AbortController();
        abortControllerRef.current = controller;
        
        // 3000ms fetch timeout
        const timeoutId = setTimeout(() => {
          controller.abort();
        }, 3000);

        let json;
        try {
          json = await fetchRuntime(controller.signal);
        } finally {
          clearTimeout(timeoutId);
        }

        if (mounted) {
          console.log("[Dashboard] Raw API payload:", json);

          if (json && typeof json === 'object') {
            setData((prev) => ({
              ...prev,
              ...json
            }));
          }
          setIsInitialLoad(false);
          setConnStatus('CONNECTED');
        }
      } catch (err) {
        if (err instanceof Error && err.name === 'AbortError') {
          console.warn("[Dashboard] Fetch aborted (timeout or cleanup)");
        } else {
          console.error("[Dashboard] Fetch error:", err);
          if (mounted) setConnStatus('DISCONNECTED');
        }
      } finally {
        if (mounted) {
          timeoutRef.current = setTimeout(poll, 2000);
        }
      }
    }

    poll();

    return () => {
      mounted = false;
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      if (abortControllerRef.current) abortControllerRef.current.abort();
    };
  }, []);

  if (isInitialLoad) {
    return (
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: "24px 24px", color: "#e2e8f0", fontFamily: "'Geist Sans', system-ui, sans-serif" }}>
        Loading runtime... {connStatus === 'DISCONNECTED' && "(Backend Disconnected)"}
      </div>
    );
  }

  const runtime = {
    state: data?.runtime?.operating_state || "UNKNOWN",
    mode: "LIVE",
    symbol: data?.active_trades?.[0]?.symbol || "BTCUSDT",
    latestPrice: data?.telemetry?.latest_price || 0,
    safeMode: data?.runtime?.safe_mode || false,
    totalTrades: data?.telemetry?.total_trades || 0,
    uptime: "Live",
    unrealizedPnl: data?.telemetry?.current_unrealized_pnl || 0,
    unrealizedPnlPct: data?.telemetry?.current_unrealized_pnl_percent || 0,
  };

  const portfolio = {
    totalCapital: data?.portfolio?.total_capital || 0,
    totalValue: data?.portfolio?.total_portfolio_value || 0,
    availableCash: data?.portfolio?.available_capital || 0,
    investedCapital: data?.portfolio?.invested_capital || 0,
    realizedPnl: (data?.portfolio?.total_portfolio_value || 0) - (data?.portfolio?.total_capital || 0) - (data?.portfolio?.total_unrealized_pnl || 0),
  };

  const activeTrades = (data?.active_trades || []).map((t) => ({
    id: t?.symbol,
    symbol: t?.symbol,
    qty: t?.quantity,
    avgEntry: t?.entry_price,
    currentPrice: t?.current_price,
    pnl: t?.unrealized_pnl,
    pnlPct: t?.unrealized_pnl_percent,
    openedAt: "Active",
  }));

  const completedTrades = (data?.trade_journal || []).map((t, i: number) => ({
    id: t?.id || String(i),
    symbol: t?.symbol || "-",
    qty: t?.quantity || 0,
    entryPrice: t?.entry_price || 0,
    exitPrice: t?.exit_price || 0,
    realizedPnl: t?.realized_pnl || t?.pnl || 0,
    fees: t?.fees || 0,
    openedAt: t?.opened_at || "-",
    closedAt: t?.closed_at || "-",
  }));

  return (
    <div style={{
      maxWidth: 1200,
      margin: "0 auto",
      padding: "24px 24px",
      fontFamily: "'Geist Sans', system-ui, sans-serif",
    }}>

      {/* Header */}
      <div style={{ display: "flex", alignItems: "baseline", gap: 16, marginBottom: 32 }}>
        <h1 style={{ fontSize: 16, fontWeight: 700, color: "#e2e8f0", margin: 0 }}>
          PAISA
        </h1>
        <span style={{ fontSize: 12, color: "#475569" }}>
          Debug Dashboard
        </span>
        <span style={{ marginLeft: "auto", fontSize: 11, fontFamily: "monospace", color: "#334155" }}>
          <StateDot state={connStatus === 'CONNECTED' ? runtime.state : 'ERROR'} />
          [{connStatus}] · {runtime.state} · {runtime.mode} · {runtime.symbol}
        </span>
      </div>

      {/* ── Runtime Overview ── */}
      <Section title="Runtime">
        <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 8 }}>
          <MetricCard
            label="Latest Price"
            value={`$${runtime.latestPrice.toLocaleString()}`}
            sub={runtime.symbol}
          />
          <MetricCard
            label="State"
            value={runtime.state}
            sub={`Mode: ${runtime.mode}`}
          />
          <MetricCard
            label="Safe Mode"
            value={runtime.safeMode ? "ENABLED" : "DISABLED"}
            color={runtime.safeMode ? "green" : "red"}
          />
          <MetricCard
            label="Total Trades"
            value={String(runtime.totalTrades)}
            sub={`Uptime: ${runtime.uptime}`}
          />
          <MetricCard
            label="Unrealized P&L"
            value={`${usd(runtime.unrealizedPnl)} (${pct(runtime.unrealizedPnlPct)})`}
            color={pnlColor(runtime.unrealizedPnl)}
          />
        </div>
      </Section>

      {/* ── Portfolio Overview ── */}
      <Section title="Portfolio">
        <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 8 }}>
          <MetricCard label="Total Capital" value={usd(portfolio.totalCapital)} />
          <MetricCard
            label="Portfolio Value"
            value={usd(portfolio.totalValue)}
            sub={`${usd(portfolio.totalValue - portfolio.totalCapital)} net`}
            color={pnlColor(portfolio.totalValue - portfolio.totalCapital)}
          />
          <MetricCard
            label="Available Cash"
            value={usd(portfolio.availableCash)}
            sub={`${((portfolio.availableCash / portfolio.totalCapital) * 100).toFixed(1)}% of capital`}
          />
          <MetricCard
            label="Invested Capital"
            value={usd(portfolio.investedCapital)}
            sub={`${((portfolio.investedCapital / portfolio.totalCapital) * 100).toFixed(1)}% deployed`}
          />
          <MetricCard
            label="Realized P&L"
            value={usd(portfolio.realizedPnl)}
            color={pnlColor(portfolio.realizedPnl)}
          />
        </div>
      </Section>

      {/* ── Active Trades ── */}
      <TradesTable<ActiveTrade>
        title="Active Positions"
        rows={activeTrades}
        emptyMessage="No open positions"
        columns={[
          { header: "Symbol", key: "symbol" },
          {
            header: "Qty", key: "qty", align: "right",
            render: (v) => Number(v).toFixed(6)
          },
          {
            header: "Avg Entry", key: "avgEntry", align: "right",
            render: (v) => `$${Number(v).toLocaleString()}`
          },
          {
            header: "Current Price", key: "currentPrice", align: "right",
            render: (v) => `$${Number(v).toLocaleString()}`
          },
          {
            header: "Unrealized P&L", key: "pnl", align: "right",
            render: (v, row) => {
              const n = Number(v);
              const color = n > 0 ? "#22c55e" : n < 0 ? "#ef4444" : "#94a3b8";
              return (
                <span style={{ color }}>
                  {n >= 0 ? "+" : ""}{usd(n)}{" "}
                  <span style={{ opacity: 0.7 }}>({pct(row.pnlPct)})</span>
                </span>
              );
            }
          },
          { header: "Opened", key: "openedAt", align: "right" },
        ]}
      />

      {/* ── Completed Trades ── */}
      <TradesTable<CompletedTrade>
        title="Completed Trades"
        rows={completedTrades}
        emptyMessage="No completed trades"
        columns={[
          { header: "Symbol", key: "symbol" },
          {
            header: "Qty", key: "qty", align: "right",
            render: (v) => Number(v).toFixed(6)
          },
          {
            header: "Entry", key: "entryPrice", align: "right",
            render: (v) => `$${Number(v).toLocaleString()}`
          },
          {
            header: "Exit", key: "exitPrice", align: "right",
            render: (v) => `$${Number(v).toLocaleString()}`
          },
          {
            header: "Realized P&L", key: "realizedPnl", align: "right",
            render: (v) => {
              const n = Number(v);
              const color = n > 0 ? "#22c55e" : n < 0 ? "#ef4444" : "#94a3b8";
              return <span style={{ color }}>{n >= 0 ? "+" : ""}{usd(n)}</span>;
            }
          },
          {
            header: "Fees", key: "fees", align: "right",
            render: (v) => `-${usd(Number(v))}`
          },
          {
            header: "Net P&L", key: "realizedPnl", align: "right",
            render: (v, row) => {
              const net = Number(v) - row.fees;
              const color = net > 0 ? "#22c55e" : net < 0 ? "#ef4444" : "#94a3b8";
              return <span style={{ color }}>{net >= 0 ? "+" : ""}{usd(net)}</span>;
            }
          },
          { header: "Opened", key: "openedAt" },
          { header: "Closed", key: "closedAt" },
        ]}
      />

    </div>
  );
}
