# Generated from C:/Users/Atif Rahman/IdeaProjects/interpol\Expr.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\7\6\79\n\7\r\7\16\7:\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\6\16L\n\16\r\16")
        buf.write("\16\16M\3\16\3\16\3\17\6\17S\n\17\r\17\16\17T\3\17\3\17")
        buf.write("\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\3\2\5\3\2\62;\4\2\f\f\17\17\4")
        buf.write("\2\13\13\"\"\2[\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5$\3\2\2")
        buf.write("\2\7+\3\2\2\2\t\60\3\2\2\2\13\65\3\2\2\2\r8\3\2\2\2\17")
        buf.write("<\3\2\2\2\21>\3\2\2\2\23@\3\2\2\2\25B\3\2\2\2\27D\3\2")
        buf.write("\2\2\31F\3\2\2\2\33K\3\2\2\2\35R\3\2\2\2\37 \7U\2\2 !")
        buf.write("\7K\2\2!\"\7\\\2\2\"#\7G\2\2#\4\3\2\2\2$%\7U\2\2%&\7V")
        buf.write("\2\2&\'\7C\2\2\'(\7V\2\2()\7G\2\2)*\7U\2\2*\6\3\2\2\2")
        buf.write("+,\7K\2\2,-\7P\2\2-.\7K\2\2./\7V\2\2/\b\3\2\2\2\60\61")
        buf.write("\7P\2\2\61\62\7G\2\2\62\63\7Z\2\2\63\64\7V\2\2\64\n\3")
        buf.write("\2\2\2\65\66\7u\2\2\66\f\3\2\2\2\679\t\2\2\28\67\3\2\2")
        buf.write("\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\16\3\2\2\2<=\7<\2\2")
        buf.write("=\20\3\2\2\2>?\7*\2\2?\22\3\2\2\2@A\7+\2\2A\24\3\2\2\2")
        buf.write("BC\7?\2\2C\26\3\2\2\2DE\7V\2\2E\30\3\2\2\2FG\7H\2\2G\32")
        buf.write("\3\2\2\2HI\7\17\2\2IL\7\f\2\2JL\t\3\2\2KH\3\2\2\2KJ\3")
        buf.write("\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\16")
        buf.write("\2\2P\34\3\2\2\2QS\t\4\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2")
        buf.write("\2TU\3\2\2\2UV\3\2\2\2VW\b\17\2\2W\36\3\2\2\2\7\2:KMT")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUMBER = 6
    COLON = 7
    OPEN_BR = 8
    CLOSE_BR = 9
    EQUALS = 10
    T = 11
    F = 12
    ENDLINE = 13
    WHITESPACE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'SIZE'", "'STATES'", "'INIT'", "'NEXT'", "'s'", "':'", "'('", 
            "')'", "'='", "'T'", "'F'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "COLON", "OPEN_BR", "CLOSE_BR", "EQUALS", "T", "F", 
            "ENDLINE", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "COLON", 
                  "OPEN_BR", "CLOSE_BR", "EQUALS", "T", "F", "ENDLINE", 
                  "WHITESPACE" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


