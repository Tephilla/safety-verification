import sys
from antlr4 import *

from Model_Checker import Model_Checker
from Propgen import Propgen
from gen.ExprLexer import ExprLexer
from gen.MyListener import MyListener
from gen.ExprParser import ExprParser
from z3 import *
from ModelChecking_BMC import ModelChecking_BMC




def create_state_formula(X, state_vals, state_no, n):
    s = state_vals[state_no]# 01
    temp = n - 1
    i = True
    for x, element in enumerate(s):

        if int(element) == 0:
            i = And(i, Not(X[temp]))
        elif int(element) == 1:
            i = And(i, X[temp])
        temp = temp - 1
    i = simplify(i)
    return i

def create_T(X, Y, dict_transitions, state_vals, n):
    temp = []
    for x, y in dict_transitions.items():
        if len(y) == 1:
            t1 = create_state_formula(X, state_vals, x, n)
            t2 = create_state_formula(Y, state_vals, y[0], n)
            t = Implies(t1,t2)
            temp.append(t)
        elif len(y) > 1:
            t1 = create_state_formula(X, state_vals, x, n)
            orval = False
            for a in y:
                t2 = create_state_formula(Y, state_vals, a, n)
                orval = Or(orval, t2)
            orval = simplify(orval)
            t = Implies(t1, orval)
            temp.append(t)
    T = And(temp)
    return T

def main(argv):

    istream = FileStream(argv[1])
    lexer = ExprLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    tree = parser.doc()

    walker = ParseTreeWalker()
    walker.walk(MyListener(), tree)
    b = MyListener()
    [state_names], [state_vals], [left_states], [right_states], init_state, data = b.return_to_main()

    print("List of states", state_names)
    print("List of state values", state_vals)
    print("Initial state = s", init_state)

    dict_transitions = {}
    for key, val in zip(left_states, right_states):
        dict_transitions.setdefault(key, []).append(val)

    print("Transition states :- " ,dict_transitions)

    print(data)
    X = [Bool('x_%i' % i) for i in range(data)]
    Y = [Bool('y_%i' % i) for i in range(data)]
    print("X = ", X)
    print("Y = ", Y)

    I = create_state_formula(X, state_vals, init_state, data)

    print("I = ", I)
    T = create_T(X, Y, dict_transitions, state_vals, data)
    print("T = ", T)
    print("Choose:- \n 1.BMC with k-induction \n 2.Interpolation")
    val = int(input())
    model = Model_Checker()
    prop_variable = Propgen(argv[2])
    Prop, prevK, K = prop_variable.return_value()
    if val == 1:
        model = ModelChecking_BMC()
        model.procedure(data, X, Y, I, T, Not(Prop))
    elif val == 2:
        model = Model_Checker()
        model.procedure(data, X, Y, I, T, Not(Prop), prevK, K)
    else:
        print("Incorrect input .. aborting")
        sys.exit()

    #prevK = 1
    #K = 1
    #Prop = Not(And(X[2], Not(X[1]), Not(X[0])))





if __name__ == '__main__':
    main(sys.argv)
