from django.db import models
from django.contrib.auth.models import User
from django_softdelete.models import SoftDeleteModel 
# Create your models here.

class Race(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Specie(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):

    name = models.CharField(max_length=50)
    TYPE = {
        "Laboratório": "Laboratório",
        "Geral": "Geral",
        "Clínica": "Clínica"
    }
    type = models.CharField(max_length=30, choices=TYPE, default="Geral")
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

class Procedure(models.Model):
    
    name = models.CharField(max_length=70)
    acronym = models.CharField(max_length=10)
    deadline_in_days = models.IntegerField()
    general_value = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    clinic_value = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    laboratory_value = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
    
class Responsible(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Exam(SoftDeleteModel):
    AGE = {}
    for meses in range(1, 12):
        AGE[f"{meses}M"] = f"{meses} Mes{'es' if meses != 1 else ''}"
    for anos in range(1, 20):
        for meses in range(0, 12):
            if meses == 0:
                AGE[f"{anos}A"] = f"{anos} Ano{'s' if anos != 1 else ''}"
            else:
                AGE[f"{anos}A{meses}M"] = f"{anos} Ano{'s' if anos != 1 else ''} e {meses} Mes{'es' if meses != 1 else ''}"
    GENDER = {
        "M": "Macho",
        "F": "Fêmea"
    }
    PAYMENT = {
        'Pago': 'Pago',
        'Pendente': 'Pendente'
    }
    name = models.CharField(max_length=50, null=False, blank=False)
    specie = models.ForeignKey(Specie, on_delete=models.PROTECT,null=False, blank=False)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, null=False, blank=False)
    age = models.CharField(max_length=10, choices=AGE,null=False, blank=False)
    owner = models.CharField(max_length=50, null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, blank=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT, null=False, blank=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, blank=False)
    payment = models.CharField(max_length=30, default='Pendente', choices=PAYMENT, null=False, blank=False)
    created_at = models.DateTimeField(editable=False, auto_now_add=True, null=False, blank=False)
    status = models.BooleanField(null=True)
    observation = models.TextField(max_length=500, null=True, blank=True)
    deadline_to_finish = models.DateTimeField(null=True)
    cod_exam = models.CharField(max_length=50, null=True)
    finished_at = models.DateTimeField(null=True)
    days_elapsed = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    responsible = models.ForeignKey(Responsible, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    
    def finished(self):
        return self.finished_at is not None
