from test_framework import generic_test

"""
- Define the weight of an nonnegative integer x as the number of bits set to 1
  in its binary representation

- Given a program that takes a nonnegative integer x
    - return a number y
        - y != x
        - with the same weight
        - smallest |y - x|

# Assumptions
- x is not all 0s or 1s

# Examples

5 = (101)_2 -> 6 = (110)_2

2 = (10)_2 -> (01)=1, (100)=4
3 = (11)_2 -> (101)_

# Remarks
- Swap the least significant bit set to 1 (i-th) with the closest 0 "on the right" (j-th)
  with j < i
    - swap(x) = x - 2^i + 2^{j}

- (1000)=8 -> (0100)=4 -> diff=-4
- (1000)=8 -> (0010)=2 -> diff=-6
- (1000)=8 -> (10000)=16 -> diff=+8

- In practice we want to find a sequence `10` and change it
    - It exists for sure because x is not all 1s or 0s

- At position `i` we find 1 and at position `i - 1` we find 0
    - x - swap(x) = 2^i - 2^{i-1} = 2^{i-1}
- Assume that there is a different swap(x) = y' such that
    - |y' - x| < |y - x| = 2^{i-1}
    - same number of bits
    - |y' - x| = 2^j - 2^k assume that j > k
        |y' - x| = 2^k(2^{j-k} - 1)

- Prove that there is no smallest (probably by contradiction)
"""


def _print(*args):
    if False:
        print(*args)


def swap(x, i, j):
    mask = 1 << j
    mask |= 1 << i
    _print("mask=", bin(mask))
    _print("x=", bin(x), x)
    y = x ^ mask
    _print("y=", bin(y), y)
    return y


def closest_int_same_bit_count(x):
    prev = None
    i = 0
    x_val = x
    while x != 0:
        #_print("i=%s x=%s" % (i, x))
        digit = x % 2
        x = (x - digit) // 2
        #_print("  -> digit=%s x=%s" % (digit, x))
        if prev is None:
            prev = digit
        else:
            #_print("  prev=%s digit=%s" % (prev, digit))
            if prev ^ digit:
                break
            else:
                prev = digit
        i += 1
    # Swap.
    #_print("i=", i)
    y = swap(x_val, i, i-1)
    # TODO - you fill in here.
    return y


if __name__ == '__main__':
    if False:
        # - x = 5 -> 101
        #       - i = 0
        #           - is_zero = False
        #       - i = 1
        #           - is_zero = True
        x = 39698800462691
        print("y=", closest_int_same_bit_count(x))
        #
        assert 0
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
