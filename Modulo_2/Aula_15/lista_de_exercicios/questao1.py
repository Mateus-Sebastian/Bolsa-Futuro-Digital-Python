class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Latido!")

animal = Animal("Animal Genérico")
cachorro = Cachorro("Rex")

animal.emitir_som()
cachorro.emitir_som()