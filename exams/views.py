from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView, CreateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from datetime import timedelta, datetime
from django.utils import timezone
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
    
class ExamDetailView(DetailView):
    model = Exam
    template_name = "exams/show_exam.html"


class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = "exams/exams_form.html"
    success_url = reverse_lazy('list_exams')

    def form_valid(self, form):
        procedure_obj = Procedure.objects.get(pk=form.instance.procedure.pk)
        count_exam = Exam.objects.filter(procedure=procedure_obj.pk).count()
        form.instance.cod_exam = procedure_obj.acronym + '000' + str(count_exam+1)
        form.instance.deadline_to_finish = datetime.now() + timedelta(procedure_obj.deadline_in_days)
        return super().form_valid(form)
    

class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = "exams/exams_form.html"
    success_url = reverse_lazy('list_exams')

    def form_valid(self, form):
        procedure_obj = Procedure.objects.get(pk=form.instance.procedure.pk)
        count_exam = Exam.objects.filter(procedure=procedure_obj.pk).count()
        form.instance.cod_exam = procedure_obj.acronym + '000' + str(count_exam+1)
        form.instance.deadline_to_finish = datetime.now() + timedelta(procedure_obj.deadline_in_days)
        return super().form_valid(form)

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'exams/delete_exam.html'
    success_url = reverse_lazy('list_exams')

def FinishExam(request):
    if request.method == 'POST':
        exam_id = request.POST.get('exam_id')
        exam = Exam.objects.get(pk=exam_id)

        exam.finished_at = timezone.now()
        days_offset = timezone.now() - exam.created_at
        exam.days_elapsed = days_offset.days
        exam.status = True

        exam.save()

        messages.success(request, "Exame Concluído com Sucesso")
        return redirect('show_exam', pk=exam_id)
    else:
        return redirect('list_exams')

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


def CustomerGetType(request):
    customer_id = request.GET.get('customer_id')
    customer = Customer.objects.get(pk=customer_id)
    customer_type = customer.type
    data = {
        'type': customer_type,
    }
    return JsonResponse(data)


def ProcedureGetValueType(request):
    procedure_id = request.GET.get('procedure_id')
    customer_type = request.GET.get('customer_type')
    value = 0
    procedure = Procedure.objects.get(pk=procedure_id)
    if customer_type == "Geral":
        value = procedure.general_value
    elif customer_type == "Clínica":
        value = procedure.clinic_value
    else:
        value = procedure.laboratory_value    
    data = {
        'value': value,
    }
    return JsonResponse(data)


#Login

class ExamLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('list_exams') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))