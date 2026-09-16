import numpy as np

def generate_sine(frequency: float, amplitude: float, sample_rate: int, duration: float) -> np.ndarray:
    """
    Generate a sine wave signal.

    Parameters:
    frequency (float): Frequency of the sine wave in Hz.
    amplitude (float): Peak amplitude of the sine wave.
    sample_rate (int): Number of samples per second.
    duration (float): Duration of the signal in seconds.

    Returns:
    np.ndarray: Array containing the generated sine wave samples.
    """
    number_of_samples = int(sample_rate * duration)
    signal = np.zeros(number_of_samples)

    for sample in range(number_of_samples):
        t = sample / sample_rate
        sample_value = amplitude * np.sin(2 * np.pi * frequency * t)
        signal[sample] = sample_value

    #t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    #signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal