class Carro:
    def __init__(self, marca: str, ano: int):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        return f"Marca: {self.marca}\nAno: {self.ano}"
    
carro1 = Carro("Toyota", 2020)
print(carro1.exibir_informacoes())