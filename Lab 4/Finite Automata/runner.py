from FiniteAutomata import FiniteAutomata

if __name__ == '__main__':
    FA = FiniteAutomata()
    FA.read_input("FA.in")
    FA.run_law("011")
    FA.run_law("100")
    FA.run_law("010")
    FA.run_law("0110")
    FA.run_law("00")
    FA.menu()
