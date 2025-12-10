import useFetch from "../hooks/useFetch";
import { useParams } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import InputField from "../components/InputField";
import { useState } from "react";
import usePostFetch from "../hooks/usePostFetch";
import usePutFetch from "../hooks/usePutFetch";
import useDeleteFetch from "../hooks/useDeleteFetch";

import { MdDeleteForever } from "react-icons/md";
import { FaEdit, FaSave } from "react-icons/fa";

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

    const [comment, setComment] = useState("");
    const [editingCommentId, setEditingCommentId] = useState<number | null>(null);

    const { user } = useAuth();

    const { data, loading, error, refetch } = useFetch<BookDetail>(
        `http://localhost:8000/api/posts/${bookId}/detail/`
    );

    const { executePostFetch, loading: postLoading } = usePostFetch();
    const { executePutFetch, loading: putLoading } = usePutFetch();
    const { executeDeleteFetch, loading: deleteLoading } = useDeleteFetch();

    // ADD or EDIT COMMENT
    async function submitComment() {
        if (!comment.trim()) return;

        if (editingCommentId) {
            await executePutFetch(
                `http://localhost:8000/api/comments/${editingCommentId}/`,
                { content: comment, post_id: Number(bookId) }
            );
            setEditingCommentId(null);
        } else {
            await executePostFetch(
                `http://localhost:8000/api/posts/${bookId}/comments/`,
                { content: comment, post_id: Number(bookId) }
            );
        }

        setComment("");
        refetch();
    }

    // DELETE COMMENT
    async function deleteComment(commentId: number) {
        await executeDeleteFetch(`http://localhost:8000/api/comments/${commentId}/`);
        refetch();
    }

    // ENTER EDIT MODE
    function startEdit(commentId: number, content: string) {
        setEditingCommentId(commentId);
        setComment(content);
    }

    if (loading) return <p className="text-white">Loading...</p>;
    if (error) return <p className="text-red-500">Error: {error}</p>;
    if (!data) return <p className="text-white">No data found.</p>;

    return (
        <>
            {/* BOOK DETAILS */}
            <div className="max-w-4xl mx-auto mt-10 bg-slate-800 text-white rounded-xl shadow-lg overflow-hidden border border-slate-700">
                <div className="flex flex-col md:flex-row">

                    <div className="md:w-1/3 bg-slate-700">
                        <img
                            src="/book.png"
                            alt={data.title}
                            className="w-full h-full object-cover p-4 rounded-lg"
                        />
                    </div>

                    <div className="md:w-2/3 p-6">
                        <h1 className="text-4xl font-bold mb-3 text-lime-300">{data.title}</h1>

                        <p className="text-amber-100 mb-4 leading-relaxed">{data.content}</p>

                        <div className="mt-4 flex justify-between items-center">
                            <div>
                                <p className="text-sm text-lime-300">
                                    <span className="font-semibold text-white">Author:</span>{" "}
                                    {data.book_author || "Unknown"}
                                </p>
                                <p className="text-sm text-lime-300">
                                    <span className="font-semibold text-white">Posted by:</span>{" "}
                                    {data.created_by.username}
                                </p>
                            </div>

                            {user && user.id === data.created_by.id && (
                                <button className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm shadow">
                                    Delete
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {/* COMMENTS */}
            <h2 className="text-3xl font-bold mt-3 mb-0 text-center text-lime-300">Comments</h2>

            <div className="min-w-4xl mx-auto bg-slate-800 text-white rounded-xl shadow p-6 border border-slate-700">

                {data.comments.length === 0 ? (
                    <p className="text-center text-amber-100">No comments yet.</p>
                ) : (
                    data.comments.map((c) =>
                        editingCommentId === c.id ? null : (
                            <div
                                key={c.id}
                                className="mb-4 p-4 bg-amber-100 text-black rounded-lg shadow-sm flex justify-between items-start"
                            >
                                <div>
                                    <p className="font-medium">{c.content}</p>
                                    <p className="text-xs text-slate-700 mt-1">
                                        By: <span className="font-semibold">{c.created_by.username}</span>{" "}
                                        on {new Date(c.created_at).toLocaleDateString()}
                                    </p>
                                </div>

                                {user && user.id === c.created_by.id && (
                                    <div className="flex flex-row items-center">

                                        {/* Edit */}
                                        <FaEdit
                                            size={24}
                                            className="text-lime-500 hover:text-lime-700 cursor-pointer mr-4"
                                            onClick={() => startEdit(c.id, c.content)}
                                        />

                                        {/* Delete */}
                                        {!deleteLoading ? (
                                            <MdDeleteForever
                                                size={28}
                                                className="text-red-600 hover:text-red-800 cursor-pointer"
                                                onClick={() => deleteComment(c.id)}
                                            />
                                        ) : (
                                            <div className="flex items-center">
                                                <svg
                                                    className="animate-spin h-6 w-6 text-red-600"
                                                    xmlns="http://www.w3.org/2000/svg"
                                                    fill="none"
                                                    viewBox="0 0 24 24"
                                                >
                                                    <circle
                                                        className="opacity-25"
                                                        cx="12"
                                                        cy="12"
                                                        r="10"
                                                        stroke="currentColor"
                                                        strokeWidth="4"
                                                    ></circle>
                                                    <path
                                                        className="opacity-75"
                                                        fill="currentColor"
                                                        d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 100 16v-4l-3 3 3 3v-4a8 8 0 01-8-8z"
                                                    ></path>
                                                </svg>
                                            </div>
                                        )}

                                    </div>
                                )}
                            </div>
                        )
                    )
                )}

                {/* ADD OR EDIT COMMENT */}
                <div className="flex flex-row mt-6 items-center space-x-4">

                    <div className="w-4/5">
                        <InputField
                            label={editingCommentId ? "Edit Comment" : "Add a Comment"}
                            type="text"
                            textarea={true}
                            placeholder="Write your comment..."
                            value={comment}
                            onChange={(e) => setComment(e.target.value)}
                            fullWidth={true}
                            height={100}
                        />
                    </div>

                    <div className="w-1/5 mt-2">
                        <button
                            className="bg-lime-500 hover:bg-lime-600 text-white w-full px-5 py-2 rounded-2xl shadow"
                            onClick={submitComment}
                            disabled={postLoading || putLoading}
                        >
                            <FaSave className="inline mr-2" />
                            {editingCommentId
                                ? putLoading ? "Saving..." : "Save Edit"
                                : postLoading ? "Posting..." : "Submit Comment"}
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
}

export default BookDetailPage;
