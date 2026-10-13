from django.shortcuts import render
from .models import Projeto


def lista_projetos(request):
    projetos = Projeto.objects.all()

    return render(request, 'projetos/lista.html', {
        'projetos': projetos
    })


def novo_projeto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')

        Projeto.objects.create(
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio
        )

        projetos = Projeto.objects.all()

        return render(request, 'projetos/lista.html', {
            'projetos': projetos
        })

    return render(request, 'projetos/form.html')
