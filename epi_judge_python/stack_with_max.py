import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
import sys


'''
Very cool implementation of the Stack class in Python. First you create a new type of named tuple called
ElementWithCachedMax which will allow you to store the maximum element encountered so far when you push 
a new element. When initializing the object, you'll want to create a list of these tuples of type 
ElementWithCachedMax. Next, when you pop, you make sure to remove that element from your list of ElementWithCachedMax.
When you need to return the max, return the list's last tuple's max value, because that will hold the maximum
for the current stack. 

Time complexity is O(1), space complexity is O(N) for the cache of N tuples.
'''

class Stack:

    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max: List[Stack.ElementWithCachedMax] = []

    def empty(self):
        # TODO - you fill in here.
        return len(self._element_with_cached_max) == 0

    def max(self):
        # TODO - you fill in here.
        return self._element_with_cached_max[-1].max

    def pop(self):
        # TODO - you fill in here.
        return self._element_with_cached_max.pop().element

    def push(self, x):
        # TODO - you fill in here.
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max()))
        )


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
