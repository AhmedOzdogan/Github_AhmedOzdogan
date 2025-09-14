function ContactMe() {
  const formStyle = {
    display: "flex",
    flexDirection: "column",
    maxWidth: "400px",
    margin: "40px auto",
    border: "1px solid #eee",
    borderRadius: "12px",
    padding: "24px",
    background: "white",
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
    fontFamily: "Arial, sans-serif",
  };

  const labelStyle = {
    marginBottom: "6px",
    fontWeight: "bold",
    fontSize: "14px",
    color: "#333",
  };

  const inputStyle = {
    padding: "10px",
    marginBottom: "16px",
    border: "1px solid #ccc",
    borderRadius: "6px",
    fontSize: "14px",
    transition: "border-color 0.2s, box-shadow 0.2s",
  };

  const textareaStyle = {
    ...inputStyle,
    minHeight: "100px",
    resize: "vertical",
  };

  const buttonStyle = {
    padding: "12px",
    border: "none",
    borderRadius: "6px",
    backgroundColor: "#007BFF",
    color: "white",
    fontSize: "16px",
    fontWeight: "bold",
    cursor: "pointer",
    transition: "background-color 0.3s, transform 0.1s",
  };

  return (
    <div>
      <form style={formStyle}>
        <label style={labelStyle} htmlFor="name">
          Name
        </label>
        <input
          style={inputStyle}
          type="text"
          id="name"
          placeholder="Your Name"
        />

        <label style={labelStyle} htmlFor="email">
          Email
        </label>
        <input
          style={inputStyle}
          type="email"
          id="email"
          placeholder="Your Email"
        />

        <label style={labelStyle} htmlFor="message">
          Message
        </label>
        <textarea
          style={textareaStyle}
          id="message"
          placeholder="Your Message"
        ></textarea>

        <button
          type="submit"
          style={buttonStyle}
          onMouseOver={(e) => (e.target.style.backgroundColor = "#0056b3")}
          onMouseOut={(e) => (e.target.style.backgroundColor = "#007BFF")}
          onMouseDown={(e) => (e.target.style.transform = "scale(0.97)")}
          onMouseUp={(e) => (e.target.style.transform = "scale(1)")}
        >
          Send ✉️
        </button>
      </form>
    </div>
  );
}

export default ContactMe;
