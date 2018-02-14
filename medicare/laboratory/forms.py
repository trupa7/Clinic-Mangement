from django import forms
from .models import Laboratory


class TestFormSelect(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ('patient_id','doctor_id','test_date','test_id','test_details','result_status',)
        

class AddTestSelect(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ('patient_id','doctor_id','test_date','test_id',)