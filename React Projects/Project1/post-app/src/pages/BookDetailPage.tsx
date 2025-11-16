import useFetch from "../hooks/useFetch";
import { useParams } from "react-router-dom";

interface BookDetail {
    id: number;
    title: string;
    content: string;
    book_author: string;
    created_by: {
        id: number;
        username: string;
        email: string;
        role: string;
        blocked: boolean;
    };
    category: {
        id: number;
        name: string;
        slug: string;
        description: string;
    } | null;
    created_at: string;
    updated_at: string;
    comments: Array<{
        id: number;
        content: string;
        created_by: {
            id: number;
            username: string;
            email: string;
            role: string;
            blocked: boolean;
        };
        created_at: string;
        approved: boolean;
    }>;
}

function BookDetailPage() {
    const { bookId } = useParams<{ bookId: string }>();

    const { data, loading, error } = useFetch<BookDetail>(
        `http://localhost:8000/api/posts/${bookId}/detail/`
    );

    if (loading) return <p className="text-white">Loading...</p>;
    if (error) return <p className="text-red-500">Error: {error}</p>;
    if (!data) return <p className="text-white">No data found.</p>;

    return (
        <div className="text-center text-white">
            <h2 className="text-2xl font-bold mb-4">{data.title}</h2>
            <p className="mb-2">{data.content}</p>

            <h3 className="font-semibold mt-4">Author:</h3>
            <p>{data.book_author}</p>

            {data.category && (
                <>
                    <h3 className="font-semibold mt-4">Category:</h3>
                    <p>{data.category.name}</p>
                </>
            )}

            <h3 className="font-semibold mt-4">Comments:</h3>
            <ul className="mt-2 space-y-2">
                {data.comments.map((comment) => (
                    <li key={comment.id} className="bg-gray-800 p-2 rounded">
                        <p>{comment.content}</p>
                        <small className="text-gray-400">
                            by {comment.created_by.username}
                        </small>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default BookDetailPage;
