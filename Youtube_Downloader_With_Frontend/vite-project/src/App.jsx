import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
    const [url, setUrl] = useState("");
    const [videoInfo, setVideoInfo] = useState(null);
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");
    const [selectedFormat, setSelectedFormat] = useState(null);

    const fetchVideoInfo = async () => {
        setLoading(true);
        setMessage("");
        setSelectedFormat(null);
        try {
            const response = await axios.post("http://127.0.0.1:8000/video-info", { url });
            setVideoInfo(response.data);
        } catch (error) {
            setMessage("Failed to fetch video info");
        }
        setLoading(false);
    };

    const downloadVideo = async () => {
        if (!selectedFormat) {
            setMessage("Please select a format to download");
            return;
        }
        setMessage("Downloading...");
        try {
            await axios.post("http://127.0.0.1:8000/download", { url });
            setMessage("Download finished! Check the downloads folder.");
        } catch (error) {
            setMessage("Download failed");
        }
    };

    return (
        <div className="container">
            <h1 className="title">YouTube Video Downloader</h1>
            <input
                type="text"
                className="input"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Enter YouTube URL"
            />
            <button className="button" onClick={fetchVideoInfo} disabled={loading}>
                Get Video Info
            </button>

            {videoInfo && (
                <div className="video-info">
                    <h2>{videoInfo.title}</h2>
                    <p>Duration: {videoInfo.duration} seconds</p>
                    <h3>Select Format:</h3>
                    <select className="dropdown" onChange={(e) => setSelectedFormat(e.target.value)}>
                        <option value="">Choose a format</option>
                        {videoInfo.formats.map((format) => (
                            <option key={format.id} value={format.id}>{format.resolution}</option>
                        ))}
                    </select>
                    <button className="download-button" onClick={downloadVideo}>
                        Download
                    </button>
                </div>
            )}

            {message && <p className="message">{message}</p>}
        </div>
    );
}

export default App;
