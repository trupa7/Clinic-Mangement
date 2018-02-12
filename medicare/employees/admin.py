from django.contrib import admin

# Register your models here.
from employees.models import Employee, Account

admin.site.register(Employee)
admin.site.register(Account)