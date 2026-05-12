"use client";

import { useEffect, useState } from "react";
import { fetchSessionTradeAnalytics } from "../../services/api";
import type { SessionRecord, TradeAnalytics } from "../../services/api";

// ─── Helpers ──────────────────────────────────────────────────────────────────

function usd(n: number | null | undefined): string {
  if (n == null) return "—";
  return n.toLocaleString("en-US", { style: "currency", currency: "USD" });
}

function pct(n: number | null | undefined, decimals = 1): string {
  if (n == null) return "—";
  return `${n.toFixed(decimals)}%`;
}

function pnlColor(n: number | null | undefined): string {
  if (n == null || n === 0) return "#94a3b8";
  return n > 0 ? "#22c55e" : "#ef4444";
}

/** Format ISO timestamp as "12 May 2026, 03:54" */
function fmtDate(iso: string | null): string {
  if (!iso) return "—";
  try {
    const d = new Date(iso);
    if (isNaN(d.getTime())) return "—";
    return d.toLocaleString("en-GB", {
      day: "2-digit",
      month: "short",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    });
  } catch {
    return "—";
  }
}

/** Format raw seconds as "2h 14m 09s" (omits hours if zero, omits minutes if also zero) */
function fmtDuration(seconds: number | null): string {
  if (seconds === null || seconds <= 0) return "—";
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = seconds % 60;
  if (h > 0) {
    return `${h}h ${String(m).padStart(2, "0")}m ${String(s).padStart(2, "0")}s`;
  }
  if (m > 0) {
    return `${m}m ${String(s).padStart(2, "0")}s`;
  }
  return `${s}s`;
}

// ─── Derived session status ───────────────────────────────────────────────────

type SessionStatus = "ACTIVE" | "COMPLETED";

function sessionStatus(s: SessionRecord): SessionStatus {
  return s.ended_at === null ? "ACTIVE" : "COMPLETED";
}

// ─── Sub-components ───────────────────────────────────────────────────────────

function Badge({
  label,
  color,
  bg,
  border,
}: {
  label: string;
  color: string;
  bg: string;
  border: string;
}): React.ReactElement {
  return (
    <span
      style={{
        display: "inline-block",
        fontSize: 8,
        fontWeight: 700,
        letterSpacing: "0.1em",
        textTransform: "uppercase",
        color,
        background: bg,
        border: `1px solid ${border}`,
        borderRadius: 3,
        padding: "1px 5px",
        fontFamily: "'Geist Sans', system-ui, sans-serif",
        whiteSpace: "nowrap",
        verticalAlign: "middle",
      }}
    >
      {label}
    </span>
  );
}

function ActiveBadge(): React.ReactElement {
  return (
    <Badge
      label="ACTIVE"
      color="#22c55e"
      bg="rgba(34,197,94,0.08)"
      border="rgba(34,197,94,0.25)"
    />
  );
}

function CompletedBadge(): React.ReactElement {
  return (
    <Badge
      label="COMPLETED"
      color="#64748b"
      bg="rgba(100,116,139,0.06)"
      border="rgba(100,116,139,0.18)"
    />
  );
}

function SafeModeBadge(): React.ReactElement {
  return (
    <Badge
      label="SAFE MODE"
      color="#a78bfa"
      bg="rgba(167,139,250,0.08)"
      border="rgba(167,139,250,0.22)"
    />
  );
}

// ─── Session row ──────────────────────────────────────────────────────────────

