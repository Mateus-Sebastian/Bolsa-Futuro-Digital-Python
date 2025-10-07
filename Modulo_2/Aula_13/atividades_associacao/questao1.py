# Crie duas classes: Autor e Livro.

# O autor tem nome e nacionalidade.
# O livro tem título e um objeto autor.
# Crie 2 autores e 3 livros.
# Mostre no terminal o nome do livro e o nome do autor.

class Autor:
    def __init__(self, nome: str, nacionalidade: str):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def set_nome(self, nome: str):
        self.nome = nome

    def set_nacionalidade(self, nacionalidade: str):
        self.nacionalidade = nacionalidade

    def get_nome(self):
        return self.nome

    def get_nacionalidade(self):
        return self.nacionalidade

class Livro:
    def __init__(self, titulo: str, autor: Autor):
        self.titulo = titulo
        self.autor = autor

    def set_titulo(self, titulo: str):
        self.titulo = titulo
    
    def set_autor(self, autor: Autor):
        self.autor = autor

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor