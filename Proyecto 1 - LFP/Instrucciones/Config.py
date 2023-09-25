from Abstract.abstract import Expression

class Configuraciones(Expression):

    def __init__(self, texto, tipo, fila, columna):
        super().__init__(fila, columna)
        self.texto = texto
        self.tipo = tipo

    def operar(self, arbol):
        pass

    def operar_texto(self):
        if self.texto != None:
            tipo = self.tipo

        if tipo == 'texto':
            return tipo
        elif tipo == 'fondo':
            return tipo
        elif tipo == 'fuente':
            return tipo
        elif tipo == 'forma':
            return tipo
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()