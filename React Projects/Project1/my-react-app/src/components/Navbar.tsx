import { Link } from "react-router-dom";
import LoginSignupButton from "./LoginSignupButton";

function Navbar() {
    return (
        <nav className="fixed top-0 left-0 right-0 h-16 w-full flex items-center justify-between px-8 bg-primary text-white shadow-md backdrop-blur-md z-50">
            {/* Left: Logo */}
            <div className="flex-shrink-0">
                <Link
                    to="/"
                    className="text-2xl font-semibold text-white hover:text-highlight transition-colors duration-200"
                >
                    MyApp
                </Link>
            </div>

            {/* Center: Menu */}
            <div className="absolute left-1/2 transform -translate-x-1/2">
                <ul className="flex space-x-6 font-medium">
                    <li>
                        <Link
                            to="/"
                            className="hover:text-highlight transition-colors duration-200"
                        >
                            Home
                        </Link>
                    </li>
                    <li>
                        <Link
                            to="/about"
                            className="hover:text-accent transition-colors duration-200"
                        >
                            About
                        </Link>
                    </li>
                    <li>
                        <Link
                            to="/contact"
                            className="hover:text-secondary transition-colors duration-200"
                        >
                            Contact
                        </Link>
                    </li>
                </ul>
            </div>

            {/* Right: Auth buttons */}
            <div className="flex ml-auto space-x-3">
                <LoginSignupButton type="login" />
                <LoginSignupButton type="signup" />
            </div>
        </nav>
    );
}

export default Navbar;
