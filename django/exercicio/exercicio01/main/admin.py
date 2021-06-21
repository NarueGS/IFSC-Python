from django.contrib import admin
from .models import Festa,Itens
# Register your models here.

@admin.register(Itens)
class ItensAdmin(admin.ModelAdmin):
    list_display = ['FestaItens','AddItem']
    raw_id_fields = ('FestaItens',)



@admin.register(Festa)
class Festa(admin.ModelAdmin):
    list_display = ['nomeCliente','telefone','slug','dataPedido','dataFesta','HoraInicio','Aluguel','Rua','Num','Tema']
    prepopulated_fields = {'slug':('nomeCliente',)}
    search_fields = ('nomeCliente','dataPedido','dataFesta')
    date_hierarchy = 'dataPedido'
    ordering = ('dataPedido',)

