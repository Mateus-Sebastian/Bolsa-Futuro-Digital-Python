class Animal:
    def __init__(self, nome: str, especie: str):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")

gato1 = Gato("Luna", "Siamese")
cachorro1 = Cachorro("Rex", "Labrador")

gato1.fazer_som()
cachorro1.fazer_som()
print(f"Gato: {gato1.nome}, Espécie: {gato1.especie}")