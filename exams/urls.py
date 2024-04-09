from django.urls import path
from .views import *
from .forms import CustomAuthenticationForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', ExamLoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', logoutSystem, name='logout'),

    path("", ExamListView.as_view(), name="list_exams"),
    path("exam/create/", ExamCreateView.as_view(), name="create_exams"),
    path("exam/edit/<int:pk>", ExamUpdateView.as_view(), name="update_exams"),
    path("exam/show/<int:pk>", ExamDetailView.as_view(), name="show_exam"),
    path("exam/delete/<int:pk>", ExamDeleteView.as_view(), name="delete_exam"),
    path("exam/finish/", FinishExam, name="finish_exam"),

    path("specie/list/", SpecieListView.as_view(), name="list_species"),
    path("specie/create/", SpecieCreateView.as_view(), name="create_species"),
    path("specie/edit/<int:pk>", SpecieUpdateView.as_view(), name="update_species"),
    path("specie/delete/<int:pk>", SpecieDeleteView.as_view(), name="delete_specie"),

    path("race/list/", RaceListView.as_view(), name="list_races"),
    path("race/create/", RaceCreateView.as_view(), name="create_races"),
    path("race/edit/<int:pk>", RaceUpdateView.as_view(), name="update_races"),
    path("race/delete/<int:pk>", RaceDeleteView.as_view(), name="delete_race"),

    path("responsibe/list/", ResponsibleListView.as_view(), name="list_responsibles"),
    path("responsible/create/", ResponsibleCreateView.as_view(), name="create_responsibles"),
    path("responsible/edit/<int:pk>", ResponsibleUpdateView.as_view(), name="update_responsibles"),
    path("responsible/delete/<int:pk>", ResponsibleDeleteView.as_view(), name="delete_responsible"),

    path("customer/list/", CustomerListView.as_view(), name="list_customers"),
    path("customer/create/", CustomerCreateView.as_view(), name="create_customers"),
    path("customer/update/<int:pk>", CustomerUpdateView.as_view(), name="update_customers"),
    path("customer/delete/<int:pk>", CustomerDeleteView.as_view(), name="delete_customers"),
    path("customer/get_type/", CustomerGetType, name="customer_get_type"),

    path("procedure/list/", ProcedureListView.as_view(), name="list_procedures"),
    path("procedure/create/", ProcedureCreateView.as_view(), name="create_procedures"),
    path("procedure/edit/<int:pk>", ProcedureUpdateView.as_view(), name="update_procedures"),
    path("procedure/delete/<int:pk>", ProcedureDeleteView.as_view(), name="delete_procedure"),
    path("procedure/get_value_type/", ProcedureGetValueType, name="procedure_get_value_type"),

    path("report/", report, name='report'),

]
