"use client";

import { MetricCard } from "./MetricCard";
import { TradesTable } from "./TradesTable";
import { SessionClock } from "./SessionClock";
import { RuntimeControls } from "./RuntimeControls";
import { SessionHistory } from "./SessionHistory";
import { AnalyticsDashboard } from "./AnalyticsDashboard";
import type { ActiveTrade, CompletedTrade } from "@/types";
import { useEffect, useState, useRef } from "react";
import { fetchRuntime, fetchSessions, fetchOverallAnalytics, fetchActiveSession } from "../../services/api";
import type { SessionRecord, SessionAnalytics, ActiveSessionResponse } from "../../services/api";

// ── helpers ───────────────────────────────────────────────────────────────────

function usd(n: number): string {
  return n.toLocaleString("en-US", { style: "currency", currency: "USD" });
}

function pct(n: number): string {
  return `${n >= 0 ? "+" : ""}${n.toFixed(2)}%`;
}

function pnlColor(n: number): "green" | "red" | "default" {
  return n > 0 ? "green" : n < 0 ? "red" : "default";
}

// ── section label ─────────────────────────────────────────────────────────────

function Section({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}): React.ReactElement {
  return (
    <section style={{ marginBottom: 32 }}>
      <div
        style={{
          fontSize: 10,
          textTransform: "uppercase",
          letterSpacing: "0.1em",
          color: "#334155",
          borderBottom: "1px solid #1e293b",
          paddingBottom: 6,
          marginBottom: 12,
        }}
      >
        {title}
      </div>
      {children}
    </section>
  );
}

// ── status dot ────────────────────────────────────────────────────────────────

function StateDot({ state }: { state: string }): React.ReactElement {
  const color =
    state === "RUNNING"
      ? "#22c55e"
      : state === "PAUSED"
      ? "#f59e0b"
      : state === "HALTED" || state === "ERROR"
      ? "#ef4444"
      : "#64748b";
  return (
    <span
      style={{
        display: "inline-block",
        width: 7,
        height: 7,
        borderRadius: "50%",
        background: color,
        marginRight: 5,
        verticalAlign: "middle",
      }}
    />
  );
}

// ── offline banner ────────────────────────────────────────────────────────────

function OfflineBanner({
  visible,
}: {
  visible: boolean;
}): React.ReactElement {
  return (
    <>
      <style>{`
        @keyframes dash-banner-pulse {
          0%, 100% { opacity: 1; }
          50%       { opacity: 0.6; }
        }
      `}</style>
      <div
        role="alert"
        aria-live="polite"
        style={{
          marginBottom: 24,
          padding: "12px 16px",
          background: "rgba(239,68,68,0.05)",
          border: "1px solid rgba(239,68,68,0.2)",
          borderRadius: 6,
          display: "flex",
          alignItems: "flex-start",
          gap: 14,
          opacity: visible ? 1 : 0,
          pointerEvents: visible ? "auto" : "none",
          transition: "opacity 0.4s ease",
        }}
      >
        {/* animated dot */}
        <span
          style={{
            width: 8,
            height: 8,
            borderRadius: "50%",
            background: "#ef4444",
            flexShrink: 0,
            marginTop: 3,
            animation: visible
              ? "dash-banner-pulse 2s ease-in-out infinite"
              : "none",
          }}
        />
        <div>
          <div
            style={{
              fontSize: 10,
              fontWeight: 700,
              letterSpacing: "0.12em",
              textTransform: "uppercase",
              color: "#ef4444",
              marginBottom: 3,
              fontFamily: "'Geist Sans', system-ui, sans-serif",
            }}
          >
            Backend Offline
          </div>
          <div
            style={{
              fontSize: 11,
              color: "#64748b",
              fontFamily: "'Geist Sans', system-ui, sans-serif",
              lineHeight: 1.5,
            }}
          >
            Live runtime unavailable — polling for recovery.
            <br />
            Historical data still accessible below.
          </div>
        </div>
      </div>
    </>
  );
}

// ── types ─────────────────────────────────────────────────────────────────────

interface BackendData {
  runtime?: { operating_state?: string; safe_mode?: boolean };
  telemetry?: {
    latest_price?: number;
    total_trades?: number;
    current_unrealized_pnl?: number;
    current_unrealized_pnl_percent?: number;
  };
  portfolio?: {
    total_capital?: number;
    total_portfolio_value?: number;
    available_capital?: number;
    invested_capital?: number;
    total_unrealized_pnl?: number;
  };
  active_trades?: Array<{
    symbol?: string;
    quantity?: number;
    entry_price?: number;
    current_price?: number;
    unrealized_pnl?: number;
    unrealized_pnl_percent?: number;
  }>;
  trade_journal?: Array<{
    id?: string;
    symbol?: string;
    quantity?: number;
    entry_price?: number;
    exit_price?: number;
    realized_pnl?: number;
    pnl?: number;
    fees?: number;
    opened_at?: string;
    closed_at?: string;
  }>;
  /** Populated by runtime_snapshot when session_started_at is set */
  session?: { started_at?: string; uptime_seconds?: number };
  controller?: {
    is_running?: boolean;
    is_paused?: boolean;
    safe_mode?: boolean;
  };
}

type ConnectionStatus = "CONNECTED" | "DISCONNECTED" | "RECONNECTING";

// ── Historical Data Hook ──────────────────────────────────────────────────────

function useHistoricalData(isBackendConnected: boolean) {
  const [sessions, setSessions] = useState<SessionRecord[]>([]);
  const [analytics, setAnalytics] = useState<SessionAnalytics | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [offline, setOffline] = useState<boolean>(false);

  const timeoutRef = useRef<NodeJS.Timeout | null>(null);
  const abortRef = useRef<AbortController | null>(null);

  useEffect(() => {
    if (!isBackendConnected) {
      setTimeout(() => {
        setOffline(true);
        setLoading(false);
      }, 0);
      return;
    }

    let mounted = true;

    async function poll() {
      if (!mounted) return;
      try {
        const controller = new AbortController();
        abortRef.current = controller;
        const fetchTimeoutId = setTimeout(() => controller.abort(), 4000);
        
        let dataSessions: SessionRecord[];
        let dataAnalytics: SessionAnalytics;
        
        try {
          [dataSessions, dataAnalytics] = await Promise.all([
            fetchSessions(controller.signal),
            fetchOverallAnalytics(controller.signal),
          ]);
        } finally {
          clearTimeout(fetchTimeoutId);
        }

        if (!mounted) return;
        dataSessions.sort((a, b) => b.id - a.id);
        
        setSessions(dataSessions);
        setAnalytics(dataAnalytics);
        setOffline(false);
        setLoading(false);
      } catch (err) {
        if (!mounted) return;
        const isAbort = err instanceof Error && err.name === "AbortError";
        if (!isAbort) {
          setOffline(true);
          setLoading(false);
        }
      } finally {
        if (mounted) {
          timeoutRef.current = setTimeout(poll, 8000);
        }
      }
    }
    
    poll();
    
    return () => {
      mounted = false;
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      if (abortRef.current) abortRef.current.abort();
    };
  }, [isBackendConnected]);

  return { sessions, analytics, loading, offline };
}

// ── Dashboard ─────────────────────────────────────────────────────────────────

