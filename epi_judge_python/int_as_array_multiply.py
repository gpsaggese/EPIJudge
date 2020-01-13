from test_framework import generic_test

"""
- Use arrays to represent integers
- one digit per entry
- the first element of the array is the most significant digit
    - [1, 9, 3, 7-> 1937
- a negative leading digit means a negative integer
- take 2 numbers and multiply them

- Examples
    1 2 4 5 x
    2 3 4 1
    -------
    1 2  4   5
  4 8 16 20   -

multiply_by_digit(a: list, b: int):

multiply_by_ten(a: list)

sum(a, b)

multiply_by_digit(-7, 4)
mul = -28
-28 % 10 = 2

(-28 - 2) = -30 / 10 = -3

# Questions:
- can a list be empty?
- for negative numbers only the first digit (array element with lowest index) can be zero
"""

if False:
    def _to_digit_carry(val): # -> Tuple[int, int]:
        assert val >= 0
        res = val % 10
        carry = int((val - res) / 10)
        return res, carry


    def sum_by_digit(a: int, b: int, c: int): # -> Tuple[int, int]:
        assert a >= 0
        assert b >= 0
        assert c >= 0
        sum_ = a + b + c
        return _to_digit_carry(sum_)


    def multiply_by_digit(a: int, b: int, c: int): # -> Tuple[int, int]:
        assert a >= 0
        assert b >= 0
        assert c >= 0
        mul = a * b + c
        return _to_digit_carry(mul)


    def multiply_number_by_digit(num1: int, a):
        acc_tmp = []
        carry = 0
        for j in reversed(range(len(num1))):
            digit, carry = multiply_by_digit(num1[j], a, carry)
            acc_tmp.insert(0, digit)
        if carry:
            acc_tmp.insert(0, carry)
        return acc_tmp


    def sum_numbers(num1: list, num2: list):
        # Make array of the same length.
        if len(num1) != len(num2):
            num = max(len(num1), len(num2))
            num1 = [0] * (num - len(num1)) + num1
            num2 = [0] * (num - len(num2)) + num2
        assert len(num1) == len(num2)
        carry = 0
        res = []
        for i in reversed(range(len(num1))):
            a = num1[i]
            b = num2[i]
            d, carry = sum_by_digit(a, b, carry)
            res.insert(0, d)
        if carry:
            res.insert(0, carry)
        return res


    def shift_by(num1: list, num_digits: int):
        assert num_digits >= 0
        res = num1[:]
        res.extend([0] * num_digits)
        return res


    def multiply(num1, num2):
        assert bool(num1), "num1=%s" % num1
        assert bool(num2), "num2=%s" % num2
        # Make numbers positive and store the sign of the result.
        is_negative = False
        for num in (num1, num2):
            if num[0] < 0:
                is_negative = not is_negative
                num[0] *= -1
        acc = [0]
        # num2 = [2, 3, 4, 1]
        for i in reversed(range(len(num2))):
            # num1 = [1, 2, 4, 5]
            # Multiply num1 by num2[j]
            acc_tmp = multiply_number_by_digit(num1, num2[i])
            acc_tmp = shift_by(acc_tmp, len(num2) - i - 1)
            acc = sum_numbers(acc, acc_tmp)
        # Handle the sign.
        if is_negative:
            acc[0] *= -1
        return acc


if __name__ == '__main__':
    if False:
        print(sum_by_digit(3, 4, 5))
        print(multiply_by_digit(3, 4, 5))
        print(sum_numbers([3], [4]))
        print(sum_numbers([3, 1], [4, 9]))
        print(shift_by([3, 1], 2))
        print(multiply([3, 1], [4, 9]))
        assert 0 
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
