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
        <div className="max-w-11xl mx-auto mt-8 px-4">
            <h1 className="text-3xl font-bold mb-6 text-center text-white">
                📚 Book Collection
            </h1>

            <div className="flex justify-center mb-6">
                <button
                    onClick={handleRefresh}
                    className="px-5 py-2 bg-lime-500 text-white font-medium rounded-lg hover:bg-lime-600 transition"
                >
                    Refresh Books
                </button>
            </div>

            {/* 🟩 Grid layout for books */}
            <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-6 gap-3">
                {bookData.map((book: any) => (
                    <div
                        key={book.id}
                        className="bg-white shadow-md rounded-xl overflow-hidden hover:shadow-lg transition-shadow duration-300"
                    >
                        <img
                            src="book.png"
                            alt={book.title}
                            className="w-full h-48 object-center object-cover"
                        />
                        <div className="p-4">
                            <h2 className="text-lg font-semibold text-gray-800 mb-2">
                                {book.title}
                            </h2>
                            <p className="text-sm text-gray-600 mb-3 wrap-normal h-20 overflow-hidden">
                                {book.content}
                            </p>
                            <div className="text-xs text-gray-500 flex justify-between">
                                <span>Author: {book.book_author || "Unknown"}</span>
                                <span>By: {book.created_by?.username || "User"}</span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default BookListPage;