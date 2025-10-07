# Polimorfismo com Sobrecarga de Operadores se baseia em permitir que operadores sejam
# redefinidos para tipos de dados definidos pelo usuário.
class Vetor:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Sobrecarga do operador + para somar dois vetores
    def __add__ (self, outro: 'Vetor') -> 'Vetor':
        return Vetor(self.x + outro.x, self.y + outro.y)

    # Sobrecarga do operador str, responsável por converter o objeto em string
    def __str__(self):
        return f"{self.x}, {self.y}"
    
vetor1 = Vetor(2, 4)
vetor2 = Vetor(5, 2)

print(f"Vetor 1: ({vetor1})")
print(f"Vetor 2: ({vetor2})")
print(f"Soma: ({vetor1 + vetor2})")