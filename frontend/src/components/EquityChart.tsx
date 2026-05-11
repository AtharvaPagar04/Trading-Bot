"use client";

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { equityCurve } from "@/mock";

interface TooltipProps {
  active?: boolean;
  payload?: Array<{ value: number }>;
  label?: string;
}

function CustomTooltip({ active, payload, label }: TooltipProps) {
  if (!active || !payload?.length) return null;
  const val = payload[0].value;
  const pnl = val - 10_000;
  return (
    <div style={{
      background: "#0f0f18",
      border: "1px solid #1e293b",
      borderRadius: 3,
      padding: "6px 10px",
      fontSize: 11,
      fontFamily: "monospace",
    }}>
      <div style={{ color: "#64748b" }}>{label}</div>
      <div style={{ color: "#e2e8f0", fontWeight: 600 }}>
        ${val.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
      </div>
      <div style={{ color: pnl >= 0 ? "#22c55e" : "#ef4444" }}>
        {pnl >= 0 ? "+" : ""}${pnl.toFixed(2)}
      </div>
    </div>
  );
}

export function EquityChart() {
  const start = equityCurve[0]?.value ?? 10_000;
  const end = equityCurve[equityCurve.length - 1]?.value ?? 10_000;
  const isPositive = end >= start;
  const color = isPositive ? "#22c55e" : "#ef4444";

  const minVal = Math.min(...equityCurve.map((p) => p.value));
  const maxVal = Math.max(...equityCurve.map((p) => p.value));
  const padding = (maxVal - minVal) * 0.15 || 50;

  return (
    <div style={{
      background: "#0f0f18",
      border: "1px solid #1e293b",
      borderRadius: 4,
      padding: "12px 16px 8px",
    }}>
      {/* header */}
      <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", marginBottom: 10 }}>
        <div>
          <div style={{ fontSize: 10, textTransform: "uppercase", letterSpacing: "0.08em", color: "#64748b" }}>
            Equity Curve
          </div>
          <div style={{ fontSize: 16, fontWeight: 600, color: "#e2e8f0", fontVariantNumeric: "tabular-nums", marginTop: 2 }}>
            ${end.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
        </div>
        <span style={{ fontSize: 12, fontFamily: "monospace", color }}>
          {isPositive ? "+" : ""}${(end - start).toFixed(2)}
        </span>
      </div>

      {/* chart */}
      <ResponsiveContainer width="100%" height={120}>
        <AreaChart data={equityCurve} margin={{ top: 0, right: 0, left: 0, bottom: 0 }}>
          <defs>
            <linearGradient id="eqGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor={color} stopOpacity={0.12} />
              <stop offset="95%" stopColor={color} stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
          <XAxis
            dataKey="time"
            tick={{ fill: "#475569", fontSize: 9, fontFamily: "monospace" }}
            axisLine={false}
            tickLine={false}
            interval="preserveStartEnd"
          />
          <YAxis
            domain={[minVal - padding, maxVal + padding]}
            tick={{ fill: "#475569", fontSize: 9, fontFamily: "monospace" }}
            axisLine={false}
            tickLine={false}
            width={56}
            tickFormatter={(v) =>
              `$${(v / 1000).toFixed(1)}k`
            }
          />
          <Tooltip content={<CustomTooltip />} cursor={{ stroke: "#334155", strokeWidth: 1 }} />
          <Area
            type="monotone"
            dataKey="value"
            stroke={color}
            strokeWidth={1.5}
            fill="url(#eqGrad)"
            dot={false}
            activeDot={{ r: 3, fill: color, strokeWidth: 0 }}
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
