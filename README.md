# 📁 Folder Launcher App

A simple and stylish desktop tool built with Python + Flask to **instantly open your frequently used folders** via a modern browser-based interface.

---

## 🚀 Features

- 🌐 Clean web UI using **Bootstrap 5**
- 🌙 **Dark mode toggle** for night-friendly use
- 📂 Folder icons for visual navigation
- 🖱️ One-click to open local folders (Windows only)
- 🧠 Remembers dark mode setting
- 🪄 Auto-launches in your browser on startup
- 🔽 Minimizes the terminal window on launch for a clean look

---

## 🎯 Use Case

As a developer and student, I often found myself constantly digging through long file paths to open my project folders — whether it's Capstone work, screenshots, side projects, or class material. Opening these folders manually every day was a small but repetitive friction — and we all know how those add up! 😓

Instead of navigating through deep directories every time, this Script gives you **instant access to your most-used folders** with one click.

---

## 🧰 Tech Stack

- `Python 3.x`
- `Flask`
- `Bootstrap 5`
- `Webbrowser` (opens browser automatically)
- `ctypes` (to minimize terminal window)

---

## 📦 Installation & Setup

1. **Clone the repo**:
   git clone https://github.com/yourusername/Folder-Launcher-Python.git
   cd Folder-Launcher-Python

2. **Install dependencies**:

   ```
   pip install flask
   ```

3. **Edit your folder paths** in `app.py`:

   ```
   FOLDERS = {
       "My Project": r"C:\path\to\project",
       "Screenshots": r"C:\Users\Me\Pictures\Screenshots",
       ...
   }
   ```

4. **Run the app**:

   ```
   python app.py
   ```

5. It will auto-launch in your browser at:
   `http://127.0.0.1:5000`

---

## 📸 Screenshot

![screenshot](screenshots/folder-launcher-ui.png)

---

## 📄 License

MIT License

## 🙌 Author

Made with ❤️ by [Lokeswara Reddy](https://www.linkedin.com/in/lokeswaramuthumula/)
