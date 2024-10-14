
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

my_file = 'LBMA-GOLD.csv'
modes_to_keep = 20
gold_val = np.loadtxt('gold_price.txt',delimiter=',')
bitcoin_val = np.loadtxt('bitcoin_price.txt',delimiter=',')


#plt.plot(gold_val)
#plt.show()

n = len(gold_val)

dt = 1
t = np.arange(0,n,dt)

ghat = np.fft.fft(gold_val,n)          # Compute the FFT
PSD = ghat * np.conj(ghat) / n         # Power spectrum (power per freq)
freq = (1/(n)) * np.arange(n)          # Create x-axis of frequencies in per day units
L = np.arange(1,np.floor(n/2),dtype='int') # Only plot the first half of freqs

to_clean = np.zeros(len(PSD))
to_clean[:modes_to_keep] = 1
PSDclean = PSD * to_clean
ghat = ghat * to_clean
gfilt = np.fft.ifft(ghat)

#plt.plot(freq,ghat,color='r',linewidth=1.5)


#plt.plot(freq[L],PSD[L],color='r',linewidth=2)
#plt.plot(t,gfilt,linewidth=1.5)

#plt.show()

print(gfilt.real)
