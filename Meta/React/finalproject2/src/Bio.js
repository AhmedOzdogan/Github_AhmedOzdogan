import avatar from "./avatar.png";

function MyBio() {
  return (
    <div>
      <h2>About Me</h2>
      <div
        className="bio-content"
        style={{
          display: "flex",
          alignItems: "center",
          background: "#08070727",
          padding: "10px",
          borderRadius: "5px",
        }}
      >
        <img
          src={avatar}
          alt="Profile"
          style={{ borderRadius: "50%", marginRight: "20px" }}
        />
        <p>
          I am a passionate web developer with experience in building dynamic
          web applications using React, Node.js, and other modern technologies.
        </p>
      </div>
    </div>
  );
}

export default MyBio;
