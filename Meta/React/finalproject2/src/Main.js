import MyBio from "./Bio";
import Projects from "./Projects";
import ContactMe from "./ContactMe";

function Main() {
  const mainStyle = {
    padding: "20px",
    textAlign: "center",
  };

  return (
    <main className="App-main" style={mainStyle}>
      <MyBio />
      <Projects />
      <ContactMe />
    </main>
  );
}
export default Main;
