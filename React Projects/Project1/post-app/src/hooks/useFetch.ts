import { useState, useEffect, useCallback, useRef } from "react";

function useFetch<T = any>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const controllerRef = useRef<AbortController | null>(null);

  // Fetch logic
  const fetchData = useCallback(async () => {
    if (!url) return;

    // Cancel previous request
    if (controllerRef.current) controllerRef.current.abort();
    const controller = new AbortController();
    controllerRef.current = controller;

    setLoading(true);
    setError(null);

    try {
      const response = await fetch(url, { signal: controller.signal });
      if (!response.ok) throw new Error(`Error: ${response.statusText}`);

      const result = await response.json();

      // ✅ Compare with previous data before setting
      setData((prev) => {
        if (JSON.stringify(prev) === JSON.stringify(result)) {
          console.log("No data change — skipping state update");
          return prev; // no re-render
        }
        return result;
      });
    } catch (err: any) {
      if (err.name !== "AbortError") setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [url]);

  // Initial fetch
  useEffect(() => {
    fetchData();
    return () => controllerRef.current?.abort();
  }, [fetchData]);

  // Stable refetch
  const refetch = useCallback(() => {
    fetchData();
  }, [fetchData]);

  return { data, loading, error, refetch };
}

export default useFetch;
