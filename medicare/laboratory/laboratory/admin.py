from django.contrib import admin
from .models import Laboratory,Doctor,Patient

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Laboratory)
