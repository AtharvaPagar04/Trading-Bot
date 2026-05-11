"use client";

import { useEffect, useState } from "react";

// ─── Types ────────────────────────────────────────────────────────────────────

interface SessionClockProps {
  /** ISO 8601 datetime string from backend */
  startedAt: string;
  /**
   * Backend-reported uptime in seconds.
   * Used ONLY as the SSR/pre-hydration fallback when startedAt cannot be
   * parsed on the server. The live ticker always derives elapsed time from
   * the startedAt wall-clock so the counter is strictly monotonic across
   * page refreshes.
   */
  uptimeSeconds: number;
  /** e.g. "RUNNING" | "PAUSED" | "HALTED" | "ERROR" */
  operatingState: string;
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

function formatStartTime(iso: string): string {
  try {
    const d = new Date(iso);
    if (isNaN(d.getTime())) return "—";
    // Format as "12 May 2026, 02:24:51"
    return d.toLocaleString("en-GB", {
      day: "2-digit",
      month: "short",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: false,
    });
  } catch {
    return "—";
  }
}

function stateColor(state: string): string {
  switch (state.toUpperCase()) {
    case "RUNNING":
      return "#22c55e";
    case "PAUSED":
      return "#f59e0b";
    case "HALTED":
    case "ERROR":
      return "#ef4444";
    default:
      return "#64748b";
  }
}

function stateBgColor(state: string): string {
  switch (state.toUpperCase()) {
    case "RUNNING":
      return "rgba(34,197,94,0.08)";
    case "PAUSED":
      return "rgba(245,158,11,0.08)";
    case "HALTED":
    case "ERROR":
      return "rgba(239,68,68,0.08)";
    default:
      return "rgba(100,116,139,0.08)";
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
        marginRight: 5,
        verticalAlign: "middle",
        flexShrink: 0,
      }}
    >
      {/* outer pulse ring — only for RUNNING */}
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
  value: string;
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

// ─── Uptime derivation ────────────────────────────────────────────────────────

/**
 * Parse startedAt and compute elapsed seconds from the wall clock.
 * Returns null when startedAt is absent or unparseable (SSR safe).
 */
function computeUptimeFromOrigin(startedAt: string): number | null {
  try {
    const origin = new Date(startedAt).getTime();
    if (isNaN(origin)) return null;
    return Math.max(0, Math.floor((Date.now() - origin) / 1000));
  } catch {
    return null;
  }
}

// ─── SessionClock ─────────────────────────────────────────────────────────────

export function SessionClock({
  startedAt,
  uptimeSeconds,
  operatingState,
}: SessionClockProps): React.ReactElement {
  /**
   * Hydration strategy:
   *   - SSR / first render: `mounted` is false → render the server-safe
   *     `uptimeSeconds` value so the HTML matches on both sides.
   *   - After mount: flip `mounted`, start interval, derive uptime purely
   *     from wall-clock so the counter never moves backwards on refresh.
   */
  const [mounted, setMounted] = useState<boolean>(false);
  const [liveUptime, setLiveUptime] = useState<number>(uptimeSeconds);

  useEffect(() => {
    // Mark mounted to unlock client-side display
    setMounted(true);

    // Immediately show the correct wall-clock value before first tick
    const tick = (): void => {
      const derived = computeUptimeFromOrigin(startedAt);
      // Fall back to uptimeSeconds only when startedAt is unresolvable
      setLiveUptime(derived ?? uptimeSeconds);
    };

    tick();
    const id = setInterval(tick, 1000);

    // Cleanup: clear interval on unmount or prop change
    return () => clearInterval(id);
  // Re-run if startedAt changes (new session after restart)
  // uptimeSeconds intentionally omitted — it is only used as fallback inside tick()
  }, [startedAt]); // eslint-disable-line react-hooks/exhaustive-deps

  const color = stateColor(operatingState);
  const bg = stateBgColor(operatingState);

  // SSR: render server snapshot to avoid hydration mismatch.
  // Client: render the wall-clock-derived value.
  const displayUptime = mounted ? formatUptime(liveUptime) : formatUptime(uptimeSeconds);

  return (
    <>
      {/* Keyframe for the ping animation */}
      <style>{`
        @keyframes session-ping {
          0%   { transform: scale(1); opacity: 0.25; }
          70%  { transform: scale(2.2); opacity: 0; }
          100% { transform: scale(2.2); opacity: 0; }
        }
      `}</style>

      {/* Section header — matches existing dashboard visual language */}
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

        {/* Card */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))",
            gap: 8,
          }}
        >
          {/* Session Start */}
          <div
            style={{
              background: "#0f172a",
              border: "1px solid #1e293b",
              borderRadius: 6,
              padding: "10px 14px",
            }}
          >
            <Cell
              label="Session Start"
              value={formatStartTime(startedAt)}
              mono
              accent="#cbd5e1"
            />
          </div>

          {/* Live Uptime */}
          <div
            style={{
              background: "#0f172a",
              border: "1px solid #1e293b",
              borderRadius: 6,
              padding: "10px 14px",
            }}
          >
            <Cell
              label="Live Uptime"
              value={displayUptime}
              mono
              accent="#7dd3fc"
            />
          </div>

          {/* Runtime State */}
          <div
            style={{
              background: bg,
              border: `1px solid ${color}22`,
              borderRadius: 6,
              padding: "10px 14px",
              display: "flex",
              alignItems: "center",
              gap: 0,
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
                Runtime State
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
                {operatingState}
              </span>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}

// ─── Fallback ─────────────────────────────────────────────────────────────────

export function SessionClockUnavailable(): React.ReactElement {
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
        Session unavailable
      </div>
    </section>
  );
}
