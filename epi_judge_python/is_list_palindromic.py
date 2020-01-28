from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    # First solution: prepending to a list as you step through the linked list, then compare reverse with original.
    if L is None:
        return True
    rev = L
    print(rev)
    prev = None
    while rev:
        nxt = rev.next
        rev.next = prev
        prev = rev
        rev = nxt

    print("Starting")
    print(prev.data)
    print("test")
    print(L)
    print("test")
    while prev and L:
        if prev.data != L.data:
            return False
        else:
            prev, L = prev.next, L.next

    return True

    '''
    Second solution will shorten time complexity as we'll be reversing the linked list and comparing the result
    with a copy of the original
    '''



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
