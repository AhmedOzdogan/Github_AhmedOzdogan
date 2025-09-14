import React from "react";
import ReactDOM from "react-dom";
import "./App.css";
import Heading from "./Heading";
import Sidebar from "./Sidebar";
import Main from "./Main";

function App() {
  return (
    <div>
      <Heading name="Anna" Surname="Smith" color="Purple" />
      <Main />
      <Sidebar />
    </div>
  );
}
export default App;
