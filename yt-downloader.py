import os
import yt_dlp
from yt_dlp.utils import DownloadError

def get_video_info(url):
    """Fetch video details like title, duration, and available formats."""
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title", "Unknown"),
                "duration": info.get("duration", 0),
                "formats": [
                    f"{f['format_id']} - {f['resolution']}" for f in info.get("formats", []) if f.get("resolution")
                ]
            }
    except DownloadError:
        return None
    

def download_video(url, quality="best", output_path="downloads"):
    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Quality selection mapping
    quality_map = {
        "best": "bestvideo+bestaudio/best",  # Best available quality
        "1080p": "bv*[height=1080]+ba/best",  # 1080p (mp4)
        "720p": "bv*[height=720]+ba/best",  # 720p (mp4)
        "480p": "bv*[height=480]+ba/best",  # 480p (mp4)
        "360p": "bv*[height=360]+ba/best",  # 360p (mp4)
        "audio": "bestaudio",  # Audio-only (mp3)
    }

    selected_format = quality_map.get(quality, "bestvideo+bestaudio/best")  # Default to best

    # Set output filename with quality label
    filename_template = f"{output_path}/%(title)s [{quality}].%(ext)s"

    # Define download options
    ydl_opts = {
        'outtmpl': filename_template,  # Save file with quality label
        'format': selected_format,
        'merge_output_format': 'mp4',  # Ensure MP4 format (ignored for audio)
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }] if quality != "audio" else [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,  # True - Only download single video | False - Download entire playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download complete!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    print("\n🎬 YouTube Downloader ▶️")

    while True:
        video_url = input("Enter YouTube video URL (or 'exit' to quit): ").strip()
        
        if video_url.lower() == 'exit':
            print("👋 Exiting.")
            break
        
        if not video_url:
            print("❌ No URL provided. Please try again.")
            continue

        video_info = get_video_info(video_url)
        if not video_info:
            print("⚠️ Unable to fetch video details. Please check the URL.")
            continue   

        print(f"\n📌 Video: {video_info['title']}")
        print(f"⏳ Duration: {video_info['duration'] // 60} min {video_info['duration'] % 60} sec")
        print("\n🎥 Choose Video Quality:")
        print("   0. Best (Default)")
        print("   1. 1080p")
        print("   2. 720p")
        print("   3. 480p")
        print("   4. 360p")
        print("   5. Audio (MP3)")

        valid_qualities = ["best", "1080p", "720p", "480p", "360p", "audio"]

        try:
            quality_index = int(input("Enter quality number: ").strip())
            selected_quality = valid_qualities[quality_index] if 0 <= quality_index < len(valid_qualities) else "best"
        except ValueError:
            print("⚠️ Invalid input. Defaulting to 'best'.")
            selected_quality = "best"

        download_video(video_url, selected_quality)
