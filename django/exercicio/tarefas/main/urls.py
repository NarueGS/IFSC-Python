from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('',views.tarefa_list, name = 'tarefa_list'),
    path('<slug:tarefa>', views.tarefa_detail, name = 'tarefa_detail'),
    ]

