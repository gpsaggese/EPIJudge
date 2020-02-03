from test_framework import generic_test

"""
- Find the maximum profit that can be made by buying and selling at most twice
- The second buy must be made > the first sale

# Remarks

# Brute force
- Generate all possible "strategy" 0 <= a <= b < c <= d < n and find the largest
- We need to consider the case where no solution with profit > 0 is possible
  (e.g., the stock is monotonically descending)

# Solution
- Assume we have a routine to find the largest profit
    - Find the first largest profit
    - Remove the interval from prices
    - Run it again
"""

def _print(*args):
    if 1:
        print(*args)


def find_best_trade(prices):
    min_i = 0
    max_i = 0
    best_profit = 0
    for i in range(len(prices)):
        if prices[i] < prices[min_i]:
            # Found a value smaller.
            min_i = i
        profit = prices[i] - prices[min_i]
        if profit > best_profit:
            best_profit = profit
            max_i = i
    return best_profit, min_i, max_i

        

def buy_and_sell_stock_twice(prices):
    _print(f"prices={prices}")
    best_profit, min_i, max_i = find_best_trade(prices)
    #_print(f"best_profit={best_profit}, min_i={min_i}, max_i={max_i}")
    _print(f"best_profit={best_profit}, min_i={prices[min_i]}, max_i={prices[max_i]}")
    #
    prices2 = prices[:min_i]
    _print(f"prices2={prices2}")
    if prices2:
        best_profit2, min_i2, max_i2 = find_best_trade(prices2)
        _print(f"best_profit2={best_profit2}, min_i2={prices2[min_i2]}, max_i2={prices2[max_i2]}")
    else:
        best_profit2 = 0
    #
    prices3 = prices[max_i + 1:]
    _print(f"prices3={prices3}")
    if prices3:
        best_profit3, min_i3, max_i3 = find_best_trade(prices3)
        _print(f"best_profit3={best_profit3}, min_i3={prices3[min_i3]}, max_i3={prices3[max_i3]}")
    else:
        best_profit3 = 0
    #
    return best_profit + max(best_profit2, best_profit3)


if __name__ == '__main__':
    if 0:
        prices=[10.6, 11.5, 9.2, 7.0, 2.1, 8.5, 5.2, 2.4, 5.3, 8.2, 4.2, 1.2,
                2.3, 3.5, 12.7, 2.3, 2.7, 5.5, 11.1 , 13.0, 11.7, 9.1, 10.9,
                1.7, 13.2, 5.5, 4.3, 6.6, 2.4, 11.5, 11.1, 10.1, 3.3, 12.6,
                7.4, 5.0, 3.3, 13.6, 10.3, 8.6, 4.3, 7.8, 10.1, 8.2, 4.9, 5.4,
                3.7, 8.0, 0.5, 4.0, 3.4, 12.6, 13.5, 3.1, 13.2, 9.7, 7.2, 11.2
                , 6.1, 2.5, 10.6, 5.8, 5.0, 12.3, 1.6, 7.3, 6.9, 0.2, 4.9, 7.1,
                1.6, 0.7, 12.7, 0.4, 0.9, 8.7, 12.3, 1.4,
                # First.
                0.1, 0.8, 8.9, 13.6,
                #
                6.5, 9.6, 6.3, 11.7, 6.9, 7.2, 11.9, 3.1,
                #  Second.
                0.4, 10.9, 2.8, 9.8, 13.6,
                #
                12.5, 6.9, 12.4, 7.0, 1.6, 1.5, 8.4, 1.2, 9.1, 9.8, 5.2,
                3.8, 1.3, 7.9, 8.1, 3.4, 2.3, 9.3, 4.5, 1.0, 11.9, 3.6, 4.9,
                10.5, 4.7, 10.6, 3.4, 6.4, 7.9, 8.3, 8.0, 10.0, 6.4, 11.6, 2.5,
                4.1, 8.7, 5.0, 4.7, 6.9, 6.1]
        # First transaction buy at 0.1 and sell first at 13.6, and second
        # transaction buy at 0 .4 and sell at 13.6
        prices = [12, 11, 13, 9, 12, 8, 14, 1, 3, 15]
        print(buy_and_sell_stock_twice(prices))
        assert 0
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
