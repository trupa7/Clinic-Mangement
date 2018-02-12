from django.urls import path

from records import views

app_name = 'records'


urlpatterns = [
    path('', views.front_desk, name='frontdesk'),
    path('newpatient/', views.new_patient, name='newpatient'),
    path('newappointment/', views.new_appointment, name='newappointment'),
    path('newhistory/', views.new_history, name='newhistory'),
    path('cancelapp/', views.cancel_appointment, name='cancelapp')
]