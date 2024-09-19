from rest_framework import serializers
from .models import Usuario, Animal

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(max_length=128)    
    class Meta:
        model = Usuario
        fields = ["id_user", "nome", "telefone", "email", "localizacao", 
                  "descricao", "foto", "conta_bancaria", "chave_pix", "tipo_usuario", 
                  "is_staff", "is_superuser", 'senha']

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['senha'])
        usuario.save()
        return usuario

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["id_animal","animal_nome","raca","idade","tamanho","sexo",
                  "localizacao","descricao","foto","data_criacao","status","data_adocao","id_doador","id_adotador"]