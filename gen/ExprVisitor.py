# Generated from C:/Users/Atif Rahman/IdeaProjects/interpol\Expr.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#doc.
    def visitDoc(self, ctx:ExprParser.DocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#field_size.
    def visitField_size(self, ctx:ExprParser.Field_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#state_seg.
    def visitState_seg(self, ctx:ExprParser.State_segContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#create_state.
    def visitCreate_state(self, ctx:ExprParser.Create_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#initialization.
    def visitInitialization(self, ctx:ExprParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#next_state.
    def visitNext_state(self, ctx:ExprParser.Next_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#create_next_state.
    def visitCreate_next_state(self, ctx:ExprParser.Create_next_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#state_name_bracket.
    def visitState_name_bracket(self, ctx:ExprParser.State_name_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#state_name.
    def visitState_name(self, ctx:ExprParser.State_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#state_name_next.
    def visitState_name_next(self, ctx:ExprParser.State_name_nextContext):
        return self.visitChildren(ctx)



del ExprParser