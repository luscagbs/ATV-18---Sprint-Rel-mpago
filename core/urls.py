from django.urls import path
from . import views

urlpatterns = [
    # Projetos
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/novo/', views.novo_projeto, name='novo_projeto'),
    path('projetos/editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/excluir/<int:id>/', views.excluir_projeto, name='excluir_projeto'),

    # Tarefas
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.nova_tarefa, name='nova_tarefa'),
    path('tarefas/editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
]