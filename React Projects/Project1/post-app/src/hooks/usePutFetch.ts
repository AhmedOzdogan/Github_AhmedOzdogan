import { useState,useCallback } from "react";

interface PutFetchResult<T> {
  url: string;
  body: T | null;
}
function usePutFetch() {
    const [result, setResult] = useState<PutFetchResult<any> | null>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const executePutFetch = useCallback(async (url: string, body: any) => {
        setLoading(true);
        setError(null);

        const csftToken = document.cookie
            .split("; ")
            .find((row) => row.startsWith("csrftoken="))
            ?.split("=")[1];

        try {
            const response = await fetch(url, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csftToken || "",
                },
                credentials: "include", // ALWAYS send cookies
                body: JSON.stringify(body),
            });

            if (!response.ok) {
                const errText = await response.text();
                throw new Error(`Request failed: ${errText || response.statusText}`);
            }
            const data = await response.json();
            setResult({ url, body: data });
        } catch (error: any) {
            setError(error.message || "An unknown error occurred");
        } finally {
            setLoading(false);
        }
    }, []);

    return { result, loading, error, executePutFetch };
}

export default usePutFetch;