from tree import NewNode
from tree import print_tree
from tree import invert



if __name__=="__main__":
    root = NewNode(2)
    root.left = NewNode(1)
    root.right = NewNode(4)
    root.right.left = NewNode(3)
    root.right.right = NewNode(5)
    print("print original tree")
    results=[]
    print_tree(root)
    print(root)
    invert(root)
    print("print invert tree")
    print_tree(root)
    print(root)
