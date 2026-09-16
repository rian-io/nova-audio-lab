import matplotlib.pyplot as plt

from nova_audio.core.signal import generate_sine


def main():
    frequency = 440.0  # A4 note
    amplitude = 1.0
    sample_rate = 44100
    duration = 1.0

    signal = generate_sine(frequency, amplitude, sample_rate, duration)

    samples_to_plot = int(sample_rate * 0.01)

    plt.plot(signal[:samples_to_plot])
    plt.title(f"Sine Wave: {frequency} Hz")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
