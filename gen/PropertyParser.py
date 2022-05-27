# Generated from C:/Users/Atif Rahman/IdeaProjects/interpol\Property.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\7\6&\n\6\f\6\16\6)")
        buf.write("\13\6\3\7\3\7\3\7\7\7.\n\7\f\7\16\7\61\13\7\3\b\3\b\3")
        buf.write("\b\5\b\66\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t?\n\t\3\n")
        buf.write("\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\7\b\2>\2")
        buf.write("\24\3\2\2\2\4\30\3\2\2\2\6\34\3\2\2\2\b \3\2\2\2\n\"\3")
        buf.write("\2\2\2\f*\3\2\2\2\16\65\3\2\2\2\20>\3\2\2\2\22@\3\2\2")
        buf.write("\2\24\25\5\6\4\2\25\26\5\4\3\2\26\27\5\b\5\2\27\3\3\2")
        buf.write("\2\2\30\31\7\3\2\2\31\32\7\f\2\2\32\33\7\r\2\2\33\5\3")
        buf.write("\2\2\2\34\35\7\4\2\2\35\36\7\f\2\2\36\37\7\r\2\2\37\7")
        buf.write("\3\2\2\2 !\5\n\6\2!\t\3\2\2\2\"\'\5\f\7\2#$\7\t\2\2$&")
        buf.write("\5\f\7\2%#\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\13")
        buf.write("\3\2\2\2)\'\3\2\2\2*/\5\16\b\2+,\7\n\2\2,.\5\16\b\2-+")
        buf.write("\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\r\3\2\2")
        buf.write("\2\61/\3\2\2\2\62\63\7\13\2\2\63\66\5\20\t\2\64\66\5\20")
        buf.write("\t\2\65\62\3\2\2\2\65\64\3\2\2\2\66\17\3\2\2\2\678\7\16")
        buf.write("\2\28?\7\r\2\29:\7\5\2\2:;\5\n\6\2;<\7\6\2\2<?\3\2\2\2")
        buf.write("=?\5\22\n\2>\67\3\2\2\2>9\3\2\2\2>=\3\2\2\2?\21\3\2\2")
        buf.write("\2@A\t\2\2\2A\23\3\2\2\2\6\'/\65>")
        return buf.getvalue()


