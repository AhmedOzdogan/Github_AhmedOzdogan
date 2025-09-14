import logo from "./logo.svg";
import "./App.css";
import Form from "./Form";
import Comment from "./Comment";
import { useState } from "react";

function App() {
  const [data, changeData] = useState([
    {
      id: 1,
      name: "Tiramisu",
      price: 25,
      picture: "https://via.placeholder.com/150",
    },
    {
      id: 2,
      name: "Cheesecake",
      price: 30,
      picture: "https://via.placeholder.com/150",
    },
    {
      id: 3,
      name: "Chocolate Cake",
      price: 28,
      picture: "https://via.placeholder.com/150",
    },
    {
      id: 4,
      name: "Lemon Tart",
      price: 22,
      picture: "https://via.placeholder.com/150",
    },
  ]);
  // key should be unique and index shouldn't be used. So that React will
  // understand that each item is distinct and can efficiently update the UI.
  const listData = data.map((item) => (
    <li key={item.id} id={"item-" + item.id}>
      {item.id} - {item.name} - ${item.price}
    </li>
  ));

  function reverseItems() {
    const reversed = [...data].reverse();
    changeData(reversed);
  }
  return (
    <div>
      <ul>{listData}</ul>
      <button onClick={reverseItems}>Reverse Order</button>
      <Form />
      <Comment data={data} />
    </div>
  );
}

export default App;
