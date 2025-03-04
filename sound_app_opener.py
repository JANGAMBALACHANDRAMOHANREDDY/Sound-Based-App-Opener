import os
import sounddevice as sd
import numpy as np

# Sound detection settings
duration = 2  # seconds to listen
threshold = 0.3  # adjust based on your environment

def open_app():
    print("Sound detected! Opening an app...")
    # Add your apps here
    os.system("start chrome")  # Opens Google Chrome
    # os.system("start notepad")  # Opens Notepad
    # os.system("calc")  # Opens Calculator

def detect_sound(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        open_app()

print("Listening for sounds... (Clap or make a loud sound)")
with sd.InputStream(callback=detect_sound):
    sd.sleep(int(duration * 100000))
