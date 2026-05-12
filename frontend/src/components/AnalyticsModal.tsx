"use client";

import {
  useCallback,
  useEffect,
  useRef,
  useState,
} from "react";
import { fetchOverallAnalytics } from "../../services/api";
import type {
  SessionAnalytics,
  TradeAnalytics,
} from "../../services/api";

// ─── Constants ────────────────────────────────────────────────────────────────

const POLL_INTERVAL_MS = 30_000; // refresh every 30 s
const FETCH_TIMEOUT_MS = 8_000;

// ─── Utility formatters ───────────────────────────────────────────────────────

function usd(n: number | null | undefined): string {
  if (n == null) return "—";
  return n.toLocaleString("en-US", { style: "currency", currency: "USD" });
}

function pct(n: number | null | undefined, decimals = 1): string {
  if (n == null) return "—";
  return `${n.toFixed(decimals)}%`;
}

function dur(seconds: number | null | undefined): string {
  if (seconds == null) return "—";
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = Math.floor(seconds % 60);
  if (h > 0) return `${h}h ${m}m`;
  if (m > 0) return `${m}m ${s}s`;
  return `${s}s`;
}

function pnlColor(n: number | null | undefined): string {
  if (n == null) return "#94a3b8";
  return n > 0 ? "#22c55e" : n < 0 ? "#ef4444" : "#94a3b8";
}

// ─── Skeleton ─────────────────────────────────────────────────────────────────

