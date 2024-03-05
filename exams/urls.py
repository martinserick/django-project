from django.urls import path
from exams.views import *

urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact),
]
