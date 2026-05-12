"use client";

import { useMemo } from "react";
import {
  BarChart,
  Bar,
  Cell,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip as RechartsTooltip,
  ResponsiveContainer,
} from "recharts";
import type { SessionRecord, SessionAnalytics } from "../../services/api";

// ─── Helpers ──────────────────────────────────────────────────────────────────

function usd(n: number | null | undefined): string {
  if (n == null) return "—";
  return n.toLocaleString("en-US", { style: "currency", currency: "USD" });
}

function pct(n: number | null | undefined, decimals = 1): string {
  if (n == null) return "—";
  return `${n.toFixed(decimals)}%`;
}

function dur(seconds: number | null | undefined): string {
  if (seconds == null || seconds <= 0) return "—";
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = Math.floor(seconds % 60);
  if (h > 0) return `${h}h ${m}m ${s}s`;
  if (m > 0) return `${m}m ${s}s`;
  return `${s}s`;
}

function pnlColor(n: number | null | undefined): string {
  if (n == null || n === 0) return "#94a3b8";
  return n > 0 ? "#22c55e" : "#ef4444";
}

// ─── Sub-components ───────────────────────────────────────────────────────────

function Skeleton({ w = "100%", h = 14 }: { w?: string | number; h?: number }) {
  return (
    <>
      <style>{`
        @keyframes ad-shimmer {
          0%   { background-position: -200% 0; }
          100% { background-position: 200% 0; }
        }
      `}</style>
      <span
        style={{
          display: "inline-block",
          width: w,
          height: h,
          borderRadius: 3,
          background: "linear-gradient(90deg, #0f1a2a 25%, #1a2d45 50%, #0f1a2a 75%)",
          backgroundSize: "200% 100%",
          animation: "ad-shimmer 1.6s ease-in-out infinite",
        }}
      />
    </>
  );
}

function KPICard({
  label,
  value,
  loading,
  valueColor,
}: {
  label: string;
  value: React.ReactNode;
  loading: boolean;
  valueColor?: string;
}) {
  return (
    <div
      style={{
        padding: "16px",
        background: "rgba(15,23,42,0.6)",
        border: "1px solid #1a2d45",
        borderRadius: 8,
        display: "flex",
        flexDirection: "column",
        gap: 8,
        transition: "background 0.2s, transform 0.15s, border-color 0.2s",
        boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = "translateY(-1px)";
        e.currentTarget.style.background = "rgba(30,41,59,0.8)";
        e.currentTarget.style.borderColor = "rgba(56,189,248,0.18)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = "none";
        e.currentTarget.style.background = "rgba(15,23,42,0.6)";
        e.currentTarget.style.borderColor = "#1a2d45";
      }}
    >
      <span
        style={{
          fontSize: 10,
          letterSpacing: "0.1em",
          textTransform: "uppercase",
          color: "#64748b",
          fontWeight: 600,
        }}
      >
        {label}
      </span>
      {loading ? (
        <Skeleton h={22} />
      ) : (
        <span
          style={{
            fontSize: 18,
            fontWeight: 700,
            color: valueColor ?? "#e2e8f0",
            letterSpacing: "-0.01em",
            fontVariantNumeric: "tabular-nums",
          }}
        >
          {value}
        </span>
      )}
    </div>
  );
}

// ─── Chart Tooltip ────────────────────────────────────────────────────────────

const CustomTooltip = ({ active, payload, label, formatter }: { active?: boolean; payload?: Array<{ color?: string; value?: number }>; label?: string; formatter?: (val: number) => string }) => {
  if (active && payload && payload.length) {
    return (
      <div
        style={{
          background: "rgba(8,15,30,0.96)",
          border: "1px solid #1e293b",
          padding: "8px 12px",
          borderRadius: 6,
          boxShadow: "0 4px 12px rgba(0,0,0,0.4)",
        }}
      >
        <p style={{ margin: "0 0 6px", fontSize: 11, color: "#64748b", fontWeight: 600 }}>
          Session #{label}
        </p>
        {payload.map((entry: { color?: string; value?: number }, index: number) => (
          <p
            key={`item-${index}`}
            style={{
              margin: 0,
              fontSize: 13,
              fontWeight: 700,
              color: entry.color || "#e2e8f0",
            }}
          >
            {formatter && entry.value !== undefined ? formatter(entry.value) : entry.value}
          </p>
        ))}
      </div>
    );
  }
  return null;
};

// ─── AnalyticsDashboard ───────────────────────────────────────────────────────

export interface AnalyticsDashboardProps {
  sessions: SessionRecord[];
  analytics: SessionAnalytics | null;
  loading: boolean;
  offline: boolean;
}

