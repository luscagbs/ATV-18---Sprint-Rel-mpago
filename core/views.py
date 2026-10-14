from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa

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


def editar_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        projeto.nome = request.POST.get('nome')
        projeto.descricao = request.POST.get('descricao')
        projeto.data_inicio = request.POST.get('data_inicio')
        projeto.save()

        projetos = Projeto.objects.all()
        return render(request, 'projetos/lista.html', {
            'projetos': projetos
        })

    return render(request, 'projetos/editar.html', {
        'projeto': projeto
    })


def excluir_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        projeto.delete()

        projetos = Projeto.objects.all()
        return render(request, 'projetos/lista.html', {
            'projetos': projetos
        })

    return render(request, 'projetos/excluir.html', {
        'projeto': projeto
    })

def lista_tarefas(request):
    tarefas = Tarefa.objects.select_related('projeto').all()

    return render(request, 'tarefas/lista.html', {
        'tarefas': tarefas
    })


def nova_tarefa(request):
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_entrega = request.POST.get('data_entrega')
        projeto_id = request.POST.get('projeto')

        projeto = get_object_or_404(Projeto, id=projeto_id)

        Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            data_entrega=data_entrega,
            projeto=projeto
        )

        return redirect('lista_tarefas')

    return render(request, 'tarefas/form.html', {
        'projetos': projetos
    })

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.data_entrega = request.POST.get('data_entrega')

        projeto_id = request.POST.get('projeto')
        tarefa.projeto = get_object_or_404(Projeto, id=projeto_id)

        tarefa.save()

        return redirect('lista_tarefas')

    return render(request, 'tarefas/editar.html', {
        'tarefa': tarefa,
        'projetos': projetos
    })


def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')

    return render(request, 'tarefas/excluir.html', {
        'tarefa': tarefa
    })