class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 7.0:
            print(f"Aluno {self.nome} aprovado(a) com nota {self.nota}.")
        else:
            print(f"Aluno {self.nome} reprovado(a) com nota {self.nota}.")

aluno_1 = Aluno("João", 8.5)
aluno_1.verificar_aprovacao()
aluno_2 = Aluno("Maria", 6.0)
aluno_2.verificar_aprovacao()