import "./App.css";
import { useEffect, useState, useReducer } from "react";

function App() {
  const [data, setData] = useState(null);
  const [selectedItem, setSelectedItem] = useState(null);

  // Load all products
  useEffect(() => {
    fetch("https://fakestoreapi.com/products")
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  // Load details of a single product
  function itemDetails(item) {
    fetch(`https://fakestoreapi.com/products/${item.id}`)
      .then((res) => res.json())
      .then((json) => {
        setSelectedItem(json);
      });
  }
  // Reducer for managing money state
  const reducer = (state, action) => {
    switch (action.type) {
      case "spend":
        if (state.money >= action.payload) {
          return { money: state.money - action.payload };
        } else {
          alert("Insufficient funds!");
          return state;
        }
      case "return":
        return { money: state.money + action.payload };
      default:
        return state;
    }
  };

  // Initial state for the money reducer
  const initialState = { money: 1500 };
  // useReducer hook for managing money state
  const [state, dispatch] = useReducer(reducer, initialState);

  function renderData() {
    if (!data) return <p>Loading...</p>;

    return (
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
          gap: "20px",
          padding: "20px",
        }}
      >
        {data.map((item) => (
          <div
            key={item.id}
            style={{
              border: "1px solid #ddd",
              borderRadius: "8px",
              padding: "15px",
              background: "#fff",
              boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
            }}
          >
            <img
              src={item.image}
              alt={item.title}
              style={{ width: "100px", height: "100px", objectFit: "contain" }}
            />
            <h3 style={{ fontSize: "16px" }}>{item.title}</h3>
            <p style={{ fontSize: "14px", color: "#555" }}>
              {item.description.slice(0, 60)}...
            </p>
            <p style={{ fontWeight: "bold" }}>💲 {item.price}</p>
            <button onClick={() => itemDetails(item)}>Details</button>
          </div>
        ))}
      </div>
    );
  }

  function renderDetails() {
    if (!selectedItem) return null;

    return (
      <div
        style={{
          margin: "20px auto",
          padding: "20px",
          maxWidth: "600px",
          border: "2px solid #007bff",
          borderRadius: "10px",
          background: "#f9f9f9",
        }}
      >
        <h2>{selectedItem.title}</h2>
        <img
          src={selectedItem.image}
          alt={selectedItem.title}
          style={{ width: "200px", height: "200px", objectFit: "contain" }}
        />
        <p>{selectedItem.description}</p>
        <p style={{ fontWeight: "bold" }}>💲 {selectedItem.price}</p>
        <button onClick={() => setSelectedItem(null)}>Back to list</button>
        <button
          onClick={() =>
            dispatch({ type: "spend", payload: selectedItem.price })
          }
        >
          Buy
        </button>
        <button
          onClick={() =>
            dispatch({ type: "return", payload: selectedItem.price })
          }
        >
          Return
        </button>
      </div>
    );
  }

  return (
    <div>
      <h1 style={{ textAlign: "center" }}>🛍️ My Store</h1>
      <h2 style={{ textAlign: "center" }}>Balance: 💲 {state.money}</h2>
      {selectedItem ? renderDetails() : renderData()}
    </div>
  );
}

export default App;
