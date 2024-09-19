from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, id_user, nome, email, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
        user = self.model(id_user=id_user, nome=nome.strip(), email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_user, nome, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(id_user, nome, email, password=password, **extra_fields)

class Usuario(AbstractBaseUser):
    id_user = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=80)
    telefone = models.TextField()
    email = models.EmailField()
    localizacao = models.TextField()
    descricao = models.CharField(max_length=180)
    foto = models.TextField(null=True)
    conta_bancaria = models.TextField(null=True)
    chave_pix = models.TextField(null=True)
    tipo_usuario_escolhas = [("PF", "Pessoa Física"),("PJ", "Pessoa Jurídica")]
    tipo_usuario = models.CharField(max_length=2, choices=tipo_usuario_escolhas)
    is_staff = models.BooleanField(null=False, default=False)
    is_superuser = models.BooleanField(null=False, default=False)

    objects = UsuarioManager()
    
    USERNAME_FIELD = 'id_user'

    def __str__(self):
        return self.nome

class Animal(models.Model):
    id_animal = models.AutoField(primary_key=True)
    animal_nome = models.CharField(max_length=80)
    raca = models.CharField(max_length=30)
    idade = models.IntegerField()
    tamanho = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    localizacao = models.CharField(max_length=80)
    descricao = models.CharField(max_length=80)
    foto = models.TextField()
    data_criacao = models.DateField(null=True)
    status = models.CharField(max_length=15)
    id_doador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='doador')
    id_adotador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='adotador', null=True)
    data_adocao = models.DateField(null=True)

    def __str__(self):
        return self.animal_nome