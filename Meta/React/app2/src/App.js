import "./App.css";
import Header from "./Header.js";
import { useState } from "react";

function App() {
  function LogInOutButton(props) {
    const [isLoggedIn, setIsLoggedIn] = useState(props.isLoggedIn);
    if (isLoggedIn) {
      return <button onClick={() => setIsLoggedIn(false)}>Logout</button>;
    } else {
      return <button onClick={() => setIsLoggedIn(true)}>Login</button>;
    }
  }

  return (
    <>
      <Header />
      <LogInOutButton isLoggedIn={false} />
    </>
  );
}
export default App;
