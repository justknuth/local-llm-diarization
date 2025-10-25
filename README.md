Here's a complete, human-readable `README.md` for your Whisper + Pyannote diarization project that walks someone through *everything* from scratch, assuming they just got a fresh computer:

---

# 🎙️ Transcription + Speaker Diarization with Whisper & Pyannote

This project uses OpenAI's [Whisper](https://github.com/openai/whisper) for **speech-to-text transcription** and [pyannote-audio](https://github.com/pyannote/pyannote-audio) for **speaker diarization** (i.e., figuring out "who spoke when").

> ✅ Works with audio or video files
> 🚀 GPU-accelerated with CUDA
> 🔐 Requires Hugging Face token (free account)
> 📁 Outputs timestamped transcripts with speaker labels

---

## 📋 Table of Contents

1. [Pre-requisites](#-pre-requisites)
2. [Installation Steps](#-installation-steps)
3. [Usage](#-usage)
4. [Example Output](#-example-output)
5. [Troubleshooting](#-troubleshooting)
6. [Credits](#-credits)

---

## 📦 Pre-requisites

**System Requirements:**

* A machine running Linux or Windows
* A GPU with **at least 4 GB VRAM** recommended (e.g., NVIDIA)
* Python **3.9 to 3.11** (avoid Python 3.12+ — some libraries may not yet support it)
* pip (Python package installer)

**Python Libraries Used:**

* `openai-whisper`
* `pyannote.audio`
* `torch`
* `torchaudio`
* `ffmpeg-python`
* `python-dotenv` (for managing your Hugging Face token)

---

## ⚙️ Installation Steps

Follow these step-by-step instructions.

### 1. ✅ Install Python

Install Python from the official site:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
Make sure to **check "Add Python to PATH"** during installation.

Then verify:

```bash
python --version
pip --version
```

---

### 2. 💻 Set up a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Linux/macOS
```

---

### 3. 📦 Install Required Packages

```bash
pip install --upgrade pip setuptools wheel

# Install Whisper
pip install git+https://github.com/openai/whisper.git

# Install PyTorch for your GPU
# Follow the instructions here: https://pytorch.org/get-started/locally/

# Example for Windows + CUDA 11.8:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install other dependencies
pip install pyannote.audio ffmpeg-python python-dotenv
```

---

### 4. 🔐 Set Up Hugging Face Token

1. Go to: [https://huggingface.co/join](https://huggingface.co/join) → create a free account

2. Then go to: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) → click **New Token**

   * Scope: **Read**
   * Copy the token

3. In your project folder, create a `.env` file and paste:

```env
HUGGINGFACE_TOKEN=your_token_here
```

---

## ▶️ Usage

Run the script from the command line:

```bash
python transcribe_diarize.py --input "your_audio_or_video.wav" --output "results.txt"
```

* Input file can be `.mp4`, `.wav`, `.mp3`, etc.
* Output is a plain text file with timestamped, speaker-labeled segments.

---

## 📝 Example Output

```
=== Transcript ===
[0.00s - 4.20s] SPEAKER_00: Hello everyone, welcome to the meeting.
[4.21s - 7.80s] SPEAKER_01: Thanks, good to be here.
[7.81s - 12.50s] SPEAKER_00: Let's get started with today's agenda...
```

---

## 🧠 Notes + Troubleshooting

* If you run out of GPU memory, use the `base` or `small` Whisper models:

  ```python
  whisper.load_model("base", device="cuda")
  ```
* Diarization will be inaccurate if the audio is low quality or has overlapping speech.
* If you're seeing `nan` errors from Whisper, try:

  * Reducing model size
  * Using `fp16=False` in `transcribe(...)` (especially on small GPUs)

---

## 🙌 Credits

* [Whisper](https://github.com/openai/whisper) by OpenAI
* [pyannote-audio](https://github.com/pyannote/pyannote-audio) by Hervé Bredin
* Maintained and used by: *You!*

---

Let me know if you want this in a downloadable file or automatically placed into your repo structure.
