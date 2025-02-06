function VideoDetails({ info }) {
    return (
      <div>
        <h2>{info.title}</h2>
        <p>Duration: {Math.floor(info.duration / 60)} min {info.duration % 60} sec</p>
        <h3>Available Formats:</h3>
        <ul>
          {info.formats.map((format) => (
            <li key={format.id}>{format.resolution}</li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default VideoDetails;
  