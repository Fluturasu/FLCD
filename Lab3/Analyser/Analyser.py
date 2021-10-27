from BST.BST import BST, DuplicateError
import re
import string


class LexicalError(Exception):
    pass


class Analyser:
    def __init__(self):
        self.__ST = BST()
        self.__PIF = []
        self.__separators = ['{', '}', '[', ']', ';', ' ']
        self.__operators = ['+', '-', '*',  '/',  ':',  '<', '<=', '=', '>=', '>']

        self.__tokens = []

        f = open("LanguageStructure/token.in", "r")
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            self.__tokens.append(line)
        f.close()

    def genPIF(self, token, st_position):
        self.__PIF.append([token, st_position])

    def checkIndentifier(self, token):
        pattern = re.compile("^[a-zA-Z]+[0-9]*$")
        return pattern.match(token)

    def checkConstant(self, token):
        int_const_re = "0|([1-9][0-9]*)$"
        str_const_re = '"[^"]*"$'  # a string that contains anything except "
        pattern = re.compile(f'({int_const_re})|({str_const_re})')
        return pattern.match(token)

    def analyse(self):

        # input: p.txt and token.in
        # analyze char by char and split by separators and operators
        # complete Program Internal Form (PIF) with all lexical elements, specifying if they
        # belong in the Symbol Table or if they are a keyword
        # In the Symbol Table we have the identifiers and the constants
        # We also check for lexical errors

        toAnalyse = open("LanguageStructure/p1.txt", "r")
        line = toAnalyse.readline()
        line_number = 1
        while line:
            line = line.strip()
            atoms = re.split("(>=|<=|!=|<|>|=|\{|\}|\[|\]|\{|\}|;|:|\+|\*|/|-|\(|\)| |,)", line)
            for atom in atoms:
                if not atom:
                    continue
                if atom in self.__tokens:
                    if atom != " ":
                        self.genPIF(atom, -1)
                else:
                    if self.checkIndentifier(atom) or self.checkConstant(atom):
                        try:
                            index = self.__ST.insertBST(atom)
                            self.genPIF(atom, index)
                        except DuplicateError as e:  #
                            pass
                    else:
                        raise LexicalError(f"Error at line {line_number}: invalid atom detected: '{atom}'")
            line = toAnalyse.readline()
            line_number += 1

    def getPIF(self):
        return self.__PIF

    def getST(self):
        return self.__ST.getBST()

    def printST(self):
        self.__ST.printBST()

    def getTokens(self):
        return self.__tokens
