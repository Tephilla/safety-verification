# Generated from C:/Users/Atif Rahman/IdeaProjects/interpol\Expr.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#doc.
    def enterDoc(self, ctx:ExprParser.DocContext):
        pass

    # Exit a parse tree produced by ExprParser#doc.
    def exitDoc(self, ctx:ExprParser.DocContext):
        pass


    # Enter a parse tree produced by ExprParser#field_size.
    def enterField_size(self, ctx:ExprParser.Field_sizeContext):
        pass

    # Exit a parse tree produced by ExprParser#field_size.
    def exitField_size(self, ctx:ExprParser.Field_sizeContext):
        pass


    # Enter a parse tree produced by ExprParser#state_seg.
    def enterState_seg(self, ctx:ExprParser.State_segContext):
        pass

    # Exit a parse tree produced by ExprParser#state_seg.
    def exitState_seg(self, ctx:ExprParser.State_segContext):
        pass


    # Enter a parse tree produced by ExprParser#create_state.
    def enterCreate_state(self, ctx:ExprParser.Create_stateContext):
        pass

    # Exit a parse tree produced by ExprParser#create_state.
    def exitCreate_state(self, ctx:ExprParser.Create_stateContext):
        pass


    # Enter a parse tree produced by ExprParser#initialization.
    def enterInitialization(self, ctx:ExprParser.InitializationContext):
        pass

    # Exit a parse tree produced by ExprParser#initialization.
    def exitInitialization(self, ctx:ExprParser.InitializationContext):
        pass


    # Enter a parse tree produced by ExprParser#next_state.
    def enterNext_state(self, ctx:ExprParser.Next_stateContext):
        pass

    # Exit a parse tree produced by ExprParser#next_state.
    def exitNext_state(self, ctx:ExprParser.Next_stateContext):
        pass


    # Enter a parse tree produced by ExprParser#create_next_state.
    def enterCreate_next_state(self, ctx:ExprParser.Create_next_stateContext):
        pass

    # Exit a parse tree produced by ExprParser#create_next_state.
    def exitCreate_next_state(self, ctx:ExprParser.Create_next_stateContext):
        pass


    # Enter a parse tree produced by ExprParser#state_name_bracket.
    def enterState_name_bracket(self, ctx:ExprParser.State_name_bracketContext):
        pass

    # Exit a parse tree produced by ExprParser#state_name_bracket.
    def exitState_name_bracket(self, ctx:ExprParser.State_name_bracketContext):
        pass


    # Enter a parse tree produced by ExprParser#state_name.
    def enterState_name(self, ctx:ExprParser.State_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#state_name.
    def exitState_name(self, ctx:ExprParser.State_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#state_name_next.
    def enterState_name_next(self, ctx:ExprParser.State_name_nextContext):
        pass

    # Exit a parse tree produced by ExprParser#state_name_next.
    def exitState_name_next(self, ctx:ExprParser.State_name_nextContext):
        pass



del ExprParser