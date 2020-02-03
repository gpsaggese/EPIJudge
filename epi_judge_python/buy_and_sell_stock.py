from test_framework import generic_test

"""
Given an array with the daily price
Find the point to buy and sell to maximize profit
Don't buy / sell if there is no profit to be made

<310, 315, 275, 295, 260, 270, 290, 230, 255, 250>

- Buy at i
- Sell at j

m = argmax_{i,j, i<=j} P[j] - P[i]

Without the constraint then it's
    max{P[j] - P[i]} = max P[j] - min P[i]

# Brute force solution
- The brute force solution is O(n^2)

# Remarks
- You want to buy low and sell high, but respecting causality
- The O(n^2) solution has lots of extra comparisons, while we can use the fact
  that certain solution dominate others

<310, 315, 275, 295, 260, 270, 290, 230, 255, 250>
      i_1  i_2

- if A[i_2] < A[i_1] then the solutions are dominated

# Solution
Scan the array keeping track of the min so far `curr_min`
Compute the max profit: `val - curr_min`
If find a value < `min`, update 

<310, 315, 275, 295, 260, 270, 290, 230, 255, 250>
  i

i = 0
    best_min = best_profits = 0
    best_min := 310
i = 1
    best_min = 310

- Instead of scanning the triangle (i, j)
- We can compute the `min(prices[i:]) = min_i` for every i
-    We can do it on O(n)
- Then do another scan and find the min of `prices[i] - min_i`
"""

def buy_and_sell_stock_once(prices):
    best_min = None
    best_profits = 0.0
    for k in range(len(prices)):
        if best_min is None or best_min > prices[k]:
            best_min = prices[k]
        profits = prices[k] - best_min
        if profits > best_profits:
            best_profits = profits
    return best_profits


"""
Variant

Find longest subarray with equal element

0 1 1 1 2 2 3 4 5

# Brute force
- For each element, scan until the end of the sequence starting from there (or
  the end)

# Better
Two scans:
1) build a map from starting index to length of the array starting from there
2) find max

length = {}
idx = None
for i in range(len(A)):
    if i > 0 and A[i] == A[i-1]:
        count += 1
    else:
        if idx is not None:
            lengths[idx] = count
        idx = i
        count = 0

# In one step

best_so_far = 0
curr_len = 0
last_elem = None
for i in range(len(A)):
    if i == 0:
        best_so_far = 1
        curr_len = 1
        last_elem = A[i]
    else:
        if A[i] == last_elem:
            curr_len += 1
            if curr_len > best_so_far:
                best_so_far = curr_len
        else:
            curr_len = 1
            last_elem = A[i]

return longest_arr


# Using a more compact view.
best_so_far = 1
last_elem = np.nan
for i in range(1, len(A)):
    if A[i] == last_elem:
        curr_len += 1
        best_so_far = max(curr_len, best_so_far)
    else:
        curr_len = 1
        last_elem = A[i]
"""

if __name__ == '__main__':
    if False:
        prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        res = buy_and_sell_stock_once(prices)
        print(res)
        assert 0

    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
