import image from "./assets/images/image.png";

function About() {
  const imageUrl = "https://picsum.photos/200";
  return (
    <div>
      <h1>Welcome to the About Page</h1>
      <img src={imageUrl} alt="Random" />
      <img src={image} alt="Local" />
      <img src={require("./assets/images/image.png")} alt="Random picture" />
    </div>
  );
}

export default About;
