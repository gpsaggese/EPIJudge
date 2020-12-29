import functools

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

"""
Select a random subset of customers
Input: array of distinct elements and a size n
Output: Subset of the given size of the array
All subsets should be equalli likely
Return the output in the input array

# Brute force
- Shuffle and pick the first n
- The problem is that one computes extra random values not needed
- Complexity is O(n)

# Remarks:
- Do we have a random number gen?
- How many subsets there are (n k)

# Horrible solution
- Select each value with prob k / n
    - Not guaranteed that the array is exactly k

# Solution
- Y = []
- Pick an element at random from Aj
- Remove element from A and add it to Y

- Complexity is O(k)
- If k > n/2 we can make it O(n - k) < O(k) by picking the one to remove

# Variant

- 0 to 5

- If R is uniform in [0, k - 1]
- Is R % n uniform in [0, n - 1]

- to be uniform <==> Pr(R % n == j) == 1/n forall j
- <==> R % n == j needs to send the same 
"""
import random


def random_sampling(k, A):
    X = []
    assert 1 <= k < len(A)
    for i in range(k):
        x = random.randint(len(A))
    return


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))]
             for a in result], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("offline_sampling.py",
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
