from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Exams
class ExamListView(ListView):
    model = Exam
    template_name = "exams/list_exams.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = self.request.GET.get('customer', None)
        if filter:
            queryset = queryset.filter(customer__name__icontains=filter)
        return queryset


class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = "exams/exams_form.html"
    success_url = reverse_lazy('list_exams')

class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = "exams/exams_form.html"
    success_url = reverse_lazy('list_exams')

# Species
class SpecieListView(ListView):
    model = Specie
    template_name = "species/list_species.html"

class SpecieCreateView(CreateView):
    model = Specie
    template_name = "species/species_form.html"
    form_class = SpecieForm
    success_url = reverse_lazy('list_species')

class SpecieUpdateView(UpdateView):
    model = Specie
    template_name = "species/species_form.html"
    form_class = SpecieForm
    success_url = reverse_lazy('list_species')


# Races
class RaceListView(ListView):
    model = Race
    template_name = "races/list_races.html"


class RaceCreateView(CreateView):
    model = Race
    template_name = "races/races_form.html"
    form_class = RaceForm
    success_url = reverse_lazy('list_races')

class RaceUpdateView(UpdateView):
    model = Race
    template_name = "races/races_form.html"
    form_class = RaceForm
    success_url = reverse_lazy('list_races')

# Procedures

class ProcedureListView(ListView):
    model = Procedure
    template_name = "procedures/list_procedures.html"



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

class CustomerListView(ListView):
    model = Customer
    template_name = "customers/list_customers.html"

class CustomerCreateView(CreateView):
    model = Customer
    template_name = "customers/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('list_customers')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "customers/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('list_customers')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/delete_customer.html'
    success_url = reverse_lazy('list_customers')