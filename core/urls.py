from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/novo/', views.novo_projeto, name='novo_projeto'),
    path('projetos/editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/excluir/<int:id>/', views.excluir_projeto, name='excluir_projeto'),
]
