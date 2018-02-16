'''
Created on Feb 14, 2018

@author: trupa7
'''
from django import forms
from pharmacist.models import Pharmacist,Prescription

class NewPrescription(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ( 'patient_id','drug_name','prescribedBy',)

class NewPharmacist(forms.ModelForm):
    class Meta:
        model = Pharmacist
        fields = ( 'name','prescription_id',)

