from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Produto, Vendas, Vendedor
from datetime import datetime
from django.db.models import Sum
import locale

# Create your views here.
def home(request):
    return render(request, 'home.html')

def retorna_total_vendido(request):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    total = locale.currency(total, grouping=True, symbol=None)
    if request.method == "GET":
        return JsonResponse({'total': total})
    
def retorna_qtd_vendas(request):
   count = Vendas.objects.all().count()
   print(count) 
   if request.method == "GET":
        return JsonResponse({'count': count})
   
def retorna_media_venda(request):
   count = Vendas.objects.all().count()
   total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
   media = total/count
   locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
   media = locale.currency(media, grouping=True, symbol=None)
   print(count) 
   if request.method == "GET":
        return JsonResponse({'mediaVenda': media})

def relatorio_faturamento(request):
    x = Vendas.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)

def relatorio_produtos(request):
    produtos = Produto.objects.all()
    label = []
    data = []
    for produto in produtos:
        vendas = Vendas.objects.filter(nome_produto=produto).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(produto.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

def relatorio_funcionario(request):
    vendedores = Vendedor.objects.all()
    label = []
    data = []
    for vendedor in vendedores:
        vendas = Vendas.objects.filter(vendedor=vendedor).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(vendedor.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})