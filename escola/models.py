from django.db import models
from uuid import uuid4


class Ano(models.Model):
    TURNOS_CHOICES = (
        ('M', "Matutino"),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )

    serie = models.IntegerField()
    turno = models.Choices(max_length=1, choices=TURNOS_CHOICES, blank=False, null=False)
    qtd_turmas = models.IntegerField()
    qtd_alunos_por_turma = models.IntegerField()
    disciplinas = models.TextField()

    def getSerie(self):
        return self.serie

    def getDisciplinas(self):
        return self.disciplinas

    def __str__(self):
        return f'Ano {self.serie}, Turno '

#-----------------------------------------------------------------------------------------------------------------------

class Aluno(Ano):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    rg_cpf = models.CharField(max_length=11)
    sexo = models.Choices(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    matricula = models.IntegerField(unique=True)
    turma = models.ForeignKey(Ano, on_delete=models.CASCADE)
    nomeMae = models.CharField(max_length=255)
    nomePai = models.CharField(max_length=255)
    desblocado = models.BooleanField(default=False)
    nascimento = models.DateField()
    ingresso = models.DateField()

    def __str__(self):
        return f'{self.nome} - Matrícula: {self.matricula}'
