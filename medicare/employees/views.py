from django.shortcuts import render, redirect

# Create your views here.
from employees.forms import NewEmployeeForm, NewAccountForm
from employees.models import Employee, Account
from records.models import Appointment


def employees(request):
    return render(request, 'employees.html')


def new_employee(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('employees:newemployee')
    else:
        form = NewEmployeeForm()

    return render(request, 'employees/add_to_db.html', {'record': form})


def new_account(request):
    if request.method == 'POST':
        form = NewAccountForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('employees:newaccount')
    else:
        form = NewAccountForm()

    return render(request, 'employees/add_to_db.html', {'record': form})

'''
def delete_employee(request):
    employees = Employee.objects.all()

    ln = request.GET.get('last_name', None)

    for employee in employees:
        if str(employee) == ln:
            # delete from Appointment by id
            Employee.objects.filter(id=employee.id).delete()
            break

    return render(request, 'employees/delete_employee.html', {'employees': employees})
'''

# cancel appointment
def delete_employee(request):
    appointments = Account.objects.all()

    patient = request.GET.get('last_name', None)

    for appointment in appointments:
        if str(appointment) == patient:
            Account.objects.filter(id=appointment.id).delete()
            break

    return render(request, 'employees/delete_employee.html', {'appointments': appointments})