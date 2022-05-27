from z3 import *
import sys

class Model_Checker():
    def __init__(self):
        pass
    def createAandB(self, X, Y, n, I, T, F, prevK, K):
        R = I
        VarA = []
        VarB = []
        listB = []
        listF = []
        L0 = [ Bool('x_%i_%i' % (0,i)) for i in range(n) ]
        L1 = [ Bool('x_%i_%i' % (1,i)) for i in range(n) ]
        VarA.extend(L0)
        VarA.extend(L1)
        subR = R
        for i in range(0,n):
            subR = substitute(subR, (X[i], L0[i]))
        subT = T
        for i in range(0,n):
            subT = substitute(subT, (X[i], L0[i]), (Y[i], L1[i]))

        A = And(subR, subT)
        temp = 0
        if(K > 1):
            while temp < K:
                L0 = [ Bool('x_%i_%i' % (temp,i)) for i in range(n) ]
                L1 = [ Bool('x_%i_%i' % (temp + 1,i)) for i in range(n) ]
                subT = T
                for i in range(0,n):
                    subT = substitute(subT, (X[i], L0[i]), (Y[i], L1[i]))
                listB.append(subT)
                temp = temp + 1
            B = And(listB)
        temp = prevK #0
        while temp <= K:
            L1 = [ Bool('x_%i_%i' % (temp,i)) for i in range(n) ]
            VarB.extend(L1)
            subF = F
            for i in range(0,n):
                subF = substitute(subF, (X[i],L1[i]))
            listF.append(subF)
            temp = temp + 1
        if listB:
            tempB = Or(listF)
            B = And(tempB, B)
        else:
            B = Or(listF)

        return A, B, VarA, VarB

    def createInterpolant(self, VarA, VarB, A):
        Var = list(set(VarA) - set(VarB)) + list(set(VarB) - set(VarA))
        tempA1 = substitute(A, (Var[0], BoolVal(True)))
        tempA2 = substitute(A, (Var[0], BoolVal(False)))
        tempA1 = simplify(tempA1)
        tempA2 = simplify(tempA2)
        tempA = Or(tempA1, tempA2)
        tempA = simplify(tempA)
        for i in range(1,len(Var)):
            tempA1 = substitute(tempA, (Var[i], BoolVal(True)))
            tempA2 = substitute(tempA, (Var[i], BoolVal(False)))
            tempA1 = simplify(tempA1)
            tempA2 = simplify(tempA2)
            tempA = Or(tempA1,tempA2)
            tempA = simplify(tempA)
        return tempA

    def replacePathwithState(self, X, n, P):
        temp = 0
        P1 = P
        while temp < n:
            L0 = [ Bool('x_%i_%i' % (temp,i)) for i in range(n) ]
            for i in range(0,n):
                P1 = substitute(P1, (L0[i], X[i]))
            temp = temp + 1
        P1 = simplify(P1)
        return P1

    def procedure(self, n, X, Y, I, T, Prop, prevK, K):
        s = Solver()
        s.add(And(I,Not(Prop)))
        if s.check() == sat:
            print("\nDoes not satisfy the property at k = %3d"%(0))
            return False # The True being returned is superfluous
        #s.reset()
        R = I
        bol = True
        while bol:
            s.reset()
            L0 = [ Bool('x_%i_%i' % (0,i)) for i in range(n) ]
            subProp = Prop
            for i in range(0,n):
                subProp = substitute(subProp, (X[i], L0[i]))
            print("K = ",K)
            A, B, VarA, VarB = self.createAandB(X, Y, n, R, T, Not(Prop), prevK, K)

            s.add(And(A,B))
            print(s.check())
            if s.check() == sat:

                if(R == I or R == True): # Is the condition correct -- why R==True?
                    print("\nDoes not satisfy the property for k >= %3d and k<= %3d"%(prevK, K))
                    print("----------------------------")
                    #bol = True -- why modify bol?
                    #print("True")
                    sys.exit()



                else:
                    print("Incrementing K by n")
                    temp = K + n # n=2 defined in main - n=no. of state variables.
                    self.procedure(n, X, Y, I, T, Prop, K,temp)

            else :# if s.check() == unsat:
                #print("\nSatisfies the property at k = %3d"%(K))
                print("----------------------------")
                P = self.createInterpolant(VarA, VarB, A)# it contains path variables
                print("P = ", P)
                R1 = self.replacePathwithState(X, n, P)# replaces path with state variables.

                s.reset()
                s.add(Not(Implies(R1,R)))#Not(Implies(R1,R)
                if s.check() == unsat :
                    #print("Property holds at k = %3d"%(K))
                    #temp = K + n -- why ?
                    #procedure(K,temp) -- why ?
                    #At this point, we may declare that property holds.
                    print("\nProperty holds for all reachable states")
                    #bol = False
                    sys.exit()

                    #sys.exit()
                R = Or(R,R1)
                R = simplify(R)