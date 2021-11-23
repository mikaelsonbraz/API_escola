from django.db import models
from uuid import uuid4


class Aluno(models.Model):
    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    matricula = models.IntegerField(unique=True)
    nomeMae = models.CharField(max_length=255)
    nomePai = models.CharField(max_length=255)
    desblocado = models.BooleanField(default=False)
    nascimento = models.DateField(input_formats=['%d/%m/%Y'])
    ingresso = models.DateField(input_formats=['%d/%m/%Y'])
