import numpy as np

from nova_audio.core.signal import generate_sine


def test_generate_sine():
    frequency = 440.0  # A4 note
    amplitude = 1.0
    sample_rate = 44100
    duration = 1.0

    signal = generate_sine(frequency, amplitude, sample_rate, duration)

    assert isinstance(signal, np.ndarray)
    assert len(signal) == int(sample_rate * duration)
    assert np.max(signal) <= amplitude
    assert np.min(signal) >= -amplitude