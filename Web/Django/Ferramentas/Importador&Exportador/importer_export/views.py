import pandas as pd
from django.http import HttpResponse
import datetime
import csv
from django.shortcuts import render, redirect
from django.views import View
from .forms import ImportarDadosForm, ClientForm, AddressForm
from .models import Cliente, Endereco
from django.views import View

from . import forms

# Create your views here.
class ImportarDadosView(View):
    template_name = 'importar_export_dados.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        clientes = Cliente.objects.all()

        self.contexto = {
                'clientes':clientes,
                'form': forms.ImportarDadosForm(
                    data=self.request.POST or None
                ),
                'fromclient': forms.ClientForm(
                    data=self.request.POST or None
                ),
                'fromAddress': forms.AddressForm(
                    data=self.request.POST or None
                )
            }

        self.fromclient = self.contexto['fromclient']
        self.fromAddress = self.contexto['fromAddress']

        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar
        

    def post(self, request):

        form = ImportarDadosForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            df = pd.read_excel(arquivo)

            for _, row in df.iterrows():
                # Itera sobre as linhas do DataFrame lido do arquivo Excel 
                self.criar_cliente_e_endereco(row)

            return redirect('importer_export:importar_export_arquivo')

        return render(request, self.template_name, {'form': form})

    def criar_cliente_e_endereco(self, row):
        # Use get_or_create para evitar a necessidade de verificar a existência antes de criar
        cliente, criado = Cliente.objects.get_or_create(
            documento=row['documento'],
            defaults={
                'nome': row['nome'],
                'profissao': row['profissao'],
                'idade': row['idade']
            }
        )

        if criado:
            # Cria o endereço associado ao cliente
            Endereco.objects.create(
                cliente=cliente,
                cep=row['cep'],
                bairro=row['bairro'],
                rua=row['rua'],
                complemento=row['complemento'],
                numero=row['numero'],
                estado=row['estado'],
                cidade=row['cidade']
            )

def exporter(request):

    form = ImportarDadosForm(request.POST or None)
    escolha = request.GET.get('combobox')
    print(escolha)
    if form.is_valid():
        escolha = form.cleaned_data['combobox']
        print(escolha)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Clientes' + \
                                            str(datetime.datetime.now())+'.csv'
            
        writer = csv.writer(response)
        writer.writerow(['Nome','Documento','Profissão','Idade','CEP','Bairro','Rua','Complemento','Numero', 'Estado', 'Cidade']) # head Titulo
            
        clientes = Cliente.objects.all()

        for cliente in clientes: 
            endereco = Endereco.objects.filter(cliente=cliente).first()
            if endereco:
                writer.writerow([cliente.nome, cliente.documento, cliente.profissao, cliente.idade, 
                                    endereco.cep, endereco.bairro, endereco.rua, endereco.complemento, 
                                    endereco.numero, endereco.estado, endereco.cidade])
            
        return response
    
    return redirect('importer_export:importar_export_arquivo') 

class criar(ImportarDadosView):
    def post(self, *args, **kwargs):
        cliente = Cliente(**self.fromclient.cleaned_data)
        ##cliente.nome = self.fromclient.cleaned_data.get('nome')
        cliente.save()
        
        endereco = Endereco(**self.fromAddress.cleaned_data)
        endereco.cliente = cliente
        endereco.save()

        return redirect('importer_export:importar_export_arquivo')  

def GetId(request, id):
    get_cliente = Cliente.objects.get(id=id) ## pega objeto   
    if get_cliente:
       return get_cliente    

def deletar(request, id):
    get_cliente = GetId(request, id)
    if get_cliente:
       get_cliente.delete()

    return redirect('importer_export:importar_export_arquivo')