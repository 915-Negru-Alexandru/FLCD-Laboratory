import re

from BasicST import SymbolTable
from PIF import PIF


#  PIF - PROGRAM INTERNAL FORM (tabelul cu tokenii)
#  ST - SYMBOL TABLE

#  pentru 3 de exemplu, definim un regex care verifica ca e numar, la fel pentru string, etc
#  documentatie: explicat regex, algoritmul pe scurt, diagrama de clase
#  check for constants (for the moment, you only have identifiers)

def do_checks(token):
    return True


def analyze(file):
    try:
        fin = open(file, 'r')
    except FileNotFoundError:
        print("Input file does not exists: " + file)
        return

    lines = fin.readlines()
    if len(lines) <= 0:
        print("Input file is empty: " + file)
        return

    tokens = []

    for line in lines:
        if line[0:2] == "//":
            continue
        if len(line) <= 1:
            continue
        line = line[:-1]
        short_tokens = re.split("(\W)", line)
        for token in short_tokens:
            if token not in [" "] and len(token):
                tokens.append(token)

    token_pif = PIF()

    known_tokens = []
    try:
        fin = open("input/token.in", 'r')
    except FileNotFoundError:
        print("Token file does not exists: token.in")
        return
    lines = fin.readlines()
    for line in lines:
        known_tokens.append(line[:-1])

    symbol_table = SymbolTable()

    for token in tokens:
        if token in known_tokens:
            token_pif.add(token, "operator/separator/x")
        else:
            symbol_ok = do_checks(token)
            if symbol_ok:
                if symbol_table.search(token) == -1:
                    symbol_table.add(token)
                token_pif.add(token, "id:" + str(symbol_table.search(token)))
            else:
                first_line = -1
                error_line = 0
                for line in lines:
                    if first_line == -1 and token in line:
                        first_line = error_line
                    error_line += 1
                print("Lexical error! I have no idea what \"" + token + "\" is.")
                print("It was found at line " + str(error_line) + ".")
                return

    symbol_table.print_table()
    token_pif.print_table()


if __name__ == '__main__':
    # file_name = input("Enter file name: ")
    # file_name = "input/" + file_name
    # analyze(file_name)
    analyze("input/p1.txt")
