import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Delete repeated elements from a sorted array

2 3 5 5 7 11 11 11 13

2 3 5 7 11 13 ? ? ?

- The repeated elements are shifted
    - No requirements for the values beyond the valid element
- Return the number of valid elements

# Strategy
- Corner cases
    - All different
    - All equal
    - All different besides the last one
    - All equal besides the middle one

# Remarks
- The sorteness means that each new element is either
    - equal to the previous one or
    - different from any of the previous ones

# Solution

i pointer to the next element to process
j pointer to the last non-redundant element

0 1 2 3 4  5  6  7  8
2 3 5 5 7 11 11 11 13
    j
      

i = 0
    A[i] = 2
    A = 2 3 5 5 7 11 11 11 13
        i
        j
    last_elem = 2

i = 1
last_elem = 2
    A[i] = 3
    -> leave the next element in place
    A = 2 3 5 5 7 11 11 11 13
          i
          j

i = 2
last_elem = 3
    A[i] = 5
    last_elem = 
    - >leave elem in place
    A = 2 3 5 5 7 11 11 11 13
            i
            j

i = 3
last_elem = 5
    A = 2 3 5 5 7 11 11 11 13
              i
            j

i = 4
last_elem = 5
    A = 2 3 5 5 7 11 11 11 13
                i
            j
    new elem


i = 5
last_elem = 5
    A = 2 3 5 5 7 11 11 11 13
                i
            j


"""

# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    # Last elem updated.
    last_elem = None
    j = -1
    for i in range(len(A)):
        if i == 0:
            last_elem = A[i]
            j += 1
        else:
            curr_elem = A[i]
            if curr_elem != last_elem:
                # Found elem never seen before, keep it.
                j += 1
                assert 0 < j <= len(A)
                A[j] = curr_elem
            else:
                # curr_elem = last_elem
                pass
            last_elem = curr_elem
    assert 0 <= j + 1 <= len(A)
    return j + 1


def delete_duplicates_variant1(A, key):
    """
    Input array and a key
    Remove all the elements equal to the key
    Shift the elements to the left

    A = [0 4 5 0 1 2 3 5]
    key = 0

    """
    # next elem to write
    j = 0
    for i in range(len(A)):
        if A[i] == key:
            pass
        else:
            A[j] = A[i]
            j += 1
    return j


def delete_dups_variant2(A):
    """
    sorted array A of integers
    positive integer m
    update A so that if x appears m times in A
        => it appears exactly min(2, m) times in A
    keep the first and the second occurrence of each elem, but not anything more

    O(n) time
    O(1) space

    # Questions:
    - no additional storage?
    # 
    A = [1, 1, 1, 2, 3, 3]
               j
               i

    A = [1, 1, 1, 2, 3, 3]
               j
                  i

    A = [1, 1, 1, 2, 3, 3]
               j
                  i

    """
    # next elem to write
    j = 2
    last_vals_2 = A[0]
    last_vals_1 = A[1]
    if len(A) < 2:
        return j
    for i in range(2, len(A)):
        is_equal = A[i] == last_vals_1 and A[i] == last_vals_2
        print("i=%s last_vals=%s is_equal=%s" % (i, str((last_vals_2, last_vals_1, A[i])), is_equal))
        last_vals_2, last_vals_1 = last_vals_1, A[i]
        if is_equal:
            # Skip.
            pass
        else:
            A[j] = A[i]
            j += 1
    return j

    # The problem with this approach is that we keep all the values.
    # So if we say we want to keep min(k, m) we need to keep k values.
    # In reality we can use a counter of how many similar elements we encountered.

def delete_dups_variant2(A):
    """
    sorted array A of integers
    positive integer m
    update A so that if x appears m times in A
        => it appears exactly min(2, m) times in A
    keep the first and the second occurrence of each elem, but not anything more

    O(n) time
    O(1) space

    # Questions:
    - no additional storage?
    # 
    A = [1, 1, 1, 2, 3, 3]
               j
               i

    A = [1, 1, 1, 2, 3, 3]
               j
                  i

    A = [1, 1, 1, 2, 3, 3]
               j
                  i

    """
    # next elem to write
    j = 2
    last_vals_2 = A[0]
    last_vals_1 = A[1]
    if len(A) < 2:
        return j
    for i in range(2, len(A)):
        is_equal = A[i] == last_vals_1 and A[i] == last_vals_2
        print("i=%s last_vals=%s is_equal=%s" % (i, str((last_vals_2, last_vals_1, A[i])), is_equal))
        last_vals_2, last_vals_1 = last_vals_1, A[i]
        if is_equal:
            # Skip.
            pass
        else:
            A[j] = A[i]
            j += 1
    return j




@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    if False:
        A = []
        # 1
        A = [1]
        # 2
        A = [1, 1]
        A = [1, 1, 2]
        A = [1, 2, 3, 4, 5]
        A = [1, 2, 2, 2, 2]
        A = [1, 2, 2, 2, 3]
        print(delete_duplicates(A))
        print(A)
        assert 0
    if True:
        #A = [1, 1, 1]
        #A = [1, 1, 1, 2, 3, 3]
        A = [1, 1, 1, 2, 3, 3, 3]
        print("before A=", A)
        j = delete_dups_variant2(A)
        print("j=", j)
        print("after  A=", A[:j])
        assert 0

    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
