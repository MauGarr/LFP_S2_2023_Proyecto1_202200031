from Abstract.abstract import Expression

class Aritmetica(Expression):

    def __init__(self, left, right, tipo, fila, columna):
        super().__init__(fila, columna)
        self.left = left
        self.right = right
        self.tipo = tipo

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''
        if self.left != None:
            leftValue = self.left.operar(arbol)
        if  self.right != None:
            rightValue = self.right.operar(arbol)
        
        if self.tipo.operar(arbol) == 'suma' or 'Suma':
            return leftValue + rightValue
        elif self.tipo.operar(arbol) == 'resta' or 'Resta':
            return leftValue - rightValue
        elif self.tipo.operar(arbol) == 'multiplicacion' or 'Multiplicacion':
            return leftValue * rightValue
        elif self.tipo.operar(arbol) == 'division' or 'Division':
            return leftValue / rightValue
        elif self.tipo.operar(arbol) == 'modulo' or 'Modulo':
            return leftValue % rightValue
        elif self.tipo.operar(arbol) == 'potencia' or 'Potencia':
            return leftValue ** rightValue
        elif self.tipo.operar(arbol) == 'raiz' or 'Raiz':
            return leftValue ** (1/rightValue)
        elif self.tipo.operar(arbol) == 'inverso' or 'Inverso':
            return 1/leftValue    
        else:
            return None
        
    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
        