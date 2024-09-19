from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.middleware.csrf import get_token

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario, Animal
from .serializers import UsuarioSerializer, AnimalSerializer

import json

@api_view(['GET', 'POST'])
def animals(request):

    if request.method == 'GET':
        animals = Animal.objects.all()

        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = AnimalSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    print('saiu')
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_animal(request, id):
    if request.method == 'GET':
        animal = None
        try:
            print('try')
            animal = Animal.objects.get(id_animal=id)
            print(animal)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AnimalSerializer(animal)

        return Response(serializer.data)

    if request.method == 'PUT':
        try:
            animal = Animal.objects.get(id_animal=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AnimalSerializer(animal, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

    if request.method == 'DELETE':

        try:
            animal = Animal.objects.get(id_animal=id)
            animal.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])

def logar(request):
    id_user= request.data['id_user']
    password = request.data['senha']
    print(id_user, password)
    user = authenticate(request, id_user=id_user, password=password)

    if user is not None:
        login_django(request, user)
        return HttpResponse({"Logado": True})

    return HttpResponse({"Logado": False})


@login_required(login_url='/api/login')
@api_view(['GET'])
def logout(request):
   logout_django(request)
   return redirect('api:login')


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
        
                      
