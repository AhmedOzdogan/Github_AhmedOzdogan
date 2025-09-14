import { useState } from "react";

function Calculator() {
  const [input, setInput] = useState("");

  const nums = [7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, "C", "=", "+"];

  const handleClick = (val) => {
    if (val === "C") {
      setInput("");
    } else if (val === "=") {
      try {
        setInput(eval(input).toString());
      } catch {
        setInput("Error");
      }
    } else {
      setInput(input + val);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        background: "#f4f4f4",
      }}
    >
      <div
        style={{
          width: "300px",
          background: "#222",
          padding: "20px",
          borderRadius: "12px",
          boxShadow: "0 4px 10px rgba(0,0,0,0.2)",
        }}
      >
        <h2
          style={{ color: "white", textAlign: "center", marginBottom: "15px" }}
        >
          Calculator
        </h2>
        <input
          type="text"
          value={input}
          readOnly
          style={{
            width: "calc(100% - 20px)",
            height: "50px",
            fontSize: "20px",
            marginBottom: "15px",
            textAlign: "right",
            padding: "10px",
            borderRadius: "8px",
            border: "none",
            outline: "none",
          }}
        />
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(4, 1fr)",
            gap: "10px",
          }}
        >
          {nums.map((n) => (
            <button
              key={n}
              onClick={() => handleClick(n)}
              style={{
                padding: "20px",
                fontSize: "18px",
                borderRadius: "8px",
                border: "none",
                cursor: "pointer",
                background:
                  typeof n === "number"
                    ? "#444"
                    : n === "="
                    ? "#28a745"
                    : n === "C"
                    ? "#dc3545"
                    : "#007bff",
                color: "white",
                fontWeight: "bold",
                transition: "0.2s",
              }}
              onMouseOver={(e) => (e.currentTarget.style.opacity = "0.8")}
              onMouseOut={(e) => (e.currentTarget.style.opacity = "1")}
            >
              {n}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Calculator;