function SessionRow({
  session,
  isProfitable,
  isLongest,
}: {
  session: SessionRecord;
  isProfitable: boolean;
  isLongest: boolean;
}): React.ReactElement {
  const [hovered, setHovered] = useState<boolean>(false);
  const [expanded, setExpanded] = useState<boolean>(false);
  const [tradeAnalytics, setTradeAnalytics] = useState<TradeAnalytics | null>(null);
  const [loadingAnalytics, setLoadingAnalytics] = useState<boolean>(false);

  useEffect(() => {
    if (!expanded || tradeAnalytics) return;
    let mounted = true;
    setTimeout(() => setLoadingAnalytics(true), 0);
    fetchSessionTradeAnalytics(session.id)
      .then(data => {
        if (mounted) setTradeAnalytics(data);
      })
      .catch(err => {
        console.error(err);
      })
      .finally(() => {
        if (mounted) setLoadingAnalytics(false);
      });
    return () => { mounted = false; };
  }, [expanded, session.id, tradeAnalytics]);

  const status = sessionStatus(session);
  const pnl = session.realized_pnl ?? 0;
  const rowPnlColor = pnl > 0 ? "#22c55e" : pnl < 0 ? "#ef4444" : "#64748b";

  // Highlight rules
  const accentLeft =
    status === "ACTIVE"
      ? "#22c55e"
      : isProfitable
      ? "#22c55e55"
      : isLongest
      ? "#38bdf855"
      : "transparent";

  return (
    <>
      <div
        onClick={() => setExpanded(!expanded)}
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        style={{
          display: "grid",
          gridTemplateColumns: "52px 1fr 1fr 80px 60px 90px 90px auto",
          gap: 0,
          alignItems: "center",
          padding: "8px 14px",
          background: expanded ? "rgba(30,41,59,0.9)" : hovered ? "rgba(30,41,59,0.7)" : "transparent",
          borderLeft: `2px solid ${accentLeft}`,
          borderBottom: expanded ? "none" : "1px solid #0f172a",
          transition: "background 0.15s ease",
          cursor: "pointer",
        }}
      >
      {/* ID */}
      <span
        style={{
          fontSize: 10,
          fontFamily: "'Geist Mono', monospace",
          color: "#475569",
          letterSpacing: "0.04em",
        }}
      >
        #{session.id}
      </span>

      {/* Started At */}
      <span
        style={{
          fontSize: 10,
          fontFamily: "'Geist Mono', monospace",
          color: "#94a3b8",
          letterSpacing: "0.02em",
        }}
      >
        {fmtDate(session.started_at)}
      </span>

      {/* Ended At */}
      <span
        style={{
          fontSize: 10,
          fontFamily: "'Geist Mono', monospace",
          color: status === "ACTIVE" ? "#22c55e" : "#64748b",
          letterSpacing: "0.02em",
        }}
      >
        {status === "ACTIVE" ? "Running…" : fmtDate(session.ended_at)}
      </span>

      {/* Duration */}
      <span
        style={{
          fontSize: 10,
          fontFamily: "'Geist Mono', monospace",
          color: isLongest ? "#38bdf8" : "#64748b",
          letterSpacing: "0.04em",
          textAlign: "right",
        }}
      >
        {fmtDuration(session.duration_seconds)}
      </span>

      {/* Total Trades */}
      <span
        style={{
          fontSize: 10,
          fontFamily: "'Geist Mono', monospace",
          color:
            (session.total_trades ?? 0) > 0 ? "#cbd5e1" : "#334155",
          textAlign: "right",
          letterSpacing: "0.04em",
        }}
      >
        {session.total_trades ?? 0}
      </span>

      {/* Realized PnL */}
      <span
        style={{
          fontSize: 10,
          fontFamily: "'Geist Mono', monospace",
          color: rowPnlColor,
          textAlign: "right",
          letterSpacing: "0.04em",
        }}
      >
        {pnl >= 0 ? "+" : ""}
        {usd(pnl)}
      </span>

      {/* Portfolio Value */}
      <span
        style={{
          fontSize: 10,
          fontFamily: "'Geist Mono', monospace",
          color: "#94a3b8",
          textAlign: "right",
          letterSpacing: "0.04em",
        }}
      >
        {session.portfolio_value !== null ? usd(session.portfolio_value) : "—"}
      </span>

      {/* Badges */}
      <div
        style={{
          display: "flex",
          gap: 4,
          justifyContent: "flex-end",
          flexWrap: "nowrap",
        }}
      >
        {status === "ACTIVE" ? <ActiveBadge /> : <CompletedBadge />}
        {session.safe_mode_triggered && <SafeModeBadge />}
      </div>
    </div>
      {expanded && (
        <div style={{ background: "rgba(15,23,42,0.4)", borderBottom: "1px solid #0f172a", padding: "16px 24px" }}>
          {loadingAnalytics ? <div style={{ fontSize: 11, color: "#64748b" }}>Loading analytics...</div> : tradeAnalytics ? (
            <div style={{ display: "grid", gridTemplateColumns: "repeat(7, 1fr)", gap: 16 }}>
              <div style={{ display: "flex", flexDirection: "column" }}>
                <span style={{ fontSize: 9, color: "#64748b", textTransform: "uppercase" }}>Total Trades</span>
                <span style={{ fontSize: 13, color: "#e2e8f0" }}>{tradeAnalytics.total_trades}</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column" }}>
                <span style={{ fontSize: 9, color: "#64748b", textTransform: "uppercase" }}>Win Rate</span>
                <span style={{ fontSize: 13, color: tradeAnalytics.win_rate >= 40 ? "#22c55e" : "#ef4444" }}>{pct(tradeAnalytics.win_rate)}</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column" }}>
                <span style={{ fontSize: 9, color: "#64748b", textTransform: "uppercase" }}>W / L</span>
                <span style={{ fontSize: 13, color: "#e2e8f0" }}><span style={{color: "#22c55e"}}>{tradeAnalytics.winning_trades}</span> / <span style={{color: "#ef4444"}}>{tradeAnalytics.losing_trades}</span></span>
              </div>
              <div style={{ display: "flex", flexDirection: "column" }}>
                <span style={{ fontSize: 9, color: "#64748b", textTransform: "uppercase" }}>Realized P&L</span>
                <span style={{ fontSize: 13, color: pnlColor(tradeAnalytics.total_realized_pnl) }}>{usd(tradeAnalytics.total_realized_pnl)}</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column" }}>
                <span style={{ fontSize: 9, color: "#64748b", textTransform: "uppercase" }}>Avg Trade</span>
                <span style={{ fontSize: 13, color: pnlColor(tradeAnalytics.avg_trade_pnl) }}>{usd(tradeAnalytics.avg_trade_pnl)}</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column" }}>
                <span style={{ fontSize: 9, color: "#64748b", textTransform: "uppercase" }}>Best Trade</span>
                <span style={{ fontSize: 13, color: pnlColor(tradeAnalytics.best_trade_pnl) }}>{usd(tradeAnalytics.best_trade_pnl)}</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column" }}>
                <span style={{ fontSize: 9, color: "#64748b", textTransform: "uppercase" }}>Worst Trade</span>
                <span style={{ fontSize: 13, color: pnlColor(tradeAnalytics.worst_trade_pnl) }}>{usd(tradeAnalytics.worst_trade_pnl)}</span>
              </div>
            </div>
          ) : <div style={{ fontSize: 11, color: "#ef4444" }}>Failed to load analytics</div>}
        </div>
      )}
    </>
  );
}

