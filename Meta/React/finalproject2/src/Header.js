import styled from "styled-components"; // inline css styling

function Header() {
  const navLinks = [
    { path: "https://www.facebook.com", label: "Facebook" },
    { path: "https://www.instagram.com", label: "Instagram" },
    { path: "https://www.linkedin.com", label: "LinkedIn" },
    { path: "https://www.twitter.com", label: "Twitter" },
    { path: "https://www.github.com", label: "GitHub" },
  ];

  const headerStyle = {
    backgroundColor: "#282c34",
    minHeight: "100px",
    display: "flex",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    fontSize: "calc(10px + 2vmin)",
    color: "white",
    padding: "0 20px",
    margin: "0",
  };
  const listStyle = {
    listStyleType: "none",
    padding: 0,
    margin: 0,
    display: "flex",
    flexDirection: "row",
    gap: "10px",
  };

  const StyledLink = styled.a`
    color: white;
    text-decoration: none;

    &:hover {
      text-decoration: underline;
      color: lightgray;
    }
  `;

  function headerLinks() {
    return (
      <ul style={listStyle}>
        {navLinks.map((link) => (
          <li key={link.path}>
            <StyledLink
              href={link.path}
              target="_blank"
              rel="noopener noreferrer"
            >
              {link.label}
            </StyledLink>
          </li>
        ))}
      </ul>
    );
  }

  return (
    <header className="App-header" style={headerStyle}>
      <h1>My React Final Project</h1>
      <nav>{headerLinks()}</nav>
    </header>
  );
}

export default Header;
