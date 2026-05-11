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
