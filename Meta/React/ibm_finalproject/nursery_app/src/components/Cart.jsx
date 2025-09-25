import { Link } from "react-router-dom";

export default function Cart({ items, updateCart }) {
  if (!items.length) {
    return (
      <div className="p-8">
        <h1 className="text-3xl font-bold mb-4">Shopping Cart</h1>
        <p>Your cart is empty.</p>
        <Link to="/products" className="text-blue-600 underline">
          Go to products
        </Link>
      </div>
    );
  }

  const subtotal = items.reduce((sum, it) => sum + it.price * (it.qty ?? 1), 0);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">Shopping Cart</h1>
      <ul className="divide-y bg-white rounded shadow">
        {items.map((it) => (
          <li key={it.name} className="p-4 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <img
                src={it.img}
                alt={it.name}
                className="w-12 h-12 object-cover rounded"
              />
              <div>
                <div className="font-semibold">{it.name}</div>
                <div className="text-sm text-gray-600">
                  ${it.price.toFixed(2)}
                </div>
              </div>
            </div>
            <div className="text-sm">Qty: {it.qty ?? 1}</div>
            <div className="flex items-center gap-2 ml-auto">
              <button
                className="bg-green-600 text-white py-1 px-2 rounded hover:bg-green-700"
                onClick={() => updateCart(it.name, 1)}
              >
                +
              </button>
              <button
                className="bg-red-600 text-white py-1 px-2 rounded hover:bg-red-700"
                onClick={() => updateCart(it.name, -1)}
              >
                -
              </button>
              <button
                className="bg-red-950 text-white py-1 px-2 rounded hover:bg-red-800"
                onClick={() => updateCart(it.name, -it.qty)}
              >
                Remove
              </button>
            </div>
          </li>
        ))}
      </ul>
      <div className="mt-4 text-right text-xl font-semibold">
        Subtotal: ${subtotal.toFixed(2)}
      </div>
      <div className="flex justify-end gap-4 mt-4">
        <button className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">
          Checkout (Coming Soon)
        </button>
        <Link
          to="/products"
          className="text-blue-600 underline flex items-center"
        >
          Continue Shopping
        </Link>
      </div>
    </div>
  );
}
