from list_node import ListNode
from test_framework import generic_test


# class ListNode:
#     def __init__(self, data = 0, next = None):
#         self.data = data
#         self.next = next

def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    '''
    At every iteration, you want to check which of the two nodes in the list is smallest, and set your result list's next
    node to that smallest node. Of course, once you've chosen a node from either list, you will advance that list's
    pointer by one. So, to emphasize this point, you only advance a list's pointer when you've chosen its element.
    You keep doing this until you've visited each node from both lists, or you've exhausted all the nodes from one
    list, and then you just append the nodes from the other list. Of course, since the lists are sorted and
    we're appending the next smallest available node at every iteration, the nodes from the remaining list will contain
    the largest values in your result list.
    Finally, return dummy_head.next because the first node has value 0 for its data.
    '''
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        # In the other case, where L1.data >= L2, choose the L2 node
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Pick up the rest of the nodes from either L1 or L2
    tail.next = L1 or L2
    return dummy_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
