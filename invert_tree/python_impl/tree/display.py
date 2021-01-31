from tree  import NewNode


def print_tree(node):
    """
    print the tree
    """
    if node == None:
        return
    print_tree(node.left)
    print(node.data)
    print_tree(node.right)