from test_framework import generic_test


def is_palindrome_number(x):
    if x < 0:
        return False
    x_to_str = str(x)
    i = 0
    j = len(x_to_str) - 1
    while i <= j:
        if i == j:
            return True
        if x_to_str[i] != x_to_str[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
