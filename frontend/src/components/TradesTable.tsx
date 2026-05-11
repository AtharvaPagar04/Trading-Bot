interface Column<T> {
  header: string;
  key: keyof T;
  align?: "left" | "right";
  render?: (value: T[keyof T], row: T) => React.ReactNode;
}

interface TradesTableProps<T extends { id: string }> {
  title: string;
  rows: T[];
  columns: Column<T>[];
  emptyMessage?: string;
}

export function TradesTable<T extends { id: string }>({
  title,
  rows,
  columns,
  emptyMessage = "No trades",
}: TradesTableProps<T>) {
  return (
    <div style={{ marginBottom: 32 }}>
      <div style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        marginBottom: 8,
      }}>
        <h2 style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: "0.08em", color: "#64748b", margin: 0 }}>
          {title}
        </h2>
        <span style={{ fontSize: 11, color: "#475569", fontFamily: "monospace" }}>
          {rows.length} {rows.length === 1 ? "record" : "records"}
        </span>
      </div>

      <div style={{ background: "#0f0f18", border: "1px solid #1e293b", borderRadius: 4, overflow: "hidden" }}>
        {rows.length === 0 ? (
          <div style={{ padding: "24px", textAlign: "center", color: "#475569", fontSize: 13 }}>
            {emptyMessage}
          </div>
        ) : (
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12 }}>
            <thead>
              <tr style={{ borderBottom: "1px solid #1e293b" }}>
                {columns.map((col, colIdx) => (
                  <th
                    key={colIdx}
                    style={{
                      padding: "8px 12px",
                      textAlign: col.align ?? "left",
                      fontSize: 10,
                      textTransform: "uppercase",
                      letterSpacing: "0.06em",
                      color: "#475569",
                      fontWeight: 500,
                    }}
                  >
                    {col.header}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((row, i) => (
                <tr
                  key={row.id}
                  style={{
                    borderBottom: i < rows.length - 1 ? "1px solid #1e293b" : "none",
                    background: i % 2 === 1 ? "rgba(255,255,255,0.02)" : "transparent",
                  }}
                >
                  {columns.map((col, colIdx) => (
                    <td
                      key={colIdx}
                      style={{
                        padding: "8px 12px",
                        textAlign: col.align ?? "left",
                        color: "#cbd5e1",
                        fontFamily: "monospace",
                        fontVariantNumeric: "tabular-nums",
                      }}
                    >
                      {col.render ? col.render(row[col.key], row) : String(row[col.key] ?? "")}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
