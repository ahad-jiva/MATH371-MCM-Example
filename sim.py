from fft_contained import fft
from moving_avgs import *
import matplotlib.pyplot as plt
import numpy as np
from trade_actions import *

# bitcoin_fft = fft('bitcoin_price.txt')
# gold_fft = fft('gold_price.txt')


# plt.plot(bitcoin_prices)
# plt.plot(bitcoin_fft)
# plt.plot(btc_s_mov_avg)
# plt.show()

btc_purchases = 0
btc_sales = 0

gold_purchases = 0
gold_sales = 0


def sim(moving_avg_window: int):
    init_capital = 1000
    portfolio = [init_capital, 0, 0]

    bitcoin_prices = np.loadtxt('bitcoin_price.txt')
    btc_s_mov_avg = s_mov_avg('bitcoin_price.txt', moving_avg_window)
    btc_purchase_quantity = 1
    btc_sell_quantity = 1

    gold_prices = np.loadtxt('gold_price.txt')
    gold_s_mov_avg = s_mov_avg('gold_price.txt', moving_avg_window)
    gold_purchase_quantity = 1
    gold_sell_quantity = 1

    for i in range(min(len(btc_s_mov_avg), len(gold_s_mov_avg)) - 1):
        # todo: include functionality for gold trading restrictions
        if (bitcoin_prices[i] < btc_s_mov_avg[i - 1]) and (
                portfolio[0] > (btc_purchase_quantity * bitcoin_prices[i]) + (
                0.02 * btc_purchase_quantity * bitcoin_prices[i])):
            buy_bitcoin(btc_purchase_quantity, bitcoin_prices[i], portfolio)
            # btc_purchases += 1
        if bitcoin_prices[i] > btc_s_mov_avg[i - 1]:
            sell_bitcoin(btc_sell_quantity * portfolio[2], bitcoin_prices[i], portfolio)
            # btc_sales += 1
        if (gold_prices[i] < gold_s_mov_avg[i - 1]) and (portfolio[0] > (gold_purchase_quantity * gold_prices[i]) + (
                0.01 * gold_purchase_quantity * gold_prices[i])):
            buy_gold(gold_purchase_quantity, gold_prices[i], portfolio)
            # gold_purchases += 1
        if gold_prices[i] > gold_s_mov_avg[i - 1]:
            sell_gold(gold_sell_quantity * portfolio[1], gold_prices[i], portfolio)
            # gold_sales += 1

    pf_value = round(portfolio[0] + (gold_prices[len(gold_prices) - 1] * portfolio[1]) + (
                bitcoin_prices[len(bitcoin_prices) - 1] * portfolio[2]), 2)
    # print(portfolio)
    # print('${:,.2f}'.format(pf_value))
    return pf_value
    # print(f'Bought and sold BTC {btc_purchases} and {btc_sales} times, respectively.')
    # print(f'Bought and sold gold {gold_purchases} and {gold_sales} times, respectively.')


results = []

for j in range(1, 251):
    results.append(sim(j))
plt.bar(list(range(1, 251)), results, width=0.6)
plt.xlabel("N-day moving average")
plt.ylabel("Total portfolio value (millions)")
plt.text(80, 1000000, f'Maximum: ${max(results):,.2f} ({results.index(max(results)) + 1}-day avg.) \n '
                      f'Minimum: ${min(results):,.2f} ({results.index(min(results)) + 1}-day avg.) \n')
plt.show()
