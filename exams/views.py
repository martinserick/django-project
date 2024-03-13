from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Exams
def list_exams(request):
    exams = Exam.objects.all()
    context = {
        "exams": exams
    }
    return render(request, "exams/list_exams.html", context=context)


def create_exams(request):
    exam = Exam.objects.first()
    context = {
        "exam": exam,
    }
    return render(request, "exams/create_exams.html", context=context)


# Species
def list_species(request):
    return render(request, "species/list_species.html")


def create_species(request):
    return render(request, "species/create_species.html")

# Races

def list_races(request):
    return render(request, "races/list_races.html")


def create_races(request):
    return render(request, "races/create_races.html")

# Procedures

def list_procedures(request):
    return render(request, "procedures/list_procedures.html")


def create_procedures(request):
    return render(request, "procedures/create_procedures.html")

# Customers

def list_customers(request):
    return render(request, "customers/list_customers.html")


def create_customers(request):
    return render(request, "customers/create_customers.html")