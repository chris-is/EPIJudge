import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

'''
Try out examples for n = 3 and n = 4, and you will see that there are 3 steps in common:
1) Move n - 1 disks from initial rod to auxiliary rod
2) Move bottom-most (largest) peg from initial rod to destination rod
3) Move n - disks from auxiliary rod to destination rod

All sub-problems follow the same exact pattern.
Remember the key with recursion is to think about how to solve it for n - 1, then assuming
that's solved, how do you solve it for n. 

Time complexity is equivalent to the number of moves that have to be made, and that's
equivalent to the recurrence relation T(n) = T(n - 1) + 1 + T(n - 1) = 1 + 2T(n - 1).
If we plug in a few different values, we see that:
T(1) = 1
T(2) = 1 + 2T(1) = 3
T(3) = 1 + 2T(2) = 7
T(4) = 1 + 2T(3) = 15
T(5) = 1 + 2T(4) = 31

which we can guess that T(n) = 2^n - 1.
This of course can be proven by induction (assume it's true for n, now prove it's true for n + 1 using n).

So time complexity is O(2^n).
                     
'''

def compute_tower_hanoi(num_rings):
    # TODO - you fill in here.
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)


    # Initialize pegs.
    result: List[List[int]] = []
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]

    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure("Illegal move from {} to {}".format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
