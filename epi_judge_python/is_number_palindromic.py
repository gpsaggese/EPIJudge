from test_framework import generic_test

"""
Determine if a decimal representation of an integer is a palindromic string.
0, 1, 7, 11, 121, 333 -> True
-1, 12, 100, -> False

# Remarks:
- The zeros in front don't matter
- We can start from 1st and last decimal digit and keep going towards the
  center
- We can break as soon as there is a mismatch
- Can we convert the string and check at the same time
    - Give n-th decimal digit
    - 2^k = 10^m

- It can also be negative!

# Questions
- Only one check or multiple?
- Any know distribution of the input?
- How large is the int?

# Brute force
- Convert into a string
- Check for palindromic

- E.g. 11 -> 8 + 2 + 1
  1011 -> 

# Smart approach
- Find find digit

"""

import math

def _print(*args):
    #print(*args)
    pass

def is_palindrome_number(x):
    _print("# x=", x)
    if x < 0:
        return False
    if x == 0:
        return True
    num_digits = math.floor(math.log(x) / math.log(10))
    _print("  num_digits=", num_digits)
    mask = 10 ** num_digits
    #for i in range(num_digits // 2):
    while x > 0:
        _print(f"  mask={mask}")
        msd = x // mask
        lsd = x % 10
        _print(f"  x={x} msd={msd} lsd={lsd}")
        if msd != lsd:
            return False
        x -= lsd + msd * mask
        x //= 10
        mask //= 100
    return True


# x = 111
# num_digits = log

if __name__ == '__main__':
    if False:
        #print(is_palindrome_number(111))
        #print(is_palindrome_number(0))
        #print(is_palindrome_number(112))
        #print(is_palindrome_number(74447))
        print(is_palindrome_number(10011))
        assert 0

    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
