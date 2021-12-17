from django.shortcuts import render

def index(request):

    receita = {
        1: 'Sorvete',
        2: 'Sopa de Legumes',
        3: 'Suco Verde'
    }

    dados = {
        'nome_das_receitas' : receita
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
