import pandas as pd
from django.http import HttpResponse
import datetime
import csv
from django.shortcuts import render, redirect
from django.views import View
from .forms import ImportarDadosForm
from .models import Cliente, Endereco

# Create your views here.
class ImportarDadosView(View):
    template_name = 'importar_export_dados.html'

    def get(self, request):
        clientes = Cliente.objects.all()
        form = ImportarDadosForm()
        return render(request, self.template_name, {
            'form': form,
            'clientes': clientes
        })

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