// ─── Table header ─────────────────────────────────────────────────────────────

function TableHeader(): React.ReactElement {
  const cell = (
    label: string,
    align: "left" | "right" = "left"
  ): React.ReactElement => (
    <span
      style={{
        fontSize: 9,
        letterSpacing: "0.1em",
        textTransform: "uppercase",
        color: "#1e3a5f",
        fontFamily: "'Geist Sans', system-ui, sans-serif",
        textAlign: align,
        display: "block",
      }}
    >
      {label}
    </span>
  );

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "52px 1fr 1fr 80px 60px 90px 90px auto",
        gap: 0,
        padding: "6px 14px",
        borderBottom: "1px solid #1e293b",
        marginBottom: 0,
      }}
    >
      {cell("ID")}
      {cell("Started")}
      {cell("Ended")}
      {cell("Duration", "right")}
      {cell("Trades", "right")}
      {cell("Realized P&L", "right")}
      {cell("Portfolio", "right")}
      {cell("Status", "right")}
    </div>
  );
}

// ─── Empty / loading states ───────────────────────────────────────────────────

function EmptyState({ offline }: { offline: boolean }): React.ReactElement {
  return (
    <div
      style={{
        padding: "20px 14px",
        fontSize: 11,
        color: "#334155",
        fontFamily: "'Geist Sans', system-ui, sans-serif",
        fontStyle: "italic",
        textAlign: "center",
      }}
    >
      {offline
        ? "Session history unavailable — backend offline"
        : "No sessions recorded yet"}
    </div>
  );
}

