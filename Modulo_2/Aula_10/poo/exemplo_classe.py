class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        return f"{self.ano} {self.marca} {self.modelo}"
    
meu_carro = Carro("Toyota", "Corolla", 2020)
print(meu_carro.exibir_informacoes())