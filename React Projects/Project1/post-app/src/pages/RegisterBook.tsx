import { useState } from "react";
import { get } from "idb-keyval";
import FormContainer from "../components/FormContainer";
import SubmitButton from "../components/SubmitButton";
import InputField from "../components/InputField";
import { useNavigate } from "react-router-dom";

function RegisterBook() {
    const [title, setTitle] = useState("");
    const [author, setAuthor] = useState("");
    const [content, setContent] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<string | null>(null);
    const navigate = useNavigate();  

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);
        setSuccess(null);

        if (!title || !author || !content) {
            setError("Please fill in all fields.");
            return;
        }

        setLoading(true);

        try {
            const token = await get("accessToken");

            const response = await fetch("http://127.0.0.1:8000/api/posts/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({ title, author, content }),
            });

            if (!response.ok) {
                throw new Error("Failed to register book");
            }

            setTitle("");
            setAuthor("");
            setContent("");
            setSuccess("Book registered successfully!");
            navigate("/booklist");
        } catch (err: any) {
            console.error("Error:", err);
            setError(err.message || "An error occurred");
        } finally {
            setLoading(false);
        }
    };

    return (
        <FormContainer title="Register Book">
            <form onSubmit={handleSubmit} className="flex flex-col gap-4 text-white">
                <InputField
                    label="Book Title"
                    type="text"
                    placeholder="Enter the book title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />

                <InputField
                    label="Author"
                    type="text"
                    placeholder="Enter author name"
                    value={author}
                    onChange={(e) => setAuthor(e.target.value)}
                />

                <div className="flex flex-col">
                    <label className="mb-1 text-sm font-medium">Content</label>
                    <textarea
                        placeholder="Write book description or summary..."
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                        className="p-3 rounded-lg text-gray-900 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-lime-400"
                        rows={4}
                    ></textarea>
                </div>

                {error && (
                    <p className="text-red-500 text-sm font-medium bg-red-100 rounded p-2">
                        ❌ {error}
                    </p>
                )}
                {success && (
                    <p className="text-lime-400 text-sm font-medium bg-lime-900/40 rounded p-2">
                        ✅ {success}
                    </p>
                )}

                <SubmitButton label={loading ? "Registering..." : "Register Book"} loading={loading} />
            </form>
        </FormContainer>
    );
}

export default RegisterBook;
