# Definindo a classe
class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"O {self.modelo}, está acelerando.")

# Criando instâncias da classe Carro
carro1 = Carro('Vermelho', 'Fusca', 1967)
carro2 = Carro('Azul', 'Civic', 2020)

# Acessando atributos e métodos das instâncias
print(carro1.cor)
carro1.acelerar()

print(carro2.cor)
carro2.acelerar()


class teste:
    def __init__(self) -> None:
        pass 