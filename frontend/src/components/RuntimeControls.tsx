"use client";

import { useCallback, useState } from "react";
import {
  startRuntime,
  stopRuntime,
  pauseRuntime,
  resumeRuntime,
  toggleSafeMode,
} from "../../services/api";

// ─── Types ────────────────────────────────────────────────────────────────────

export interface RuntimeControlsProps {
  /** Current operating state from backend: "RUNNING" | "PAUSED" | "HALTED" | "ERROR" | "STOPPED" | "UNKNOWN" */
  operatingState: string;
  /** Whether safe mode is currently active */
  safeModeActive: boolean;
}

type ButtonId = "start" | "stop" | "pause" | "resume" | "safeMode";
type FeedbackKind = "success" | "error";

interface ButtonFeedback {
  kind: FeedbackKind;
  message: string;
}

interface ButtonState {
  loading: boolean;
  feedback: ButtonFeedback | null;
}

type ControlState = Record<ButtonId, ButtonState>;

// ─── Helpers ──────────────────────────────────────────────────────────────────

const INITIAL_STATE: ControlState = {
  start:    { loading: false, feedback: null },
  stop:     { loading: false, feedback: null },
  pause:    { loading: false, feedback: null },
  resume:   { loading: false, feedback: null },
  safeMode: { loading: false, feedback: null },
};

/** Milliseconds to show success/error feedback before clearing. */
const FEEDBACK_TTL_MS = 2400;

// ─── Sub-components ───────────────────────────────────────────────────────────

/** Tiny spinner made from pure CSS — no dependencies. */
function Spinner(): React.ReactElement {
  return (
    <>
      <style>{`
        @keyframes ctrl-spin {
          to { transform: rotate(360deg); }
        }
      `}</style>
      <span
        style={{
          display: "inline-block",
          width: 10,
          height: 10,
          border: "1.5px solid currentColor",
          borderTopColor: "transparent",
          borderRadius: "50%",
          animation: "ctrl-spin 0.6s linear infinite",
          marginRight: 5,
          verticalAlign: "middle",
          flexShrink: 0,
        }}
      />
    </>
  );
}

/** Status pill shown in the header bar. */
function StatusPill({
  label,
  active,
  activeColor,
  activeBg,
}: {
  label: string;
  active: boolean;
  activeColor: string;
  activeBg: string;
}): React.ReactElement {
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 5,
        fontSize: 9,
        letterSpacing: "0.08em",
        textTransform: "uppercase",
        fontWeight: 600,
        padding: "2px 7px",
        borderRadius: 3,
        color: active ? activeColor : "#334155",
        background: active ? activeBg : "transparent",
        border: `1px solid ${active ? activeColor + "33" : "#1e293b"}`,
        transition: "color 0.2s, background 0.2s, border-color 0.2s",
      }}
    >
      <span
        style={{
          width: 5,
          height: 5,
          borderRadius: "50%",
          background: active ? activeColor : "#1e293b",
          display: "inline-block",
          flexShrink: 0,
          transition: "background 0.2s",
        }}
      />
      {label}
    </span>
  );
}

// ─── Control button ───────────────────────────────────────────────────────────

interface CtrlButtonProps {
  id: ButtonId;
  label: string;
  state: ButtonState;
  disabled: boolean;
  variant: "neutral" | "green" | "red" | "amber" | "sky" | "violet";
  onClick: (id: ButtonId) => void;
}

const VARIANT_COLORS: Record<
  CtrlButtonProps["variant"],
  { fg: string; border: string; hoverBg: string; activeFg: string }
> = {
  neutral: { fg: "#64748b", border: "#1e293b",      hoverBg: "rgba(100,116,139,0.08)", activeFg: "#94a3b8" },
  green:   { fg: "#22c55e", border: "#22c55e33",    hoverBg: "rgba(34,197,94,0.10)",   activeFg: "#4ade80" },
  red:     { fg: "#ef4444", border: "#ef444433",    hoverBg: "rgba(239,68,68,0.10)",   activeFg: "#f87171" },
  amber:   { fg: "#f59e0b", border: "#f59e0b33",    hoverBg: "rgba(245,158,11,0.10)",  activeFg: "#fbbf24" },
  sky:     { fg: "#38bdf8", border: "#38bdf833",    hoverBg: "rgba(56,189,248,0.10)",  activeFg: "#7dd3fc" },
  violet:  { fg: "#a78bfa", border: "#a78bfa33",    hoverBg: "rgba(167,139,250,0.10)", activeFg: "#c4b5fd" },
};

function CtrlButton({
  id,
  label,
  state,
  disabled,
  variant,
  onClick,
}: CtrlButtonProps): React.ReactElement {
  const [hovered, setHovered] = useState(false);
  const col = VARIANT_COLORS[variant];

  const isDisabled = disabled || state.loading;
  const feedback = state.feedback;

  const fg =
    feedback?.kind === "success" ? "#22c55e"
    : feedback?.kind === "error"   ? "#ef4444"
    : isDisabled                   ? "#1e293b"
    : hovered                      ? col.activeFg
    : col.fg;

  const border =
    feedback?.kind === "success" ? "#22c55e55"
    : feedback?.kind === "error"   ? "#ef444455"
    : isDisabled                   ? "#0f172a"
    : hovered                      ? col.border
    : "#1e293b";

  const bg =
    feedback?.kind === "success" ? "rgba(34,197,94,0.08)"
    : feedback?.kind === "error"   ? "rgba(239,68,68,0.08)"
    : hovered && !isDisabled       ? col.hoverBg
    : "#0a111e";

  return (
    <button
      disabled={isDisabled}
      onClick={() => onClick(id)}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        gap: 4,
        padding: "6px 14px",
        fontSize: 10,
        fontFamily: "'Geist Sans', system-ui, sans-serif",
        fontWeight: 600,
        letterSpacing: "0.08em",
        textTransform: "uppercase",
        color: fg,
        background: bg,
        border: `1px solid ${border}`,
        borderRadius: 4,
        cursor: isDisabled ? "not-allowed" : "pointer",
        opacity: isDisabled && !feedback ? 0.35 : 1,
        transition: "color 0.15s, background 0.15s, border-color 0.15s, opacity 0.15s",
        minWidth: 78,
        whiteSpace: "nowrap",
        outline: "none",
      }}
    >
      {state.loading && <Spinner />}
      {feedback?.kind === "success" && !state.loading && (
        <span style={{ marginRight: 4, fontSize: 10 }}>✓</span>
      )}
      {feedback?.kind === "error" && !state.loading && (
        <span style={{ marginRight: 4, fontSize: 10 }}>✕</span>
      )}
      {feedback ? feedback.message : label}
    </button>
  );
}

