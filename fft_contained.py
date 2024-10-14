import numpy as np


# calculate fft of a list of data
# refactored from test_fft2.py
def fft(data_csv: str):
    asset_val = np.loadtxt(data_csv, delimiter=',')

    modes = 20

    n = len(asset_val)
    dt = 1
    t = np.arange(0, n, dt)

    ghat = np.fft.fft(asset_val, n)  # Compute the FFT
    PSD = ghat * np.conj(ghat) / n  # Power spectrum (power per freq)
    freq = (1 / (n)) * np.arange(n)  # Create x-axis of frequencies in per day units
    L = np.arange(1, np.floor(n / 2), dtype='int')  # Only plot the first half of freqs

    to_clean = np.zeros(len(PSD))
    to_clean[:modes] = 1
    PSDclean = PSD * to_clean
    ghat = ghat * to_clean
    gfilt = np.fft.ifft(ghat)

    return gfilt.real

