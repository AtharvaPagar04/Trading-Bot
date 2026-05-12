"use client";

import React from "react";
import type { ActiveSessionResponse } from "../../services/api";

interface SessionClockProps {
  activeSession: ActiveSessionResponse | null;
  connStatus: string;
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

function formatUptime(totalSeconds: number): string {
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;
  return [
    String(h).padStart(2, "0") + "h",
    String(m).padStart(2, "0") + "m",
    String(s).padStart(2, "0") + "s",
  ].join(" ");
}

function usd(n: number): string {
  return n.toLocaleString("en-US", { style: "currency", currency: "USD" });
}

function statusColor(status: string): string {
  switch (status.toUpperCase()) {
    case "ACTIVE":
      return "#22c55e";
    case "RECOVERING":
      return "#f59e0b";
    case "STOPPED":
    default:
      return "#ef4444";
  }
}

function statusBgColor(status: string): string {
  switch (status.toUpperCase()) {
    case "ACTIVE":
      return "rgba(34,197,94,0.08)";
    case "RECOVERING":
      return "rgba(245,158,11,0.08)";
    case "STOPPED":
    default:
      return "rgba(239,68,68,0.08)";
  }
}

// ─── Dot ──────────────────────────────────────────────────────────────────────

function PulseDot({ color }: { color: string }) {
  return (
    <span
      style={{
        position: "relative",
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        width: 8,
        height: 8,
        marginRight: 6,
        verticalAlign: "middle",
        flexShrink: 0,
      }}
    >
      <span
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: "50%",
          background: color,
          opacity: 0.25,
          animation: color === "#22c55e" ? "session-ping 1.6s ease-out infinite" : "none",
        }}
      />
      <span
        style={{
          width: 6,
          height: 6,
          borderRadius: "50%",
          background: color,
          display: "block",
          flexShrink: 0,
        }}
      />
    </span>
  );
}

// ─── Cell ─────────────────────────────────────────────────────────────────────

function Cell({
  label,
  value,
  mono = false,
  accent,
}: {
  label: string;
  value: React.ReactNode;
  mono?: boolean;
  accent?: string;
}) {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: 4,
      }}
    >
      <span
        style={{
          fontSize: 9,
          letterSpacing: "0.1em",
          textTransform: "uppercase",
          color: "#334155",
          fontFamily: "'Geist Sans', system-ui, sans-serif",
        }}
      >
        {label}
      </span>
      <span
        style={{
          fontSize: 12,
          fontFamily: mono ? "'Geist Mono', 'Fira Code', monospace" : "'Geist Sans', system-ui, sans-serif",
          fontWeight: 500,
          color: accent ?? "#94a3b8",
          letterSpacing: mono ? "0.04em" : undefined,
        }}
      >
        {value}
      </span>
    </div>
  );
}

// ─── SessionClock ─────────────────────────────────────────────────────────────

export function SessionClock({
  activeSession,
  connStatus,
}: SessionClockProps): React.ReactElement {
  let status = "STOPPED";
  if (connStatus !== "CONNECTED") {
    status = "RECOVERING";
  } else if (activeSession?.active) {
    status = "ACTIVE";
  }

  // Handle loading state implicitly with activeSession === null, but since we also have isInitialLoad in Dashboard, we can just show loading or "No Active Session"
  if (!activeSession) {
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
          Session
        </div>
        <div
          style={{
            background: "#0f172a",
            border: "1px solid #1e293b",
            borderRadius: 6,
            padding: "10px 14px",
            fontSize: 11,
            color: "#475569",
            fontFamily: "'Geist Sans', system-ui, sans-serif",
            fontStyle: "italic",
          }}
        >
          Loading session data...
        </div>
      </section>
    );
  }

  if (!activeSession.active || !activeSession.session) {
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
          Session
        </div>
        <div
          style={{
            background: "#0f172a",
            border: "1px solid #1e293b",
            borderRadius: 6,
            padding: "10px 14px",
            fontSize: 11,
            color: "#475569",
            fontFamily: "'Geist Sans', system-ui, sans-serif",
            fontStyle: "italic",
          }}
        >
          No Active Runtime Session
        </div>
      </section>
    );
  }

  const color = statusColor(status);
  const bg = statusBgColor(status);
  const s = activeSession.session;

  return (
    <>
      <style>{`
        @keyframes session-ping {
          0%   { transform: scale(1); opacity: 0.25; }
          70%  { transform: scale(2.2); opacity: 0; }
          100% { transform: scale(2.2); opacity: 0; }
        }
      `}</style>

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
          Session
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))",
            gap: 8,
          }}
        >
          {/* Active Session ID */}
          <div
            style={{
              background: "#0f172a",
              border: "1px solid #1e293b",
              borderRadius: 6,
              padding: "10px 14px",
            }}
          >
            <Cell
              label="Session ID"
              value={`#${s.id}`}
              mono
              accent="#cbd5e1"
            />
          </div>

          {/* Runtime Duration */}
          <div
            style={{
              background: "#0f172a",
              border: "1px solid #1e293b",
              borderRadius: 6,
              padding: "10px 14px",
            }}
          >
            <Cell
              label="Runtime Duration"
              value={formatUptime(s.duration_seconds || 0)}
              mono
              accent="#7dd3fc"
            />
          </div>

          {/* Live Portfolio Value */}
          <div
            style={{
              background: "#0f172a",
              border: "1px solid #1e293b",
              borderRadius: 6,
              padding: "10px 14px",
            }}
          >
            <Cell
              label="Portfolio Value"
              value={usd(s.portfolio_value || 0)}
              mono
              accent="#cbd5e1"
            />
          </div>

          {/* Total Trades */}
          <div
            style={{
              background: "#0f172a",
              border: "1px solid #1e293b",
              borderRadius: 6,
              padding: "10px 14px",
            }}
          >
            <Cell
              label="Total Trades"
              value={s.total_trades?.toString() || "0"}
              mono
              accent="#cbd5e1"
            />
          </div>

          {/* Realized PnL */}
          <div
            style={{
              background: "#0f172a",
              border: "1px solid #1e293b",
              borderRadius: 6,
              padding: "10px 14px",
            }}
          >
            <Cell
              label="Realized PnL"
              value={
                <span style={{ color: (s.realized_pnl || 0) > 0 ? "#22c55e" : (s.realized_pnl || 0) < 0 ? "#ef4444" : "#cbd5e1" }}>
                  {(s.realized_pnl || 0) >= 0 ? "+" : ""}{usd(s.realized_pnl || 0)}
                </span>
              }
              mono
            />
          </div>

          {/* Session Status */}
          <div
            style={{
              background: bg,
              border: `1px solid ${color}22`,
              borderRadius: 6,
              padding: "10px 14px",
              display: "flex",
              alignItems: "center",
            }}
          >
            <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
              <span
                style={{
                  fontSize: 9,
                  letterSpacing: "0.1em",
                  textTransform: "uppercase",
                  color: "#334155",
                  fontFamily: "'Geist Sans', system-ui, sans-serif",
                }}
              >
                Session Status
              </span>
              <span
                style={{
                  fontSize: 12,
                  fontWeight: 600,
                  color,
                  display: "flex",
                  alignItems: "center",
                  fontFamily: "'Geist Sans', system-ui, sans-serif",
                  letterSpacing: "0.04em",
                }}
              >
                <PulseDot color={color} />
                {status}
              </span>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}

