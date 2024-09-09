from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer

import json

@api_view(['GET'])
def get_usuarios(request):
    
    if request.method == 'GET':
        
        usuarios = Usuario.objects.all()
        
        serializer = UsuarioSerializer(usuarios, many=True)
        
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_id(request, id):
        
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.get(pk="euzinha")
            print(f"olha o usuário: {usuario}")
            serializer = UsuarioSerializer(usuario)
        except:
            print(Exception)
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        return Response(serializer.data)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def usuario_manager(request):
    
#     if request.method == 'GET':
        
#         try:
#             request.GET['nome']:
                
#                 nome = request.GET[nome]  
                
                 