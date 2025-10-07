#classes abstratas em python são criadas utilizando o módulo abc (Abstract Base Classes)
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> float | int | None:
        return

    @abstractmethod
    def perimetro(self) -> float | int | None:
        return

# Subclasse concreta
class Quadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

q = Quadrado(5)
print("Área:", q.area())
print("Perímetro:", q.perimetro())