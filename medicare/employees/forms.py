from django import forms

from employees.models import Employee


class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('last_name', 'first_name','username','password','type_label', 'speciality_label')

