from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario, Animal
from .serializers import UsuarioSerizalizer, AnimalSerizalizer

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