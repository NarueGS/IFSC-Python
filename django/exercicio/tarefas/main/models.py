from django.db import models
from django.urls import reverse

class AtivaManager(models.Manager):
    def get_queryset(self):
        return super(AtivaManager, self).get_queryset().filter(status = 'a')
    
class Tarefa(models.Model):
    num_prioridade = models.DecimalField(max_digits = 5, decimal_places = 2)
    nome = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    data_limite_execucao = models.DateField(null = False, blank = False)
    detalhamento = models.TextField()
    percentual_conclusao = models.DecimalField(max_digits = 3, decimal_places = 2)
    STATUS = (('a', 'Ativa'), ('c', 'Concluida'))
    status = models.CharField(max_length = 1, choices = STATUS)
    data_criacao = models.DateTimeField(auto_now_add = True)
    data_atualizacao = models.DateTimeField(auto_now = True)
    ativa = AtivaManager()
    
    def get_absolute_url(self):
        return reverse('main:tarefa_detail', args = [self.slug])
    
    def __str__(self):
        return self.nome
    
class ItemExecucao(models.Model):
    percentual = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0.00)
    descricao = models.TextField()
    data_execucao = models.DateField(blank = True)
    tarefa = models.ForeignKey(Tarefa, on_delete = models.CASCADE, related_name = 'itens')  
    slug = models.SlugField(max_length = 100)
    data_criacao = models.DateTimeField(auto_now_add = True)
    data_atualizacao = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.descricao
    
    