import type {
  RuntimeData,
  PortfolioData,
  ActiveTrade,
  CompletedTrade,
  RuntimeEvent,
  TradingStats,
  EquityPoint,
} from "@/types";

export const runtime: RuntimeData = {
  state: "RUNNING",
  mode: "PAPER",
  safeMode: true,
  symbol: "BTCUSDT",
  latestPrice: 67_842.15,
  totalTrades: 47,
  unrealizedPnl: 234.18,
  unrealizedPnlPct: 2.34,
  uptime: "5h 5m",
  lastUpdateSeconds: 2,
  wsStatus: "CONNECTED",
};

export const portfolio: PortfolioData = {
  totalCapital: 10_000.0,
  availableCash: 7_832.55,
  investedCapital: 2_167.45,
  holdingsValue: 2_401.63,
  totalValue: 10_234.18,
  realizedPnl: 1_124.72,
};

export const activeTrades: ActiveTrade[] = [
  {
    id: "t1",
    symbol: "BTCUSDT",
    qty: 0.032,
    avgEntry: 66_920.0,
    currentPrice: 67_842.15,
    pnl: 29.5,
    pnlPct: 1.38,
    openedAt: "2026-05-11 02:53",
  },
  {
    id: "t2",
    symbol: "ETHUSDT",
    qty: 0.8,
    avgEntry: 3_180.5,
    currentPrice: 3_214.3,
    pnl: 27.04,
    pnlPct: 1.06,
    openedAt: "2026-05-11 04:08",
  },
];

export const completedTrades: CompletedTrade[] = [
  {
    id: "c1",
    symbol: "BTCUSDT",
    qty: 0.025,
    entryPrice: 65_200.0,
    exitPrice: 66_850.0,
    realizedPnl: 41.25,
    fees: 1.32,
    openedAt: "2026-05-10 20:00",
    closedAt: "2026-05-10 23:00",
  },
  {
    id: "c2",
    symbol: "ETHUSDT",
    qty: 1.2,
    entryPrice: 3_050.0,
    exitPrice: 3_180.5,
    realizedPnl: 156.6,
    fees: 2.78,
    openedAt: "2026-05-10 04:00",
    closedAt: "2026-05-10 10:00",
  },
  {
    id: "c3",
    symbol: "BTCUSDT",
    qty: 0.018,
    entryPrice: 67_100.0,
    exitPrice: 66_800.0,
    realizedPnl: -5.4,
    fees: 0.94,
    openedAt: "2026-05-11 00:00",
    closedAt: "2026-05-11 01:30",
  },
  {
    id: "c4",
    symbol: "BTCUSDT",
    qty: 0.04,
    entryPrice: 64_500.0,
    exitPrice: 65_900.0,
    realizedPnl: 56.0,
    fees: 1.85,
    openedAt: "2026-05-09 18:00",
    closedAt: "2026-05-10 00:00",
  },
  {
    id: "c5",
    symbol: "ETHUSDT",
    qty: 0.5,
    entryPrice: 3_220.0,
    exitPrice: 3_190.0,
    realizedPnl: -15.0,
    fees: 0.72,
    openedAt: "2026-05-10 16:00",
    closedAt: "2026-05-10 18:00",
  },
];

// ── Runtime Events (newest first) ────────────────────────────────────────────

export const runtimeEvents: RuntimeEvent[] = [
  {
    id: "e1",
    timestamp: "04:08:12",
    severity: "SUCCESS",
    message: "BUY ETHUSDT 0.800 @ $3,180.50 — order filled",
  },
  {
    id: "e2",
    timestamp: "04:08:10",
    severity: "INFO",
    message: "Execution approved by governance layer — within risk limits",
  },
  {
    id: "e3",
    timestamp: "04:07:55",
    severity: "INFO",
    message: "Signal generated: ETHUSDT LONG — RSI 31.4, BB lower touch",
  },
  {
    id: "e4",
    timestamp: "03:45:00",
    severity: "INFO",
    message: "Heartbeat OK — runtime healthy",
  },
  {
    id: "e5",
    timestamp: "03:12:44",
    severity: "WARNING",
    message: "Daily loss threshold at 68% — monitoring exposure",
  },
  {
    id: "e6",
    timestamp: "02:53:01",
    severity: "SUCCESS",
    message: "BUY BTCUSDT 0.032 @ $66,920.00 — order filled",
  },
  {
    id: "e7",
    timestamp: "02:52:59",
    severity: "INFO",
    message: "Execution approved by governance layer — within risk limits",
  },
  {
    id: "e8",
    timestamp: "01:30:22",
    severity: "ERROR",
    message: "SELL BTCUSDT 0.018 @ $66,800 — stop loss triggered, PnL: -$6.34",
  },
  {
    id: "e9",
    timestamp: "01:15:08",
    severity: "WARNING",
    message: "WebSocket reconnect after 8s interruption — stream resumed",
  },
  {
    id: "e10",
    timestamp: "00:00:11",
    severity: "SUCCESS",
    message: "BUY BTCUSDT 0.018 @ $67,100 — order filled",
  },
  {
    id: "e11",
    timestamp: "00:00:09",
    severity: "INFO",
    message: "Signal generated: BTCUSDT LONG — candle breakout confirmed",
  },
  {
    id: "e12",
    timestamp: "23:00:01",
    severity: "SUCCESS",
    message: "SELL BTCUSDT 0.025 @ $66,850 — closed, PnL: +$39.93",
  },
  {
    id: "e13",
    timestamp: "22:59:50",
    severity: "INFO",
    message: "Take-profit target reached: BTCUSDT +2.53%",
  },
  {
    id: "e14",
    timestamp: "21:00:00",
    severity: "INFO",
    message: "Runtime initialized — PAPER mode, safe mode ENABLED",
  },
];

// ── Trading Stats ─────────────────────────────────────────────────────────────

export const tradingStats: TradingStats = {
  winRate: 68.1,
  avgWin: 78.43,
  avgLoss: 10.58,
  profitFactor: 3.14,
  totalWins: 32,
  totalLosses: 15,
};

// ── Equity Curve ─────────────────────────────────────────────────────────────

export const equityCurve: EquityPoint[] = [
  { time: "21:00", value: 10_000 },
  { time: "21:30", value: 10_018 },
  { time: "22:00", value: 10_045 },
  { time: "22:30", value: 10_032 },
  { time: "23:00", value: 10_071 },
  { time: "23:30", value: 10_055 },
  { time: "00:00", value: 10_110 },
  { time: "00:30", value: 10_088 },
  { time: "01:00", value: 10_103 },
  { time: "01:30", value: 10_097 },
  { time: "02:00", value: 10_118 },
  { time: "02:30", value: 10_142 },
  { time: "03:00", value: 10_138 },
  { time: "03:30", value: 10_165 },
  { time: "04:00", value: 10_198 },
  { time: "04:30", value: 10_234 },
];
