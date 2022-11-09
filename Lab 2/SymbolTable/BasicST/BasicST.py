from BSTNode import BSTNode, insert, search


class SymbolTable:
    def __init__(self):
        self.__size = 0
        self.__bst = BSTNode(None, -1)

    def add(self, element):
        if element == "None":
            print("Element could not be added!")
            return
        self.__size += 1
        new_index = self.__size
        self.__bst = insert(self.__bst, element, new_index)

    def search(self, element):
        value_index = search(self.__bst, element)
        if value_index == -1:
            print("+Element " + str(element) + " not found in BST.")
        else:
            print("+Element " + str(element) + " at " + str(value_index) + " in BST.")
