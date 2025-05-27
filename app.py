from flask import Flask, render_template_string, redirect, url_for
import os
import webbrowser
import ctypes
import sys

app = Flask(__name__)

FOLDERS = {
    "Downloads": r"C:\Users\yourpcname\Downloads",
    "Desktop": r"C:\Users\yourpcname\Desktop",
    "Screenshots": r"C:\Users\yourpcname\Pictures\Screenshots",
    "Projects": r"D:\Projects"
}

@app.route("/")
def home():
    return render_template_string(""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>📁 Folder Launcher</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
                padding-top: 60px;
                transition: background-color 0.3s, color 0.3s;
            }
            .dark-mode {
                background-color: #121212;
                color: white;
            }
            .dark-mode .card {
                background-color: #1e1e1e;
                color: white;
                border-color: #333;
            }
            .folder-card {
                transition: transform 0.2s ease;
            }
            .folder-card:hover {
                transform: scale(1.02);
            }
            code {
                font-size: 0.85em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h1 class="mb-0">📁 My Folder Launcher</h1>
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" id="darkModeToggle">
                  <label class="form-check-label" for="darkModeToggle">🌙 Dark Mode</label>
                </div>
            </div>
            <div class="row">
                {% for name, path in folders.items() %}
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card folder-card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title"><i class="bi bi-folder-fill text-warning me-2"></i>{{ name }}</h5>
                            <p class="card-text"><code>{{ path }}</code></p>
                            <a href="{{ url_for('open_folder', folder_name=name) }}" class="btn btn-primary">Open Folder</a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

        <script>
            const toggle = document.getElementById('darkModeToggle');
            toggle.addEventListener('change', () => {
                document.body.classList.toggle('dark-mode');
                localStorage.setItem('darkMode', toggle.checked);
            });

            window.onload = () => {
                if (localStorage.getItem('darkMode') === 'true') {
                    document.body.classList.add('dark-mode');
                    toggle.checked = true;
                }
            };
        </script>
    </body>
    </html>
    """, folders=FOLDERS)

@app.route("/open/<folder_name>")
def open_folder(folder_name):
    path = FOLDERS.get(folder_name)
    if path and os.path.exists(path):
        os.startfile(path)
    return redirect(url_for('home'))

def minimize_terminal():
    if sys.platform == "win32":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    minimize_terminal()
    app.run(debug=False)
