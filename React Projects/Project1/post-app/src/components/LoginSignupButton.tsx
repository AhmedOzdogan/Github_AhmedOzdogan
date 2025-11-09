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
                    ? "text-lime-300 border border-amber-100 hover:bg-amber-100 hover:text-slate-800"
                    : "bg-amber-100 text-slate-800 border border-lime-300 hover:bg-slate-600 hover:text-lime-300"
                }`}
        >
            {isLogin ? "Login" : "Sign Up"}
        </Link>

    );
}

export default LoginSignupButton;
