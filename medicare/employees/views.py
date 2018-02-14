from django.shortcuts import render, redirect

# Create your views here.
<<<<<<< HEAD
from employees.forms import NewEmployeeForm
from employees.models import Employee
=======
from employees.forms import NewEmployeeForm, NewAccountForm
from employees.models import Employee, Account
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
from records.models import Appointment


def employees(request):
<<<<<<< HEAD
    employees_list=Employee.objects.all()
    return render(request, 'employees/em_desk.html',{"employees_list":employees_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    
=======
    return render(request, 'employees.html')
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408


def new_employee(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
<<<<<<< HEAD
            return redirect('employees:frontdesk')
    else:
        form = NewEmployeeForm()

    return render(request, 'employees/add_employee.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})




def delete_employee(request):
    employees = Employee.objects.all()

    employee1 = request.GET.get('employee', None)
   
    for employee in employees:
        if str(employee) == employee1:
            Employee.objects.filter(id=employee.id).delete()
            return redirect('employees:frontdesk')
            break

    return render(request, 'employees/delete_employee.html', {'employees': employees,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
=======
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
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
