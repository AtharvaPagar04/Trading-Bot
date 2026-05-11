interface MetricCardProps {
  label: string;
  value: string;
  sub?: string;
  color?: "green" | "red" | "default";
}

export function MetricCard({ label, value, sub, color = "default" }: MetricCardProps) {
  const valueColor =
    color === "green"
      ? "#22c55e"
      : color === "red"
        ? "#ef4444"
        : "#e2e8f0";

  return (
    <div style={{
      background: "#0f0f18",
      border: "1px solid #1e293b",
      borderRadius: 4,
      padding: "12px 16px",
    }}>
      <div style={{ fontSize: 10, textTransform: "uppercase", letterSpacing: "0.08em", color: "#64748b", marginBottom: 6 }}>
        {label}
      </div>
      <div style={{ fontSize: 18, fontWeight: 600, color: valueColor, fontVariantNumeric: "tabular-nums" }}>
        {value}
      </div>
      {sub && (
        <div style={{ fontSize: 11, color: "#64748b", marginTop: 2, fontFamily: "monospace" }}>
          {sub}
        </div>
      )}
    </div>
  );
}
