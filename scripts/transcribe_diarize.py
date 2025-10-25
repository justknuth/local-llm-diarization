import argparse
from pathlib import Path
import whisper
import torch
from pyannote.audio import Pipeline, Model
import os
from dotenv import load_dotenv

load_dotenv() 

# Avoids symlink creation and makes model usage more stable on Windows.
os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"

# Load hugging face token from .env. Token is needed even if model is cached.
token = os.getenv("HUGGINGFACE_TOKEN")

model = Model.from_pretrained("pyannote/segmentation", use_auth_token=token)

# This downloads the model. It should be run once and then commented out. Use the 'pipeline' below this one.
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token=token)

# After you run the script once, and the model is downloaded (Above), the below line gets the model from cache.
# pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=token)
pipeline.to(torch.device("cuda"))
whisper_model = whisper.load_model("large", device="cuda")

print("Whisper model loaded on:", whisper_model.device)
print("PyTorch using CUDA:", torch.cuda.is_available())


 # Load Whisper model


def get_speaker_for_segment(start, end, diarization):
    prominent_speaker = "UNKNOWN"
    max_overlap = 0.0
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        overlap = max(0.0, min(end, turn.end) - max(start,turn.start))
        if (overlap > max_overlap):
            max_overlap = overlap
            prominent_speaker = speaker
    return prominent_speaker


def main(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)

   

    # Transcribe audio/video | 
    # 'fp16=False' must be explicitly set if your GPU's dedicated VRAM < 4gb (estimate based on my machine with 4gb VRAM)
    print(f"Transcribing {input_path}...")
    result = whisper_model.transcribe(str(input_path), fp16=False)

    print("Running diarization")
    diarization = pipeline(str(input_path))


    # Combine or save outputs (example: save text + diarization segments)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== Transcript ===\n")
        for seg in result["segments"]:
            start, end, text = seg["start"], seg["end"], seg["text"]
            speaker = get_speaker_for_segment(start, end, diarization)
            f.write(f"[{start:.2f}s - {end:.2f}s] {speaker}: {text}\n")
        # f.write(result["text"] + "\n\n")
        # f.write("=== Diarization Segments ===\n")

       # ''' for turn, _, speaker in diarization.itertracks(yield_label=True):
       #     f.write(f"{turn.start:.1f}s - {turn.end:.1f}s: Speaker {speaker}\n") '''

    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe and diarize audio/video")
    parser.add_argument("--input", required=True, help="Input media file")
    parser.add_argument("--output", required=True, help="Output result file")
    args = parser.parse_args()

    main(args.input, args.output)
