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

    name = models.CharField(max_length=50, null=False)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    GENDER = {
        "M": "Male",
        "F": "Female"
    }
    gender = models.CharField(max_length=1, choices=GENDER)
    AGE = {
        "1M": "1 Mes",
        "2M": "2 Meses",
        "3M": "3 Meses",
        "4M": "4 Meses",
        "5M": "5 Meses",
        "6M": "6 Meses",
        "7M": "7 Meses",
        "8M": "8 Meses",
        "9M": "9 Meses",
        "10M": "10 Meses",
        "11M": "11 Meses",
        "1A": "1 Ano",
        "1A1M": "1 Ano e 1 Mês",
        "1A2M": "1 Ano e 2 Meses",
        "1A3M": "1 Ano e 3 Meses",
        "1A4M": "1 Ano e 4 Meses",
        "1A5M": "1 Ano e 5 Meses",
        "1A6M": "1 Ano e 6 Meses",
        "1A7M": "1 Ano e 7 Meses",
        "1A8M": "1 Ano e 8 Meses",
        "1A9M": "1 Ano e 9 Meses",
        "1A10M": "1 Ano e 10 Meses",
        "1A11M": "1 Ano e 11 Meses",
        "2A": "2 Anos",
    }
    age = models.CharField(max_length=10, choices=AGE)
    owner = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.BooleanField()
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.name
