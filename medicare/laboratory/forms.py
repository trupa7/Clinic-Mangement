from django import forms
from .models import Laboratory


class TestFormSelect(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ('result_status','patient_id','doctor_id','test_date','test_id','test_details',)