# Generated from C:/Users/Atif Rahman/IdeaProjects/interpol\Property.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PropertyParser import PropertyParser
else:
    from PropertyParser import PropertyParser

# This class defines a complete listener for a parse tree produced by PropertyParser.
class PropertyListener(ParseTreeListener):

    # Enter a parse tree produced by PropertyParser#pr.
    def enterPr(self, ctx:PropertyParser.PrContext):
        pass

    # Exit a parse tree produced by PropertyParser#pr.
    def exitPr(self, ctx:PropertyParser.PrContext):
        pass


    # Enter a parse tree produced by PropertyParser#k.
    def enterK(self, ctx:PropertyParser.KContext):
        pass

    # Exit a parse tree produced by PropertyParser#k.
    def exitK(self, ctx:PropertyParser.KContext):
        pass


    # Enter a parse tree produced by PropertyParser#prevK.
    def enterPrevK(self, ctx:PropertyParser.PrevKContext):
        pass

    # Exit a parse tree produced by PropertyParser#prevK.
    def exitPrevK(self, ctx:PropertyParser.PrevKContext):
        pass


    # Enter a parse tree produced by PropertyParser#expression.
    def enterExpression(self, ctx:PropertyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PropertyParser#expression.
    def exitExpression(self, ctx:PropertyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PropertyParser#andexpression.
    def enterAndexpression(self, ctx:PropertyParser.AndexpressionContext):
        pass

    # Exit a parse tree produced by PropertyParser#andexpression.
    def exitAndexpression(self, ctx:PropertyParser.AndexpressionContext):
        pass


    # Enter a parse tree produced by PropertyParser#orexpression.
    def enterOrexpression(self, ctx:PropertyParser.OrexpressionContext):
        pass

    # Exit a parse tree produced by PropertyParser#orexpression.
    def exitOrexpression(self, ctx:PropertyParser.OrexpressionContext):
        pass


    # Enter a parse tree produced by PropertyParser#notexpression.
    def enterNotexpression(self, ctx:PropertyParser.NotexpressionContext):
        pass

    # Exit a parse tree produced by PropertyParser#notexpression.
    def exitNotexpression(self, ctx:PropertyParser.NotexpressionContext):
        pass


    # Enter a parse tree produced by PropertyParser#atom.
    def enterAtom(self, ctx:PropertyParser.AtomContext):
        pass

    # Exit a parse tree produced by PropertyParser#atom.
    def exitAtom(self, ctx:PropertyParser.AtomContext):
        pass


    # Enter a parse tree produced by PropertyParser#boolean.
    def enterBoolean(self, ctx:PropertyParser.BooleanContext):
        pass

    # Exit a parse tree produced by PropertyParser#boolean.
    def exitBoolean(self, ctx:PropertyParser.BooleanContext):
        pass



del PropertyParser