# Work on LL(1)

class Grammar:
    def __init__(self):
        self.terminals = []
        self.non_terminals = []
        self.production_rules = []
        self.starting_symbol = None

        self.parsing_table = None

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

        self.create_table()

        self.print_non_terminals()
        self.print_terminals()
        self.print_set_of_productions()
        self.print_productions_for_terminal("whilestmt")
        self.print_productions_for_terminal("RELATION")
        self.check_cfg()
        # self.first()
        self.print_table()

    def create_table(self):
        self.parsing_table = {}
        for symbol in self.non_terminals:
            self.parsing_table[symbol] = {}
            for col_symbol in self.terminals:
                self.parsing_table[symbol][col_symbol] = " "
            self.parsing_table[symbol]['$'] = " "

        for symbol in self.terminals:
            self.parsing_table[symbol] = {}
            for col_symbol in self.terminals:
                self.parsing_table[symbol][col_symbol] = " "
            self.parsing_table[symbol]['$'] = " "

        self.parsing_table['$'] = {}
        for col_symbol in self.terminals:
            self.parsing_table['$'][col_symbol] = " "

        for line in self.parsing_table:
            for column in self.parsing_table[line]:
                if line == column:
                    self.parsing_table[line][column] = 'POP'
        self.parsing_table['$']['$'] = "ACC"


    def print_table(self):
        print("------------- PARSING TABLE ----------------")
        for line in self.parsing_table:
            print(str(line) + ": " + str(self.parsing_table[line]))
        print('\n')
        table_line = "+---+"
        for column in self.parsing_table[self.non_terminals[0]]:
            table_line += "--------+"
        print(table_line)
        print("| \ ", end="")
        for column in self.parsing_table[self.non_terminals[0]]:
            print("|", end="")
            result = column
            for i in range(0, int((8-len(result))/2)):
                print(" ", end="")
            print(result, end="")
            for i in range(0, int((8-len(result))/2) + 1):
                print(" ", end="")
        print("|")
        print(table_line)
        for line in self.parsing_table:
            print("|", end="")
            line_title = line
            if len(line_title) == 1:
                print(" " + line_title + " ", end="")
            if len(line_title) == 3:
                print(line_title, end="")
            for column in self.parsing_table[line]:
                print("|", end="")
                result = self.parsing_table[line][column]
                for i in range(0, int((8-len(result))/2)):
                    print(" ", end="")
                print(result, end="")
                for i in range(0, int((8-len(result))/2) + 1):
                    print(" ", end="")
            print("|")
            print(table_line)


        print("\n\n\n")

        print("--------------------------------------------")

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

    def first(self, symbol):
        print("------------------ FIRST -------------------")
        first = {}

        if symbol in self.terminals:
            return {symbol: symbol}

        for production in self.production_rules:
            print(production)
            if production[0] == symbol:
                first[symbol].update(self.first(symbol))

        print("--------------------------------------------")

    def follow(self, symbol):
        print("------------------ FIRST -------------------")

        # CODE FOR FOLLOW

        print("--------------------------------------------")


if __name__ == '__main__':
    grammar = Grammar()
    grammar.read_grammar("g1.txt")
