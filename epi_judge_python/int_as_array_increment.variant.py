from test_framework import generic_test

"""
- s and t are strings of bits encoding binary numbers Bs and Bt
- return B_s + B_t

s = 00001
t = 00100

# Questions
- Are s and t of the same length?
- Do we return the string to have same number of digits of s and t

# Solution
- Scan the strings together, i, j
    - sum i, j and get carry
- Handle carry at the end

O(n) time
O(n) space

# Examples
"""


def add_two_numbers(L1, L2):
    assert len(L1) == len(L2)
    res = ""
    carry = 0
    #for k, (i, j) in enumerate(zip(L1, L2)):
    for k in reversed(range(0, len(L1))):
        i = L1[k]
        j = L2[k]
        i = int(i)
        j = int(j)
        sum = i + j + carry
        #print(f"i={i}, j={i} -> sum={sum}")
        assert 0 <= sum <= 3
        carry = int(sum / 2)
        sum = sum % 2
        res = str(sum) + res
        if sum <= 1:
            break
    if carry > 0:
        res = str(carry) + res
    return res


if __name__ == '__main__':
    #print(add_two_numbers("0001", "0000"))
    #print(add_two_numbers("0001", "0001"))
    #assert 0
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
