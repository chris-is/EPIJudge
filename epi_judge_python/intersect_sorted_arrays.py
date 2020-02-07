from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    '''
    Naive solution: for every element in A, check to see if it also exists in B. O(mn) time.
    Space is not counted here since output space is not part of space complexity analysis.
    The a != A[i - 1] is used so as not to append duplicates (current integer
    should be different the last integer to be appended since we want distinct integers in the intersection).

    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]
    '''

    '''
    Better approach: same thing as before, but instead of linearly scanning B for every integer in A,
    use binary search to find the element in B.
    Time complexity is O(m log n) where m is the length of the array being iterated over.0
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and binary_search(a, B) != -1]
    '''

    '''
    Optimal solution: one pass over both arrays. If A[i] > B[i] that means we need to advance the pointer in
    B so that we get to the larger integers that may match A. If A[i] < B[i] that means we need to advance the 
    pointer in A so that we get to the larger integers that may match B. If A[i] == B[i] and it's a new distinct
    number, add it the result list.
    O(m + n) time complexity since we spend O(1) time per input array element. 
    '''

    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[i]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[i]:
            i += 1
        else: # A[i] > B[j]
            j += 1

    return intersection_A_B


def binary_search(t: int, A: List[int]) -> int:
    L, U = 0, len(A) - 1
    while L <= U:
        M = (L + U) // 2
        if A[M] < t:
            L = M + 1
        elif A[M] > t:
            U = M - 1
        else:
            return M
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
