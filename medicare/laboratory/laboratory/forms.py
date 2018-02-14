from django import forms
from .models import Laboratory

class LabDetailsForm(forms.ModelForm):
    model = Laboratory
    fields = ('test_id','patient_id','test_date','doctor_id','result_status','test_details')