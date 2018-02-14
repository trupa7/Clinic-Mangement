from django.urls import path

from records import views

app_name = 'records'


urlpatterns = [
    path('', views.front_desk, name='frontdesk'),
    path('newpatient/', views.new_patient, name='newpatient'),
    path('newappointment/', views.new_appointment, name='newappointment'),
<<<<<<< HEAD
    path('newhistory/', views.new_history, name='newhistory'),
    path('cancelapp/', views.cancel_appointment, name='cancelapp'),
    path('newadmit/', views.new_admit, name='newadmit'),
    path('deladmit/', views.cancel_admit, name='deladmit')
=======
    path('cancelapp/<appointment_id>/', views.cancel_appointment, name='cancelapp'),
    path('appointments/', views.appointments, name='appointments'),
    path('updatehistory/<appointment_id>/', views.update_history, name='updatehistory'),
    path('displayhistory/<appointment_id>/', views.display_history, name='displayhistory'),
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
]