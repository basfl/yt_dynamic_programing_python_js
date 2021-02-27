class Node():
    def __init__(self, v, right=None, left=None):
        self.v = v
        self.right = right
        self.left = left

    def insert_ndoe(self, v):
        if self.v < v:
            # right
            if self.right == None:
                self.right = Node(v)
            else:
                self.right.insert_ndoe(v)
        elif self.v > v:
            # left
            if self.left == None:
                self.left = Node(v)
            else:
                self.left.insert_ndoe(v)
        else:
            self.v = v

    def search_tree(self, v):
       
        if self.v < v:
            if self.right==None:
                return False
            return self.right.search_tree(v)
        elif self.v > v:
            if self.left==None:
                return False
            return self.left.search_tree(v)
        return True
        

    # Print the tree

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.v),
        if self.right:
            self.right.printTree()


if __name__ == "__main__":

    tree = Node(6)
    tree.insert_ndoe(15)
    tree.insert_ndoe(2)
    tree.insert_ndoe(12)
    tree.insert_ndoe(3)
    print(tree.printTree())
    print(tree.search_tree(12))
