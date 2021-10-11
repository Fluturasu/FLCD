

class Analyser:
    def __init__(self, atoms_table, sym_table):
        self.__atoms_table = atoms_table
        self.__sym_table = sym_table

        self.__tokens = []
        f = open("LanguageStructure/token.in", "r")
        lines = f.readlines()
        for line in lines:
            self.__tokens.append(line)
        f.close()


    def analyse(self):
        toAnalyse = open("p1.txt", "r")
        line = toAnalyse.readline()
        # input: p.txt and token.in
        # analyze char by char and split by separators and operators
        # complete Program Internal Form (PIF) with all lexical elements, specifying if they
        # belong in the Symbol Table or if they are a keyword
        # In the Symbol Table we have the identifiers and the constants
        # We also check for lexical errors
        while line:
