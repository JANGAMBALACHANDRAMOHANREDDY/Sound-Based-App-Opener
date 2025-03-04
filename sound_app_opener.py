import os
import sounddevice as sd
import numpy as np

# Sound detection settings
duration = 2  # seconds to listen
threshold = 0.1  # Lowered threshold to detect quieter sounds

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
    print(f"Sound level: {volume_norm:.2f}")
    if volume_norm > threshold:
        print("Sound detected!")
        app_name = input("Enter app name to open (chrome, notepad, calculator, vscode): ").strip().lower()
        open_app(app_name)

print("Listening for sounds... (Clap or make a loud sound)")
with sd.InputStream(callback=detect_sound):
    sd.sleep(int(duration * 100000))
