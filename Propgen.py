from antlr4 import *

from gen.MyListener import MyListener
from gen.PropListener import PropListener
from gen.PropertyLexer import PropertyLexer
from gen.PropertyParser import PropertyParser
from z3 import *


class Propgen():
    prop = True
    prevK = 0
    K = 0

    def __init__(self, input):
        istream = FileStream(input)
        lexer = PropertyLexer(istream)
        stream = CommonTokenStream(lexer)
        parser = PropertyParser(stream)

        tree = parser.pr()

        walker = ParseTreeWalker()
        walker.walk(PropListener(), tree)

        c = PropListener()
        self.prevK, self.K, formula = c.return_to_main()
        print("Prevk:- ", self.prevK)
        print("K = ", self.K)
        print("Boolean formula:- ", formula)
        data_field = MyListener()
        data = data_field.return_data()
        X = [Bool('x_%i' % i) for i in range(data)]
        Y = [Bool('y_%i' % i) for i in range(data)]

        identifier_list = self.find_identifiers(formula, X)
        print("Identifiers:- ", identifier_list)

        operations_list = self.find_operations(formula)
        print("Operations:- ", operations_list)

        self.prop = self.create_prop(identifier_list, operations_list)
        print("Z3 formula := ", self.prop)

    def find_identifiers(self, formula, X):
        identifier_list = []
        final_identifiers = []
        not_identifier_list = []
        for i in range(len(formula)):
            if formula[i] == 'X':
                identifier_list.append(int(formula[i + 1]))
                if i != 0 and formula[i - 1] == '~':
                    not_identifier_list.append(1)
                else:
                    not_identifier_list.append(0)

        for i in range(len(identifier_list)):
            final_identifiers.append(X[identifier_list[i]])

        for j in range(len(not_identifier_list)):
            if not_identifier_list[j] == 1:
                final_identifiers[j] = Not(X[identifier_list[j]])

        return final_identifiers

    def find_operations(self, formula):
        operations_list = []
        for i in range(len(formula)):
            if formula[i] == '&' or formula[i] == '|':
                operations_list.append(formula[i])
        return operations_list

    def create_prop(self, identifier_list, operations_list):
        self.prop = identifier_list[0]
        for i in range(len(operations_list)):
            if operations_list[i] == '&':
                self.prop = And(identifier_list[i + 1], self.prop)
            elif operations_list[i] == '|':
                prop = Or(identifier_list[i + 1], self.prop)
        self.prop = simplify(self.prop)
        return self.prop

    def return_value(self):
        return self.prop, self.prevK, self.K
