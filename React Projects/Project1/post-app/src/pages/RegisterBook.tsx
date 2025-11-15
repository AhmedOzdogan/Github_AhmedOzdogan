import React, { useReducer } from "react";
import FormContainer from "../components/FormContainer";
import SubmitButton from "../components/SubmitButton";
import InputField from "../components/InputField";
import SelectField from "../components/SelectField";
import { useNavigate } from "react-router-dom";
import usePostFetch from "../hooks/usePostFetch";
import useFetch from "../hooks/useFetch";

function reducer(state: any, action: any) {
    switch (action.type) {
        case "SET_TITLE":
            return { ...state, title: action.payload };
        case "SET_AUTHOR":
            return { ...state, author: action.payload };
        case "SET_CONTENT":
            return { ...state, content: action.payload };
        case "SET_CATEGORY":
            return { ...state, category_id: action.payload };
        case "SET_LOADING":
            return { ...state, loading: action.payload };
        case "SET_ERROR":
            return { ...state, error: action.payload };
        case "SET_SUCCESS":
            return { ...state, success: action.payload };
        default:
            return state;
    }
}

function RegisterBook() {
    const [state, dispatch] = useReducer(reducer, {
        title: "",
        author: "",
        content: "",
        category_id: null,
        loading: false,
        error: null,
        success: null,
    });

    const {
        data: categories,
        loading: categoriesLoading,
        error: categoriesError,
    } = useFetch<any[]>("http://127.0.0.1:8000/api/categories/");

    // Navigation
    const navigate = useNavigate();

    const {
        executePostFetch,
        loading: postLoading,
        error: postError
    } = usePostFetch();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        if (!state.title || !state.author || !state.content || !state.category_id) {
            dispatch({ type: "SET_ERROR", payload: "Please fill in all fields." });
            return;
        }

        dispatch({ type: "SET_LOADING", payload: true });

        try {

            await executePostFetch(
                "http://localhost:8000/api/posts/create/",
                {
                    title: state.title,
                    book_author: state.author,
                    content: state.content,
                    category_id: state.category_id,
                },
            );

            dispatch({ type: "SET_SUCCESS", payload: "Book registered successfully!" });
            navigate("/booklist");

        } catch (err: any) {
            dispatch({ type: "SET_ERROR", payload: err.message || "Error" });
        } finally {
            dispatch({ type: "SET_LOADING", payload: false });
        }
    };

    return (
        <FormContainer title="Register Book">
            <form onSubmit={handleSubmit} className="flex flex-col gap-4 text-white">

                {/* TITLE */}
                <InputField
                    label="Book Title"
                    type="text"
                    placeholder="Enter the book title"
                    value={state.title}
                    onChange={(e) => dispatch({ type: "SET_TITLE", payload: e.target.value })}
                />

                {/* AUTHOR */}
                <InputField
                    label="Author"
                    type="text"
                    placeholder="Enter author name"
                    value={state.author}
                    onChange={(e) => dispatch({ type: "SET_AUTHOR", payload: e.target.value })}
                />

                {/* CONTENT */}
                <InputField
                    label="Content"
                    type="textarea"
                    placeholder="Write book description..."
                    value={state.content}
                    onChange={(e) => dispatch({ type: "SET_CONTENT", payload: e.target.value })}
                    size="md"
                    height={150}
                    textarea={true}
                />

                {/* CATEGORY SELECT */}

                <SelectField
                    label="Category"
                    value={state.category_id || ""}
                    onChange={(e) =>
                        dispatch({ type: "SET_CATEGORY", payload: Number(e.target.value) })
                    }
                    options={!categoriesLoading ? categories?.map((cat) => ({
                        value: cat.id,
                        label: cat.name,
                        id: cat.id
                    })) : []}
                    defaultOption="Select Category"
                    error={categoriesError ? "Error loading categories" : undefined}
                />

                {/* ERRORS */}
                {state.error && (
                    <p className="text-red-500 bg-red-100 p-2 rounded">{state.error}</p>
                )}
                {categoriesError && (
                    <p className="text-red-500 bg-red-100 p-2 rounded">
                        Error loading categories
                    </p>
                )}
                {postError && (
                    <p className="text-red-500 bg-red-100 p-2 rounded">{postError}</p>
                )}

                {/* SUCCESS */}
                {state.success && (
                    <p className="text-lime-400 bg-lime-900/40 p-2 rounded">
                        {state.success}
                    </p>
                )}

                <SubmitButton
                    label={postLoading ? "Saving..." : "Register Book"}
                    loading={postLoading}
                />
            </form>
        </FormContainer>
    );
}

export default RegisterBook;
