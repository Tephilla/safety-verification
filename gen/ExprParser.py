# Generated from C:/Users/Atif Rahman/IdeaProjects/interpol\Expr.g4 by ANTLR 4.9.2
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
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\6\4\"\n\4\r\4\16\4#\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\7\6\7.\n\7\r\7\16\7/\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\29\2\26\3\2\2\2")
        buf.write("\4\33\3\2\2\2\6\37\3\2\2\2\b%\3\2\2\2\n)\3\2\2\2\f-\3")
        buf.write("\2\2\2\16\61\3\2\2\2\20\67\3\2\2\2\22;\3\2\2\2\24>\3\2")
        buf.write("\2\2\26\27\5\4\3\2\27\30\5\6\4\2\30\31\5\n\6\2\31\32\5")
        buf.write("\f\7\2\32\3\3\2\2\2\33\34\7\3\2\2\34\35\7\t\2\2\35\36")
        buf.write("\7\b\2\2\36\5\3\2\2\2\37!\7\4\2\2 \"\5\b\5\2! \3\2\2\2")
        buf.write("\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\7\3\2\2\2%&\5\22\n\2")
        buf.write("&\'\7\t\2\2\'(\7\b\2\2(\t\3\2\2\2)*\7\5\2\2*+\5\20\t\2")
        buf.write("+\13\3\2\2\2,.\5\16\b\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2")
        buf.write("/\60\3\2\2\2\60\r\3\2\2\2\61\62\7\6\2\2\62\63\5\20\t\2")
        buf.write("\63\64\7\t\2\2\64\65\7\f\2\2\65\66\5\24\13\2\66\17\3\2")
        buf.write("\2\2\678\7\n\2\289\5\24\13\29:\7\13\2\2:\21\3\2\2\2;<")
        buf.write("\7\7\2\2<=\7\b\2\2=\23\3\2\2\2>?\7\7\2\2?@\7\b\2\2@\25")
        buf.write("\3\2\2\2\4#/")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SIZE'", "'STATES'", "'INIT'", "'NEXT'", 
                     "'s'", "<INVALID>", "':'", "'('", "')'", "'='", "'T'", 
                     "'F'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "COLON", "OPEN_BR", 
                      "CLOSE_BR", "EQUALS", "T", "F", "ENDLINE", "WHITESPACE" ]

    RULE_doc = 0
    RULE_field_size = 1
    RULE_state_seg = 2
    RULE_create_state = 3
    RULE_initialization = 4
    RULE_next_state = 5
    RULE_create_next_state = 6
    RULE_state_name_bracket = 7
    RULE_state_name = 8
    RULE_state_name_next = 9

    ruleNames =  [ "doc", "field_size", "state_seg", "create_state", "initialization", 
                   "next_state", "create_next_state", "state_name_bracket", 
                   "state_name", "state_name_next" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    COLON=7
    OPEN_BR=8
    CLOSE_BR=9
    EQUALS=10
    T=11
    F=12
    ENDLINE=13
    WHITESPACE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_size(self):
            return self.getTypedRuleContext(ExprParser.Field_sizeContext,0)


        def state_seg(self):
            return self.getTypedRuleContext(ExprParser.State_segContext,0)


        def initialization(self):
            return self.getTypedRuleContext(ExprParser.InitializationContext,0)


        def next_state(self):
            return self.getTypedRuleContext(ExprParser.Next_stateContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_doc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoc" ):
                listener.enterDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoc" ):
                listener.exitDoc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoc" ):
                return visitor.visitDoc(self)
            else:
                return visitor.visitChildren(self)




    def doc(self):

        localctx = ExprParser.DocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_doc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.field_size()
            self.state = 21
            self.state_seg()
            self.state = 22
            self.initialization()
            self.state = 23
            self.next_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_field_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_size" ):
                listener.enterField_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_size" ):
                listener.exitField_size(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_size" ):
                return visitor.visitField_size(self)
            else:
                return visitor.visitChildren(self)




    def field_size(self):

        localctx = ExprParser.Field_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_field_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ExprParser.T__0)
            self.state = 26
            self.match(ExprParser.COLON)
            self.state = 27
            self.match(ExprParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class State_segContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_state(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Create_stateContext)
            else:
                return self.getTypedRuleContext(ExprParser.Create_stateContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_state_seg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterState_seg" ):
                listener.enterState_seg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitState_seg" ):
                listener.exitState_seg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitState_seg" ):
                return visitor.visitState_seg(self)
            else:
                return visitor.visitChildren(self)




    def state_seg(self):

        localctx = ExprParser.State_segContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_state_seg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ExprParser.T__1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.create_state()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.T__4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_name(self):
            return self.getTypedRuleContext(ExprParser.State_nameContext,0)


        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_create_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_state" ):
                listener.enterCreate_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_state" ):
                listener.exitCreate_state(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_state" ):
                return visitor.visitCreate_state(self)
            else:
                return visitor.visitChildren(self)




    def create_state(self):

        localctx = ExprParser.Create_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_create_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.state_name()
            self.state = 36
            self.match(ExprParser.COLON)
            self.state = 37
            self.match(ExprParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_name_bracket(self):
            return self.getTypedRuleContext(ExprParser.State_name_bracketContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialization" ):
                listener.enterInitialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialization" ):
                listener.exitInitialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = ExprParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ExprParser.T__2)
            self.state = 40
            self.state_name_bracket()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_next_state(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Create_next_stateContext)
            else:
                return self.getTypedRuleContext(ExprParser.Create_next_stateContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_next_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext_state" ):
                listener.enterNext_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext_state" ):
                listener.exitNext_state(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_state" ):
                return visitor.visitNext_state(self)
            else:
                return visitor.visitChildren(self)




    def next_state(self):

        localctx = ExprParser.Next_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_next_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.create_next_state()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.T__3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_next_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_name_bracket(self):
            return self.getTypedRuleContext(ExprParser.State_name_bracketContext,0)


        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def EQUALS(self):
            return self.getToken(ExprParser.EQUALS, 0)

        def state_name_next(self):
            return self.getTypedRuleContext(ExprParser.State_name_nextContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_create_next_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_next_state" ):
                listener.enterCreate_next_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_next_state" ):
                listener.exitCreate_next_state(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_next_state" ):
                return visitor.visitCreate_next_state(self)
            else:
                return visitor.visitChildren(self)




    def create_next_state(self):

        localctx = ExprParser.Create_next_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_create_next_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ExprParser.T__3)
            self.state = 48
            self.state_name_bracket()
            self.state = 49
            self.match(ExprParser.COLON)
            self.state = 50
            self.match(ExprParser.EQUALS)
            self.state = 51
            self.state_name_next()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class State_name_bracketContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BR(self):
            return self.getToken(ExprParser.OPEN_BR, 0)

        def state_name_next(self):
            return self.getTypedRuleContext(ExprParser.State_name_nextContext,0)


        def CLOSE_BR(self):
            return self.getToken(ExprParser.CLOSE_BR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_state_name_bracket

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterState_name_bracket" ):
                listener.enterState_name_bracket(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitState_name_bracket" ):
                listener.exitState_name_bracket(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitState_name_bracket" ):
                return visitor.visitState_name_bracket(self)
            else:
                return visitor.visitChildren(self)




    def state_name_bracket(self):

        localctx = ExprParser.State_name_bracketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_state_name_bracket)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExprParser.OPEN_BR)
            self.state = 54
            self.state_name_next()
            self.state = 55
            self.match(ExprParser.CLOSE_BR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class State_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_state_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterState_name" ):
                listener.enterState_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitState_name" ):
                listener.exitState_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitState_name" ):
                return visitor.visitState_name(self)
            else:
                return visitor.visitChildren(self)




    def state_name(self):

        localctx = ExprParser.State_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_state_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExprParser.T__4)
            self.state = 58
            self.match(ExprParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class State_name_nextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_state_name_next

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterState_name_next" ):
                listener.enterState_name_next(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitState_name_next" ):
                listener.exitState_name_next(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitState_name_next" ):
                return visitor.visitState_name_next(self)
            else:
                return visitor.visitChildren(self)




    def state_name_next(self):

        localctx = ExprParser.State_name_nextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_state_name_next)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ExprParser.T__4)
            self.state = 61
            self.match(ExprParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





