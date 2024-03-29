from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput, Select, NumberInput, Textarea
from .models import *

class ExamForm(ModelForm):
    
    class Meta:
        model = Exam
        exclude = ('status','deadline_to_finish', 'days_elapsed', 'cod_exam', 'finished_at')
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
            'observation': Textarea(attrs={'class': 'form-control mb-2', 'required': False}),
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

class RaceForm(ModelForm):
    
    class Meta:
        model = Race
        fields = "__all__"

        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2'}),
        }
        labels = {
            'name': "Raça"
        }

class ProcedureForm(ModelForm):
    
    class Meta:
        model = Procedure
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2'}),
            'acronym': TextInput(attrs={'class': 'form-control mb-2'}),
            'deadline_in_days': NumberInput(attrs={'class': 'form-control mb-2'}),
            'general_value': NumberInput(attrs={'class': 'form-control mb-2'}),
            'clinic_value': NumberInput(attrs={'class': 'form-control mb-2'}),
            'laboratory_value': NumberInput(attrs={'class': 'form-control mb-2'})
        }
        labels = {
            'name': "Nome",
            'acronym': "Sigla",
            'deadline_in_days': "Prazo",
            'general_value': 'Valor Geral',
            'clinic_value': 'Valor Clínica',
            'laboratory_value': "Valor Laboratório"
        }

class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2'}),
            'type': Select(attrs={'class': 'form-select mb-2'}),
            'email': TextInput(attrs={'class': 'form-control mb-2'}),
        }
        labels = {
            'name': 'Nome',
            'type': 'Tipo',
            'email': 'E-mail'
        }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione a classe CSS desejada ao campo de entrada
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

