class Calculadora:
    def __init__(self):
        self.valor = 0

    def sumar(self, n):
        self.valor += n
        return self.valor

    def reset(self):
        self.valor = 0
 