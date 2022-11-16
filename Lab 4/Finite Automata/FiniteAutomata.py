class FiniteAutomata:
    def __init__(self):
        self.__set_of_states = None
        self.__initial_states = None
        self.__final_states = None
        self.__input_symbols = None
        self.__transition_functions = None

    def read_input(self, file):
        try:
            fin = open(file, 'r')
        except FileNotFoundError:
            print("Input file does not exists: " + file)
            return

        lines = fin.readlines()
        if len(lines) != 5:
            print("Wrong input format")
            return

        file_format = ["SS: ", "IS: ", "FS: ", "AL: ", "TF: "]
        for i in range(0, 5):
            lines[i] = lines[i][:-1]
            line = lines[i]
            if line[0:4] != file_format[i]:
                print("Wrong input format")
            lines[i] = lines[i][4:]

        self.__set_of_states = lines[0].split()
        self.__initial_states = lines[1].split()
        self.__final_states = lines[2].split()
        self.__input_symbols = lines[3].split()
        self.__transition_functions = lines[4].split('|')

    def apply_transition(self, from_state, law_to_use):
        for function in self.__transition_functions:
            start_state = function.split('-')[0]
            law = function.split('-')[1]
            end_state = function.split('-')[2]
            if start_state == from_state and law == law_to_use:
                return end_state
        return None

    def run_law(self, sequence):
        for initial_state in self.__initial_states:
            last_element = initial_state
            checked_states = [last_element]
            for law in sequence:
                last_element = self.apply_transition(last_element, law)
                if last_element not in checked_states:
                    checked_states.append(last_element)
                if last_element is None:
                    break
                # print(last_element)
            fully_checked = None not in checked_states and checked_states.sort() == self.__set_of_states.sort()
            if last_element in self.__final_states and fully_checked:
                print("Run " + sequence + " accepted")
            else:
                print("Run " + sequence + " not accepted")

    def check_determinism(self):
        for function in self.__transition_functions:
            start_state = function.split('-')[0]
            law = function.split('-')[1]
            end_state = function.split('-')[2]
            for other_function in self.__transition_functions:
                other_start_state = other_function.split('-')[0]
                other_law = other_function.split('-')[1]
                other_end_state = other_function.split('-')[2]
                if start_state == other_start_state and law == other_law and end_state != other_end_state:
                    return False
        return True



    def menu(self):
        print("----\n0.Exit\n1.Print Set of States\n2.Print Initial State\n3.Print Final State\n4."
              "Print Set of Symbols\n5.Print Transition Functions\n6.Run Sequence\n7.Check deterministic\n----")
        option = None
        while option != '0':
            option = input(">>")
            if option == '1':
                for state in self.__set_of_states:
                    print(state, end=" ")
                    print("")
            elif option == '2':
                for state in self.__initial_states:
                    print(state, end=" ")
                    print("")
            elif option == '3':
                for state in self.__final_states:
                    print(state, end=" ")
                print("")
            elif option == '4':
                for symbol in self.__input_symbols:
                    print(symbol, end=" ")
                    print("")
            elif option == '5':
                for function in self.__transition_functions:
                    start_state = function.split('-')[0]
                    law = function.split('-')[1]
                    end_state = function.split('-')[2]
                    print(start_state + ", " + law + " -> " + end_state)
            elif option == '6':
                if not self.check_determinism():
                    print("FA is not deterministic!")
                else:
                    sequence_to_run = input("Sequence: ")
                    for transition in sequence_to_run:
                        if transition not in self.__input_symbols:
                            print("Sequence Invalid")
                    self.run_law(sequence_to_run)
            elif option == '7':
                if self.check_determinism():
                    print("FA is deterministic")
                else:
                    print("FA is not deterministic!")
            else:
                print(option + " is an invalid option!")
