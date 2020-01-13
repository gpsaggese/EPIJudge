from test_framework import generic_test

"""
- A player advances through a sequence of positions
- Each position has a non-negative integer (>= 0)
    - represents the max you can advance from that pos in one move

- E.g.,
       0  1  2  3  4  5  6
- A = [3, 3, 1, 0, 2, 0, 1]
    - i = 0
        - A[0] = 3, you can take at most 3
        - take 1 step
    - i = 1
        - A[1] = 3 -> you can take at most 3
        - take 3 step
    - i = 4
        - A[4] = 2
        - take 2 steps
    - i = 6

# Questions
- Do I need to get exactly to the last position or pass it?
    - Those conditions are equivalent

# Assumptions
- If the last is a 0, we won

# Problem formulation
    \sum i_j = len(A)
    i_j = 0
    i_j - i_{j-1} <= A[i_j]

# Remarks
- Everytime we end up in a 0 the game is over
- As long as we not end up in a 0 we keep moving at least 1 step

- Necessary condition for finishing the game
    - sum of all elements is larger than len()

- Sufficient condition
    - there are no 0s

# Brute force solution
- We are in i_j
- Consider A[i_j]
- for i in A[i_j]
"""

def can_reach_end(A):
    # TODO - you fill in here.
    return True



def can_reach_bruteforce(A, sol=None, rec_level=0):
    indent = ".." * rec_level

    def _print(s):
        print("%s%s" % (indent, s))

    if not sol:
        sol = []
    _print("A=%s len=%s sol=%s" % (A, len(A), sol))
    if len(A) == 0:
        return sol, True
    max_steps = A[0]
    _print("max_steps=%s" % max_steps)
    for i in range(1, max_steps + 1):
        _print("i=%s" % i)
        sol_, res = can_reach_bruteforce(A[i:], sol + [i], rec_level+1)
        if res:
            _print("-> True (sol_=%s)" % sol_)
            return sol_, True
    _print("-> False")
    return [], False


if __name__ == '__main__':
    #A = [3, 3, 1, 0, 2, 0, 1]
    A = [3, 2, 0, 0, 2, 0, 1]

    # 2 0 2 0 2 0
    # 2 2 0 x


    # 0 1 2 3 4 5
    # -----------
    # 3 4 2 0 0 ?

    # a b 0

    # We want to do it in O(n)

    print(can_reach_bruteforce(A))
    assert 0
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
