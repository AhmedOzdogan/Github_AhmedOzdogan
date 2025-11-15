import { useAuth } from "../context/AuthContext";
import LoginSignupButton from "./LoginSignupButton";

function NavbarAuthSection() {
    const { user, logout } = useAuth();

    return (
        <div className="flex ml-auto items-center space-x-3">
            {user ? (
                <>
                    <span className="text-white font-medium">👋 {user.username}</span>
                    <button
                        onClick={logout}
                        className="bg-red-500 hover:bg-red-600 text-white px-4 py-1 rounded-lg transition"
                    >
                        Logout
                    </button>
                </>
            ) : (
                <>
                    <LoginSignupButton type="login" />
                    <LoginSignupButton type="signup" />
                </>
            )}
        </div>
    );
}

export default NavbarAuthSection;
