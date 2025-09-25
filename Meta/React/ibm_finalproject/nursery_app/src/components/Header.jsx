import { Link } from "react-router-dom";

export default function Header({ cartCount = 0 }) {
  return (
    <header className="bg-green-600 text-white p-4 flex items-center justify-between">
      <div className="text-4xl font-bold mr-10">Nursery</div>
      <ul className="flex items-center gap-6 text-lg">
        <li>
          <Link to="/" className="hover:text-gray-200">
            Home
          </Link>
        </li>
        <li>
          <Link to="/products" className="hover:text-gray-200">
            Products
          </Link>
        </li>
        <li className="relative">
          <Link to="/cart" className="hover:text-gray-200">
            Cart
          </Link>
          {cartCount > 0 && (
            <span className="ml-2 text-sm bg-white text-green-700 rounded-full px-2 py-0.5">
              {cartCount}
            </span>
          )}
        </li>
      </ul>
    </header>
  );
}
