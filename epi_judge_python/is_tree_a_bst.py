from test_framework import generic_test

'''
Remember that the BST property is that they key stored at a node is >= the keys stored at the nodes
of its left subtree and <= the keys stored at the nodes of its right subtree. 
The optimal approach is to check constraints on the values of each subtree. 
The general idea is that if all nodes in the tree must have keys in the range [low_range, high_range],
and they key at the root is w (which itself must be between [low_range, high_range] otherwise BST property is
violated at the root itself), then all the keys in the left subtree must be in the range [low_range, w],
and all the keys stored in the right subtree must be in the range [w, high_range].
NOTE THAT ON THE SKEWED PATHS (SIDES OF THE TREE), THE RANGE ON THE LEFT SUBTREE IS [-inf, parent.data],
AND THE RANGE ON THE RIGHT SUBTREE IS [parent.data, +inf].

Time complexity is O(n) since we have to visit each node in the tree, and the space complexity is ==
to the height of tree, so O(h).   
'''
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # TODO - you fill in here.
    if not tree:
        return True

    elif not low_range <= tree.data <= high_range:
        return False

    return (is_binary_tree_bst(tree.left, low_range, tree.data)
            and is_binary_tree_bst(tree.right, tree.data, high_range))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
