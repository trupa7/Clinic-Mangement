from django.urls import path

from employees import views

app_name = 'employees'


urlpatterns = [
    path('', views.employees, name='employees'),
    path('newemployee/', views.new_employee, name='newemployee'),
    path('newaccount/', views.new_account, name='newaccount'),
    path('deleteemployee/', views.delete_employee, name='deleteemployee')
]