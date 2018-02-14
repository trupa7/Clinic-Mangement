from django import forms

<<<<<<< HEAD
from employees.models import Employee
=======
from employees.models import Employee, Account
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408


class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
<<<<<<< HEAD
        fields = ('last_name', 'first_name','username','password','type_label', 'speciality_label')

=======
        fields = ('last_name', 'first_name', 'specialty_label')


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user','username', 'password', 'type_label')
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
