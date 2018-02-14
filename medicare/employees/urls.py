from django.urls import path

from employees import views

app_name = 'employees'


urlpatterns = [
<<<<<<< HEAD
    path('', views.employees, name='frontdesk'),
    path('newemployee/', views.new_employee, name='newemployee'),

=======
    path('', views.employees, name='employees'),
    path('newemployee/', views.new_employee, name='newemployee'),
    path('newaccount/', views.new_account, name='newaccount'),
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
    path('deleteemployee/', views.delete_employee, name='deleteemployee')
]