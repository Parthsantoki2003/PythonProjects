Got it — I’ll make a **README.md** for a YouTube Video Downloader in Python using `yt-dlp`.
You can drop this file in your project folder so GitHub (or anyone else) knows how to use it.


# 🎥 YouTube Video Downloader (Python + yt-dlp)

A simple Python script to download YouTube videos in the highest quality using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).  
This tool works for single videos, playlists, and even other supported sites like Instagram, Twitter, and Facebook.


📌 Features
- Download videos in the **best quality available**  
- Save videos with their **original title**  
- Supports **hundreds of sites** (YouTube, Instagram, Twitter, etc.)  
- Playlist support  
- Audio-only download option (MP3)  


## 🛠️ Requirements
- **Python 3.7+** installed  
- Internet connection  

---

## 📦 Installation

1. Install dependencies
   python -m pip install yt-dlp
  


## Download a video

Enter the YouTube video URL when prompted, and it will download in the highest quality.

## 🎵 Download Audio Only (MP3)

Change `ydl_opts` to:

```python
ydl_opts = {
    'format': 'bestaudio',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
```

---

## ⚠ Disclaimer

This script is for **personal use only**.
Downloading copyrighted content without permission may violate YouTube’s [Terms of Service](https://www.youtube.com/static?template=terms) and applicable laws.

---

💡 Author

* **Parth Santoki** – [GitHub Profile](https://github.com/Parthsantoki2003)

