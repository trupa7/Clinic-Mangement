from django import forms

from employees.models import Employee, Account


class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('last_name', 'first_name', 'specialty_label')


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user','username', 'password', 'type_label')