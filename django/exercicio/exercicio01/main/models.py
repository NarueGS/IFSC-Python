from django.db import models
from django.db.models.fields import CharField, DateField, FloatField, SlugField, related

# Create your models here.
class Festa(models.Model):
    nomeCliente = models.CharField(max_length=120,   null=False,blank = False)
    telefone = models.CharField(max_length=12,null=False,blank = False)
    dataPedido = models.DateField(auto_now_add=True, null=False,blank = False)
    dataFesta = models.DateField(null=False,blank = False)
    Rua = models.CharField(max_length=300, null=False,blank = False)
    Num = models.IntegerField(null=False,blank = False)
    Tema = models.TextField()
    HoraInicio = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    Aluguel = models.FloatField()
    def __str__(self):
        return("Cliente " + self.nomeCliente + " Telefone: " + str(self.telefone))
class Itens(models.Model):
    FestaItens = models.ForeignKey(Festa, on_delete=models.CASCADE, related_name='itens')
    AddItem = models.TextField(null=False)