class Calculadora:
    def __init__(self):
        self.resultado = 0
        
    def somar(self, a, b):
        self.resultado = a + b

    def imprimir_resultado_soma(self):
        print(f"O resultado da soma é:", self.resultado)

    def subtrair(self, a, b):
        self.resultado = a - b

    def imprimir_resultado_subtrai(self):
        print(f"O resultado da subtração é:", self.resultado)
       

num1 = int(input('digite: '))
num2 = int(input('digite: '))

calculadora = Calculadora()
calculadora.somar(num1, num2)
calculadora.imprimir_resultado_soma()

calculadora.subtrair(num1, num2)
calculadora.imprimir_resultado_subtrai()
