import {useState,useCallback} from "react";

interface DeleteFetchResult {
  url: string;
  success: boolean;
}

function useDeleteFetch() {
    const [result, setResult] = useState<DeleteFetchResult | null>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const executeDeleteFetch = useCallback(async (url: string) => {
        setLoading(true);
        setError(null);

        try {
            const response = await fetch(url, {
                method: "DELETE",
                headers: {  
                    "Content-Type": "application/json",
                },
                credentials: "include", // ALWAYS send cookies
            });
            if (!response.ok) {
                const errText = await response.text();
                throw new Error(`Request failed: ${errText || response.statusText}`);
            }
            setResult({ url, success: true });
        } catch (error: any) {
            setError(error.message || "An unknown error occurred");
        } finally {
            setLoading(false);
        }
    }, []);

    return { result, loading, error, executeDeleteFetch };
}

export default useDeleteFetch;