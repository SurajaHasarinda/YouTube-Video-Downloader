import { useState } from "react";

function VideoForm({ onSubmit }) {
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!url.trim()) {
      alert("Please enter a valid URL");
      return;
    }
    onSubmit(url);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter YouTube URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <button type="submit">Fetch Video Info</button>
    </form>
  );
}

export default VideoForm;
