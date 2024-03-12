from django.contrib import admin
from .models import Procedure, Specie, Exam, Race, Customer

# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "specie", "race", "gender", "age", "owner", "customer")

admin.site.register(Procedure)
admin.site.register(Specie)
admin.site.register(Race)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Customer)