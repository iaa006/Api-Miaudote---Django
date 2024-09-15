from rest_framework import serializers

from .models import Usuario, Animal

class UsuarioSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AnimalSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'