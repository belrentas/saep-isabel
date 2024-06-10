from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

class Turma(models.Model):
    Nome_Turma = models.CharField(verbose_name='Turma', max_length=99, null=False, blank=False)
    Nome_Professor = models.CharField(verbose_name='Nome Professor', max_length=99, null=False, blank=False)
    id_professor = models.ForeignKey(User, verbose_name='Id-Professor', on_delete=models.CASCADE, null=False, blank=False)

class Atividades(models.Model):
    Nome_item = models.CharField(verbose_name='Atividade', max_length=99, null=False, blank=False)
    id_professor = models.ForeignKey(User, verbose_name='Id-Professor', on_delete=models.CASCADE, null=False, blank=False)
    Nome_Professor = models.CharField(verbose_name='Nome Professor', max_length=99, null=False, blank=False)
    id_turma = models.ForeignKey(Turma, verbose_name='Id-Turma', on_delete=models.CASCADE, null=False, blank=False)
    Nome_Turma = models.CharField(verbose_name='Nome Professor', max_length=99, null=False, blank=False)
