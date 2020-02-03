from test_framework import generic_test

"""
A permutation is a rearrangement of elements of a sequence into a new sequence
Can be represented by an array P[i] with P[i] is the location of the element i
[2 0 1 3] maps element 0 to location 2

Given an array A of n elemens and a permutation P, apply P to A

2 0 1 3

a b c d

* Brute force
- create a new array and populate it
- O(n) in space and time

* Improved solution
- O(n) in time and O(1) in space
- Keep an element

0 1 2 3
-------
2 0 1 3

target=P[0]=2

* P[0] = 2
A[2] = 2
curr=P[2]=1
? 0 2 3

* P[2] = 1
curr

P = 1 0 2 3
A = a b c d
->  b a c d

One can use P as an indication of the work to do
If there is an element out of position, we process it

P = 1 0 2 3
A = a b c d

->  - a c d
extra=b
P = 1 0 2 3


P = 1 2 3 0
A = a b c d

->  
P = 2 1 3 0
A = b a c d

->  
P = 3 1 2 0
A = c a b d

->  
P = 0 1 2 3
A = d a b a

if there is no "fixed" point it can be done by following the pointers

P = 3 2 0 1
A = a b c d

P = 1 2 0 3
    *

P = 2 1 0 3
    *

P = 0 1 2 3

"""

def apply_permutation2(perm, A):
    assert len(perm) == len(A)
    assert sorted(perm) == list(range(0, len(A)))
    B = [0] * len(A)
    for k in range(0, len(A)):
        B[perm[k]] = A[k]
    A[:] = B
    return B


def apply_permutation(P, A):
    assert len(P) == len(A)
    assert sorted(P) == list(range(0, len(A)))
    # Find first element in P out of position.
    # i -> j=P[j]
    # Swap P[i], P[j] and A[i], A[j]
    min_elem = 0
    done = False
    while not done:
        done = True
        print(f"range={min_elem}, {len(P)}")
        for i in range(min_elem, len(P)):
            j = P[i]
            print(f"i={i}, j={j}")
            if j != i:
                # Move element in position i to j.
                P[j], P[i] = P[i], P[j]
                A[j], A[i] = A[i], A[j]
                done = False
            else:
                new_min_elem = i
        min_elem = new_min_elem
    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    if True:
        P = [3, 2, 0, 1]
        A = "a b c d".split()
        apply_permutation(P, A)
        print(A)
        assert 0
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
