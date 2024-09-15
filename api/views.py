from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario, Animal
from .serializers import UsuarioSerializer, AnimalSerizalizer

import json

@api_view(['GET', 'POST'])
def animals(request):

    if request.method == 'GET':
        animals = Animal.objects.all()

        serializer = AnimalSerizalizer(animals, many=True)

        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request,data

        serializer = AnimalSerizalizer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_animal(request, id):
    if request.method == 'GET':
        try:
            animal = Animal.objects.filter(id_animal=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AnimalSerizalizer(animal, many=False)

        return Response(serializer.data)

    if request.method == 'PUT':
        try:
            animal = Animal.objects.filter(id_animal=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AnimalSerizalizer(animal, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

    if request.method == 'DELETE':

        try:
            animal = Animal.objects.filter(id_animal=id)
            animal.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_usuarios(request):
    
    if request.method == 'GET':
        
        usuarios = Usuario.objects.all()
        
        serializer = UsuarioSerializer(usuarios, many=True)
        
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_id(request, id):
    
    try:
        usuario = Usuario.objects.get(pk=id)    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND) 
      
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usuario_manager(request):
    
    if request.method == 'GET':
        
        try:
            if request.GET['id']:
                
                id_user = request.GET['id']
                
                try:
                    id = Usuario.objects.get(pk=id_user)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                    
                serializer = UsuarioSerializer(id)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
                
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
              
              
    if request.method == 'POST':
    
        novo_usuario = request.data 
        
        serializer = UsuarioSerializer(data=novo_usuario)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'PUT':
        
        id = request.data['id_user'] 
        
        try:
            update_id = Usuario.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print(request.data)
        
        serializer = UsuarioSerializer(update_id, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'DELETE':
        
        try:
            id_p_deletar = Usuario.objects.get(pk=request.data['id_user'])
            id_p_deletar.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
                      
