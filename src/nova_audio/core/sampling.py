import numpy as np

def sample_signal(signal: np.ndarray, original_sample_rate: int, target_sample_rate: int) -> np.ndarray:
    """
    Sample a signal to a different sample rate.

    Parameters:
    signal (np.ndarray): Input signal to be sampled.
    original_sample_rate (int): Original sample rate of the input signal.
    target_sample_rate (int): Desired sample rate for the output signal.

    Returns:
    np.ndarray: Array containing the sampled signal.
    """
    # Calculate the resampling factor
    resample_factor = target_sample_rate / original_sample_rate

    # Calculate the number of samples in the resampled signal
    num_samples = int(len(signal) * resample_factor)

    # Create an array of indices for the resampled signal
    resampled_indices = np.linspace(0, len(signal) - 1, num_samples)

    # Use linear interpolation to sample the signal at the new indices
    resampled_signal = np.interp(resampled_indices, np.arange(len(signal)), signal)

    return resampled_signal


def resample_signal(signal: np.ndarray, original_sample_rate: int, target_sample_rate: int) -> np.ndarray:
    """
    Resample a signal to a different sample rate using Fourier method.

    Parameters:
    signal (np.ndarray): Input signal to be resampled.
    original_sample_rate (int): Original sample rate of the input signal.
    target_sample_rate (int): Desired sample rate for the output signal.

    Returns:
    np.ndarray: Array containing the resampled signal.
    """
    # Calculate the resampling factor
    resample_factor = target_sample_rate / original_sample_rate

    # Calculate the number of samples in the resampled signal
    num_samples = int(len(signal) * resample_factor)

    # Perform Fourier transform on the input signal
    freq_domain_signal = np.fft.fft(signal)

    # Create an array of frequencies for the original and target sample rates
    original_freqs = np.fft.fftfreq(len(signal), d=1/original_sample_rate)
    target_freqs = np.fft.fftfreq(num_samples, d=1/target_sample_rate)

    # Interpolate the frequency domain signal to match the target frequencies
    resampled_freq_domain_signal = np.interp(target_freqs, original_freqs, freq_domain_signal)

    # Perform inverse Fourier transform to get the time domain resampled signal
    resampled_signal = np.fft.ifft(resampled_freq_domain_signal)

    return np.real(resampled_signal)
