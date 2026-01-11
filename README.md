# 🎤 Offline Voice-Controlled PowerPoint Controller

A Python-based **offline voice-controlled presentation controller** that allows you to navigate PowerPoint slides using simple voice commands like **“next slide”** and **“previous slide”** — without any internet connection.

Built using **Vosk (offline speech recognition)**, **PyAudio**, and **PyAutoGUI**.

---

## 🚀 Features

* ✅ Fully **offline speech recognition**
* ✅ Runs in background
* ✅ Hands-free PowerPoint control
* ✅ Supports wake-word based commands
* ✅ Works with PowerPoint, PDFs, Google Slides
* ✅ Lightweight and fast

---

## 🗂️ Project Structure

```
audio_ppt_controller/
│
├── main.py
├── requirements.txt
├── vosk-model-small-en-us-0.15/
│   └── (speech model files)
└── README.md
```

---

## 🧠 Supported Voice Commands

| Voice Command        | Action               |
| ---------------------| -------------------- |
| `next slide`         | Next slide           |
| `next      `         | Next slide           |
| `previous slide`     | Previous slide       |
| `previous      `     | Previous slide       |
| `start presentation` | Start slideshow (F5) |
| `exit`               | Stop program         |
| `stop`               | Stop program         |
| `stop presentation`  | Stop program         |

> 💡 Wake word **"assistant"** improves accuracy and avoids false triggers.

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jigneshshiyal/audio_ppt_controller
cd audio_ppt_controller
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

⚠️ **If PyAudio installation fails on Windows**
Download precompiled wheel from:
[https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
Then install using:

```bash
pip install PyAudio-0.2.xx-cp3x-win_amd64.whl
```

---

## 📦 Download Vosk Offline Model

Download the English model:

🔗 [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)

Recommended:

```
vosk-model-small-en-us-0.15
```

Extract it inside the project directory and update the path in `main.py`:

```python
MODEL_PATH = r"path_to_vosk_model"
```

---

## ▶️ Run the Application

1. Open **PowerPoint**
2. Focus the presentation window
3. Run:

```bash
python main.py
```

4. Speak commands 🎙️

---

## 🔍 How It Works

* **Vosk** → Converts microphone audio to text (offline)
* **PyAudio** → Streams live microphone input
* **PyAutoGUI** → Simulates keyboard actions
* **Grammar restriction + wake word** → High accuracy

---

## 🧪 Accuracy Tips

* Use **clear, short commands**
* Speak after a short pause
* Avoid background noise
* Use a headset mic for best results

<!-- ---

## 🧾 Resume / Portfolio Description

> Developed an **offline voice-controlled PowerPoint automation tool** using Python and Vosk, enabling hands-free slide navigation without internet dependency.

---

## 📜 License

MIT License (free to use and modify)

---

If you want, I can also:

* Add **badges**
* Make **professional screenshots**
* Write **GitHub project description**
* Prepare **EXE packaging guide**

Just tell me 👍 -->
