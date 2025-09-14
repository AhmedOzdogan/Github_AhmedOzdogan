import { useState } from "react";

function Comment(props) {
  const [score, setScore] = useState(0);
  const [comment, setComment] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (score > 10 || comment.length < 10) {
      alert("Please provide a better comment");
    }
    const formData = {
      score,
      comment,
    };
    console.log(props.data);
    console.log("Form submitted:", formData);
    setScore(0);
    setComment("");
  };
  return (
    <div className="formDivision">
      <form onSubmit={handleSubmit}>
        <fieldset>
          <h1>Comments</h1>
          <div className="Field">
            <label>Stars {score}</label>
            <input
              type="range"
              min="0"
              max="10"
              value={score}
              onChange={(e) => setScore(e.target.value)}
            />
          </div>
          <div className="Field">
            <label>Comments</label>
            <textarea
              value={comment}
              onChange={(e) => setComment(e.target.value)}
            ></textarea>
          </div>
        </fieldset>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Comment;
