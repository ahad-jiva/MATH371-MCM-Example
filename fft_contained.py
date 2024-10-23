import numpy as np


# calculate fft of a list of data
# refactored from test_fft2.py
def fft(data_csv: str):
    asset_val = np.loadtxt(data_csv, delimiter=',')

    modes = 20

    n = len(asset_val)
    ghat = np.fft.fft(asset_val, n)  # Compute the FFT
    PSD = ghat * np.conj(ghat) / n  # Power spectrum (power per freq)

    to_clean = np.zeros(len(PSD))
    to_clean[:modes] = 1
    ghat = ghat * to_clean
    gfilt = np.fft.ifft(ghat)

    return gfilt.real

