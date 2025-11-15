import { useState, useCallback } from "react";

interface PostFetchResult<T> {
  url: string;
  body: T | null;
}

function usePostFetch<TResponse = any, TBody = any>() {
  const [result, setResult] = useState<PostFetchResult<TResponse> | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const executePostFetch = useCallback(async (url: string, body: TBody) => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include", // ALWAYS send cookies
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        const errText = await response.text();
        throw new Error(`Request failed: ${errText || response.statusText}`);
      }

      const data = (await response.json()) as TResponse;

      setResult({ url, body: data });
      return data;
    } catch (err: any) {
      console.error("❌ POST error:", err);
      setError(err.message || "Something went wrong");
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return { result, loading, error, executePostFetch };
}

export default usePostFetch;
