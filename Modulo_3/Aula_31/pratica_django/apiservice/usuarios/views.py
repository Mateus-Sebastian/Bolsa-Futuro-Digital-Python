from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Banco de dados em memória
usuarios = [
    {"id": 1, "nome": "Ana", "email": "ana@email.com"}
]

@api_view(["GET"])
def listar_usuarios(request):
    return Response(usuarios)
    
@api_view(["POST"])
def criar_usuario(request):
    novo = request.data
    if not novo.get("nome") or not novo.get("email"):
        return Response(
            {"erro": "Os campos 'nome' e 'email' são obrigatórios."},
            status=400
        )
    novo_ordem = {"id": len(usuarios) + 1}
    novo_ordem.update(novo)
    usuarios.append(novo_ordem)
    return Response(novo, status=201)