from django.urls import path

from records import views

app_name = 'records'


urlpatterns = [
    path('', views.front_desk, name='frontdesk'),
    path('newpatient/', views.new_patient, name='newpatient'),
    path('newappointment/', views.new_appointment, name='newappointment'),
    path('viewpatient', views.view_patient, name='viewpatient'),
    path('patient_details/<int:id>', views.detail_patient, name='patient_details'),
    path('cancelapp/', views.cancel_appointment, name='cancelapp'),
    path('newadmit/', views.new_admit, name='newadmit'),
    path('deladmit/', views.cancel_admit, name='deladmit')
]