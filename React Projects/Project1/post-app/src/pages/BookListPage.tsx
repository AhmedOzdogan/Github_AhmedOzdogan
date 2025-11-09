import useFetch from "../hooks/useFetch";

function BookListPage() {
    // useFetch automatically handles loading, error, and data
    const { data, loading, error } = useFetch("http://127.0.0.1:8000/api/posts/");

    if (loading) {
        return <p className="text-center text-gray-500">Loading books...</p>;
    }

    if (error) {
        return <p className="text-center text-red-500">Error: {error}</p>;
    }

    if (!data || data.length === 0) {
        return <p className="text-center text-gray-400">No books available.</p>;
    }

    return (
        <div className="max-w-2xl mx-auto mt-8">
            <h1 className="text-2xl font-bold mb-4 text-center">Book List</h1>
            <ul className="space-y-3">
                {data.map((book: any) => (
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
