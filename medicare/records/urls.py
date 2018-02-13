from django.urls import path

from records import views

app_name = 'records'


urlpatterns = [
    path('', views.front_desk, name='frontdesk'),
    path('newpatient/', views.new_patient, name='newpatient'),
    path('newappointment/', views.new_appointment, name='newappointment'),
    path('cancelapp/<appointment_id>/', views.cancel_appointment, name='cancelapp'),
    path('appointments/', views.appointments, name='appointments'),
    path('updatehistory/<appointment_id>/', views.update_history, name='updatehistory'),
    path('displayhistory/<appointment_id>/', views.display_history, name='displayhistory'),
]