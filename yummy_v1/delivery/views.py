from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Sobremesa


def index(request):
    sobremesas = Sobremesa.objects.order_by('-date_sobremesa').filter(publicada=True)

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


def buscar(request):
    lista_sobremesas = Sobremesa.objects.order_by('-date_sobremesa').filter(publicada=True)

    if 'buscar' in request.GET: #Verificando se o campo de busca possui algum valor
        nome_a_buscar = request.GET['buscar'] #Conteúdo que queremos buscar
        if buscar: #Se tem de fato um valor, filtramos o valor dessa lista
            lista_sobremesas = lista_sobremesas.filter(nome_sobremesa__icontains=nome_a_buscar) #Verificando se temos alguma sobremesa que contem esse valor
    
    dados = {
        'sobremesas' : lista_sobremesas 
    }

    return render(request, 'buscar.html', dados)
