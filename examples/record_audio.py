import sounddevice as sd
import soundfile as sf

def main() -> None:
    sample_rate = 16_000
    duration = 5

    print("Recording for 5 seconds... Speak now!")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    output_path = "output.wav"
    sf.write(output_path, audio, sample_rate)

    print(f"Gravação salva em: {output_path}")
    print(f"Formato: {audio.shape}")
    print(f"Tipo de dado: {audio.dtype}")
    print(f"Taxa de amostragem: {sample_rate} Hz")
    print(f"Duração: {len(audio) / sample_rate:.2f} segundos")
    print(f"Amplitude máxima: {abs(audio).max():.4f}")

    print("Reproduzindo a gravação...")
    sd.play(audio, samplerate=sample_rate)
    sd.wait()

if __name__ == "__main__":
    main()
