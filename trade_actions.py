
def buy_gold(quantity, price, portfolio):
    cost = (quantity * price) + (0.01 * quantity)
    portfolio[0] -= cost
    portfolio[1] += quantity


def buy_bitcoin(quantity, price, portfolio):
    cost = (quantity * price) + (0.02 * quantity)
    portfolio[0] -= cost
    portfolio[2] += quantity


def sell_gold(quantity, price, portfolio):
    gain = (quantity * price) - (0.01 * quantity)
    portfolio[0] += gain
    portfolio[1] -= quantity


def sell_bitcoin(quantity, price, portfolio):
    gain = (quantity * price) - (0.02 * quantity)
    portfolio[0] += gain
    portfolio[2] -= quantity
