import { useContext, useReducer } from "react";
import InputField from "../components/InputField";
import FormContainer from "../components/FormContainer";
import SubmitButton from "../components/SubmitButton";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import usePostFetch from "../hooks/usePostFetch";

function reducer(state: any, action: any) {
    switch (action.type) {
        case "SET_USERNAME":
            return { ...state, username: action.payload };
        case "SET_PASSWORD":
            return { ...state, password: action.payload };
        case "SET_LOADING":
            return { ...state, loading: action.payload };
        case "SET_ERROR":
            return { ...state, error: action.payload };
        default:
            return state;
    }
}

function LoginPage() {
    const [state, dispatch] = useReducer(reducer, {
        username: "",
        password: "",
        loading: false,
        error: null,
    });

    const { executePostFetch, loading, error } = usePostFetch<{ access: string; refresh: string }>();
    const authContext = useContext(AuthContext);
    const navigate = useNavigate();

    if (!authContext) {
        throw new Error("AuthContext must be used within an AuthProvider");
    }

    const { login } = authContext;

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();

        if (!state.username || !state.password) {
            dispatch({ type: "SET_ERROR", payload: "Please fill in all fields." });
            return;
        }

        dispatch({ type: "SET_LOADING", payload: true });

        try {
            // call executePostFetch instead of usePostFetch
            const data = await executePostFetch("http://127.0.0.1:8000/api/token/", {
                username: state.username,
                password: state.password,
            });

            login(state.username, data.access, data.refresh);
            navigate("/booklist");
        } catch (err: any) {
            dispatch({ type: "SET_ERROR", payload: err.message || "Login failed" });
        } finally {
            dispatch({ type: "SET_LOADING", payload: false });
        }
    };

    return (
        <FormContainer title="Login">
            <form onSubmit={handleLogin}>
                <InputField
                    label="Username"
                    type="text"
                    placeholder="Enter your username"
                    value={state.username}
                    onChange={(e) => dispatch({ type: "SET_USERNAME", payload: e.target.value })}
                />
                <InputField
                    label="Password"
                    type="password"
                    placeholder="Enter your password"
                    value={state.password}
                    onChange={(e) => dispatch({ type: "SET_PASSWORD", payload: e.target.value })}
                />

                {(state.error || error) && (
                    <p className="text-red-500 text-sm mb-2">{state.error || error}</p>
                )}

                <SubmitButton label="Login" loading={state.loading || loading} />
            </form>
        </FormContainer>
    );
}

export default LoginPage;
