import Product from "./Product";

export default function ProductsPage({ onAddToCart }) {
  const products = [
    {
      name: "Sunflower",
      price: 29.99,
      description: "Bright and happy.",
      img: "/img/sunflower.png",
    },
    {
      name: "Red Rose",
      price: 39.99,
      description: "Classic romance.",
      img: "/img/redrose.png",
    },
    {
      name: "White Rose",
      price: 49.99,
      description: "Pure and elegant.",
      img: "/img/whiterose.png",
    },
    {
      name: "Pink Rose",
      price: 29.99,
      description: "Soft and sweet.",
      img: "/img/pinkrose.png",
    },
    {
      name: "Black Rose",
      price: 39.99,
      description: "Bold and rare.",
      img: "/img/blackrose.png",
    },
    {
      name: "Daisy",
      price: 49.99,
      description: "Simple joy.",
      img: "/img/daisy.png",
    },
  ];

  return (
    <div className="p-8 flex flex-col items-center bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-bold mb-8">Products List</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
        {products.map((p) => (
          <Product
            key={p.name}
            name={p.name}
            price={p.price}
            description={p.description}
            img={p.img}
            onAddToCart={onAddToCart}
          />
        ))}
      </div>
    </div>
  );
}
