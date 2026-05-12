const API_BASE = "http://127.0.0.1:8000";

export async function fetchRuntime(signal?: AbortSignal) {
  try {
    const response = await fetch(`${API_BASE}/runtime`, { signal });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    // We let AbortError bubble up cleanly to be handled by the caller
    if (error instanceof Error && error.name !== 'AbortError') {
      console.error("[API] fetchRuntime error:", error);
    }
    throw error;
  }
}

// ─── Runtime control helpers ──────────────────────────────────────────────────

/** Generic POST to a runtime control endpoint. Returns parsed JSON or throws. */
async function runtimePost(path: string): Promise<Record<string, unknown>> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });

  if (!response.ok) {
    const text = await response.text().catch(() => "");
    throw new Error(`[${path}] HTTP ${response.status}${text ? ": " + text : ""}`);
  }

  return (await response.json()) as Record<string, unknown>;
}

export async function startRuntime(): Promise<Record<string, unknown>> {
  return runtimePost("/runtime/start");
}

export async function stopRuntime(): Promise<Record<string, unknown>> {
  return runtimePost("/runtime/stop");
}

export async function pauseRuntime(): Promise<Record<string, unknown>> {
  return runtimePost("/runtime/pause");
}

export async function resumeRuntime(): Promise<Record<string, unknown>> {
  return runtimePost("/runtime/resume");
}

export async function toggleSafeMode(): Promise<Record<string, unknown>> {
  return runtimePost("/runtime/safe-mode");
}

// ─── Session history ──────────────────────────────────────────────────────────

export interface SessionRecord {
  id: number;
  started_at: string | null;
  ended_at: string | null;
  duration_seconds: number | null;
  total_trades: number | null;
  realized_pnl: number | null;
  portfolio_value: number | null;
  safe_mode_triggered: boolean | null;
}

export async function fetchSessionById(
  id: number,
  signal?: AbortSignal
): Promise<SessionRecord> {
  const response = await fetch(`${API_BASE}/sessions/${id}`, { signal });

  if (!response.ok) {
    throw new Error(`[/sessions/${id}] HTTP ${response.status}`);
  }

  return (await response.json()) as SessionRecord;
}

export async function fetchSessions(
  signal?: AbortSignal
): Promise<SessionRecord[]> {
  const response = await fetch(`${API_BASE}/sessions`, { signal });

  if (!response.ok) {
    throw new Error(`[/sessions] HTTP ${response.status}`);
  }

  return (await response.json()) as SessionRecord[];
}

// ─── Analytics ────────────────────────────────────────────────────────────────

export interface ActiveSessionResponse {
  active: boolean;
  session?: SessionRecord;
}

export async function fetchActiveSession(
  signal?: AbortSignal
): Promise<ActiveSessionResponse> {
  const response = await fetch(`${API_BASE}/active-session`, { signal });
  if (!response.ok) {
    throw new Error(`[/active-session] HTTP ${response.status}`);
  }
  return (await response.json()) as ActiveSessionResponse;
}


export interface SessionAnalytics {
  total_sessions: number;
  profitable_sessions: number;
  losing_sessions: number;
  safe_mode_sessions: number;
  win_rate: number;
  total_realized_pnl: number;
  average_session_duration: number | null;
  best_session_pnl: number | null;
  worst_session_pnl: number | null;
}

export interface TradeAnalytics {
  total_trades: number;
  winning_trades: number;
  losing_trades: number;
  win_rate: number;
  total_realized_pnl: number;
  avg_trade_pnl: number | null;
  best_trade_pnl: number | null;
  worst_trade_pnl: number | null;
}

export async function fetchOverallAnalytics(
  signal?: AbortSignal
): Promise<SessionAnalytics> {
  const response = await fetch(`${API_BASE}/analytics`, { signal });
  if (!response.ok) {
    throw new Error(`[/analytics] HTTP ${response.status}`);
  }
  return (await response.json()) as SessionAnalytics;
}

export async function fetchSessionTradeAnalytics(
  sessionId: number,
  signal?: AbortSignal
): Promise<TradeAnalytics> {
  const response = await fetch(`${API_BASE}/sessions/${sessionId}/analytics`, { signal });
  if (!response.ok) {
    throw new Error(`[/sessions/${sessionId}/analytics] HTTP ${response.status}`);
  }
  return (await response.json()) as TradeAnalytics;
}

