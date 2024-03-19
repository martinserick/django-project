from django.db import models

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

class Exam(models.Model):
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
    name = models.CharField(max_length=50, null=False)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.CharField(max_length=10, choices=AGE)
    owner = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment = models.CharField(max_length=30, default='Pendente', choices=PAYMENT)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    status = models.BooleanField(null=True)
    observation = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
