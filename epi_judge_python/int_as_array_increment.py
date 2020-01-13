from test_framework import generic_test

"""
- Array of digits encoding a nonnegative decimal integer D
- Updates the array to represent the integer D+1

# Representation
- The first element is most significant digit?

   0  1  2
- (1, 2, 9) -> (1, 3, 0)

#
Start from last digit and increment, if larger than increment the next one

1 2 9
    i

1 2 10
    i
"""


if False:
    def plus_one(A):
        carry = 0
        for i in reversed(range(len(A))):
            tmp = A[i]
            tmp_plus_one = tmp + 1 + carry
            if tmp_plus_one > 9:
                tmp_plus_one = tmp_plus_one % 10
                carry = tmp_plus_one - 10
            else:
                carry = 0
            A[i] = tmp_plus_one
            if carry == 0:
                break
        if carry:
            A.insert(0, carry)
        return []


# 1, 2, 9
# Sum 1 to A[-1]
# A = 1, 2, 10
#
# i = 2 -> A[i]=9
# 

def plus_one(A):
    #print("A=", A)
    A[-1] += 1
    for i in reversed(range(len(A))):
        #print("i=", i, "A[i]=", A[i])
        if A[i] == 10:
            if i > 0:
                A[i - 1] += 1
                A[i] = 0
            else:
                A[0] = 0
                A.insert(0, 1)
        else:
            break
    return A



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
