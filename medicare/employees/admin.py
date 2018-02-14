from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from employees.models import Employee

admin.site.register(Employee)
=======
from employees.models import Employee, Account

admin.site.register(Employee)
admin.site.register(Account)
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
