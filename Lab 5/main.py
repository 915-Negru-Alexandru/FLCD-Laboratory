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

        line_1 = lines[0]
        print(line_1)

    def print_non_terminals(self):
        print(self.non_terminals)

    def print_terminals(self):
        print(self.terminals)

    def set_of_productions(self):
        for rule in self.production_rules:
            print(rule)

    def productions_for_terminal(self, terminal):
        for rule in self.production_rules:
            if rule[0] == terminal:
                print(terminal[1:])

    def check_cfg(self):
        if len(self.non_terminals) > 1:
            return False

if __name__ == '__main__':
    print("hello")