from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Banco de dados em memória
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 49.90},
    {"id": 2, "nome": "Tênis", "preco": 199.90},
]

@api_view(["GET"])
def listar_produtos(request):
    return Response(produtos)

@api_view(["POST"])
def criar_produto(request):
    novo = request.data.copy()
    novo_ordered = {"id": len(produtos) + 1}
    novo_ordered.update(novo)
    produtos.append(novo_ordered)
    return Response(novo_ordered, status=201)