// ─── RuntimeControls ──────────────────────────────────────────────────────────

export function RuntimeControls({
  operatingState,
  safeModeActive,
}: RuntimeControlsProps): React.ReactElement {
  const [ctrlState, setCtrlState] = useState<ControlState>(INITIAL_STATE);

  // ── helpers ──────────────────────────────────────────────────────────────

  function setLoading(id: ButtonId, loading: boolean): void {
    setCtrlState((prev) => ({
      ...prev,
      [id]: { ...prev[id], loading },
    }));
  }

  function setFeedback(id: ButtonId, feedback: ButtonFeedback | null): void {
    setCtrlState((prev) => ({
      ...prev,
      [id]: { ...prev[id], feedback },
    }));
  }

  /** Run an async control action with loading / feedback lifecycle. */
  const runAction = useCallback(
    async (id: ButtonId, action: () => Promise<unknown>): Promise<void> => {
      // Guard: prevent duplicate clicks
      if (ctrlState[id].loading) return;

      setLoading(id, true);
      setFeedback(id, null);

      try {
        await action();
        setFeedback(id, { kind: "success", message: "OK" });
      } catch (err) {
        const msg =
          err instanceof Error ? err.message.slice(0, 24) : "Error";
        console.error(`[RuntimeControls] ${id} failed:`, err);
        setFeedback(id, { kind: "error", message: msg });
      } finally {
        setLoading(id, false);
        // Auto-clear feedback after TTL
        setTimeout(() => setFeedback(id, null), FEEDBACK_TTL_MS);
      }
    },
    [ctrlState]
  );

  // ── derived operating states ──────────────────────────────────────────────

  const state = operatingState.toUpperCase();
  const isRunning = state === "RUNNING";
  const isPaused  = state === "PAUSED";
  const isStopped = state === "STOPPED" || state === "HALTED" || state === "UNKNOWN" || state === "ERROR";

  // ── button click handler ──────────────────────────────────────────────────

  function handleClick(id: ButtonId): void {
    const actions: Record<ButtonId, () => Promise<unknown>> = {
      start:    startRuntime,
      stop:     stopRuntime,
      pause:    pauseRuntime,
      resume:   resumeRuntime,
      safeMode: toggleSafeMode,
    };
    void runAction(id, actions[id]);
  }

  // ── disable rules ─────────────────────────────────────────────────────────
  // A button is disabled when its action makes no contextual sense.

  const disabled: Record<ButtonId, boolean> = {
    start:    isRunning || isPaused,
    stop:     isStopped,
    pause:    !isRunning,
    resume:   !isPaused,
    safeMode: false,   // always available
  };

  // ─────────────────────────────────────────────────────────────────────────

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
          marginBottom: 12,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <span>Controls</span>

        {/* Status pills */}
        <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
          <StatusPill
            label="Running"
            active={isRunning}
            activeColor="#22c55e"
            activeBg="rgba(34,197,94,0.08)"
          />
          <StatusPill
            label="Paused"
            active={isPaused}
            activeColor="#f59e0b"
            activeBg="rgba(245,158,11,0.08)"
          />
          <StatusPill
            label="Safe Mode"
            active={safeModeActive}
            activeColor="#a78bfa"
            activeBg="rgba(167,139,250,0.08)"
          />
        </div>
      </div>

      {/* Button row */}
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: 8,
          alignItems: "center",
        }}
      >
        <CtrlButton
          id="start"
          label="Start"
          state={ctrlState.start}
          disabled={disabled.start}
          variant="green"
          onClick={handleClick}
        />
        <CtrlButton
          id="stop"
          label="Stop"
          state={ctrlState.stop}
          disabled={disabled.stop}
          variant="red"
          onClick={handleClick}
        />

        {/* Divider */}
        <span
          style={{
            width: 1,
            height: 20,
            background: "#1e293b",
            display: "inline-block",
            margin: "0 2px",
          }}
        />

        <CtrlButton
          id="pause"
          label="Pause"
          state={ctrlState.pause}
          disabled={disabled.pause}
          variant="amber"
          onClick={handleClick}
        />
        <CtrlButton
          id="resume"
          label="Resume"
          state={ctrlState.resume}
          disabled={disabled.resume}
          variant="sky"
          onClick={handleClick}
        />

        {/* Divider */}
        <span
          style={{
            width: 1,
            height: 20,
            background: "#1e293b",
            display: "inline-block",
            margin: "0 2px",
          }}
        />

        <CtrlButton
          id="safeMode"
          label={safeModeActive ? "Disable Safe Mode" : "Enable Safe Mode"}
          state={ctrlState.safeMode}
          disabled={disabled.safeMode}
          variant="violet"
          onClick={handleClick}
        />
      </div>
    </section>
  );
}
