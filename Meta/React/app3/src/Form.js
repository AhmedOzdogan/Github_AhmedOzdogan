import { useRef, useState } from "react";

function Form() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    setName("");
    setPrice(0);
    console.log("Form Submitted!!");
  };
  return (
    <form onSubmit={handleSubmit}>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        type="text"
        placeholder="Name"
      />
      <input
        value={price}
        onChange={(e) => setPrice(Number(e.target.value))}
        type="number"
        placeholder="Price"
      />
      <button disabled={!name || !price} type="submit">
        Add Item
      </button>
    </form>
  );
}

export default Form;
