import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Given an array A of n numbers
Rearrange A into an array B with the property

B[0] <= B[1] 
B[2] <= B[1]
B[2] <= B[3]
B[4] <= B[3]
B[4] <= B[5]
B[6] <= B[5]
B[6] <= B[7]
...

- The pattern is that the odd position numbers are larger than the adjacent
    - There is no relationship between "groups"

- Assuming the numbers are all different (otherwise there are obvious more
  valid organization), is there any other valid combination?
    - Yes if we do another swap between 0 and 2, we still have a combination

0 1 2 3 4 5 6
-------------
0 2 1 4 3 

If I sort and swap adjacent elements, seems to work
A -> C
C[0] <= C[1] <= C[2] <= C[3]

C[0] <= C[2] < C[1] 

- Only local decisions

Look at a chunk of 3
A B C

Order them A <= B <= C

7 6 1 -> 6 7 1

3 3 4 -> 3 4 3

min max last

        min   max   last
"""

def _print(*args):
    #print(*args)
    pass

def rearrange2(A):
    for i in range(1, len(A), 2):
        vals = A[i - 1: i + 2]
        #_print("i=%s, A=%s, vals=%s" % (i, A, vals))
        #
        if i == len(A) - 1:
            if not vals[0] <= vals[1]:
                A[i - 1: i] = A[i - 1: i: -1]
        else:
            if not vals[0] <= vals[1]:
                vals[1], vals[0] = vals[0], vals[1]
            if not vals[1] <= vals[2]:
                vals[2], vals[1] = vals[1], vals[2]
            if not vals[0] <= vals[1]:
                vals[1], vals[0] = vals[0], vals[1]
            min_, middle, max_ = vals
            #print([ min_, middle, max_], sorted(vals))
            #assert [ min_, middle, max_] == sorted(vals)
            #_print("  -> %s" % str((min_, middle, max_)))
            #
            #_print("  -> assign: %s = %s" % (A[i-1:i+2], [min_, max_, middle]))
            A[i-1:i+2] = [min_, max_, middle]
    return A


def rearrange(A):
    for i in range(1, len(A), 2):
        vals = A[i-1: i+2]
        vals = sorted(vals)
        if len(vals) > 2:
            vals[2], vals[1] = vals[1], vals[2]
        A[i-1:i+2] = vals
    return A

#      0  1  2  3  4  5  6  7
# A = [4, 3, 2, 5, 1, 0, 2, 0]
# len(A) = 8
# range(1, 8, 2) = 1, 3, 5, 7
# i = 1
#   vals = 4, 3, 2
#   reorder -> 2 3 4
#   2 4 3
#   A = 2 4 3 5 1 0 2 0
# i = 3
#   vals = 3 5 1
#   reorder -> 1 3 5 -> 1 5 3
#   A = 2 4 1 5 3 0 2 0
# i = 5
#   vals = 3 0 2
#   -> 0 3 2
#   A = 2 4 1 5 0 3 2
#   -> 7


@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i - 1, i),
                            '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i, i + 1),
                                '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i - 1, i),
                                '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] <= A[{}]'.format(i, i + 1),
                                '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    if False:
        A = [4, 3, 2, 5, 1, 0, 2, 0]
        print("A  =", A)
        print("sol=", rearrange(A))
        assert 0
    exit(
        generic_test.generic_test_main("alternating_array.py",
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
