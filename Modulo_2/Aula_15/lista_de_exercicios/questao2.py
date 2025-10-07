from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float | int:
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

retangulo1 = Retangulo(4, 5)
print("Área do retângulo:", retangulo1.calcular_area())