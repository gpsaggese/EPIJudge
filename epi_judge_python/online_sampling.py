import functools

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


"""
Take as input a size k
Read packets
Continously maintaining a uniform random subset of size k of the read packets

0 1 2 3 4 5 

For the first k packets just pick all of them

Assume we have seen n packets, and we have k packets with the correct distribution
A packet n + 1 comes what do we do?

What is the probability that sampling off-line k out of n + 1 packets, then (n
+ 1)-th packet is selected?

\Pr(new elem selected)
= \Pr(new elem is in a set of k elems out of n + 1)
= 1 / (n + 1) or 

"""

# Assumption: there are at least k elements in the stream.
def online_random_sample(stream, k):
    # TODO - you fill in here.
    return []


@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(lambda : [online_random_sample(iter(stream), k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0)
             for result in results], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_sampling.py",
                                       "online_sampling.tsv",
                                       online_random_sample_wrapper))
