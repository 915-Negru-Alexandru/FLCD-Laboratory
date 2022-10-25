from BasicST.BasicST import SymbolTable

if __name__ == '__main__':
    identifiers = SymbolTable()
    identifiers.add("hello1")
    identifiers.add(4)
    identifiers.add(5)
    identifiers.add(1)
    identifiers.add("hello2")
    identifiers.add(3)
    identifiers.search("hello1")
    identifiers.search("hello2")
    identifiers.search(1)
    identifiers.search(2)
    identifiers.search(3)
    identifiers.search(4)
    identifiers.search(5)