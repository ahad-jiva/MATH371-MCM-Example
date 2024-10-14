import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# function to calculate an n-window simple moving average of a list of values
# input a filename string and moving average window size as int
def s_mov_avg(data: str, window_size: int):
    asset_val = np.loadtxt(data)
    i = 0

    averages = []

    while i < len(asset_val) - window_size + 1:
        window_avg = round(np.sum(asset_val[i:i + window_size]) / window_size, 2)
        averages.append(window_avg)
        i += 1

    return averages


# function to calculate an n-window exponential moving average of a list of values
def e_mov_avg(data: str, window_size: int):
    asset_val = np.loadtxt(data)
    df = pd.DataFrame(asset_val)
    averages = df.ewm(span=window_size, adjust=False).mean().values.tolist()
    output = []
    for element in averages:
        output.append(element[0])
    return output



period = 100
weighting_factor = 0.2

print(e_mov_avg('bitcoin_price.txt', period))

ema = e_mov_avg('bitcoin_price.txt', period)
sma = s_mov_avg('bitcoin_price.txt', period)
plt.plot(np.loadtxt('bitcoin_price.txt'))
plt.plot(ema, label="EMA")
plt.plot(sma, label="SMA")
plt.legend()

plt.show()
