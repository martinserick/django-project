from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView, ListView
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Exams
class ExamListView(ListView):
    model = Exam
    template_name = "exams/list_exams.html" 


def create_exams(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_exams')
        else:
            errors = form.errors
            return render(request, 'exams/create_exams.html', {'form': form, 'errors': errors})
    else:
        form = ExamForm()

    return render(request, "exams/create_exams.html", {'form': form})    


# Species
def list_species(request):
    species = Specie.objects.all()
    return render(request, "species/list_species.html", {'species': species})


def create_species(request):
    if request.method == "POST":
        form = SpecieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_species')
        else:
            errors = form.errors
            return render(request, 'species/create_species.html', {'form': form, 'errors': errors})
    else:
        form = SpecieForm()

    return render(request, "species/create_species.html", {'form': form})
# Races

def list_races(request):
    races = Race.objects.all()
    return render(request, "races/list_races.html", {'races': races})
    

def create_races(request):
    if request.method == "POST":
        form = RaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_races')
        else:
            errors = form.errors
            return render(request, 'races/create_races.html', {'form': form, 'errors': errors})
    else:
        form = RaceForm()

    return render(request, "races/create_races.html", {'form': form})

# Procedures

def list_procedures(request):
    procedures = Procedure.objects.all()
    return render(request, "procedures/list_procedures.html", {'procedures': procedures})


class ProcedureCreateView(CreateView):
    model = Procedure
    template_name = "procedures/procedure_form.html"
    form_class = ProcedureForm
    success_url = reverse_lazy('list_procedures')
    

class ProcedureUpdateView(UpdateView):
    model = Procedure
    form_class = ProcedureForm
    template_name = "procedures/procedure_form.html"
    success_url = reverse_lazy('list_procedures')

# Customers

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "customers/list_customers.html", {'customers': customers})


def create_customers(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_customers')
        else:
            errors = form.errors
            return render(request, 'customers/create_customers.html', {'form': form, 'errors': errors})
    else:
        form = CustomerForm()

    return render(request, "customers/create_customers.html", {'form': form})