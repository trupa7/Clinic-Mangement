from django.contrib import admin
from .models import Pharmacist,Prescription
# Register your models here.
admin.site.register([Prescription,Pharmacist])
