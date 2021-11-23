from django.contrib import admin
from escola.models import Ano, Aluno


class Anos(admin.ModelAdmin):
    list_display = ('id', 'serie', 'turno', 'qtd_turmas', 'qtd_alunos_por_turma', 'disciplinas')
    search_fields = ('serie', 'disciplinas')


class Alunos(admin.ModelAdmin):
    list_display = ('id_aluno', 'nome', 'rg_cpf', 'sexo', 'matricula', 'turma', 'nomeMae', 'nomePai',
                    'desblocado', 'nascimento', 'ingresso')
    search_fields = ('nome', 'rg_cpf', 'matricula', 'turma', 'desblocado')


admin.site.register(Ano, Anos)
admin.site.register(Aluno, Alunos)