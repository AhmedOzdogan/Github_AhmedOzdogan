import React, { useState, useEffect, useContext } from "react";

function Main() {
  const [num, setNum] = useState(0);

  function increment() {
    setNum(num + 1);

    if (num + 1 > 5) {
      setNum(0);
    }
  }

  function mouseOver() {
    setNum(num + 1);
  }

  const [darkMode, setDarkMode] = useState("white");

  const darkModeToggle = () => {
    setDarkMode(darkMode === "white" ? "black" : "white");
  };

  function Timer() {
    const [seconds, setSeconds] = useState(0);

    useEffect(() => {
      const interval = setInterval(() => {
        setSeconds((prev) => (prev >= 10 ? 0 : prev + 1));
      }, 1000);

      return () => clearInterval(interval);
    }, []);

    const style = {
      fontSize: "24px",
      fontWeight: "bold",
      color: seconds > 5 ? "red" : "blue",
    };

    return <div style={style}>Timer: {seconds} seconds</div>;
  }

  const ThemeContext = React.createContext("light");

  function ThemedButton() {
    const theme = useContext(ThemeContext);
    return <button className={theme}>I am {theme} mode</button>;
  }

  return (
    <div>
      <h2>Main Content</h2>
      <button onClick={increment} onMouseOver={mouseOver}>
        Click Me
      </button>
      <p>Total Number is :{num}</p>

      <button
        style={{
          backgroundColor: darkMode === "white" ? "black" : "white",
          color: darkMode === "white" ? "white" : "black",
          width: "100px",
          height: "40px",
          border: darkMode === "white" ? "3px solid white" : "3px solid black",
          borderRadius: "5px",
        }}
        onClick={darkModeToggle}
      >
        Toggle Dark Mode
      </button>
      <p>Dark Mode is {darkMode === "white" ? "Off" : "On"}</p>
      <Timer />

      <ThemeContext.Provider value={darkMode}>
        <ThemedButton />
      </ThemeContext.Provider>
    </div>
  );
}

export default Main;
