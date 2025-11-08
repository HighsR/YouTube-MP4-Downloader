# Simple YouTube MP4 Downloader 🎬

A simple Python script that uses `yt-dlp` to download any YouTube video. It automatically selects the best video and audio, merges them, and saves the file as an MP4 named after the video's title (e.g., `My Video Title.mp4`).

---

## ✨ Features

* **Best Quality:** Automatically finds the best MP4 video (`bestvideo[ext=mp4]`) and best M4A audio (`bestaudio[ext=m4a]`) streams.
* **Merges Automatically:** Combines the separate video and audio files into a single, high-quality MP4 file.
* **Smart Naming:** Saves the file using the video's official title (e.g., `Funny Cat Video.mp4`).

---

## 🔧 Requirements

1.  **Python 3.x**
2.  **`yt-dlp` Python library:**
    ```bash
    pip install yt-dlp
    ```
3.  **FFmpeg:** **(Required for merging)**
    `yt-dlp` needs FFmpeg to be installed on your system to combine the video and audio.
    * **Windows:** [Download FFmpeg](https://ffmpeg.org/download.html) and add the `bin` folder to your system's PATH.
    * **macOS (using Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    * **Linux (using apt):**
        ```bash
        sudo apt install ffmpeg
        ```

---

## 🚀 How to Use

1.  Save the code as a Python file (e.g., `download.py`).
2.  Run the script from your terminal:
    ```bash
    python download.py
    ```
3.  When prompted, paste the full YouTube video URL and press Enter:
    ```
    Enter the YouTube video URL: [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
    ```
4.  The script will download and merge the video. The final `.mp4` file will appear in the same folder as the script.
---

## ⚠️ Disclaimer

This script is provided for educational purposes only. It is intended to be used as a learning tool to understand how video downloading and processing can be automated with Python.

Do not use this script to download copyrighted content. The user is solely responsible for ensuring they have the rights to download and use any content. The author of this script assumes no liability for any misuse.
---

## 📄 License

This project is distributed under the **Educational Use License** — see the [LICENSE](./LICENSE) file for full details.

> ⚠️ This tool is provided **for personal and educational purposes only**.  
> Redistribution, resale, or use of this software to download copyrighted
> material may violate **YouTube’s Terms of Service** and applicable laws.  
> Use responsibly.
---
## 🙏 Credits & Libraries

This project uses the following open-source tools:

- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) —  
  A modern, actively maintained fork of `youtube-dl` that handles video and audio downloads, format selection, and metadata merging.  
  Licensed under the [Unlicense](https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE).

- [**FFmpeg**](https://ffmpeg.org/) —  
  A cross-platform multimedia framework used to merge and convert audio/video streams.  
  Licensed under the [GNU LGPL v2.1](https://ffmpeg.org/legal.html) or later.

> All credit for these underlying tools belongs to their respective authors and contributors.  
> This project simply provides a lightweight Python interface for educational demonstration purposes.
