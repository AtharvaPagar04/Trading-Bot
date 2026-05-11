// Minimal types for the debug dashboard

export type RuntimeMode = "PAPER" | "LIVE";
export type OperatingState = "RUNNING" | "PAUSED" | "HALTED" | "ERROR" | "STOPPED";
export type WsStatus = "CONNECTED" | "RECONNECTING" | "DISCONNECTED";
export type Severity = "INFO" | "SUCCESS" | "WARNING" | "ERROR";

export interface RuntimeData {
  state: OperatingState;
  mode: RuntimeMode;
  safeMode: boolean;
  symbol: string;
  latestPrice: number;
  totalTrades: number;
  unrealizedPnl: number;
  unrealizedPnlPct: number;
  uptime: string;
  lastUpdateSeconds: number; // seconds since last heartbeat
  wsStatus: WsStatus;
}

export interface PortfolioData {
  totalCapital: number;
  availableCash: number;
  investedCapital: number;
  holdingsValue: number;
  totalValue: number;
  realizedPnl: number;
}

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
  winRate: number;       // percentage 0-100
  avgWin: number;        // dollars
  avgLoss: number;       // dollars (positive value)
  profitFactor: number;  // ratio
  totalWins: number;
  totalLosses: number;
}

export interface EquityPoint {
  time: string;
  value: number;
}
