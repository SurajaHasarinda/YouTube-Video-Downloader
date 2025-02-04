## Setting up ffmpeg on Windows 🛠️

1. Open Start Menu and search for "Environment Variables", then click "Edit the system environment variables".
2. In the System Properties window, click "Environment Variables...".
3. Under `System variables`, find and select `Path`, then click Edit...
4. Click `New` and enter:
  ```bash
  <your-ffmpeg-path>\ffmpeg\bin
  ```
5. Click `OK` on all windows to save changes.

## Downloading videos from YouTube 💾

1. Install `yt-dlp` library.
  ```bash
   pip install yt-dlp
  ```
2. Run the `yt-downloader.py` script.
3. Enter the URL of the YouTube video you want to download.
