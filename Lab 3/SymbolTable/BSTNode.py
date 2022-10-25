class BSTNode:
    def __init__(self, value, index):
        self.left = None
        self.right = None
        self.value = value
        self.index = index


def insert(root, value, index):
    if root is None:
        return BSTNode(value, index)
    else:
        if str(root.value) == str(value):
            return root
        elif str(root.value) < str(value):
            root.right = insert(root.right, value, index)
            return root
        else:
            root.left = insert(root.left, value, index)
            return root


def search(root, value):
    if root is None:
        return -1
    else:
        if str(root.value) == str(value):
            return root.index
        elif str(root.value) < str(value):
            return search(root.right, value)
        else:
            return search(root.left, value)