function LoadingState(): React.ReactElement {
  return (
    <div
      style={{
        padding: "20px 14px",
        fontSize: 10,
        color: "#1e3a5f",
        fontFamily: "'Geist Mono', monospace",
        letterSpacing: "0.06em",
        textAlign: "center",
      }}
    >
      Loading sessions…
    </div>
  );
}

// ─── SessionHistory ───────────────────────────────────────────────────────────

interface SessionHistoryProps {
  sessions: SessionRecord[];
  isLoading: boolean;
  offline: boolean;
}

export function SessionHistory({
  sessions,
  isLoading,
  offline,
}: SessionHistoryProps): React.ReactElement {

  // ── derived highlights ────────────────────────────────────────────────────

  /** ID of the session with the highest duration_seconds */
  const longestId: number | null =
    sessions.length === 0
      ? null
      : sessions.reduce<SessionRecord>((best, s) => {
          const bd = best.duration_seconds ?? 0;
          const sd = s.duration_seconds ?? 0;
          return sd > bd ? s : best;
        }, sessions[0]).id;

  // ── render ────────────────────────────────────────────────────────────────

  return (
    <section style={{ marginBottom: 32 }}>
      {/* Section header */}
      <div
        style={{
          fontSize: 10,
          textTransform: "uppercase",
          letterSpacing: "0.1em",
          color: "#334155",
          borderBottom: "1px solid #1e293b",
          paddingBottom: 6,
          marginBottom: 0,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <span>Session History</span>
        {sessions.length > 0 && (
          <span
            style={{
              fontSize: 9,
              color: "#1e3a5f",
              letterSpacing: "0.06em",
              fontFamily: "'Geist Mono', monospace",
            }}
          >
            {sessions.length} session{sessions.length !== 1 ? "s" : ""}
          </span>
        )}
      </div>

      {/* Table container */}
      <div
        style={{
          background: "#0a111e",
          border: "1px solid #1e293b",
          borderTop: "none",
          borderRadius: "0 0 6px 6px",
          overflow: "hidden",
        }}
      >
        {isLoading ? (
          <LoadingState />
        ) : offline && sessions.length === 0 ? (
          <EmptyState offline />
        ) : sessions.length === 0 ? (
          <EmptyState offline={false} />
        ) : (
          <>
            <TableHeader />
            {sessions.map((s) => (
              <SessionRow
                key={s.id}
                session={s}
                isProfitable={(s.realized_pnl ?? 0) > 0}
                isLongest={s.id === longestId}
              />
            ))}
          </>
        )}
      </div>

      {/* Legend */}
      {sessions.length > 0 && (
        <div
          style={{
            display: "flex",
            gap: 14,
            marginTop: 8,
            paddingLeft: 2,
          }}
        >
          {[
            { color: "#22c55e", label: "Profitable session" },
            { color: "#38bdf8", label: "Longest session" },
          ].map(({ color, label }) => (
            <span
              key={label}
              style={{
                display: "inline-flex",
                alignItems: "center",
                gap: 5,
                fontSize: 9,
                color: "#334155",
                fontFamily: "'Geist Sans', system-ui, sans-serif",
                letterSpacing: "0.06em",
              }}
            >
              <span
                style={{
                  width: 8,
                  height: 8,
                  background: color,
                  borderRadius: 1,
                  display: "inline-block",
                  flexShrink: 0,
                  opacity: 0.55,
                }}
              />
              {label}
            </span>
          ))}
        </div>
      )}
    </section>
  );
}
