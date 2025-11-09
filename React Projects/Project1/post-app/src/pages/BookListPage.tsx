import { useCallback, useMemo } from "react";
import useFetch from "../hooks/useFetch";

function BookListPage() {
    const { data, loading, error, refetch } = useFetch<any[]>(
        "http://127.0.0.1:8000/api/posts/"
    );

    // Stable refresh handler
    const handleRefresh = useCallback(() => {
        refetch();
    }, [refetch]);

    // Memoize book data to avoid creating new array references unnecessarily
    const bookData = useMemo(() => {
        if (!data) return [];
        return data;
    }, [JSON.stringify(data)]);

    // Handle loading / error / empty states
    if (loading) {
        return <p className="text-center text-gray-500">Loading books...</p>;
    }

    if (error) {
        return <p className="text-center text-red-500">Error: {error}</p>;
    }

    if (!bookData || bookData.length === 0) {
        return (
            <div className="text-center mt-8">
                <p className="text-gray-400 mb-2">No books available.</p>
                <button
                    onClick={handleRefresh}
                    className="px-4 py-2 bg-lime-500 text-white rounded hover:bg-lime-600 transition"
                >
                    Refresh
                </button>
            </div>
        );
    }

    // 🧾 Main UI
    return (
        <div className="max-w-2xl mx-auto mt-8">
            <h1 className="text-2xl font-bold mb-4 text-center text-white">
                Book List
            </h1>

            <div className="flex justify-center mb-4">
                <button
                    onClick={handleRefresh}
                    className="px-4 py-2 bg-lime-500 text-white rounded hover:bg-lime-600 transition"
                >
                    Refresh Books
                </button>
            </div>

            <ul className="space-y-3">
                {bookData.map((book: any) => (
                    <li
                        key={book.id}
                        className="p-4 bg-white shadow rounded hover:shadow-md transition"
                    >
                        <h2 className="font-semibold text-lg">{book.title}</h2>
                        <p className="text-sm text-gray-600">{book.content}</p>
                        <p className="text-xs text-gray-400 mt-2">
                            Author: {book.author || "Unknown"}
                        </p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default BookListPage;
