// ─── Frontend Runtime State Machine ──────────────────────────────────────────
// This is the ONLY place runtime lifecycle state is defined on the frontend.
// It is always derived from backend /runtime + /active-session responses.

export type FrontendRuntimeState =
  | "OFFLINE"    // Backend unreachable
  | "IDLE"       // Backend online, no active runtime
  | "STARTING"   // POST /runtime/start pending
  | "ACTIVE"     // Runtime + session live
  | "PAUSED"     // Runtime paused
  | "STOPPING";  // POST /runtime/stop pending

// ─── Backend /runtime response ────────────────────────────────────────────────

export type BackendOperatingState =
  | "RUNNING"
  | "PAUSED"
  | "HALTED"
  | "ERROR"
  | "STOPPED"
  | "IDLE";

export interface RuntimeResponse {
  operating_state: BackendOperatingState;
  safe_mode: boolean;
  symbol?: string;
  mode?: string;
}

// ─── Legacy types kept for chart/trade data ───────────────────────────────────

export type RuntimeMode = "PAPER" | "LIVE";
export type OperatingState = "RUNNING" | "PAUSED" | "HALTED" | "ERROR" | "STOPPED";
export type WsStatus = "CONNECTED" | "RECONNECTING" | "DISCONNECTED";
export type Severity = "INFO" | "SUCCESS" | "WARNING" | "ERROR";

export interface ActiveTrade {
  id: string;
  symbol: string;
  qty: number;
  avgEntry: number;
  currentPrice: number;
  pnl: number;
  pnlPct: number;
  openedAt: string;
}

export interface CompletedTrade {
  id: string;
  symbol: string;
  qty: number;
  entryPrice: number;
  exitPrice: number;
  realizedPnl: number;
  fees: number;
  openedAt: string;
  closedAt: string;
}

export interface RuntimeEvent {
  id: string;
  timestamp: string;
  severity: Severity;
  message: string;
}

export interface TradingStats {
  winRate: number;
  avgWin: number;
  avgLoss: number;
  profitFactor: number;
  totalWins: number;
  totalLosses: number;
}

export interface EquityPoint {
  time: string;
  value: number;
}
