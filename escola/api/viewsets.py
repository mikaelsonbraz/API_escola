from rest_framework import viewsets
from escola.models import Ano, Aluno
from escola.api import serializer


class AnosViewSet(viewsets.ModelViewSet):
    queryset = Ano.objects.all()
    serializer_class = serializer.AnoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = serializer.AlunoSerializer
