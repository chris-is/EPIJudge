import collections
from test_framework import generic_test

'''
The non-efficient solution would be to count for each character in the character set the number of times
it appears in the letter and in the magazine. This approach is slow because it iterates over all characters, including
those that do not occur in the letter or magazine. It also makes multiple passes over both the letter and the 
magazine - as many passes as there are characters in the character set. 

The optimal solution is to make a single pass over the letter, storing the character counts for the letter in 
a single hash table - keys are characters, and values are the number of times that character appears. 
Then make a pass over the magazine, every time you find a key in the letter's hash table, subtract the corresponding
value by 1. If your hash table is empty, return True. Otherwise, return False.
O(n + m) time where m and n are the number of characters in the letter and magazine respectively.
O(L) space where L is the number of distinct characters appearing in the letter.
'''
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)
    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                # Exit for loop if your hash table for letter_text is now empty,
                # no need to keep iterating through the rest of magazine_text.
                if not char_frequency_for_letter:
                    # All characters for letter_text are matched.
                    return True

    # Empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text.
    return not char_frequency_for_letter


def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
