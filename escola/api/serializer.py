from rest_framework import serializers
from escola.models import Ano, Aluno


class AnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ano
        fields = ['id', 'serie', 'turno', 'disciplinas']


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id_aluno', 'nome', 'turma', 'matricula', 'desblocado', 'nascimento', 'ingresso']