function Skeleton({ w = "100%", h = 14 }: { w?: string | number; h?: number }): React.ReactElement {
  return (
    <>
      <style>{`
        @keyframes am-shimmer {
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
          animation: "am-shimmer 1.6s ease-in-out infinite",
        }}
      />
    </>
  );
}

// ─── Metric card ─────────────────────────────────────────────────────────────

interface MetricProps {
  label: string;
  value: string | React.ReactNode;
  sub?: string;
  highlight?: boolean;
  loading?: boolean;
  valueColor?: string;
}

function Metric({
  label,
  value,
  sub,
  highlight = false,
  loading = false,
  valueColor,
}: MetricProps): React.ReactElement {
  const [hovered, setHovered] = useState(false);

  return (
    <div
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{
        padding: "14px 16px",
        background: hovered
          ? "rgba(30,41,59,0.8)"
          : highlight
          ? "rgba(167,139,250,0.04)"
          : "rgba(15,23,42,0.6)",
        border: `1px solid ${highlight ? "rgba(167,139,250,0.18)" : hovered ? "rgba(56,189,248,0.18)" : "#1a2d45"}`,
        borderRadius: 8,
        backdropFilter: "blur(8px)",
        transition: "background 0.2s, border-color 0.2s, transform 0.15s",
        transform: hovered ? "translateY(-1px)" : "none",
        position: "relative",
        overflow: "hidden",
      }}
    >
      {highlight && (
        <span
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            height: 2,
            background: "linear-gradient(90deg, transparent, rgba(167,139,250,0.5), transparent)",
          }}
        />
      )}
      <div
        style={{
          fontSize: 9,
          letterSpacing: "0.1em",
          textTransform: "uppercase",
          color: "#475569",
          marginBottom: 8,
          fontWeight: 600,
        }}
      >
        {label}
      </div>
      {loading ? (
        <Skeleton h={18} />
      ) : (
        <div
          style={{
            fontSize: 15,
            fontWeight: 700,
            color: valueColor ?? "#e2e8f0",
            letterSpacing: "-0.01em",
            fontVariantNumeric: "tabular-nums",
          }}
        >
          {value}
        </div>
      )}
      {sub && !loading && (
        <div
          style={{
            fontSize: 10,
            color: "#334155",
            marginTop: 4,
          }}
        >
          {sub}
        </div>
      )}
    </div>
  );
}

// ─── Section header ───────────────────────────────────────────────────────────

function AnalyticsSection({
  title,
  icon,
  children,
}: {
  title: string;
  icon: string;
  children: React.ReactNode;
}): React.ReactElement {
  return (
    <div style={{ marginBottom: 28 }}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 8,
          marginBottom: 14,
          paddingBottom: 10,
          borderBottom: "1px solid #1a2d45",
        }}
      >
        <span style={{ fontSize: 14 }}>{icon}</span>
        <span
          style={{
            fontSize: 11,
            fontWeight: 700,
            letterSpacing: "0.08em",
            textTransform: "uppercase",
            color: "#94a3b8",
          }}
        >
          {title}
        </span>
      </div>
      {children}
    </div>
  );
}

// ─── Error state ─────────────────────────────────────────────────────────────

function ErrorState({ message, onRetry }: { message: string; onRetry: () => void }): React.ReactElement {
  const [hovered, setHovered] = useState(false);
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 12,
        padding: "32px 16px",
        textAlign: "center",
      }}
    >
      <span style={{ fontSize: 28 }}>⚡</span>
      <div style={{ fontSize: 12, color: "#ef4444", fontWeight: 600, letterSpacing: "0.05em" }}>
        Backend Offline
      </div>
      <div style={{ fontSize: 11, color: "#475569", maxWidth: 260, lineHeight: 1.6 }}>
        {message}
      </div>
      <button
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        onClick={onRetry}
        style={{
          marginTop: 4,
          padding: "7px 18px",
          fontSize: 10,
          fontWeight: 600,
          letterSpacing: "0.08em",
          textTransform: "uppercase",
          color: hovered ? "#e2e8f0" : "#64748b",
          background: hovered ? "rgba(30,41,59,0.8)" : "transparent",
          border: `1px solid ${hovered ? "#334155" : "#1e293b"}`,
          borderRadius: 5,
          cursor: "pointer",
          transition: "color 0.15s, background 0.15s, border-color 0.15s",
          outline: "none",
        }}
      >
        Retry
      </button>
    </div>
  );
}

// ─── Session analytics panel ──────────────────────────────────────────────────

function SessionPanel({
  data,
  loading,
}: {
  data: SessionAnalytics | null;
  loading: boolean;
}): React.ReactElement {
  return (
    <AnalyticsSection title="Session Analytics" icon="📊">
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, 1fr)",
          gap: 10,
        }}
      >
        <Metric
          label="Total Sessions"
          value={data?.total_sessions ?? "—"}
          loading={loading}
        />
        <Metric
          label="Profitable Sessions"
          value={data?.profitable_sessions ?? "—"}
          loading={loading}
          valueColor={data ? pnlColor(data.profitable_sessions - data.losing_sessions) : undefined}
        />
        <Metric
          label="Losing Sessions"
          value={data?.losing_sessions ?? "—"}
          loading={loading}
          valueColor={data && data.losing_sessions > 0 ? "#ef4444" : undefined}
        />
        <Metric
          label="Safe Mode Sessions"
          value={data?.safe_mode_sessions ?? "—"}
          loading={loading}
          valueColor={data && data.safe_mode_sessions > 0 ? "#a78bfa" : undefined}
        />
        <Metric
          label="Win Rate"
          value={pct(data?.win_rate)}
          loading={loading}
          highlight
          valueColor={
            data == null ? undefined
            : data.win_rate >= 60 ? "#22c55e"
            : data.win_rate >= 40 ? "#f59e0b"
            : "#ef4444"
          }
        />
        <Metric
          label="Total Realized P&L"
          value={usd(data?.total_realized_pnl)}
          loading={loading}
          highlight
          valueColor={data ? pnlColor(data.total_realized_pnl) : undefined}
        />
        <Metric
          label="Avg Session Duration"
          value={dur(data?.average_session_duration)}
          loading={loading}
          sub={data?.average_session_duration != null ? "per session" : undefined}
        />
        <Metric
          label="Best Session P&L"
          value={usd(data?.best_session_pnl)}
          loading={loading}
          highlight
          valueColor={data ? pnlColor(data.best_session_pnl) : undefined}
        />
        <Metric
          label="Worst Session P&L"
          value={usd(data?.worst_session_pnl)}
          loading={loading}
          highlight
          valueColor={data ? pnlColor(data.worst_session_pnl) : undefined}
        />
      </div>
    </AnalyticsSection>
  );
}

// ─── Trade analytics panel ────────────────────────────────────────────────────

function TradePanel({
  data,
  loading,
}: {
  data: TradeAnalytics | null;
  loading: boolean;
}): React.ReactElement {
  return (
    <AnalyticsSection title="Trade Analytics" icon="💹">
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 10,
        }}
      >
        <Metric
          label="Total Trades"
          value={data?.total_trades ?? "—"}
          loading={loading}
        />
        <Metric
          label="Winning Trades"
          value={data?.winning_trades ?? "—"}
          loading={loading}
          valueColor={data && data.winning_trades > 0 ? "#22c55e" : undefined}
        />
        <Metric
          label="Losing Trades"
          value={data?.losing_trades ?? "—"}
          loading={loading}
          valueColor={data && data.losing_trades > 0 ? "#ef4444" : undefined}
        />
        <Metric
          label="Win Rate"
          value={pct(data?.win_rate)}
          loading={loading}
          highlight
          valueColor={
            data == null ? undefined
            : data.win_rate >= 60 ? "#22c55e"
            : data.win_rate >= 40 ? "#f59e0b"
            : "#ef4444"
          }
        />
        <Metric
          label="Total Realized P&L"
          value={usd(data?.total_realized_pnl)}
          loading={loading}
          highlight
          valueColor={data ? pnlColor(data.total_realized_pnl) : undefined}
        />
        <Metric
          label="Avg Trade P&L"
          value={usd(data?.avg_trade_pnl)}
          loading={loading}
          valueColor={data ? pnlColor(data.avg_trade_pnl) : undefined}
        />
        <Metric
          label="Best Trade P&L"
          value={usd(data?.best_trade_pnl)}
          loading={loading}
          highlight
          valueColor={data ? pnlColor(data.best_trade_pnl) : undefined}
        />
        <Metric
          label="Worst Trade P&L"
          value={usd(data?.worst_trade_pnl)}
          loading={loading}
          highlight
          valueColor={data ? pnlColor(data.worst_trade_pnl) : undefined}
        />
      </div>
    </AnalyticsSection>
  );
}

// ─── Hook: analytics data ─────────────────────────────────────────────────────

type FetchState = "idle" | "loading" | "success" | "error";

interface AnalyticsState {
  sessionData: SessionAnalytics | null;
  tradeData: TradeAnalytics | null;
  fetchState: FetchState;
  errorMessage: string;
  lastFetched: Date | null;
}

function useAnalytics(open: boolean): AnalyticsState & { refresh: () => void } {
  const [state, setState] = useState<AnalyticsState>({
    sessionData: null,
    tradeData: null,
    fetchState: "idle",
    errorMessage: "",
    lastFetched: null,
  });

  const mountedRef = useRef(true);
  const timerRef = useRef<NodeJS.Timeout | null>(null);
  const abortRef = useRef<AbortController | null>(null);

  const fetchAll = useCallback(async (): Promise<void> => {
    if (!mountedRef.current) return;

    // Cancel any in-flight request
    abortRef.current?.abort();
    const controller = new AbortController();
    abortRef.current = controller;

    const timeoutId = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);

    setState((prev) => ({ ...prev, fetchState: "loading" }));

    try {
      const data = await fetchOverallAnalytics(controller.signal);

      if (!mountedRef.current) return;

      setState({
        sessionData: data,
        tradeData: null as unknown as TradeAnalytics,
        fetchState: "success",
        errorMessage: "",
        lastFetched: new Date(),
      });
    } catch (err) {
      if (!mountedRef.current) return;
      if (err instanceof Error && err.name === "AbortError") return;

      setState((prev) => ({
        ...prev,
        fetchState: "error",
        errorMessage:
          err instanceof Error
            ? err.message
            : "Failed to reach analytics endpoints.",
      }));
    } finally {
      clearTimeout(timeoutId);
    }
  }, []);

  // Start / stop polling based on open state
  useEffect(() => {
    mountedRef.current = true;

    if (!open) {
      // Clean up when modal closes
      abortRef.current?.abort();
      if (timerRef.current) clearTimeout(timerRef.current);
      return;
    }

    async function poll(): Promise<void> {
      await fetchAll();
      if (mountedRef.current && open) {
        timerRef.current = setTimeout(poll, POLL_INTERVAL_MS);
      }
    }

    void poll();

    return () => {
      mountedRef.current = false;
      abortRef.current?.abort();
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [open, fetchAll]);

  return { ...state, refresh: fetchAll };
}

// ─── AnalyticsModal ───────────────────────────────────────────────────────────

export interface AnalyticsModalProps {
  /** Whether the modal is currently open */
  open: boolean;
  /** Called when the user requests close (ESC, backdrop, ✕) */
  onClose: () => void;
}

export function AnalyticsModal({
  open,
  onClose,
}: AnalyticsModalProps): React.ReactElement | null {
  const { sessionData, tradeData, fetchState, errorMessage, lastFetched, refresh } =
    useAnalytics(open);

  // ── Visibility & animation ─────────────────────────────────────────────────

  // We keep the element in DOM during the exit animation
  const [visible, setVisible] = useState(false);
  const [rendered, setRendered] = useState(false);

  useEffect(() => {
    if (open) {
      setTimeout(() => setRendered(true), 0);
      // tiny delay so CSS transition fires
      requestAnimationFrame(() => {
        requestAnimationFrame(() => setVisible(true));
      });
    } else {
      setTimeout(() => setVisible(false), 0);
      const id = setTimeout(() => setRendered(false), 320);
      return () => clearTimeout(id);
    }
  }, [open]);

  // ── ESC key close ──────────────────────────────────────────────────────────

  useEffect(() => {
    if (!open) return;

    function onKeyDown(e: KeyboardEvent): void {
      if (e.key === "Escape") onClose();
    }

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [open, onClose]);

  // ── Body scroll lock ───────────────────────────────────────────────────────

  useEffect(() => {
    if (open) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => { document.body.style.overflow = ""; };
  }, [open]);

  if (!rendered) return null;

  const isLoading = fetchState === "idle" || fetchState === "loading";
  const isError = fetchState === "error";

  return (
    <>
      {/* ── keyframes ── */}
      <style>{`
        @keyframes am-fade-in {
          from { opacity: 0; }
          to   { opacity: 1; }
        }
        @keyframes am-slide-up {
          from { opacity: 0; transform: translateY(24px) scale(0.98); }
          to   { opacity: 1; transform: translateY(0)    scale(1);    }
        }
        @keyframes am-pulse-dot {
          0%, 100% { opacity: 1; }
          50%       { opacity: 0.4; }
        }
      `}</style>

      {/* ── Backdrop ── */}
      <div
        id="analytics-modal-backdrop"
        aria-hidden="true"
        onClick={onClose}
        style={{
          position: "fixed",
          inset: 0,
          zIndex: 1000,
          background: "rgba(2,8,20,0.75)",
          backdropFilter: visible ? "blur(8px)" : "blur(0px)",
          WebkitBackdropFilter: visible ? "blur(8px)" : "blur(0px)",
          opacity: visible ? 1 : 0,
          transition: "opacity 0.3s ease, backdrop-filter 0.3s ease",
        }}
      />

      {/* ── Modal panel ── */}
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby="analytics-modal-title"
        id="analytics-modal"
        style={{
          position: "fixed",
          inset: 0,
          zIndex: 1001,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          padding: "16px",
          pointerEvents: "none",
        }}
      >
        <div
          onClick={(e) => e.stopPropagation()}
          style={{
            pointerEvents: "auto",
            width: "100%",
            maxWidth: 820,
            maxHeight: "90vh",
            overflowY: "auto",
            background: "rgba(8,15,30,0.96)",
            border: "1px solid rgba(30,41,59,0.9)",
            borderRadius: 14,
            boxShadow:
              "0 0 0 1px rgba(167,139,250,0.06), 0 32px 80px rgba(0,0,0,0.7), 0 0 60px rgba(56,189,248,0.04)",
            opacity: visible ? 1 : 0,
            transform: visible ? "translateY(0) scale(1)" : "translateY(20px) scale(0.97)",
            transition: "opacity 0.32s cubic-bezier(0.22,1,0.36,1), transform 0.32s cubic-bezier(0.22,1,0.36,1)",
            scrollbarWidth: "thin",
            scrollbarColor: "#1e293b transparent",
          }}
        >
          {/* ── Modal header ── */}
          <div
            style={{
              position: "sticky",
              top: 0,
              zIndex: 10,
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              padding: "18px 22px 16px",
              background: "rgba(8,15,30,0.98)",
              borderBottom: "1px solid #1a2d45",
              backdropFilter: "blur(16px)",
            }}
          >
            <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <div
                style={{
                  width: 32,
                  height: 32,
                  borderRadius: 8,
                  background: "rgba(167,139,250,0.1)",
                  border: "1px solid rgba(167,139,250,0.2)",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: 15,
                }}
              >
                📈
              </div>
              <div>
                <h2
                  id="analytics-modal-title"
                  style={{
                    margin: 0,
                    fontSize: 14,
                    fontWeight: 700,
                    color: "#e2e8f0",
                    letterSpacing: "-0.01em",
                    fontFamily: "'Geist Sans', system-ui, sans-serif",
                  }}
                >
                  Analytics
                </h2>
                <div
                  style={{
                    fontSize: 10,
                    color: "#334155",
                    marginTop: 1,
                    fontFamily: "'Geist Sans', system-ui, sans-serif",
                  }}
                >
                  Historical runtime &amp; trade intelligence
                </div>
              </div>
            </div>

            {/* Right side: last updated + close */}
            <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
              {fetchState === "success" && lastFetched && (
                <div style={{ display: "flex", alignItems: "center", gap: 5 }}>
                  <span
                    style={{
                      width: 5,
                      height: 5,
                      borderRadius: "50%",
                      background: "#22c55e",
                      display: "inline-block",
                      animation: "am-pulse-dot 2.5s ease-in-out infinite",
                    }}
                  />
                  <span
                    style={{
                      fontSize: 9,
                      color: "#334155",
                      letterSpacing: "0.06em",
                      fontFamily: "monospace",
                    }}
                  >
                    {lastFetched.toLocaleTimeString([], {
                      hour: "2-digit",
                      minute: "2-digit",
                      second: "2-digit",
                    })}
                  </span>
                </div>
              )}

              <button
                id="analytics-modal-close"
                aria-label="Close analytics modal"
                onClick={onClose}
                style={{
                  width: 28,
                  height: 28,
                  borderRadius: 6,
                  border: "1px solid #1e293b",
                  background: "transparent",
                  color: "#475569",
                  cursor: "pointer",
                  fontSize: 14,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  outline: "none",
                  transition: "color 0.15s, background 0.15s, border-color 0.15s",
                  lineHeight: 1,
                }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLButtonElement).style.color = "#e2e8f0";
                  (e.currentTarget as HTMLButtonElement).style.background = "rgba(30,41,59,0.8)";
                  (e.currentTarget as HTMLButtonElement).style.borderColor = "#334155";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLButtonElement).style.color = "#475569";
                  (e.currentTarget as HTMLButtonElement).style.background = "transparent";
                  (e.currentTarget as HTMLButtonElement).style.borderColor = "#1e293b";
                }}
              >
                ✕
              </button>
            </div>
          </div>

          {/* ── Modal body ── */}
          <div style={{ padding: "22px 22px 24px" }}>
            {isError ? (
              <ErrorState message={errorMessage} onRetry={refresh} />
            ) : (
              <>
                <SessionPanel data={sessionData} loading={isLoading} />
                <TradePanel data={tradeData} loading={isLoading} />
              </>
            )}
          </div>
        </div>
      </div>
    </>
  );
}

// ─── Analytics trigger button ─────────────────────────────────────────────────

export interface AnalyticsButtonProps {
  onClick: () => void;
}

export function AnalyticsButton({ onClick }: AnalyticsButtonProps): React.ReactElement {
  const [hovered, setHovered] = useState(false);

  return (
    <button
      id="analytics-open-button"
      aria-label="Open analytics"
      onClick={onClick}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 5,
        padding: "6px 14px",
        fontSize: 10,
        fontFamily: "'Geist Sans', system-ui, sans-serif",
        fontWeight: 600,
        letterSpacing: "0.08em",
        textTransform: "uppercase",
        color: hovered ? "#c4b5fd" : "#a78bfa",
        background: hovered ? "rgba(167,139,250,0.12)" : "rgba(167,139,250,0.05)",
        border: `1px solid ${hovered ? "rgba(167,139,250,0.35)" : "rgba(167,139,250,0.18)"}`,
        borderRadius: 4,
        cursor: "pointer",
        outline: "none",
        transition: "color 0.15s, background 0.15s, border-color 0.15s",
        whiteSpace: "nowrap",
      }}
    >
      <span style={{ fontSize: 11 }}>📈</span>
      Analytics
    </button>
  );
}
