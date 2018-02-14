'''
Created on Feb 14, 2018

@author: trupa7
'''
from django.urls import path

from . import views

app_name = 'doctors'


urlpatterns = [

    path('cancelapp/<appointment_id>/', views.cancel_appointment, name='cancelapp'),
    path('appointments/', views.appointments, name='appointments'),
    path('updatehistory/<appointment_id>/', views.update_history, name='updatehistory'),
    path('displayhistory/<appointment_id>/', views.display_history, name='displayhistory'),
    path('addlab/', views.new_lab, name='addlab'),
]