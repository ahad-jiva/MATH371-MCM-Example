# MATH371-MCM-Example Problem Summary
You can find the problem statement [here.](https://www.mathmodels.org/Problems/2022/MCM-C/2022_MCM_Problem_C.pdf)
## Goal
With the data given, the goal is to develop a mathematical model that makes optimal daily trades using only previous price data. $1000 is given at the start, and the model must make as much profit as possible.

## My Solution
This solution uses mean reversion, the idea that asset prices in the long run will revert to their averages. Using the five years of price data given, a moving average is tracked as time passes and the model will either buy if the price is below the average or sell if above the average. The size of the moving average window is a parameter that affects model performance.

## Parameters
sim.py is where you can run the model simulation and modify parameters to change model behavior. You can play around with the following variables and see how they impact total profit (or loss!)
* ```init_capital```: Initial cash in hand usable for trades. Too low of a value will prevent the model from buying anything.
* ```btc_purchase_quantity``` and ```btc_sell_quantity```: These are the number of bitcoins that can be bought/sold in a trade, respectively. Avoid making the former too large or else the model will never be able to buy bitcoin at the beginning of the simulation.
* ```gold_purchase_quantity``` and ```gold_sell_quantity```: Same as above, but for gold.
* ```btc_commission``` and ```gold_commission```: Every buy/sell action requires a commission. Too high of a commission will eat into profits. The default values are from the problem statement.

## Usage
Run sim.py after setting parameters to simulate trading over all the data. By default, the program will loop over 250 simulations, each with a different moving average window size, and then plot the results for each window on a graph. All parameters left at their default should result in a 21-day moving average scoring the highest and a 1-day moving average scoring the worst.

To just run one simulation, comment out the ```for``` loop on lines 76-78 and call the ```sim``` function with a specific moving average window size as an argument. Uncomment line 79 to print the results of the simulation. The ```sim``` function returns a list containing the total portfolio value, the number of times bitcoin and gold were bought and sold, and the total amount of commission paid.
