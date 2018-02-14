'''
Created on Feb 14, 2018

@author: trupa7
'''

from django import forms

from .models import  History

# update patient history based on appointment
class NewHistoryForm(forms.ModelForm):
    prescribed = forms.CharField(max_length=150, required=False)

    class Meta:
        model = History
        fields = ('appointment', 'prescription', 'prescribed', 'visit_record')
