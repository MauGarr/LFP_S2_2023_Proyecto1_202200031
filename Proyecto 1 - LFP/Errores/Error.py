from Abstract.abstract import Expression

class Error(Expression):

    def __init__(self, lexema, fila, columna):
        super().__init__(fila, columna)
        self.lexema = lexema

    def operar(self, no):
        lex = "Error en : " + self.lexema
        return lex
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()