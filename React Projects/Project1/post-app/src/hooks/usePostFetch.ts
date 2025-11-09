import { useState, useCallback } from "react";

interface PostFetchResult<T> {
  url: string;
  body: T | null;
  bearerToken?: string;
}

function usePostFetch<TResponse = any, TBody = any>() {
  const [result, setResult] = useState<PostFetchResult<TResponse> | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // useCallback to ensure stable reference
  const executePostFetch = useCallback(
    async (url: string, body: TBody, bearerToken?: string) => {
      setLoading(true);
      setError(null);

      try {
        const headers: HeadersInit = {
          "Content-Type": "application/json",
        };
        if (bearerToken) {
          headers["Authorization"] = `Bearer ${bearerToken}`;
        }

        const response = await fetch(url, {
          method: "POST",
          headers,
          body: JSON.stringify(body),
        });

        if (!response.ok) {
          const errText = await response.text();
          throw new Error(`Request failed: ${errText || response.statusText}`);
        }

        const data = (await response.json()) as TResponse;
        setResult({ url, body: data, bearerToken });
        return data; // ✅ allow direct result usage in components
      } catch (err: any) {
        console.error("❌ POST error:", err);
        setError(err.message || "Something went wrong");
        throw err; // ✅ let the caller handle it too if needed
      } finally {
        setLoading(false);
      }
    },
    []
  );

  return { result, loading, error, executePostFetch };
}

export default usePostFetch;
