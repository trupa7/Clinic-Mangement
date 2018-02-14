<<<<<<< HEAD
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
=======
from django import forms
from .models import Laboratory


class TestFormSelect(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ('result_status','patient_id','doctor_id','test_date','test_id','test_details',)
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
