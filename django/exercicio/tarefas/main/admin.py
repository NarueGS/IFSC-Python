from django.contrib import admin
from .models import Tarefa, ItemExecucao

@admin.register(ItemExecucao)
class ItemExecucaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'percentual', 'tarefa', 'data_execucao', 'slug']
    list_filter = ['data_execucao', 'tarefa']
    prepopulated_fields = {'slug':('descricao',)}
    search_fields = ('descricao',)
    raw_id_fields = ('tarefa',)
    date_hierarchy = 'data_criacao'
    ordering = ('data_execucao',)
    
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['num_prioridade', 'nome', 'slug', 'data_limite_execucao',
                    'detalhamento', 'percentual_conclusao', 'status'
                    ]
    list_filter = ['data_limite_execucao', 'status', 'percentual_conclusao']
    prepopulated_fields = {'slug':('nome',)}
    search_fields = ('nome', 'detalhamento')
    date_hierarchy = 'data_limite_execucao'
    ordering = ('data_criacao',)
    
    


