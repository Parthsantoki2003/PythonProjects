🖥️ System Health Viewer

A simple Python tool to keep an eye on your computer’s vital stats in real time.
It shows your CPU usage, RAM usage, disk space, and battery level — all in a clean, refreshing terminal view.

✨ Features

* 📊 **Live Updates** — refreshes every 2 seconds with the latest system info.
* ⚡ **CPU Usage** — see how hard your processor is working.
* 🧠 **RAM Usage** — monitor memory consumption in real time.
* 💽 **Disk Usage** — check how much storage space you’re using.
* 🔋 **Battery Info** — percentage and charging status (if available).
* 🪶 Lightweight and easy to run — no complex setup needed.

🛠 Requirements

* Python 3.7+
* `psutil` library (install with `pip install psutil`)
* Works on Windows, Linux, and macOS

📦 Installation

1. Download or copy the script to your computer.
2. Install the required library:

  
   pip install psutil
  
▶ Usage

Run the script in your terminal:

python system_monitor.py


Example output:

=== System Health Monitor ===
🖥️ CPU Usage: 15%
📊 RAM Usage: 48%
💽 Disk Usage: 67%
🔋 Battery: 85% (Charging)
⚠ Notes

* Refresh rate can be adjusted by changing the `time.sleep(1)` value in the code.
* Battery info may not appear on desktop PCs or servers without a battery.

📜 License

Free to use, modify, and share for personal or educational purposes.(Give credits if you are using it)
