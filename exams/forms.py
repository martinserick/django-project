from django.forms import ModelForm, TextInput, Select, NumberInput, Textarea
from .models import *

class ExamForm(ModelForm):
    
    class Meta:
        model = Exam
        exclude = ('status',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2'}),
            'specie': Select(attrs={'class': 'form-select mb-2'}),
            'race': Select(attrs={'class': 'form-select mb-2'}),
            'gender': Select(attrs={'class': 'form-select mb-2'}),
            'age': Select(attrs={'class': 'form-select mb-2'}),
            'owner': TextInput(attrs={'class': 'form-control mb-2'}),
            'customer': Select(attrs={'class': 'form-select mb-2'}),
            'procedure': Select(attrs={'class': 'form-select mb-2'}),
            'discount': NumberInput(attrs={'class': 'form-control mb-2'}),
            'total_value': NumberInput(attrs={'class': 'form-control mb-2'}),
            'payment': Select(attrs={'class': 'form-select mb-2'}),
            'observation': Textarea(attrs={'class': 'form-control mb-2'}),
        }
        labels = {
            'name': "Nome do Pet",
            'specie': "Espécie",
            'race': "Raça",
            'gender': "Sexo",
            'age': "Idade",
            'owner': "Dono",
            'customer': "Cliente",
            'procedure': "Exame",
            'discount': "Desconto",
            'total_value': "Valor Total",
            'payment': "Pagamento",
            'status': "Status",
            'observation': 'Observação'
        }

class SpecieForm(ModelForm):
    
    class Meta:
        model = Specie
        fields = "__all__"

        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2'}),
        }
        labels = {
            'name': "Espécie"
        }

