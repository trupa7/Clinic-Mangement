from django.shortcuts import render, redirect

# Create your views here.
from employees.forms import NewEmployeeForm
from employees.models import Employee,Doctor
from records.models import Appointment
from django.forms.forms import Form


def employees(request):
    employees_list=Employee.objects.all()
    return render(request, 'employees/em_desk.html',{"employees_list":employees_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    


def new_employee(request):
    if request.method == 'POST':
        user_id=request.POST['username']
        user_type=request.POST['type_label']
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            if 'DO' in user_type:
                Doctor(username=user_id).save()
            return redirect('employees:frontdesk')
        else:
            return render(request, 'employees/add_employee.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec'],'error':"Username is Taken"})

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
