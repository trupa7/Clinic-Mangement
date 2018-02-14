<<<<<<< HEAD
from django.shortcuts import render, redirect

# Create your views here.
from records.froms import NewPatientForm, NewAppointmentForm, NewHistoryForm,NewAdmitForm
from records.models import Appointment,Admit
from nurses.models import Nurses

=======
from datetime import date

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from records.froms import NewPatientForm, NewAppointmentForm, NewHistoryForm
from records.models import Appointment, History, Patient, CompleteAppointment
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408


#
def front_desk(request):
<<<<<<< HEAD
    Appoinment_list=Appointment.objects.all()
   
    return render(request, "records/re_desk.html",{"Appoinment_list":Appoinment_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    #return render(request, "front_desk.html",{"Appoinment_list":Appoinment_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
=======
    return render(request, "front_desk.html")

>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408

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
<<<<<<< HEAD
    return render(request, 'records/add_patient.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
=======

    return render(request, 'records/add_to_db.html', {'record': form})
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408


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

<<<<<<< HEAD
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
=======
    return render(request, 'records/add_to_db.html', {'record': form})




'''
# cancel appointment
def cancel_appointment(request):
    appointments = list(Appointment.objects.all())
    history = list(History.objects.all())
    for a in appointments:
        for h in history:
            if a.id == h.appointment_id:
                appointments.remove(a)
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408

    patient = request.GET.get('patient', None)

    for appointment in appointments:
        if str(appointment) == patient:
            # delete from Appointment by id
            Appointment.objects.filter(id=appointment.id).delete()
<<<<<<< HEAD
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
=======
            break

    return render(request, 'records/cancel_app.html', {'appointments': appointments})
'''

# cancel appointment
def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    app = CompleteAppointment(patient=appointment.patient,
                              appointment_date=appointment.appointment_date,
                              appointment_time=appointment.appointment_time,
                              visit_reason=appointment.visit_reason,
                              doctor=appointment.doctor)
    app.save()
    record = History(appointment=app, prescription='n', prescribed='none', visit_record='Appointment Canceled')
    record.save()
    Appointment.objects.filter(id=appointment.id).delete()

    return appointments(request)



def appointments(request):
    appointments = list(Appointment.objects.all())
    history = list(History.objects.all())
    todays_appointments = []
    future_appointments = []
    for a in appointments:
        for h in history:
            if a.id == h.appointment_id:
                appointments.remove(a)
    todays_date = date.today()
    for a in appointments:
        if str(a.appointment_date) == str(todays_date):
            todays_appointments.append(a)
        else:
            future_appointments.append(a)



    return render(request, 'records/current_appointments.html', {'todays_appointments': todays_appointments,
                                                                 'future_appointments': future_appointments,
                                                                 'todays_date':todays_date})

def display_history(request, appointment_id):
    try:
        # isolate the patient and all appointments
        appointments = get_object_or_404(Appointment, pk=appointment_id)
        name = Patient.objects.get(id=appointments.patient_id)
        # get patient name for display

        appointment = CompleteAppointment.objects.filter(patient_id=appointments.patient_id)
        history = list(History.objects.all())
        # append the history for patient to val
        val = []
        for h in history:
            for a in appointment:
                if h.appointment_id == a.id:
                    val.append(h)
                    break

    except:
        raise Http404('no employee found')

    return render(request, 'records/display_history.html', {'name':name, 'history':val})

def update_history(request, appointment_id):

    appointment = get_object_or_404(Appointment, pk=appointment_id)
    # get patient name for display

    print(type(appointment))
    prescription = request.GET.get('precription', None)
    prescribed = request.GET.get('medication', '')
    notes = request.GET.get('notes', None)
    prescript = 'n'
    if prescription == 'on':
        prescript = 'y'
    if notes:

        # create history record
        app = CompleteAppointment(patient=appointment.patient,
                                  appointment_date=appointment.appointment_date,
                                  appointment_time=appointment.appointment_time,
                                  visit_reason=appointment.visit_reason,
                                  doctor=appointment.doctor)
        app.save()
        record = History(appointment=app, prescription=prescript, prescribed=prescribed, visit_record=notes)
        record.save()
        # create complete appointment record
        # delete from current appointment
        Appointment.objects.filter(id=appointment.id).delete()
        return redirect('records:frontdesk')


    name = Patient.objects.get(id=appointment.patient_id)
    return render(request, 'records/custom_form.html',{"name":name})
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
