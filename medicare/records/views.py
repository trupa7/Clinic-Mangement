from django.shortcuts import render, redirect

# Create your views here.
from records.froms import NewPatientForm, NewAppointmentForm, NewHistoryForm,NewAdmitForm
from records.models import Appointment,Admit
from nurses.models import Nurses



#
def front_desk(request):
    Appoinment_list=Appointment.objects.all()
   
    return render(request, "records/re_desk.html",{"Appoinment_list":Appoinment_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    #return render(request, "front_desk.html",{"Appoinment_list":Appoinment_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

# add patient
def new_patient(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
    else:
        form = NewPatientForm()
    return render(request, 'records/add_patient.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


# add appointment
def new_appointment(request):
    if request.method == 'POST':
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
    else:
        form = NewAppointmentForm()

    return render(request, 'records/add_appoinment.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})



# update history
# TODO:: delete appintment ifno after history is updated
def new_history(request):
    if request.method == 'POST':
        form = NewHistoryForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
    else:
        form = NewHistoryForm()

    return render(request, 'records/add_to_db.html', {'record': form})


# cancel appointment
def cancel_appointment(request):
    appointments = Appointment.objects.all()

    patient = request.GET.get('patient', None)

    for appointment in appointments:
        if str(appointment) == patient:
            # delete from Appointment by id
            Appointment.objects.filter(id=appointment.id).delete()
            return redirect('records:frontdesk')
            break

    return render(request, 'records/cancel_appointment.html', {'appointments': appointments,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

# add admit
def new_admit(request):
    if request.method == 'POST':
        form = NewAdmitForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
        else:
            a=[]
            a.append('INAVLID ID OR PASSWORD')
            return render(request, 'records/add_admit.html', {"error":'Already Admited','record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


    else:
        form = NewAdmitForm()

    return render(request, 'records/add_admit.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


# cancel admit    
def cancel_admit(request):
    admits = Admit.objects.all()

    admit_id = request.GET.get('patient', None)
 
    for admit in admits:
        
        if str(admit) == admit_id:
            # delete from Appointment by id
            Admit.objects.filter(id=admit.id).delete()
            Nurses.objects.filter(patient_id_id=admit.patient_id_id).delete()
            return redirect('records:frontdesk')
            break

    return render(request, 'records/cancel_admit.html', {'admits': admits,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
