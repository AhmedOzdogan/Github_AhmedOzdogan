import { Link } from "react-router-dom";
import NavbarAuthSection from "./NavbarAuthSection";

function Navbar() {
    return (
        <nav className="fixed top-0 left-0 right-0 h-16 w-full flex items-center justify-between px-8 bg-slate-600 text-lime-300 shadow-md backdrop-blur-md z-50">
            {/* Left: Logo */}
            <div className="shrink-0">
                <Link
                    to="/"
                    className="text-2xl font-semibold text-orange-150 hover:text-highlight transition-colors duration-200"
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
                            to="/nestedmenu"
                            className="hover:text-highlight transition-colors duration-200"
                        >
                            Nested Menu
                        </Link>
                    </li>
                    <li>
                        <Link
                            to="/booklist"
                            className="hover:text-accent transition-colors duration-200"
                        >
                            Book List
                        </Link>
                    </li>
                    <li>
                        <Link
                            to="/registerbook"
                            className="hover:text-secondary transition-colors duration-200"
                        >
                            Register Book
                        </Link>
                    </li>
                </ul>
            </div>

            <NavbarAuthSection />
        </nav>
    );
}

export default Navbar;
