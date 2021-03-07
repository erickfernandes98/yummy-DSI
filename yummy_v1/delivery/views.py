from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Sobremesa


def index(request):
    sobremesas = Sobremesa.objects.all()

    dados = {
        'sobremesas': sobremesas
    }
    return render(request, 'index.html', dados) #retorna a renderização do arquivo index.html


def sobremesa(request, sobremesa_id):
    sobremesa = get_object_or_404(Sobremesa, pk=sobremesa_id)

    sobremesa_a_exibir = {
        'sobremesa': sobremesa
    }

    return render(request, 'sobremesa.html', sobremesa_a_exibir)