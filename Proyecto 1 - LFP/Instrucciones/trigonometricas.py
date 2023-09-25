from Abstract.abstract import Expression
from math import *

class Trigonometrica(Expression):

    def __init__(self, left, tipo, fila, columna):
        super().__init__(fila, columna)
        self.left = left
        self.tipo = tipo

    def operar(self, arbol):  
        leffValue = ''
        if self.left != None:
            leffValue = self.left.operar(arbol)

        if self.tipo.operar(arbol) == 'seno' or 'Seno':
            return sin(leffValue)
        elif self.tipo.operar(arbol) == 'coseno' or 'Coseno':
            return cos(leffValue)
        elif self.tipo.operar(arbol) == 'tangente' or 'Tangente':
            return tan(leffValue)
        else:
            return None
        
    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
