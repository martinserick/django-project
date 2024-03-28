from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView, CreateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from datetime import timedelta, datetime
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *


# Exams
class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = "exams/list_exams.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = self.request.GET.get('customer', None)
        if filter:
            queryset = queryset.filter(customer__name__icontains=filter)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'list_exams'  # Supondo que 'inicio' seja a aba padrão
        return context
    
class ExamDetailView(LoginRequiredMixin, DetailView):
    model = Exam
    template_name = "exams/show_exam.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'detail_exam'  # Supondo que 'inicio' seja a aba padrão
        return context

class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = "exams/exams_form.html"
    success_url = reverse_lazy('list_exams')

    def form_valid(self, form):
        procedure_obj = Procedure.objects.get(pk=form.instance.procedure.pk)
        count_exam = Exam.objects.filter(procedure=procedure_obj.pk).count()
        form.instance.cod_exam = procedure_obj.acronym + '000' + str(count_exam+1)
        form.instance.deadline_to_finish = datetime.now() + timedelta(procedure_obj.deadline_in_days)
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['aba_ativa'] = 'create_exam'
        return context
    

class ExamUpdateView(LoginRequiredMixin, UpdateView):
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'update_exams'  # Supondo que 'inicio' seja a aba padrão
        return context

class ExamDeleteView(LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = 'exams/delete_exam.html'
    success_url = reverse_lazy('list_exams')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'delete_exam'  # Supondo que 'inicio' seja a aba padrão
        return context

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
class SpecieListView(LoginRequiredMixin, ListView):
    model = Specie
    template_name = "species/list_species.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'list_species'  # Supondo que 'inicio' seja a aba padrão
        return context

class SpecieCreateView(LoginRequiredMixin, CreateView):
    model = Specie
    template_name = "species/species_form.html"
    form_class = SpecieForm
    success_url = reverse_lazy('list_species')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'create_species'  # Supondo que 'inicio' seja a aba padrão
        return context

class SpecieUpdateView(LoginRequiredMixin, UpdateView):
    model = Specie
    template_name = "species/species_form.html"
    form_class = SpecieForm
    success_url = reverse_lazy('list_species')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'update_specie'  # Supondo que 'inicio' seja a aba padrão
        return context

class SpecieDeleteView(LoginRequiredMixin, DeleteView):
    model = Specie
    template_name = 'species/delete_specie.html'
    success_url = reverse_lazy('list_species')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'delete_specie'  # Supondo que 'inicio' seja a aba padrão
        return context


# Races
class RaceListView(LoginRequiredMixin, ListView):
    model = Race
    template_name = "races/list_races.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'list_races'  # Supondo que 'inicio' seja a aba padrão
        return context


class RaceCreateView(LoginRequiredMixin, CreateView):
    model = Race
    template_name = "races/races_form.html"
    form_class = RaceForm
    success_url = reverse_lazy('list_races')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'create_race'  # Supondo que 'inicio' seja a aba padrão
        return context

class RaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Race
    template_name = "races/races_form.html"
    form_class = RaceForm
    success_url = reverse_lazy('list_races')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'update_race'  # Supondo que 'inicio' seja a aba padrão
        return context

class RaceDeleteView(LoginRequiredMixin, DeleteView):
    model = Race
    template_name = 'races/delete_races.html'
    success_url = reverse_lazy('list_races')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'delete_race'  # Supondo que 'inicio' seja a aba padrão
        return context

# Procedures

class ProcedureListView(LoginRequiredMixin, ListView):
    model = Procedure
    template_name = "procedures/list_procedures.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'list_procedures'  # Supondo que 'inicio' seja a aba padrão
        return context



class ProcedureCreateView(LoginRequiredMixin, CreateView):
    model = Procedure
    template_name = "procedures/procedure_form.html"
    form_class = ProcedureForm
    success_url = reverse_lazy('list_procedures')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'create_procedure'  # Supondo que 'inicio' seja a aba padrão
        return context
    

class ProcedureUpdateView(LoginRequiredMixin, UpdateView):
    model = Procedure
    form_class = ProcedureForm
    template_name = "procedures/procedure_form.html"
    success_url = reverse_lazy('list_procedures')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'update_procedure'  # Supondo que 'inicio' seja a aba padrão
        return context

class ProcedureDeleteView(LoginRequiredMixin, DeleteView):
    model = Procedure
    template_name = 'procedures/delete_procedure.html'
    success_url = reverse_lazy('list_procedures')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'delete_procedure'  # Supondo que 'inicio' seja a aba padrão
        return context


# Customers

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customers/list_customers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'list_customers'  # Supondo que 'inicio' seja a aba padrão
        return context

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = "customers/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('list_customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'create_customer'  # Supondo que 'inicio' seja a aba padrão
        return context

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = "customers/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('list_customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'update_customer'  # Supondo que 'inicio' seja a aba padrão
        return context

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/delete_customer.html'
    success_url = reverse_lazy('list_customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione uma chave ao contexto para indicar qual aba está ativa
        context['aba_ativa'] = 'delete_customer'  # Supondo que 'inicio' seja a aba padrão
        return context


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
        messages.error(self.request,'Usuário ou senha inválidos!')
        return self.render_to_response(self.get_context_data(form=form))
    
def logoutSystem(request):
    logout(request)
    return redirect('login')

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            # Obter dados do formulário
            customer_name = form.cleaned_data['customer_name']
            initial_date = form.cleaned_data['initial_date']
            final_date = form.cleaned_data['final_date']
            status = form.cleaned_data['status']
            payment = form.cleaned_data['payment']

            # Filtrar o modelo com base nos dados do formulário
            query = Exam.objects.all()
            if customer_name:
                query = query.filter(customer=customer_name)
            if initial_date:
                query = query.filter(created_at__date__gte=initial_date)
            if final_date:
                query = query.filter(created_at__date__lte=final_date)
            if status:
                query = query.filter(status=status)
            if payment:
                query = query.filter(payment=payment)

            return render(request, 'report/report_template.html', {'form': form, 'query': query, 'aba_ativa': 'report'})
    else:
        form = ReportForm()
        context = {
            'aba_ativa': 'report',
            'form': form
        }
        return render(request, 'report/report_template.html', context=context)