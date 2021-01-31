class NewNode:
    """
    A Node containing data , left and right pointers

    """

    def __init__(self, data):
        self.data = data
        self.right = self.left = None

    def __str__(self):
        return f'data={self.data} left={self.left} right={self.right}'