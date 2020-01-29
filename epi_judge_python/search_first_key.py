from test_framework import generic_test


'''
The idea here is to leverage the standard binary search algorithm, with one additional 
feature: we know that if we match on the target, then there's no way "previous" occurrences
are in the subsequent elements. So either our current match is the first occurrence
or there are other occurrences in array[left, current_mid - 1].

Time complexity is O(log n) because each iteration reduces the size of the candidate set by half.

'''

def search_first_of_k(A, k):
    # TODO - you fill in here.
    return binary_search_helper(A, k, 0, len(A) - 1)


def binary_search_helper(A, k, left, right):
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else: # A[mid] < k
            left = mid + 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
