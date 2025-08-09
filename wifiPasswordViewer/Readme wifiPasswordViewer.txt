📶 Wi-Fi Password Viewer

A small Python script to view all saved Wi-Fi networks and their passwords on your Windows PC.
Perfect for those moments when you’ve forgotten a Wi-Fi password but it’s still stored on your device.


✨ Features

* Lists all saved Wi-Fi profiles on your PC.
* Displays each network’s password (if available).
* Works entirely offline — no internet connection needed.
* Simple and lightweight, runs directly in the terminal.

🛠 Requirements

* **Windows** (uses `netsh` command, not compatible with macOS/Linux)
* Python 3.7+ installed


📦 Installation

1. Clone or download this repository.
2. Save the script as `wifi_passwords.py` (or any name you prefer).

▶ Usage

Open Command Prompt or PowerShell and run:


python wifi_passwords.py


Example output:


Saved Wi-Fi Networks & Passwords:

📶 My_Home_WiFi — 🔑 mysecretpass123
📶 Cafe_WiFi — 🔑 coffee4life
📶 Old_Network — 🔑 N/A
```


⚠ Notes

* Some networks may show `N/A` if the password was never stored or requires admin access.
* If you get an error, try running the script as **Administrator**.
* This script is for **personal use only** — don’t use it on other people’s devices without permission.

📜 License

This project is open-source and free to use for educational or personal purposes but you should give credit. 


