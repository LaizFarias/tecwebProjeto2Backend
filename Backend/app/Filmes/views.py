
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Filme
from .serializers import FilmeSerializer
import json

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

@api_view(['POST','GET'])
def save(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        backdrop_path = data['backdrop_path']
        Filme.objects.get_or_create(nome=name, backdrop_path=backdrop_path)


    filme = Filme.objects.all()
    serialized_filme =FilmeSerializer(filme, many=True)
    
    return Response(serialized_filme.data)
