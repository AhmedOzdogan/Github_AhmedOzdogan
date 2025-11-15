import { useContext, useReducer } from "react";
import { useNavigate } from "react-router-dom";
import InputField from "../components/InputField";
import FormContainer from "../components/FormContainer";
import SubmitButton from "../components/SubmitButton";
import { AuthContext } from "../context/AuthContext";
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
        case "SET_EMAIL":
            return { ...state, email: action.payload };
        case "SET_PASSWORD":
            return { ...state, password: action.payload };
        case "SET_CONFIRM_PASSWORD":
            return { ...state, confirmPassword: action.payload };
        case "SET_LOADING":
            return { ...state, loading: action.payload };
        case "SET_ERROR":
            return { ...state, error: action.payload };
        default:
            return state;
    }
}

function SignupPage() {
    const auth = useContext(AuthContext);
    if (!auth) throw new Error("AuthContext required");

    const navigate = useNavigate();

    const [state, dispatch] = useReducer(reducer, {
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
        loading: false,
        error: null,
    });

    // usePostFetch with LoginResponse type 
    const {
        executePostFetch,
        loading: postLoading,
        error: postError,
    } = usePostFetch<LoginResponse>();

    const handleSignup = async (e: React.FormEvent) => {
        e.preventDefault();
        dispatch({ type: "SET_ERROR", payload: null });

        if (
            !state.username ||
            !state.email ||
            !state.password ||
            !state.confirmPassword
        ) {
            dispatch({
                type: "SET_ERROR",
                payload: "Please fill in all fields.",
            });
            return;
        }

        if (state.password !== state.confirmPassword) {
            dispatch({
                type: "SET_ERROR",
                payload: "Passwords do not match.",
            });
            return;
        }

        dispatch({ type: "SET_LOADING", payload: true });

        try {
            //  SIGNUP 
            await executePostFetch("http://localhost:8000/api/users/register/", {
                username: state.username,
                email: state.email,
                password: state.password,
            });

            // AUTO LOGIN – 
            const loginData = (await executePostFetch(
                "http://localhost:8000/api/login/",
                {
                    username: state.username,
                    password: state.password,
                }
            )) as LoginResponse;

            // Save user in AuthContext (cookies already set HttpOnly)
            await auth.login(loginData.user);

            navigate("/booklist");
        } catch (err: any) {
            dispatch({
                type: "SET_ERROR",
                payload: err.message || "Signup failed.",
            });
        } finally {
            dispatch({ type: "SET_LOADING", payload: false });
        }
    };

    return (
        <FormContainer title="Signup">
            <form onSubmit={handleSignup} className="space-y-4">
                <InputField
                    label="Username"
                    type="text"
                    placeholder="Enter your username"
                    value={state.username}
                    onChange={(e) =>
                        dispatch({ type: "SET_USERNAME", payload: e.target.value })
                    }
                />

                <InputField
                    label="Email"
                    type="email"
                    placeholder="Enter your email"
                    value={state.email}
                    onChange={(e) =>
                        dispatch({ type: "SET_EMAIL", payload: e.target.value })
                    }
                />

                <InputField
                    label="Password"
                    type="password"
                    placeholder="Enter your password"
                    value={state.password}
                    onChange={(e) =>
                        dispatch({ type: "SET_PASSWORD", payload: e.target.value })
                    }
                />

                <InputField
                    label="Confirm Password"
                    type="password"
                    placeholder="Re-enter your password"
                    value={state.confirmPassword}
                    onChange={(e) =>
                        dispatch({
                            type: "SET_CONFIRM_PASSWORD",
                            payload: e.target.value,
                        })
                    }
                />

                {(state.error || postError) && (
                    <p className="text-red-500 text-sm mb-2">
                        {state.error || postError}
                    </p>
                )}

                <SubmitButton
                    label={state.loading || postLoading ? "Signing up..." : "Signup"}
                    loading={state.loading || postLoading}
                />
            </form>

            <p className="text-sm text-white text-center mt-4">
                Already have an account?{" "}
                <a href="/login" className="text-lime-300 hover:underline">
                    Login
                </a>
            </p>
        </FormContainer>
    );
}

export default SignupPage;
