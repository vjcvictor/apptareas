from django.db import models
from django.contrib.auth.models import AbstractUser
from familias.models import Familia

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    id_familia = models.ForeignKey(Familia, on_delete=models.RESTRICT, null=True, db_column='id_familia')

    #COMENTAR EN CASO DE NECESIDAD PARA CREAR MAS SUPERUARIOS

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []