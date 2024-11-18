from django import forms
from . import models

TIPO_FORMATADOR =( 
    ("1", "EXCEL"), 
    ("2", "PDF"), 
    ("3", "CSV"), 
) 

class ImportarDadosForm(forms.Form):
    arquivo = forms.FileField()
    combobox = forms.ChoiceField(choices = TIPO_FORMATADOR, label='Formatador de Texto')


class ClientForm(forms.ModelForm):
    documento = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'OnKeyPress':'formatar("###.###.###-##", this)', 'placeholder': 'Informe seu Documento'}), label="CPF")
    class Meta:
        model = models.Cliente
        ##fields = '__all__'
        fields = (
            'nome', 'documento', 'profissao','idade', 
        )
        exclude = ('Endereco',)

        widgets = {
           "nome"         : forms.TextInput(attrs={'placeholder': 'Informe seu Nome'}),
           "documento"      : forms.TextInput(attrs={'placeholder': 'Informe seu Documento'}),
           "profissao"         : forms.TextInput(attrs={'placeholder': 'Informe sua Profissão'}),
           "idade" : forms.TextInput(attrs={'placeholder': 'Informe sua Idade'}),
        }

class AddressForm(forms.ModelForm):
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'OnKeyPress':'formatar("#####-###", this)', 'placeholder': 'Informe seu CEP'}), label="cep")
    class Meta:
        model = models.Endereco
        fields = (
            'cep', 'bairro', 'rua',
            'complemento', 'numero', 'estado',
            'cidade',
        )

        widgets = {
           "cep"         : forms.TextInput(attrs={'placeholder': 'Informe seu CEP'}),
           "bairro"      : forms.TextInput(attrs={'placeholder': 'Informe seu bairro'}),
           "rua"         : forms.TextInput(attrs={'placeholder': 'Informe sua rua'}),
           "complemento" : forms.TextInput(attrs={'placeholder': 'Informe seu complemento'}),
           "numero"      : forms.TextInput(attrs={'placeholder': 'Informe seu numero'}),
           "estado"      : forms.TextInput(attrs={'placeholder': 'Informe seu estado'}),
           "cidade"      : forms.TextInput(attrs={'placeholder': 'Informe sua cidade'})
        }
    
