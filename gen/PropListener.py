from gen.MyListener import MyListener
from gen.PropertyListener import PropertyListener
from gen.PropertyParser import PropertyParser


class PropListener(PropertyListener):
    prevk = 0
    k = 0
    formula = " "
    def exitPrevK(self, ctx:PropertyParser.PrevKContext):
        PropListener.prevk = int(ctx.NUMBER().getText())

    def exitK(self, ctx:PropertyParser.KContext):
        PropListener.k = int(ctx.NUMBER().getText())

    def enterExpression(self, ctx:PropertyParser.ExpressionContext):
        PropListener.formula = ctx.getText()

    def enterAtom(self, ctx:PropertyParser.AtomContext):
        c = MyListener()
        data = c.return_data()
        number = int(ctx.NUMBER().getText())
        if number>= data:
            print("Given property is not valid")
            exit()

    def return_to_main(self):
        return self.prevk, self.k, self.formula


