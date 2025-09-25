import "./App.css";
import Header from "./components/Header";
import LandingPage from "./components/LandingPage";
import ProductsPage from "./components/ProductsPage";
import Cart from "./components/Cart";
import { Routes, Route } from "react-router-dom";
import { useState } from "react";

export default function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    console.log("Adding to cart:", product);
    setCart((prev) => {
      const idx = prev.findIndex((p) => p.name === product.name);
      if (idx > -1) {
        // increase quantity if already in cart
        return prev.map((p, i) =>
          i === idx ? { ...p, qty: (p.qty ?? 1) + 1 } : p
        );
      }
      return [...prev, { ...product, qty: 1 }];
    });
  };

  const updateCart = (productName, delta) => {
    setCart((prev) => {
      const idx = prev.findIndex((p) => p.name === productName);
      if (idx === -1) return prev; // not found, do nothing
      const newQty = (prev[idx].qty ?? 1) + delta;
      if (newQty <= 0) {
        // remove from cart if qty goes to 0 or below
        return prev.filter((p, i) => i !== idx);
      }
      return prev.map((p, i) => (i === idx ? { ...p, qty: newQty } : p));
    });
  };

  return (
    <>
      <Header cartCount={cart.reduce((n, i) => n + (i.qty ?? 1), 0)} />
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route
          path="/products"
          element={<ProductsPage onAddToCart={addToCart} />}
        />
        <Route
          path="/cart"
          element={<Cart items={cart} updateCart={updateCart} />}
        />
      </Routes>
    </>
  );
}
