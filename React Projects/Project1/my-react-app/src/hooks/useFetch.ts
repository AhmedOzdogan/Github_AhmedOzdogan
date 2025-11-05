import { useState, useEffect } from "react";

// Custom hook for fetching data from an API

function useFetch<T = any>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // return if no url is provided
    if (!url) return;

    // Setup for aborting fetch on cleanup
    const controller = new AbortController();
    const signal = controller.signal;

    // Async function to fetch data
    const fetchData = async () => {
      // Reset state before new fetch
      setError(null);
      setLoading(true);

      // Fetch data from the provided URL
      try {
        const response = await fetch(url, { signal });
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        const result = await response.json();
        setData(result);
        // Handle fetch errors
      } catch (err: any) {
        // Ignore abort errors
        if (err.name !== "AbortError") {
          setError(err.message);
        }
        // Finally block to set loading to false
      } finally {
        setLoading(false);
      }
    };

    // Call the fetch function
    fetchData();

    return () => {
      controller.abort();
    };
  }, [url]);

  return { data, loading, error };
}

export default useFetch;
