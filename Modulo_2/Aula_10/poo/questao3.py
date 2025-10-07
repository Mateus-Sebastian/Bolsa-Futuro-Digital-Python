class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self, produto: Produto):
        self.produtos = {produto.nome: (produto.preco, produto.quantidade)}
        self.total = produto.quantidade
        print(f"Estoque inciado com {produto.quantidade} unidade(s) do produto {produto.nome}.")

    def adicionar_produto(self, produto: Produto):
        self.produtos.update({produto.nome: (produto.preco, produto.quantidade)})
        self.total += produto.quantidade
        print(f"{produto.quantidade} unidade(s) do produto {produto.nome} adicionado(s) ao estoque.")
        print(f"Total de itens no estoque: {self.total}")

    def total_em_estoque(self):
        total = 0
        for preco, quantidade in self.produtos.values():
            total += preco * quantidade
        print(f"Valor total em estoque: R${total:.2f}")