export function Dashboard(): React.ReactElement {
  const [data, setData] = useState<BackendData>({
    runtime: {},
    telemetry: {},
    portfolio: {},
    active_trades: [],
    trade_journal: [],
  });

  const [activeSession, setActiveSession] = useState<ActiveSessionResponse | null>(null);

  // True only during the very first fetch attempt (before any response or error)
  const [isInitialLoad, setIsInitialLoad] = useState<boolean>(true);

  const [connStatus, setConnStatus] =
    useState<ConnectionStatus>("RECONNECTING");

  const timeoutRef = useRef<NodeJS.Timeout | null>(null);
  const abortControllerRef = useRef<AbortController | null>(null);

  /**
   * Noise suppressor: tracks whether we've already logged the offline warning
   * for the current disconnect episode.  Resets to false on recovery so the
   * next disconnect will log once again.
   */
  const hasLoggedOffline = useRef<boolean>(false);

  // ── polling loop ────────────────────────────────────────────────────────────

  useEffect(() => {
    let mounted = true;

    async function poll(): Promise<void> {
      if (!mounted) return;

      try {
        const controller = new AbortController();
        abortControllerRef.current = controller;

        // 3 s fetch timeout — aborts with AbortError on expiry
        const fetchTimeoutId = setTimeout(() => controller.abort(), 3000);

        let json: unknown;
        let activeSessionJson: ActiveSessionResponse;
        try {
          [json, activeSessionJson] = await Promise.all([
            fetchRuntime(controller.signal),
            fetchActiveSession(controller.signal)
          ]);
        } finally {
          clearTimeout(fetchTimeoutId);
        }

        if (!mounted) return;

        if (json && typeof json === "object") {
          setData((prev) => ({ ...prev, ...(json as BackendData) }));
        }
        
        setActiveSession(activeSessionJson);

        // Recovery: reset offline log gate so next disconnect fires once
        hasLoggedOffline.current = false;

        setIsInitialLoad(false);
        setConnStatus("CONNECTED");
      } catch (err) {
        if (!mounted) return;

        const isAbort = err instanceof Error && err.name === "AbortError";

        if (!isAbort) {
          // Log only on the first failure of each disconnect episode
          if (!hasLoggedOffline.current) {
            console.warn(
              "[Dashboard] Backend offline — polling silently until recovery.",
              err
            );
            hasLoggedOffline.current = true;
          }
          setConnStatus("DISCONNECTED");
        }
        // AbortErrors from cleanup are intentional — stay silent

        // If we've never had a successful response, reveal the offline state
        // so the user sees the banner rather than an infinite "Loading…"
        setIsInitialLoad(false);
      } finally {
        if (mounted) {
          // Back off slightly when disconnected to reduce noise
          const delay = connStatus === "DISCONNECTED" ? 4000 : 2000;
          timeoutRef.current = setTimeout(poll, delay);
        }
      }
    }

    poll();

    return () => {
      mounted = false;
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      if (abortControllerRef.current) abortControllerRef.current.abort();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // ── derived state ───────────────────────────────────────────────────────────

  const isBackendConnected: boolean = connStatus === "CONNECTED";
  
  const { sessions, analytics, loading: historicalLoading, offline: historicalOffline } = useHistoricalData(isBackendConnected);

  const runtime = {
    state: data?.runtime?.operating_state ?? "UNKNOWN",
    mode: "LIVE",
    symbol: data?.active_trades?.[0]?.symbol ?? "BTCUSDT",
    latestPrice: data?.telemetry?.latest_price ?? 0,
    safeMode: data?.runtime?.safe_mode ?? false,
    totalTrades: data?.telemetry?.total_trades ?? 0,
    uptime: "Live",
    unrealizedPnl: data?.telemetry?.current_unrealized_pnl ?? 0,
    unrealizedPnlPct: data?.telemetry?.current_unrealized_pnl_percent ?? 0,
  };

  const portfolio = {
    totalCapital: data?.portfolio?.total_capital ?? 0,
    totalValue: data?.portfolio?.total_portfolio_value ?? 0,
    availableCash: data?.portfolio?.available_capital ?? 0,
    investedCapital: data?.portfolio?.invested_capital ?? 0,
    realizedPnl:
      (data?.portfolio?.total_portfolio_value ?? 0) -
      (data?.portfolio?.total_capital ?? 0) -
      (data?.portfolio?.total_unrealized_pnl ?? 0),
  };

  const activeTrades = (data?.active_trades ?? []).map((t) => ({
    id: t?.symbol ?? "",
    symbol: t?.symbol ?? "",
    qty: t?.quantity ?? 0,
    avgEntry: t?.entry_price ?? 0,
    currentPrice: t?.current_price ?? 0,
    pnl: t?.unrealized_pnl ?? 0,
    pnlPct: t?.unrealized_pnl_percent ?? 0,
    openedAt: "Active",
  }));

  const completedTrades = (data?.trade_journal ?? []).map((t, i: number) => ({
    id: t?.id ?? String(i),
    symbol: t?.symbol ?? "-",
    qty: t?.quantity ?? 0,
    entryPrice: t?.entry_price ?? 0,
    exitPrice: t?.exit_price ?? 0,
    realizedPnl: t?.realized_pnl ?? t?.pnl ?? 0,
    fees: t?.fees ?? 0,
    openedAt: t?.opened_at ?? "-",
    closedAt: t?.closed_at ?? "-",
  }));

  // ── initial probe — show nothing until first response or first failure ───────

  if (isInitialLoad) {
    return (
      <div
        style={{
          maxWidth: 1200,
          margin: "0 auto",
          padding: "24px 24px",
          color: "#475569",
          fontFamily: "'Geist Sans', system-ui, sans-serif",
          fontSize: 11,
          letterSpacing: "0.06em",
        }}
      >
        Connecting to runtime…
      </div>
    );
  }

  // ── render ──────────────────────────────────────────────────────────────────

  /**
   * Live-only panels are wrapped in a single container that transitions opacity
   * and blur between connected/offline states.  This avoids conditional unmounting
   * (which causes flicker) while clearly communicating data staleness.
   */
  const liveStyle: React.CSSProperties = {
    opacity: isBackendConnected ? 1 : 0.22,
    filter: isBackendConnected ? "none" : "grayscale(60%)",
    pointerEvents: isBackendConnected ? "auto" : "none",
    transition: "opacity 0.5s ease, filter 0.5s ease",
  };

  return (
    <div
      style={{
        maxWidth: 1200,
        margin: "0 auto",
        padding: "24px 24px",
        fontFamily: "'Geist Sans', system-ui, sans-serif",
      }}
    >
      {/* ── Header ── */}
      <div
        style={{
          display: "flex",
          alignItems: "baseline",
          gap: 16,
          marginBottom: 32,
        }}
      >
        <h1 style={{ fontSize: 16, fontWeight: 700, color: "#e2e8f0", margin: 0 }}>
          PAISA
        </h1>
        <span style={{ fontSize: 12, color: "#475569" }}>Debug Dashboard</span>
        <span
          style={{
            marginLeft: "auto",
            fontSize: 11,
            fontFamily: "monospace",
            color: "#334155",
          }}
        >
          <StateDot
            state={isBackendConnected ? runtime.state : "ERROR"}
          />
          [{connStatus}]
          {isBackendConnected && ` · ${runtime.state} · ${runtime.mode} · ${runtime.symbol}`}
        </span>
      </div>

      {/* ── Offline banner — always rendered, opacity-gated ── */}
      <OfflineBanner visible={!isBackendConnected} />

      {/* ══════════════════════════════════════════════════════
          LIVE PANELS — faded + non-interactive when offline
         ══════════════════════════════════════════════════════ */}
      <div style={liveStyle} aria-hidden={!isBackendConnected}>

        {/* Session Clock */}
        <SessionClock
          activeSession={activeSession}
          connStatus={connStatus}
        />

        {/* Runtime Controls */}
        <RuntimeControls
          isRunning={data?.controller?.is_running ?? false}
          isPaused={data?.controller?.is_paused ?? false}
          safeModeActive={data?.controller?.safe_mode ?? false}
        />

        {/* Runtime Overview */}
        <Section title="Runtime">
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(5, 1fr)",
              gap: 8,
            }}
          >
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

        {/* Portfolio Overview */}
        <Section title="Portfolio">
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(5, 1fr)",
              gap: 8,
            }}
          >
            <MetricCard
              label="Total Capital"
              value={usd(portfolio.totalCapital)}
            />
            <MetricCard
              label="Portfolio Value"
              value={usd(portfolio.totalValue)}
              sub={`${usd(portfolio.totalValue - portfolio.totalCapital)} net`}
              color={pnlColor(portfolio.totalValue - portfolio.totalCapital)}
            />
            <MetricCard
              label="Available Cash"
              value={usd(portfolio.availableCash)}
              sub={`${((portfolio.availableCash / (portfolio.totalCapital || 1)) * 100).toFixed(1)}% of capital`}
            />
            <MetricCard
              label="Invested Capital"
              value={usd(portfolio.investedCapital)}
              sub={`${((portfolio.investedCapital / (portfolio.totalCapital || 1)) * 100).toFixed(1)}% deployed`}
            />
            <MetricCard
              label="Realized P&L"
              value={usd(portfolio.realizedPnl)}
              color={pnlColor(portfolio.realizedPnl)}
            />
          </div>
        </Section>

        {/* Active Positions */}
        <TradesTable<ActiveTrade>
          title="Active Positions"
          rows={activeTrades}
          emptyMessage="No open positions"
          columns={[
            { header: "Symbol", key: "symbol" },
            {
              header: "Qty",
              key: "qty",
              align: "right",
              render: (v) => Number(v).toFixed(6),
            },
            {
              header: "Avg Entry",
              key: "avgEntry",
              align: "right",
              render: (v) => `$${Number(v).toLocaleString()}`,
            },
            {
              header: "Current Price",
              key: "currentPrice",
              align: "right",
              render: (v) => `$${Number(v).toLocaleString()}`,
            },
            {
              header: "Unrealized P&L",
              key: "pnl",
              align: "right",
              render: (v, row) => {
                const n = Number(v);
                const color =
                  n > 0 ? "#22c55e" : n < 0 ? "#ef4444" : "#94a3b8";
                return (
                  <span style={{ color }}>
                    {n >= 0 ? "+" : ""}
                    {usd(n)}{" "}
                    <span style={{ opacity: 0.7 }}>({pct(row.pnlPct)})</span>
                  </span>
                );
              },
            },
            { header: "Opened", key: "openedAt", align: "right" },
          ]}
        />

      </div>{/* end live panels */}

      {/* ══════════════════════════════════════════════════════
          HISTORICAL PANELS — always fully visible
         ══════════════════════════════════════════════════════ */}

      {/* Completed Trades */}
      <TradesTable<CompletedTrade>
        title="Completed Trades"
        rows={completedTrades}
        emptyMessage="No completed trades"
        columns={[
          { header: "Symbol", key: "symbol" },
          {
            header: "Qty",
            key: "qty",
            align: "right",
            render: (v) => Number(v).toFixed(6),
          },
          {
            header: "Entry",
            key: "entryPrice",
            align: "right",
            render: (v) => `$${Number(v).toLocaleString()}`,
          },
          {
            header: "Exit",
            key: "exitPrice",
            align: "right",
            render: (v) => `$${Number(v).toLocaleString()}`,
          },
          {
            header: "Realized P&L",
            key: "realizedPnl",
            align: "right",
            render: (v) => {
              const n = Number(v);
              const color = n > 0 ? "#22c55e" : n < 0 ? "#ef4444" : "#94a3b8";
              return (
                <span style={{ color }}>
                  {n >= 0 ? "+" : ""}
                  {usd(n)}
                </span>
              );
            },
          },
          {
            header: "Fees",
            key: "fees",
            align: "right",
            render: (v) => `-${usd(Number(v))}`,
          },
          {
            header: "Net P&L",
            key: "realizedPnl",
            align: "right",
            render: (v, row) => {
              const net = Number(v) - row.fees;
              const color =
                net > 0 ? "#22c55e" : net < 0 ? "#ef4444" : "#94a3b8";
              return (
                <span style={{ color }}>
                  {net >= 0 ? "+" : ""}
                  {usd(net)}
                </span>
              );
            },
          },
          { header: "Opened", key: "openedAt" },
          { header: "Closed", key: "closedAt" },
        ]}
      />

      {/* ── Analytics Dashboard ── */}
      <AnalyticsDashboard
        sessions={sessions}
        analytics={analytics}
        loading={historicalLoading}
        offline={historicalOffline}
      />

      {/* ── Session History ── */}
      <SessionHistory
        sessions={sessions}
        isLoading={historicalLoading}
        offline={historicalOffline}
      />

    </div>
  );
}
