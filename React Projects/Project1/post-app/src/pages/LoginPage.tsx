import { useContext, useReducer } from "react";
import InputField from "../components/InputField";
import FormContainer from "../components/FormContainer";
import SubmitButton from "../components/SubmitButton";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import usePostFetch from "../hooks/usePostFetch";

interface LoginResponse {
    user: {
        id: number;
        username: string;
        email: string;
        role: string;
        blocked: boolean;
    };
}

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

    const { executePostFetch, loading, error } = usePostFetch<LoginResponse>();
    const auth = useContext(AuthContext);
    const navigate = useNavigate();

    if (!auth) throw new Error("AuthContext required");
    const { login } = auth;

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();

        dispatch({ type: "SET_LOADING", payload: true });

        try {
            const data = await executePostFetch(
                "http://localhost:8000/api/login/",
                {
                    username: state.username,
                    password: state.password,
                }
            );

            await login(data.user);
            navigate("/booklist");

        } catch (err: any) {
            dispatch({ type: "SET_ERROR", payload: err.message });
        } finally {
            dispatch({ type: "SET_LOADING", payload: false });
        }
    };

    return (
        <FormContainer title="Login">
            <form onSubmit={handleLogin}>
                <InputField
                    label="Username or Email"
                    type="text"
                    value={state.username}
                    onChange={(e) => dispatch({ type: "SET_USERNAME", payload: e.target.value })}
                />

                <InputField
                    label="Password"
                    type="password"
                    value={state.password}
                    onChange={(e) => dispatch({ type: "SET_PASSWORD", payload: e.target.value })}
                />

                {(state.error || error) && (
                    <p className="text-red-500">{state.error || error}</p>
                )}

                <SubmitButton label="Login" loading={state.loading || loading} />
            </form>
        </FormContainer>
    );
}

export default LoginPage;
