# Local Transcription & Diarization Pipeline

This project is a local pipeline that processes audio files to:
1.  **Transcribe:** Convert speech to text using **Whisper**.
2.  **Diarize:** Identify *who* spoke *when* using **Pyannote.audio**.

The main script processes all files from the `inbound/` folder and saves the results to the `outbound/` folder.

## Prerequisites

Before you begin, you **must** have the following:

1.  **An NVIDIA GPU with CUDA:** This project is designed for GPU acceleration. The models will be extremely slow (or fail) on a CPU.
2.  **Python 3.10+**
3.  **A Hugging Face Account & Token:**
    * The `pyannote` models are "gated," which means you need to agree to their terms of use.
    * Create an account at [huggingface.co](https://huggingface.co/).
    * Go to the [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1) model page and agree to the terms.
    * Go to the [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0) model page and agree to the terms.
    * Go to your [Hugging Face Settings](https://huggingface.co/settings/tokens) and create a new Access Token. You will need this token in the setup step.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/LOCAL-LLM-DIARIZATION.git](https://github.com/YOUR_USERNAME/LOCAL-LLM-DIARIZATION.git)
    cd LOCAL-LLM-DIARIZATION
    ```

2.  **Create and activate the virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    
    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    *(This assumes you have created the `requirements.txt` file as requested)*.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create your Environment File:**
    * Create a new file in the root folder named `.env`.
    * Add your Hugging Face token to it like this:

    ```env
    HF_TOKEN=hf_YOUR_TOKEN_GOES_HERE
    ```

## How to Use

1.  **Add Audio:**
    * Place your `.wav` or `.mp3` files into the `inbound/` folder.

2.  **Run the Pipeline:**
    * Execute the PowerShell script:
    ```powershell
    .\run_transcribe_diarize.ps1
    ```

3.  **Get Results:**
    * The script will process each file and save a raw `.json` output in the `outbound/` folder. This file contains the transcription text, timestamps, and generic speaker labels (e.g., `SPEAKER_00`, `SPEAKER_01`).

4.  **(Optional) Post-Processing:**
    * To get a more human-readable output, use the `replace_with_real_names.py` script to map the generic speaker labels to actual names (e.g., "John", "Jane").
    *(You may need to edit this script or check its code to see how it expects you to provide the names).*