class PropertyParser ( Parser ):

    grammarFileName = "Property.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'K'", "'prevK'", "'('", "')'", "'TRUE'", 
                     "'FALSE'", "'&'", "'|'", "'~'", "'='", "<INVALID>", 
                     "'X'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", 
                      "TRUE", "FALSE", "AND", "OR", "NOT", "EQUALS", "NUMBER", 
                      "IDENTIFIER", "ENDLINE", "WHITESPACE" ]

    RULE_pr = 0
    RULE_k = 1
    RULE_prevK = 2
    RULE_expression = 3
    RULE_andexpression = 4
    RULE_orexpression = 5
    RULE_notexpression = 6
    RULE_atom = 7
    RULE_boolean = 8

    ruleNames =  [ "pr", "k", "prevK", "expression", "andexpression", "orexpression", 
                   "notexpression", "atom", "boolean" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    LPAREN=3
    RPAREN=4
    TRUE=5
    FALSE=6
    AND=7
    OR=8
    NOT=9
    EQUALS=10
    NUMBER=11
    IDENTIFIER=12
    ENDLINE=13
    WHITESPACE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prevK(self):
            return self.getTypedRuleContext(PropertyParser.PrevKContext,0)


        def k(self):
            return self.getTypedRuleContext(PropertyParser.KContext,0)


        def expression(self):
            return self.getTypedRuleContext(PropertyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PropertyParser.RULE_pr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPr" ):
                listener.enterPr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPr" ):
                listener.exitPr(self)




    def pr(self):

        localctx = PropertyParser.PrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.prevK()
            self.state = 19
            self.k()
            self.state = 20
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(PropertyParser.EQUALS, 0)

        def NUMBER(self):
            return self.getToken(PropertyParser.NUMBER, 0)

        def getRuleIndex(self):
            return PropertyParser.RULE_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterK" ):
                listener.enterK(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitK" ):
                listener.exitK(self)




    def k(self):

        localctx = PropertyParser.KContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_k)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(PropertyParser.T__0)
            self.state = 23
            self.match(PropertyParser.EQUALS)
            self.state = 24
            self.match(PropertyParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrevKContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(PropertyParser.EQUALS, 0)

        def NUMBER(self):
            return self.getToken(PropertyParser.NUMBER, 0)

        def getRuleIndex(self):
            return PropertyParser.RULE_prevK

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrevK" ):
                listener.enterPrevK(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrevK" ):
                listener.exitPrevK(self)




    def prevK(self):

        localctx = PropertyParser.PrevKContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_prevK)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(PropertyParser.T__1)
            self.state = 27
            self.match(PropertyParser.EQUALS)
            self.state = 28
            self.match(PropertyParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andexpression(self):
            return self.getTypedRuleContext(PropertyParser.AndexpressionContext,0)


        def getRuleIndex(self):
            return PropertyParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PropertyParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.andexpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orexpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropertyParser.OrexpressionContext)
            else:
                return self.getTypedRuleContext(PropertyParser.OrexpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(PropertyParser.AND)
            else:
                return self.getToken(PropertyParser.AND, i)

        def getRuleIndex(self):
            return PropertyParser.RULE_andexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndexpression" ):
                listener.enterAndexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndexpression" ):
                listener.exitAndexpression(self)




    def andexpression(self):

        localctx = PropertyParser.AndexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_andexpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.orexpression()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PropertyParser.AND:
                self.state = 33
                self.match(PropertyParser.AND)
                self.state = 34
                self.orexpression()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notexpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PropertyParser.NotexpressionContext)
            else:
                return self.getTypedRuleContext(PropertyParser.NotexpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(PropertyParser.OR)
            else:
                return self.getToken(PropertyParser.OR, i)

        def getRuleIndex(self):
            return PropertyParser.RULE_orexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrexpression" ):
                listener.enterOrexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrexpression" ):
                listener.exitOrexpression(self)




    def orexpression(self):

        localctx = PropertyParser.OrexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_orexpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.notexpression()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PropertyParser.OR:
                self.state = 41
                self.match(PropertyParser.OR)
                self.state = 42
                self.notexpression()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PropertyParser.NOT, 0)

        def atom(self):
            return self.getTypedRuleContext(PropertyParser.AtomContext,0)


        def getRuleIndex(self):
            return PropertyParser.RULE_notexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotexpression" ):
                listener.enterNotexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotexpression" ):
                listener.exitNotexpression(self)




    def notexpression(self):

        localctx = PropertyParser.NotexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_notexpression)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PropertyParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(PropertyParser.NOT)
                self.state = 49
                self.atom()
                pass
            elif token in [PropertyParser.LPAREN, PropertyParser.TRUE, PropertyParser.FALSE, PropertyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PropertyParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(PropertyParser.NUMBER, 0)

        def LPAREN(self):
            return self.getToken(PropertyParser.LPAREN, 0)

        def andexpression(self):
            return self.getTypedRuleContext(PropertyParser.AndexpressionContext,0)


        def RPAREN(self):
            return self.getToken(PropertyParser.RPAREN, 0)

        def boolean(self):
            return self.getTypedRuleContext(PropertyParser.BooleanContext,0)


        def getRuleIndex(self):
            return PropertyParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = PropertyParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atom)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PropertyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(PropertyParser.IDENTIFIER)
                self.state = 54
                self.match(PropertyParser.NUMBER)
                pass
            elif token in [PropertyParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(PropertyParser.LPAREN)
                self.state = 56
                self.andexpression()
                self.state = 57
                self.match(PropertyParser.RPAREN)
                pass
            elif token in [PropertyParser.TRUE, PropertyParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.boolean()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(PropertyParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PropertyParser.FALSE, 0)

        def getRuleIndex(self):
            return PropertyParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)




    def boolean(self):

        localctx = PropertyParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==PropertyParser.TRUE or _la==PropertyParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





