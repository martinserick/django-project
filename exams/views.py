from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    exams = Exam.objects.all()
    context = {
        "exams": exams
    }
    return render(request, "exams/home.html", context=context)


def about(request):
    return HttpResponse("About us")


def contact(request):
    return HttpResponse("Contact")
    