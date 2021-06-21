from django.shortcuts import render, get_object_or_404
from .models import Tarefa, ItemExecucao

def tarefa_list(request):
    tarefas = Tarefa.ativa.all()
    return render(request, 'tarefas/list_tarefas.html', {'tarefas':tarefas})

def tarefa_detail(request, tarefa):
    tarefa = get_object_or_404(Tarefa, slug = tarefa, status = 'a')
    itens = tarefa.itens.all()
    return render(request, 'tarefas/detail_tarefas.html', {'tarefa':tarefa, 'itens':itens})
