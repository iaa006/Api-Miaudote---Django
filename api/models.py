from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_user = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=80)
    senha = models.TextField()
    telefone = models.TextField()
    email = models.EmailField()
    localizacao = models.TextField()
    descricao = models.CharField(max_length=180)
    foto = models.TextField()
    conta_bancaria = models.TextField()
    chave_pix = models.TextField()
    tipo_usuario_escolhas = [("PF", "Pessoa Física"),("PJ", "Pessoa Jurídica")]
    tipo_usuario = models.CharField(max_length=2, choices=tipo_usuario_escolhas)

class Animal(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    raca = models.CharField(max_length=30)
    idade = models.IntegerField()
    tamanho = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    localizacao = models.CharField(max_length=80)
    descricao = models.CharField(max_length=80)
    foto = models.TextField()
    data_criacao = models.DateField()
    status = models.CharField()
    id_doador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_adotador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_adocao = models.DateField()