export function AnalyticsDashboard({
  sessions,
  analytics,
  loading,
  offline,
}: AnalyticsDashboardProps) {
  // ── Derived Metrics ──
  const derived = useMemo(() => {
    if (!sessions || sessions.length === 0) return null;

    const completed = sessions.filter((s) => s.ended_at != null && s.duration_seconds != null);
    
    let longest = 0;
    let shortest = Number.MAX_SAFE_INTEGER;
    
    completed.forEach((s) => {
      if (s.duration_seconds! > longest) longest = s.duration_seconds!;
      if (s.duration_seconds! < shortest) shortest = s.duration_seconds!;
    });
    if (shortest === Number.MAX_SAFE_INTEGER) shortest = 0;

    const totalRealized = analytics?.total_realized_pnl ?? 0;
    const avgPnlPerSession = analytics?.total_sessions ? totalRealized / analytics.total_sessions : 0;
    
    // Runtime efficiency: (Profitable Sessions / Total Sessions) * 100 ... or win rate
    const efficiencyScore = analytics?.total_sessions 
      ? (analytics.profitable_sessions / analytics.total_sessions) * 100 
      : 0;

    return {
      longestSession: longest,
      shortestSession: shortest,
      avgPnlPerSession,
      efficiencyScore,
    };
  }, [sessions, analytics]);

  // ── Health Status ──
  const healthStatus = useMemo(() => {
    if (!analytics) return { state: "WARNING", color: "#f59e0b", bg: "rgba(245,158,11,0.15)" };
    
    const pnl = analytics.total_realized_pnl;
    const wr = analytics.win_rate;

    if (pnl > 0 && wr >= 40) {
      return { state: "HEALTHY", color: "#22c55e", bg: "rgba(34,197,94,0.15)" };
    }
    if (pnl <= -10) {
      return { state: "CRITICAL", color: "#ef4444", bg: "rgba(239,68,68,0.15)" };
    }
    return { state: "WARNING", color: "#f59e0b", bg: "rgba(245,158,11,0.15)" };
  }, [analytics]);

  // ── Chart Data ──
  const chartData = useMemo(() => {
    // Reverse to show chronological left-to-right (assuming sessions are desc by id)
    return [...sessions].reverse().map((s) => ({
      id: s.id,
      pnl: s.realized_pnl ?? 0,
      duration: s.duration_seconds ?? 0,
    }));
  }, [sessions]);

  // ── Render Helpers ──
  if (offline && !analytics && sessions.length === 0) {
    return (
      <section style={{ marginBottom: 32 }}>
        <div style={{ padding: "32px 14px", textAlign: "center", background: "#0a111e", border: "1px solid #1e293b", borderRadius: 8 }}>
          <span style={{ fontSize: 24 }}>🔌</span>
          <div style={{ marginTop: 12, fontSize: 13, color: "#ef4444", fontWeight: 600 }}>Backend Offline</div>
          <div style={{ fontSize: 11, color: "#64748b", marginTop: 4 }}>Analytics unavailable.</div>
        </div>
      </section>
    );
  }

  if (!loading && !offline && sessions.length === 0) {
    return (
      <section style={{ marginBottom: 32 }}>
        <div style={{ padding: "32px 14px", textAlign: "center", background: "#0a111e", border: "1px solid #1e293b", borderRadius: 8 }}>
          <span style={{ fontSize: 24 }}>📊</span>
          <div style={{ marginTop: 12, fontSize: 13, color: "#94a3b8", fontWeight: 600 }}>No Sessions Recorded</div>
          <div style={{ fontSize: 11, color: "#64748b", marginTop: 4 }}>Run the bot to collect analytics.</div>
        </div>
      </section>
    );
  }

  return (
    <section style={{ marginBottom: 32 }}>
      {/* ── Section Header & Health Banner ── */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          borderBottom: "1px solid #1e293b",
          paddingBottom: 8,
          marginBottom: 16,
        }}
      >
        <span
          style={{
            fontSize: 12,
            textTransform: "uppercase",
            letterSpacing: "0.1em",
            color: "#e2e8f0",
            fontWeight: 700,
          }}
        >
          Performance Analytics
        </span>
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,
            padding: "4px 10px",
            background: loading ? "rgba(100,116,139,0.1)" : healthStatus.bg,
            border: `1px solid ${loading ? "rgba(100,116,139,0.2)" : healthStatus.color + "40"}`,
            borderRadius: 4,
          }}
        >
          <span style={{ fontSize: 9, color: "#64748b", fontWeight: 700, letterSpacing: "0.1em" }}>HEALTH STATUS</span>
          {loading ? (
            <Skeleton w={40} h={10} />
          ) : (
            <span style={{ fontSize: 10, color: healthStatus.color, fontWeight: 800, letterSpacing: "0.05em" }}>
              {healthStatus.state}
            </span>
          )}
        </div>
      </div>

      {/* ── Core KPIs Grid ── */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))",
          gap: 12,
          marginBottom: 16,
        }}
      >
        <KPICard label="Total Sessions" value={analytics?.total_sessions ?? "—"} loading={loading} />
        <KPICard label="Total Realized P&L" value={usd(analytics?.total_realized_pnl)} loading={loading} valueColor={pnlColor(analytics?.total_realized_pnl)} />
        <KPICard label="Win Rate" value={pct(analytics?.win_rate)} loading={loading} valueColor={analytics && analytics.win_rate >= 40 ? "#22c55e" : "#ef4444"} />
        <KPICard label="Avg Duration" value={dur(analytics?.average_session_duration)} loading={loading} />
        <KPICard label="Best Session P&L" value={usd(analytics?.best_session_pnl)} loading={loading} valueColor={pnlColor(analytics?.best_session_pnl)} />
        <KPICard label="Worst Session P&L" value={usd(analytics?.worst_session_pnl)} loading={loading} valueColor={pnlColor(analytics?.worst_session_pnl)} />
        <KPICard label="Profitable" value={analytics?.profitable_sessions ?? "—"} loading={loading} valueColor={analytics && analytics.profitable_sessions > 0 ? "#22c55e" : undefined} />
        <KPICard label="Losing" value={analytics?.losing_sessions ?? "—"} loading={loading} valueColor={analytics && analytics.losing_sessions > 0 ? "#ef4444" : undefined} />
        <KPICard label="Safe Mode" value={analytics?.safe_mode_sessions ?? "—"} loading={loading} valueColor={analytics && analytics.safe_mode_sessions > 0 ? "#f59e0b" : undefined} />
      </div>

      {/* ── Derived Metrics & Charts ── */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 2fr",
          gap: 12,
        }}
      >
        {/* Derived Column */}
        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          <KPICard label="Avg P&L / Session" value={usd(derived?.avgPnlPerSession)} loading={loading} valueColor={pnlColor(derived?.avgPnlPerSession)} />
          <KPICard label="Efficiency Score" value={pct(derived?.efficiencyScore)} loading={loading} valueColor={derived && derived.efficiencyScore >= 50 ? "#22c55e" : "#f59e0b"} />
          <KPICard label="Longest Session" value={dur(derived?.longestSession)} loading={loading} />
          <KPICard label="Shortest Session" value={dur(derived?.shortestSession)} loading={loading} />
        </div>

        {/* Charts Column */}
        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          <div
            style={{
              background: "rgba(15,23,42,0.4)",
              border: "1px solid #1a2d45",
              borderRadius: 8,
              padding: "16px",
              height: 180,
            }}
          >
            <span style={{ fontSize: 10, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.1em", fontWeight: 600, display: "block", marginBottom: 12 }}>
              Session P&L History
            </span>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 0, right: 0, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="id" stroke="#475569" fontSize={10} tickLine={false} axisLine={false} />
                <YAxis stroke="#475569" fontSize={10} tickLine={false} axisLine={false} tickFormatter={(val) => `$${val}`} />
                <RechartsTooltip content={<CustomTooltip formatter={(val: number) => usd(val)} />} cursor={{ fill: "rgba(30,41,59,0.5)" }} />
                <Bar dataKey="pnl">
                  {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.pnl >= 0 ? "#22c55e" : "#ef4444"} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
          
          <div
            style={{
              background: "rgba(15,23,42,0.4)",
              border: "1px solid #1a2d45",
              borderRadius: 8,
              padding: "16px",
              height: 180,
            }}
          >
            <span style={{ fontSize: 10, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.1em", fontWeight: 600, display: "block", marginBottom: 12 }}>
              Session Duration (Seconds)
            </span>
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={chartData} margin={{ top: 0, right: 0, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="id" stroke="#475569" fontSize={10} tickLine={false} axisLine={false} />
                <YAxis stroke="#475569" fontSize={10} tickLine={false} axisLine={false} />
                <RechartsTooltip content={<CustomTooltip formatter={(val: number) => `${val}s`} />} />
                <Line type="monotone" dataKey="duration" stroke="#38bdf8" strokeWidth={2} dot={{ r: 3, fill: "#0f172a", strokeWidth: 2 }} activeDot={{ r: 5 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </section>
  );
}
