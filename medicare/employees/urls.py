from django.urls import path

from employees import views

app_name = 'employees'


urlpatterns = [
    path('', views.employees, name='frontdesk'),
    path('newemployee/', views.new_employee, name='newemployee'),

    path('deleteemployee/', views.delete_employee, name='deleteemployee')
]