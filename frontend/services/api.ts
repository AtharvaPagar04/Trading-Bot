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

