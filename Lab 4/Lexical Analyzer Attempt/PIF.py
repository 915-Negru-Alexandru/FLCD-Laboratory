import math


class PIF:
    def __init__(self):
        self.elements = []

    def add(self, element, element_type):
        if element_type[0:3] == "id:":
            id_location = element_type[3:]
            self.elements.append(["id", id_location])
        elif element_type != "identifier":
            self.elements.append([element, -1])
        else:
            self.elements.append([element, -1])

    def print_table(self):
        bar_length = 20
        print("+--------------------+--------------------+")
        print("|       TOKEN        |       ST_POS       |")
        print("+--------------------+--------------------+")
        for element in self.elements:
            token = element[0]
            st_pos = element[1]
            print("|", end="")
            if len(token) <= bar_length:
                first_piece = " " * int((bar_length - len(token))/2)
                first_piece += token
                second_piece = " " * (bar_length - len(first_piece))
                print(first_piece + second_piece, end="")
            else:
                print(token[0:bar_length-3]+"...", end="")
            print("|", end="")
            if len(str(st_pos)) <= bar_length:
                first_piece = " " * math.ceil((bar_length - len(str(st_pos)))/2)
                first_piece += str(st_pos)
                second_piece = " " * (bar_length - len(first_piece))
                print(first_piece + second_piece, end="")
            else:
                print(str(st_pos)[0:bar_length-3]+"...", end="")
            print("|")
        print("+--------------------+--------------------+")
