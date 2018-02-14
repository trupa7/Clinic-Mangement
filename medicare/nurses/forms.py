'''
Created on Feb 12, 2018

@author: trupa7
'''
from django import forms
from nurses.models import Nurses

class NewFollowups(forms.ModelForm):
    class Meta:
        model = Nurses
        fields = ( 'created_date','details')

