"use client";

import { useEffect, useRef, useState } from "react";
import { fetchSessionById } from "../../services/api";
import type { SessionRecord } from "../../services/api";

// ─── Utility formatters ───────────────────────────────────────────────────────

function usd(n: number | null | undefined): string {
  if (n == null) return "—";
  return n.toLocaleString("en-US", { style: "currency", currency: "USD" });
}

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
      second: "2-digit",
      hour12: false,
    });
  } catch {
    return "—";
  }
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
  if (n == null) return "#94a3b8";
  return n > 0 ? "#22c55e" : n < 0 ? "#ef4444" : "#94a3b8";
}

// ─── Components ─────────────────────────────────────────────────────────────

function Skeleton({ w = "100%", h = 14 }: { w?: string | number; h?: number }): React.ReactElement {
  return (
    <>
      <style>{`
        @keyframes sdm-shimmer {
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
          animation: "sdm-shimmer 1.6s ease-in-out infinite",
        }}
      />
    </>
  );
}

function DetailCard({
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
      }}
    >
      <span
        style={{
          fontSize: 10,
          letterSpacing: "0.1em",
          textTransform: "uppercase",
          color: "#475569",
          fontWeight: 600,
        }}
      >
        {label}
      </span>
      {loading ? (
        <Skeleton h={18} />
      ) : (
        <span
          style={{
            fontSize: 15,
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
}) {
  return (
    <span
      style={{
        display: "inline-block",
        fontSize: 10,
        fontWeight: 700,
        letterSpacing: "0.1em",
        textTransform: "uppercase",
        color,
        background: bg,
        border: `1px solid ${border}`,
        borderRadius: 4,
        padding: "3px 8px",
        fontFamily: "'Geist Sans', system-ui, sans-serif",
      }}
    >
      {label}
    </span>
  );
}

// ─── Modal Component ──────────────────────────────────────────────────────────

export interface SessionDetailsModalProps {
  open: boolean;
  sessionId: number | null;
  onClose: () => void;
}

export function SessionDetailsModal({
  open,
  sessionId,
  onClose,
}: SessionDetailsModalProps): React.ReactElement | null {
  const [session, setSession] = useState<SessionRecord | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const mountedRef = useRef(true);
  const abortRef = useRef<AbortController | null>(null);

  useEffect(() => {
    mountedRef.current = true;
    return () => { mountedRef.current = false; };
  }, []);

  useEffect(() => {
    if (!open || sessionId === null) return;

    abortRef.current?.abort();
    const controller = new AbortController();
    abortRef.current = controller;

    setTimeout(() => {
      setLoading(true);
      setError(null);
      setSession(null);
    }, 0);

    fetchSessionById(sessionId, controller.signal)
      .then((data) => {
        if (!mountedRef.current) return;
        setSession(data);
        setLoading(false);
      })
      .catch((err) => {
        if (!mountedRef.current) return;
        if (err.name === "AbortError") return;
        setError(err.message || "Failed to load session details.");
        setLoading(false);
      });

    return () => {
      abortRef.current?.abort();
    };
  }, [open, sessionId]);

  // Animation handling
  const [visible, setVisible] = useState(false);
  const [rendered, setRendered] = useState(false);

  useEffect(() => {
    if (open) {
      setTimeout(() => setRendered(true), 0);
      requestAnimationFrame(() => {
        requestAnimationFrame(() => setVisible(true));
      });
    } else {
      setTimeout(() => setVisible(false), 0);
      const id = setTimeout(() => setRendered(false), 320);
      return () => clearTimeout(id);
    }
  }, [open]);

  // ESC handling
  useEffect(() => {
    if (!open) return;
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [open, onClose]);

  // Body scroll lock
  useEffect(() => {
    if (open) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => { document.body.style.overflow = ""; };
  }, [open]);

  if (!rendered) return null;

  const isCompleted = session?.ended_at != null;

  return (
    <>
      {/* Backdrop */}
      <div
        onClick={onClose}
        style={{
          position: "fixed",
          inset: 0,
          zIndex: 2000,
          background: "rgba(2,8,20,0.75)",
          backdropFilter: visible ? "blur(8px)" : "blur(0px)",
          opacity: visible ? 1 : 0,
          transition: "opacity 0.3s ease, backdrop-filter 0.3s ease",
        }}
      />

      {/* Modal Container */}
      <div
        role="dialog"
        aria-modal="true"
        style={{
          position: "fixed",
          inset: 0,
          zIndex: 2001,
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
            maxWidth: 640,
            background: "rgba(8,15,30,0.96)",
            border: "1px solid rgba(30,41,59,0.9)",
            borderRadius: 14,
            boxShadow:
              "0 0 0 1px rgba(167,139,250,0.06), 0 32px 80px rgba(0,0,0,0.7)",
            opacity: visible ? 1 : 0,
            transform: visible ? "translateY(0) scale(1)" : "translateY(20px) scale(0.97)",
            transition: "opacity 0.32s cubic-bezier(0.22,1,0.36,1), transform 0.32s cubic-bezier(0.22,1,0.36,1)",
            overflow: "hidden",
            display: "flex",
            flexDirection: "column",
          }}
        >
          {/* Header */}
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              padding: "18px 22px",
              background: "rgba(8,15,30,0.98)",
              borderBottom: "1px solid #1a2d45",
            }}
          >
            <div>
              <h2
                style={{
                  margin: 0,
                  fontSize: 16,
                  fontWeight: 700,
                  color: "#e2e8f0",
                  fontFamily: "'Geist Sans', system-ui, sans-serif",
                }}
              >
                Session Details
              </h2>
              <div
                style={{
                  fontSize: 11,
                  color: "#475569",
                  marginTop: 2,
                  fontFamily: "'Geist Mono', monospace",
                }}
              >
                {sessionId != null ? `Session #${sessionId}` : "Loading..."}
              </div>
            </div>

            <button
              onClick={onClose}
              style={{
                width: 28,
                height: 28,
                borderRadius: 6,
                border: "1px solid #1e293b",
                background: "transparent",
                color: "#475569",
                cursor: "pointer",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                transition: "color 0.15s, background 0.15s",
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.color = "#e2e8f0";
                e.currentTarget.style.background = "rgba(30,41,59,0.8)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.color = "#475569";
                e.currentTarget.style.background = "transparent";
              }}
            >
              ✕
            </button>
          </div>

          {/* Body */}
          <div style={{ padding: "24px 22px" }}>
            {error ? (
              <div
                style={{
                  color: "#ef4444",
                  fontSize: 13,
                  textAlign: "center",
                  padding: "40px 0",
                }}
              >
                {error}
              </div>
            ) : (
              <>
                {/* Badges Row */}
                <div style={{ display: "flex", gap: 12, marginBottom: 24 }}>
                  {loading ? (
                    <Skeleton w={80} h={24} />
                  ) : (
                    <>
                      {isCompleted ? (
                        <Badge
                          label="COMPLETED"
                          color="#64748b"
                          bg="rgba(100,116,139,0.06)"
                          border="rgba(100,116,139,0.18)"
                        />
                      ) : (
                        <Badge
                          label="ACTIVE"
                          color="#22c55e"
                          bg="rgba(34,197,94,0.08)"
                          border="rgba(34,197,94,0.25)"
                        />
                      )}
                      {session?.safe_mode_triggered && (
                        <Badge
                          label="SAFE MODE"
                          color="#f59e0b"
                          bg="rgba(245,158,11,0.08)"
                          border="rgba(245,158,11,0.22)"
                        />
                      )}
                    </>
                  )}
                </div>

                {/* Grid */}
                <div
                  style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(2, 1fr)",
                    gap: 12,
                  }}
                >
                  <DetailCard
                    label="Started At"
                    value={fmtDate(session?.started_at ?? null)}
                    loading={loading}
                  />
                  <DetailCard
                    label="Ended At"
                    value={
                      !loading && !isCompleted
                        ? "Running..."
                        : fmtDate(session?.ended_at ?? null)
                    }
                    loading={loading}
                    valueColor={!loading && !isCompleted ? "#22c55e" : undefined}
                  />
                  <DetailCard
                    label="Duration"
                    value={dur(session?.duration_seconds)}
                    loading={loading}
                  />
                  <DetailCard
                    label="Total Trades"
                    value={session?.total_trades ?? 0}
                    loading={loading}
                  />
                  <DetailCard
                    label="Realized P&L"
                    value={usd(session?.realized_pnl)}
                    loading={loading}
                    valueColor={pnlColor(session?.realized_pnl)}
                  />
                  <DetailCard
                    label="Portfolio Value"
                    value={session?.portfolio_value ? usd(session.portfolio_value) : "—"}
                    loading={loading}
                  />
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
