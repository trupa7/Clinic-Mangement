'''
Created on Feb 12, 2018

@author: trupa7
'''
from django.urls import path

from nurses import views

app_name = 'nurses'


urlpatterns = [
    path('', views.nurses, name='frontdesk'),
    path('newhistory/<int:id>', views.new_history, name='newhistory'),
    path('addfollowups/<int:id>', views.new_followup, name='addfollowups'),
    path('addfollowups/', views.auth_followup, name='authfollowup'),

    #path('deleteemployee/', views.delete_employee, name='deleteemployee')
]