import sys
from pathlib import Path

import torch
from transformers import pipeline


MODEL_ID = "openai/whisper-tiny"


def main() -> None:
    if len(sys.argv) > 2:
        print("Usage: python examples/transcribe_audio.py [audio_file_path]")
        raise SystemExit(1)

    audio_file_path = Path(sys.argv[1])

    if not audio_file_path.is_file():
        print(f"Error: {audio_file_path} is not a valid file.")
        raise SystemExit(1)

    if not torch.backends.mps.is_available():
        raise RuntimeError("Warning: MPS (Metal Performance Shaders) is not available. Using CPU for inference.")

    print(f"Loading model '{MODEL_ID}'...")
    print("In the first run data will be downloaded, this may take a while depending on your system and internet connection.")

    transcriber = pipeline(
        task="automatic-speech-recognition",
        model=MODEL_ID,
        device="mps"
    )

    print(f"Transcribing audio file: {audio_file_path}")

    result = transcriber(
        str(audio_file_path),
        generate_kwargs={
            "language": "portuguese",
            "task": "transcribe",
        },
    )

    print("\nTranscription result:")
    print(result["text"].strip())


if __name__ == "__main__":
    main()
