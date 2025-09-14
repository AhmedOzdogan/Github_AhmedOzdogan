function Projects() {
  function SingleProject({ title, description }) {
    const boxStyle = {
      border: "1px solid #ddd",
      borderRadius: "8px",
      padding: "16px",
      background: "#fafafa",
      boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
      transition: "transform 0.2s",
    };

    return (
      <li style={boxStyle}>
        <h3 style={{ margin: "0 0 8px" }}>{title}</h3>
        <p style={{ margin: 0, fontSize: "14px", color: "#555" }}>
          {description}
        </p>
      </li>
    );
  }

  const projects = [
    {
      title: "Weather App",
      description: "A React app that shows current weather for any city.",
    },
    {
      title: "Task Manager",
      description: "A simple to-do list application with CRUD features.",
    },
    {
      title: "Portfolio Website",
      description: "Personal portfolio built with React and styled-components.",
    },
    {
      title: "Recipe Finder",
      description: "Search and view recipes using a public API.",
    },
    {
      title: "Chat App",
      description: "Real-time chat application using Socket.io and Node.js.",
    },
  ];

  return (
    <div>
      <h2 style={{ textAlign: "center" }}>My Projects</h2>
      <ul
        style={{
          listStyleType: "none",
          padding: 0,
          margin: "20px auto",
          display: "grid",
          gridTemplateColumns: "repeat(3, 1fr)", // ✅ 3 per row
          gap: "20px", // spacing between boxes
          maxWidth: "1000px",
        }}
      >
        {projects.map((project) => (
          <SingleProject
            key={project.title}
            title={project.title}
            description={project.description}
          />
        ))}
      </ul>
    </div>
  );
}

export default Projects;
