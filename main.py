import json
import pyaudio
import pyautogui
from vosk import Model, KaldiRecognizer

MODEL_PATH = r"C:\Users\jigne\Documents\project\audio_ppt_controller\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15"

commands = [
    "next slide",
    "next",
    "previous",
    "previous slide",
    "start presentation",
    "exit",
    "stop presentation"
    "stop"
]

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000, json.dumps(commands))
recognizer.SetWords(True)

mic = pyaudio.PyAudio()

stream = mic.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=2048
)

stream.start_stream()

print("🎤 Say: assistant next slide")

while True:
    data = stream.read(2048, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        text = json.loads(recognizer.Result()).get("text", "")
        print("Heard:", text)

        if text ==  "next slide" or text == "next":
            pyautogui.press("right")

        elif text == "previous slide" or text == "previous":
            pyautogui.press("left")

        elif text == "start presentation":
            pyautogui.press("f5")
        elif text == "stop presentation" or text == "exit":
            pyautogui.press("esc")

        elif text == "exit":
            break

stream.stop_stream()
stream.close()
mic.terminate()
