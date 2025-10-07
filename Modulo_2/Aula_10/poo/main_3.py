from questao3 import Produto, Estoque

produto_1 = Produto("Caneta", 1.0, 100)
produto_2 = Produto("Caderno", 10.0, 50)
produto_3 = Produto("Borracha", 0.5, 200)

estoque = Estoque(produto_1)
estoque.adicionar_produto(produto_2)
estoque.adicionar_produto(produto_3)
estoque.total_em_estoque()