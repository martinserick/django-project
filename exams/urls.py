from django.urls import path
from exams.views import *

urlpatterns = [
    path("", ExamListView.as_view(), name="list_exams"),
    path("exam/create/", create_exams, name="create_exams"),

    path("specie/list/", list_species, name="list_species"),
    path("specie/create/", create_species, name="create_species"),

    path("race/list/", list_races, name="list_races"),
    path("race/create/", create_races, name="create_races"),

    path("customer/list/", list_customers, name="list_customers"),
    path("customer/create/", create_customers, name="create_customers"),

    path("procedure/list/", list_procedures, name="list_procedures"),
    path("procedure/create/", ProcedureCreateView.as_view(), name="create_procedures"),
    path("procedure/edit/<int:pk>", ProcedureUpdateView.as_view(), name="update_procedures")

]
