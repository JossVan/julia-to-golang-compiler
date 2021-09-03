from Abstractas.Objeto import Objeto

class Primitivo(Objeto):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor=valor

    def toString(self):
        return str(self.valor)

    def getValue(self):
        return self.valor