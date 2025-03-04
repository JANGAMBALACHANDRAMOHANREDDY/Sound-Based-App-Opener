import os
import sounddevice as sd
import numpy as np

# Sound detection settings
duration = 2  # seconds to listen
threshold = 0.3  # adjust based on your environment

# Define app commands
app_commands = {
    "chrome": "start chrome",
    "notepad": "start notepad",
    "calculator": "calc",
    "vscode": "code"
}

def open_app(app_name):
    command = app_commands.get(app_name.lower())
    if command:
        print(f"Opening {app_name}...")
        os.system(command)
    else:
        print(f"App '{app_name}' not recognized.")

def detect_sound(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        print("Sound detected! Choose an app to open: chrome, notepad, calculator, vscode")
        app_name = input("Enter app name: ")
        open_app(app_name)

print("Listening for sounds... (Clap or make a loud sound)")
with sd.InputStream(callback=detect_sound):
    sd.sleep(int(duration * 100000))
