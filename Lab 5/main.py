# Work on LL(1)

class Grammar:
    def __init__(self):
        self.terminals = []
        self.non_terminals = []
        self.production_rules = []
        self.starting_symbol = None

    def read_grammar(self, file):
        try:
            fin = open(file, 'r')
        except FileNotFoundError:
            print("Input file does not exists: " + file)
            return

        lines = fin.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i][:-1]

        prefixes = ["N = ", "E = ", "S = ", "P = "]

        for i in range(0, 4):
            if lines[i][:4] != prefixes[i]:
                print("Wrong file format!")
                return

        self.terminals = lines[1][5:][:-2].split()
        self.non_terminals = lines[0][5:][:-2].split()
        self.starting_symbol = lines[2].split()[-1]

        if self.starting_symbol not in self.non_terminals:
            print("Not ok, starting symbol is not a non-terminal!")
            return

        crude_lines = lines[4:]
        crude_lines = crude_lines[:-1]
        for i in range(0, len(crude_lines)):
            crude_lines[i] = crude_lines[i][4:]

        for line in crude_lines:
            splitted = line.split(" -> ")
            new_rule = [None, None]
            new_rule[0] = splitted[0]
            self.production_rules.append(new_rule)
            right_side = splitted[1].split(" | ")
            new_rule[1] = right_side

        self.print_non_terminals()
        self.print_terminals()
        self.print_set_of_productions()
        self.print_productions_for_terminal("while_stmt")
        self.print_productions_for_terminal("relation")
        self.check_cfg()

    def print_non_terminals(self):
        print("------------- NON TERMINALS ----------------")
        print(self.non_terminals)
        print("--------------------------------------------")
        print('\n')

    def print_terminals(self):
        print("--------------- TERMINALS ------------------")
        print(self.terminals)
        print("--------------------------------------------")
        print('\n')

    def print_set_of_productions(self):
        print("------------ SET OF PRODUCTIONS ------------")
        for rule in self.production_rules:
            right_side = ""
            for element in rule[1]:
                right_side += element + " | "
            right_side = right_side[:-2]
            print(str(rule[0]) + " -> " + right_side)
        print("--------------------------------------------")
        print('\n')

    def print_productions_for_terminal(self, terminal):
        print("----- PRODUCTIONS FOR: \"" + terminal, end="\" ")
        for i in range(0, 18-len(terminal)):
            print("-", end="")
        print("")
        for rule in self.production_rules:
            if rule[0] == terminal:
                for element in rule[1]:
                    print(element)
        print("--------------------------------------------")
        print('\n')

    def check_cfg(self):
        print("--------------------------------------------")
        for rule in self.production_rules:
            if rule[0] is list:
                print("Grammar not CFG!")
                print("--------------------------------------------")
                return

        print("Grammar CFG")
        print("--------------------------------------------")


if __name__ == '__main__':
    grammar = Grammar()
    grammar.read_grammar("example.txt")
