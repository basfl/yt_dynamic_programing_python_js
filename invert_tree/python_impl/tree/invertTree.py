from tree import NewNode
from functools import lru_cache
@lru_cache(maxsize=10000)
def invert(node):
    if node == None:
        return
    else:
        temp = node
        # recursive call
        invert(node.left)
        invert(node.right)
        # swap the pointers
        temp = node.left
        node.left = node.right
        node.right = temp