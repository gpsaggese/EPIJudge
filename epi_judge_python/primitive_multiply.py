from test_framework import generic_test

"""
- Multiply two non-negative integers using
    - assignment
    - bitwise operators
    - equality checks

- You can't use increment / decrement or test for y < x

   1 0 1 1 1
     1 0 1 1

# Remarks:
- Use shift-and-add to multiple

- How to add?
    - Either sum at bit level and propagate the carry
        - 1 0 1 1
          1 0 0 1
    xor = 0 0 1 0
    and = 1 0 0 1
    - Use carry save representation

# Brute force
- Sum x a number y of times
"""

def multiply(x, y):
    # Multiply x and y, by
    # - shift y one bit at the time
    # - multiply y to x
    # - shift result
    # - accumulate
    while y:
        #
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
