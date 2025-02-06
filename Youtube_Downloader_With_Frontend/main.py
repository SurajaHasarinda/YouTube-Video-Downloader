from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

def get_video_info(url):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title", "Unknown"),
                "duration": info.get("duration", 0),
                "formats": [
                    {"id": f["format_id"], "resolution": f.get("resolution", "Unknown")}
                    for f in info.get("formats", []) if f.get("resolution")
                ]
            }
    except yt_dlp.utils.DownloadError:
        return None

@app.post("/video-info")
async def video_info(request: VideoRequest):
    info = get_video_info(request.url)
    if not info:
        raise HTTPException(status_code=400, detail="Invalid URL or unable to fetch details")
    return info

@app.post("/download")
async def download_video(request: VideoRequest):
    output_path = "downloads"
    os.makedirs(output_path, exist_ok=True)
    filename_template = f"{output_path}/%(title)s.%(ext)s"
    
    ydl_opts = {
        'outtmpl': filename_template,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([request.url])
        return {"message": "Download started! Check the downloads folder."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
