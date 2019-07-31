from test_framework import generic_test


def apply_permutation(perm, A):
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]

    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))

'''
The brute force solution I had before consisted of creating a results array and inserting at [element] whatever's
in A[index]. The time and complexity for that solution are O(n). What if the interviewer asks me not use extra memory and
now instead I have to rely on only A and perm? Well, swap elements in A, and then swap in permutation to record where
the element has moved to; remember that permutation array in the beginning is referring to a desired positioning of elements
based on A. So if you swap elements in A, naturally the permutation array will have to reflect the change - otherwise 
the permutation array is still basing itself on the original A and you'll end up with incorrect subsequent swaps in A.

Not sure why the time complexity in this case is O(n), I figured it would be O(n^2) since we have an inner loop.
Space complexity is O(n) because we're modifying the permutation array...but aren't we also modifying A?
'''