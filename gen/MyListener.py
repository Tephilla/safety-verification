from gen.ExprListener import ExprListener
from gen.ExprParser import ExprParser
from z3 import *


class MyListener(ExprListener):
    data = 0
    init_flag = -1
    init_state = 0
    left_state = 0
    right_state = 1
    state_names = []
    state_vals = []
    left_states = []
    right_states = []

    def enterField_size(self, ctx):
        print("N = ")

    def exitField_size(self, ctx):
        MyListener.data = int(ctx.NUMBER().getText())
        print(self.data)

    def enterState_name(self, ctx):
        if self.state_names.count(int(ctx.NUMBER().getText())) == 0:
            self.state_names.append(int(ctx.NUMBER().getText()))
        else:
            print("state s%d is already assigned"%(int(ctx.NUMBER().getText())))
            sys.exit()
    def exitCreate_state(self, ctx: ExprParser.Create_stateContext):
        if len(ctx.NUMBER().getText()) == self.data:
            self.state_vals.append(ctx.NUMBER().getText())
        else:
            print("State value is incorrect")
            sys.exit()

        if len(self.state_vals) > pow(2, self.data):
            print("For size %d, maximum of %d states can be initialized" % (self.data, pow(2, self.data)))
            sys.exit()

    def exitState_name_next(self, ctx: ExprParser.State_name_nextContext):
        if self.init_flag == -1:
            if self.state_names.count(int(ctx.NUMBER().getText())) == 1:
                MyListener.init_state = int(ctx.NUMBER().getText())
                self.init_flag = 0
            else:
                print("Initialized state s%d is not found" %(int(ctx.NUMBER().getText())))
                sys.exit()
        elif self.left_state == 0:
            self.left_states.append(int(ctx.NUMBER().getText()))

            self.right_state = 0
            self.left_state = 1
        elif self.right_state == 0:
            self.right_states.append(int(ctx.NUMBER().getText()))
            self.right_state = 1
            self.left_state = 0

    def return_to_main(self):
        return [self.state_names], [self.state_vals], [self.left_states], [
            self.right_states], self.init_state, self.data

    def return_data(self):
        return self.data
