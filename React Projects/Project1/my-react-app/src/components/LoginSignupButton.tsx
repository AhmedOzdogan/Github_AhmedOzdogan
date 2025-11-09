import { Link } from "react-router-dom";

interface LoginSignupButtonProps {
    type: "login" | "signup";
}

function LoginSignupButton({ type }: LoginSignupButtonProps) {
    const isLogin = type === "login";
    const path = isLogin ? "/login" : "/signup";

    return (
        <Link
            to={path}
            className={`px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-200 
        ${isLogin
                    ? "text-blue-600 border border-blue-600 hover:bg-blue-600 hover:text-white"
                    : "bg-blue-600 text-white hover:bg-blue-700"
                }`}
        >
            {isLogin ? "Login" : "Sign Up"}
        </Link>
    );
}

export default LoginSignupButton;
