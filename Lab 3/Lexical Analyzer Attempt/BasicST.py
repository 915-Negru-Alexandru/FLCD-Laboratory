import math

from BSTNode import BSTNode, insert, search, inorder


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
        return value_index
        # if value_index == -1:
        #     print("+Element " + str(element) + " not found in BST.")
        # else:
        #     print("+Element " + str(element) + " at " + str(value_index) + " in BST.")

    def print_table(self):
        bar_length = 20
        print("+--------------------+--------------------+")
        print("|       ST_POS       |       SYMBOL       |")
        print("+--------------------+--------------------+")
        elements = []
        inorder(self.__bst, elements)
        elements.remove([None, -1])
        for element in elements:
            token = element[0]
            st_pos = element[1]
            print("|", end="")
            if len(str(st_pos)) <= bar_length:
                first_piece = " " * math.ceil((bar_length - len(str(st_pos)))/2)
                first_piece += str(st_pos)
                second_piece = " " * (bar_length - len(first_piece))
                print(first_piece + second_piece, end="")
            else:
                print(str(st_pos)[0:bar_length-3]+"...", end="")
            print("|", end="")
            if len(token) <= bar_length:
                first_piece = " " * int((bar_length - len(token))/2)
                first_piece += token
                second_piece = " " * (bar_length - len(first_piece))
                print(first_piece + second_piece, end="")
            else:
                print(token[0:bar_length-3]+"...", end="")
            print("|")
        print("+--------------------+--------------------+\n")
