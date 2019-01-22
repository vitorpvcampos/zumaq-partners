from django.forms import ModelForm, TextInput, Select, NumberInput

from .models import Produto, CustomCoeficiente, CustomCoeficienteItens


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['pago_na_china',
                  'reminmbi',
                  'dolar_cotado',
                  'impostos_na_china',
                  'porcentagem_importacao',
                  'coeficiente', ]
        widgets = {
            'pago_na_china': TextInput(attrs={'class': 'form-control', 'placeholder': 'Pago na China'}),
            'reminmbi': TextInput(attrs={'class': 'form-control', 'placeholder': 'Reminmbi'}),
            'dolar_cotado': TextInput(attrs={'class': 'form-control', 'placeholder': 'Dolar Cotado'}),
            'impostos_na_china': TextInput(attrs={'class': 'form-control', 'placeholder': 'Impostos na China'}),
            'porcentagem_importacao': TextInput(attrs={'class': 'form-control', 'placeholder': '% Importação'}),
            'coeficiente': TextInput(attrs={'class': 'form-control', 'placeholder': 'Coeficiente'}),
        }

class CustomCoeficienteForm(ModelForm):
    class Meta:
        model = CustomCoeficiente
        fields = ['parceiro']
        widgets = {
            'parceiro': Select(attrs={'class': 'form-control', 'placeholder': 'Parceiro', 'disabled': ''}),
        }

class CustomCoeficienteItensForm(ModelForm):
    class Meta:
        model = CustomCoeficienteItens
        fields = ['parceiro', 'produto', 'coeficiente']
        widgets = {
            'parceiro': Select(attrs={'class': 'form-control', 'placeholder': 'Parceiro', 'disabled': ''}),
            'produto': Select(attrs={'class': 'form-control'}),
            'coeficiente': NumberInput(attrs={'class': 'form-control'}),
        }
