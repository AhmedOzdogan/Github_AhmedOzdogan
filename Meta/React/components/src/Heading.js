function formatName(name, surname) {
  return name + " " + surname.toUpperCase();
}
const user = "John Doe";

function Name(props) {
  return <span>{formatName(props.name, props.Surname)}</span>;
}

function Heading(props) {
  const bag = {
    padding: "20px",
    border: "1px solid gray",
    background: "#7a0808ff",
    margin: "20px 0",
  };
  return (
    <h1 style={bag}>
      My name is <Name name={props.name} Surname={props.Surname} />{" "}
      {user == formatName(props.name, props.Surname)
        ? " (You)"
        : "Anonymous User"}
    </h1>
  );
}

export default Heading;
