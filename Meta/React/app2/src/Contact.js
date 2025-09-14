import ReactPlayer from "react-player";

function Contact() {
  const videoUrl = "https://www.facebook.com/natgeo/videos/10153231379946729/";

  return (
    <div>
      <h1>Welcome to the Contact Page</h1>
      <ReactPlayer
        url={videoUrl}
        width="640px"
        height="360px"
        playing={false}
        controls
      />
    </div>
  );
}

export default Contact;
