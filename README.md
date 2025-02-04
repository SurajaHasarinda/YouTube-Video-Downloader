## Setting up ffmpeg on Windows 🛠️

1. Open Start Menu and search for "Environment Variables", then click "Edit the system environment variables".
2. In the System Properties window, click "Environment Variables...".
3. Under `System variables`, find and select `Path`, then click Edit...
4. Click `New` and enter:
  ```bash
  <your-ffmpeg-path>\ffmpeg\bin
  ```
5. Click `OK` on all windows to save changes.

## Setting up python on Windows 🐍

1. Open directory in command prompt.
2. Create a virtual environment.
  ```bash
  python -m venv venv
  ```
3. Activate the virtual environment.
  ```bash
  .\venv\Scripts\activate
  ```
4.. Install `yt-dlp` library.
  ```bash
   pip install yt-dlp
  ```

## Downloading videos from YouTube 💾

1. Run the `yt-downloader.py` script.
2. Enter the URL of the YouTube video you want to download.
