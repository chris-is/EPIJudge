from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import OrderedDict

'''
The idea here is to use an OrderedDict to preserve the insertion order. As such, the least
recently used item will always be at the head of the OrderedDict. When we have a lookup, 
make sure to pop off the key from the OrderedDict and re-insert it in order to follow the timeline
of events. Finally, if LRU cache is at capacity and you want to insert, use method popitem(last=False)
to specify that you want to remove the HEAD of the OrderedDict.
Time complexity for this hash table lookup is O(1) and hash table update is O(1). 
'''
class LruCache:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self._isbn_price_table: OrderedDict[int, int] = OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        # TODO - you fill in here.
        if isbn not in self._isbn_price_table:
            return - 1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price


    def insert(self, isbn, price):
        # We add the value for key only if key is not present - according to spec., we
        # don't update existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            # Remove the first item queued as it is the least recently used item
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
