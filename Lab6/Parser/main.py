from Grammar import GrammarParser, Grammar
from Parser import LR0Parser, state_as_string


def write_to_file(filename, collection):
    with open(filename, "w") as g:
        for state in collection:
            g.write(state_as_string(state) + '\n')

def run_tests():
    with open("g1.test.txt", "r") as f:
        grammar = GrammarParser().parse(f)
    parser = LR0Parser(grammar)
    collection = parser.build_canonical_collection()
    write_to_file("g1.colcan.txt", collection)
    pass

if __name__ == "__main__":
    run_tests()