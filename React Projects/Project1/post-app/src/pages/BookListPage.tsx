import { useCallback, useState, useMemo } from "react";
import useFetch from "../hooks/useFetch";
import { useNavigate } from "react-router-dom";
import Searchbar from "../components/Searchbar";

function BookListPage() {
    const [page, setPage] = useState(1);
    const navigate = useNavigate();

    // Filters
    const [filters, setFilters] = useState({
        title: "",
        author: "",
        category: "",
    });

    interface PostListResponse {
        count: number;
        next: string | null;
        previous: string | null;
        results: any[];
    }

    // Build URL dynamically (only add non-empty filters)
    const apiUrl = useMemo(() => {
        let url = `http://localhost:8000/api/posts/?page=${page}`;

        if (filters.title) url += `&title=${filters.title}`;
        if (filters.author) url += `&book_author=${filters.author}`;
        if (filters.category) url += `&category=${filters.category}`;

        return url;
    }, [page, filters]);

    console.log("API URL:", apiUrl);

    const { data, loading, error, refetch } = useFetch<PostListResponse>(apiUrl);

    const handleRefresh = useCallback(() => {
        refetch();
        setFilters({ title: "", author: "", category: "" });
        setPage(1);
    }, [refetch]);

    const bookData = useMemo(() => data?.results ?? [], [data]);

    if (loading) return <p className="text-center text-gray-500">Loading books...</p>;
    if (error) return <p className="text-center text-red-500">Error: {error}</p>;

    return (
        <div className="max-w-full mx-auto mt-8 px-4 flex">

            {/* Search Sidebar */}
            <div className="w-1/5 mr-4">
                <Searchbar
                    onSearch={(criteria) => {
                        setFilters(criteria);
                        setPage(1);
                    }}
                />
            </div>

            {/* Main Content */}
            <div className="w-4/5">

                <h1 className="text-3xl font-bold mb-6 text-center text-white">
                    📚 Book Collection
                </h1>

                <div className="flex justify-center mb-6">
                    <button
                        onClick={handleRefresh}
                        className="px-5 py-2 bg-lime-500 text-white rounded-lg hover:bg-lime-600 transition"
                    >
                        Refresh Books
                    </button>
                </div>

                {/* Books Grid */}
                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 xl:grid-cols-6 gap-4">
                    {bookData.map((book) => (
                        <div
                            key={book.id}
                            className="bg-white shadow-md rounded-xl overflow-hidden hover:shadow-xl transition"
                        >
                            <img
                                src="book.png"
                                alt={book.title}
                                className="w-full h-48 object-cover"
                            />

                            <div className="p-4">
                                <h2 className="text-lg font-semibold text-gray-800 mb-2">{book.title}</h2>
                                <p className="text-sm text-gray-600 mb-3 h-20 overflow-hidden">{book.content}</p>

                                <div className="text-xs text-gray-500">
                                    <p>Author: {book.book_author || "Unknown"}</p>
                                    <p>By: {book.created_by?.username || "User"}</p>
                                </div>
                            </div>

                            <button
                                className="w-full bg-lime-500 text-white py-2 hover:bg-lime-600 transition"
                                onClick={() => navigate(`/details/${book.id}`)}
                            >
                                Details
                            </button>
                        </div>
                    ))}
                </div>

                {/* Pagination */}
                <div className="flex justify-center mt-6 space-x-4">
                    <button
                        onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
                        disabled={!data?.previous}
                        className="px-4 py-2 bg-lime-500 text-white rounded hover:bg-lime-600 disabled:opacity-50"
                    >
                        Previous
                    </button>

                    <button
                        onClick={() => setPage((prev) => prev + 1)}
                        disabled={!data?.next}
                        className="px-4 py-2 bg-lime-500 text-white rounded hover:bg-lime-600 disabled:opacity-50"
                    >
                        Next
                    </button>
                </div>

            </div>
        </div>
    );
}

export default BookListPage;
