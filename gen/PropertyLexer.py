# Generated from C:/Users/Atif Rahman/IdeaProjects/interpol\Property.g4 by ANTLR 4.9.2
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
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\f@\n\f\r\f\16")
        buf.write("\fA\3\r\3\r\3\16\3\16\3\16\6\16I\n\16\r\16\16\16J\3\16")
        buf.write("\3\16\3\17\6\17P\n\17\r\17\16\17Q\3\17\3\17\2\2\20\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\3\2\5\3\2\62;\4\2\f\f\17\17\4\2\13\13\"\"")
        buf.write("\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7\'\3\2\2")
        buf.write("\2\t)\3\2\2\2\13+\3\2\2\2\r\60\3\2\2\2\17\66\3\2\2\2\21")
        buf.write("8\3\2\2\2\23:\3\2\2\2\25<\3\2\2\2\27?\3\2\2\2\31C\3\2")
        buf.write("\2\2\33H\3\2\2\2\35O\3\2\2\2\37 \7M\2\2 \4\3\2\2\2!\"")
        buf.write("\7r\2\2\"#\7t\2\2#$\7g\2\2$%\7x\2\2%&\7M\2\2&\6\3\2\2")
        buf.write("\2\'(\7*\2\2(\b\3\2\2\2)*\7+\2\2*\n\3\2\2\2+,\7V\2\2,")
        buf.write("-\7T\2\2-.\7W\2\2./\7G\2\2/\f\3\2\2\2\60\61\7H\2\2\61")
        buf.write("\62\7C\2\2\62\63\7N\2\2\63\64\7U\2\2\64\65\7G\2\2\65\16")
        buf.write("\3\2\2\2\66\67\7(\2\2\67\20\3\2\2\289\7~\2\29\22\3\2\2")
        buf.write("\2:;\7\u0080\2\2;\24\3\2\2\2<=\7?\2\2=\26\3\2\2\2>@\t")
        buf.write("\2\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\30\3\2")
        buf.write("\2\2CD\7Z\2\2D\32\3\2\2\2EF\7\17\2\2FI\7\f\2\2GI\t\3\2")
        buf.write("\2HE\3\2\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K")
        buf.write("L\3\2\2\2LM\b\16\2\2M\34\3\2\2\2NP\t\4\2\2ON\3\2\2\2P")
        buf.write("Q\3\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\b\17\2\2T\36")
        buf.write("\3\2\2\2\7\2AHJQ\3\b\2\2")
        return buf.getvalue()


class PropertyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    LPAREN = 3
    RPAREN = 4
    TRUE = 5
    FALSE = 6
    AND = 7
    OR = 8
    NOT = 9
    EQUALS = 10
    NUMBER = 11
    IDENTIFIER = 12
    ENDLINE = 13
    WHITESPACE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'K'", "'prevK'", "'('", "')'", "'TRUE'", "'FALSE'", "'&'", 
            "'|'", "'~'", "'='", "'X'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "TRUE", "FALSE", "AND", "OR", "NOT", "EQUALS", 
            "NUMBER", "IDENTIFIER", "ENDLINE", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "LPAREN", "RPAREN", "TRUE", "FALSE", "AND", 
                  "OR", "NOT", "EQUALS", "NUMBER", "IDENTIFIER", "ENDLINE", 
                  "WHITESPACE" ]

    grammarFileName = "Property.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


