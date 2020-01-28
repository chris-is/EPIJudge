from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    result = 0
    '''
    The basic idea behind this is that it's almost like balancing parentheses...if you have bit 1, followed by another
    bit 1, then they'll "cancel" each other out, and we'll add up back with bit 0. But if there's third bit 1 after,
    then we'll have 0 ^ 1 which is 1...thereby having an "unbalanced" (no match for the last bit 1) number of bit 1s, i.e, an odd number of bit 1s. 
    
    Time complexity is O(n) where n is the word size since we're iteratively testing the value of each bit while tracking
    the number of 1s seen so far.
    '''
    while x:
        result ^= x & 1
        x >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
