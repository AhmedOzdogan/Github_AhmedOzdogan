export default function Product({
  name,
  price,
  description,
  img,
  onAddToCart,
}) {
  return (
    <div className="p-4 flex flex-col items-center border rounded shadow-md bg-white">
      <h2 className="text-2xl font-bold mb-4">{name}</h2>
      <img className="w-32 h-32 object-cover mb-4" src={img} alt={name} />
      <p className="text-lg text-gray-700 text-center">{description}</p>
      <p className="text-xl font-semibold mt-2">${price}</p>
      <button
        className="mt-4 bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600"
        onClick={() => onAddToCart({ name, price, img })}
      >
        Add to Cart
      </button>
    </div>
  );
}
